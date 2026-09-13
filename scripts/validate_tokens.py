#!/usr/bin/env python3
"""Validate references/effects.tokens.json for the xanimations skill.

Standard library only. Exits non-zero with every problem listed.

Usage: python3 scripts/validate_tokens.py [path/to/effects.tokens.json]
"""

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

DEFAULT = Path(__file__).resolve().parent.parent / "references" / "effects.tokens.json"

TOP_LEVEL = ("version", "generated", "sources", "extractionPolicy", "cssNativeValues", "tokens")
CSS_NATIVE = ("native", "partial", "non-native")
HTML_FIELDS = ("semanticSkeleton", "selectors", "attributes", "relationships")
CSS_FIELDS = ("customProperties", "selectors", "properties", "atRules", "keyframes", "timelines", "stateQueries")
RECORD_FIELDS = ("id", "title", "category", "source", "demo", "mechanism", "cssNative",
                 "html", "css", "accessibility", "fallback", "notes")

CHROME_IDS = (
    "chrome-first-scroll-state-query",
    "chrome-stuck-shadow",
    "chrome-current-stuck-header",
    "chrome-boost-snapped-item",
    "chrome-snapped-caption",
    "chrome-animated-slide-elements",
    "chrome-scroll-shadows",
    "chrome-scroll-arrow-prompt",
    "chrome-return-to-top",
)
PRISMIC_ID = re.compile(r"^prismic-(\d{2})-[a-z0-9-]+$")


def is_url(value):
    parsed = urlparse(value or "")
    return parsed.scheme in ("http", "https") and bool(parsed.netloc)


def validate(path):
    errors = []

    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except FileNotFoundError:
        return [f"{path}: file not found"]
    except json.JSONDecodeError as exc:
        return [f"{path}: invalid JSON: {exc}"]

    if not isinstance(data, dict):
        return [f"{path}: top level must be an object"]

    for field in TOP_LEVEL:
        if field not in data:
            errors.append(f"missing top-level field: {field}")

    if data.get("cssNativeValues") not in (None, list(CSS_NATIVE)):
        errors.append(f"cssNativeValues must be {list(CSS_NATIVE)}")

    sources = data.get("sources")
    if not isinstance(sources, dict) or not is_url(sources.get("chrome")) or not is_url(sources.get("prismic")):
        errors.append("sources.chrome and sources.prismic must both be URLs")

    tokens = data.get("tokens")
    if not isinstance(tokens, list):
        errors.append("tokens must be a list")
        return errors

    seen = set()
    prismic_numbers = set()
    chrome_seen = set()

    for index, record in enumerate(tokens):
        label = f"tokens[{index}]"
        if not isinstance(record, dict):
            errors.append(f"{label}: must be an object")
            continue

        token_id = record.get("id")
        label = f"{token_id or label}"

        for field in RECORD_FIELDS:
            if field not in record:
                errors.append(f"{label}: missing field '{field}'")

        if not isinstance(token_id, str) or not token_id:
            errors.append(f"{label}: id must be a non-empty string")
        elif token_id in seen:
            errors.append(f"{label}: duplicate id")
        else:
            seen.add(token_id)
            match = PRISMIC_ID.match(token_id)
            if match:
                prismic_numbers.add(int(match.group(1)))
            elif token_id in CHROME_IDS:
                chrome_seen.add(token_id)

        for field in ("title", "category", "mechanism"):
            if not isinstance(record.get(field), str) or not record.get(field, "").strip():
                errors.append(f"{label}: {field} must be a non-empty string")

        if not is_url(record.get("source", "")):
            errors.append(f"{label}: source must be a URL")

        demo = record.get("demo", "")
        if demo is not None and not is_url(demo):
            errors.append(f"{label}: demo must be a URL or null")

        if record.get("cssNative") not in CSS_NATIVE:
            errors.append(f"{label}: cssNative must be one of {list(CSS_NATIVE)}")

        html = record.get("html")
        if not isinstance(html, dict):
            errors.append(f"{label}: html must be an object")
        else:
            for field in HTML_FIELDS:
                if field not in html:
                    errors.append(f"{label}: html.{field} is missing")
            if not str(html.get("semanticSkeleton", "")).strip():
                errors.append(f"{label}: html.semanticSkeleton must not be empty")
            for field in ("selectors", "attributes", "relationships"):
                if field in html and not isinstance(html[field], list):
                    errors.append(f"{label}: html.{field} must be a list")

        css = record.get("css")
        if not isinstance(css, dict):
            errors.append(f"{label}: css must be an object")
        else:
            for field in CSS_FIELDS:
                if field not in css:
                    errors.append(f"{label}: css.{field} is missing")
            if "customProperties" in css and not isinstance(css["customProperties"], dict):
                errors.append(f"{label}: css.customProperties must be an object")
            for field in ("selectors", "properties", "atRules", "keyframes", "timelines", "stateQueries"):
                if field in css and not isinstance(css[field], list):
                    errors.append(f"{label}: css.{field} must be a list")
            if not css.get("properties"):
                errors.append(f"{label}: css.properties must list at least one property")

        for field in ("accessibility", "fallback", "notes"):
            if field in record and not isinstance(record[field], list):
                errors.append(f"{label}: {field} must be a list")

    for number in range(1, 51):
        if number not in prismic_numbers:
            errors.append(f"missing Prismic record {number} (expected id prismic-{number:02d}-*)")

    for chrome_id in CHROME_IDS:
        if chrome_id not in chrome_seen:
            errors.append(f"missing Chrome record: {chrome_id}")

    expected = 50 + len(CHROME_IDS)
    if len(tokens) != expected:
        errors.append(f"expected {expected} records, found {len(tokens)}")

    return errors


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT
    errors = validate(path)
    if errors:
        for error in errors:
            print(f"FAIL {error}")
        print(f"\n{len(errors)} problem(s) in {path}")
        return 1
    print(f"OK {path}: 59 records valid (50 Prismic + 9 Chrome)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

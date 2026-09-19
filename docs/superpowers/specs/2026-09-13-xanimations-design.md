# xanimations — design spec

Date: 2026-09-13
Status: implemented
Repository: `xanimations-skill`

## Purpose

A global, auto-discoverable skill for CSS-native animation architecture: scroll-driven timelines, scroll-state queries, sticky and snap interactions, parallax, reveals, and scroll affordances. It owns DOM structure, CSS triggers, timelines, state queries, progressive enhancement, and CSS/HTML token extraction. It does not own named transition recipes or motion-token values.

## Authoritative sources

Both must be navigated live on every relevant invocation, before the local references are trusted:

- <https://developer.chrome.com/blog/css-scroll-state-queries>
- <https://prismic.io/blog/css-scroll-effects>

The local references are a cached index of those pages as read on 2026-09-13. Baseline support and article contents move; the live pages win.

## Package layout

```
SKILL.md                                    # triggers, ladder, rules, ownership boundary, workflow
agents/openai.yaml                          # harness metadata + $xanimations default prompt
references/chrome-scroll-state-queries.md   # scroll-state() reference
references/prismic-scroll-effects.md        # 50 catalogued examples, grouped by article category
references/baseline-skills-comparison.md    # scope boundaries vs. five researched skills
references/effects.tokens.json              # 59 machine-readable token records
scripts/validate_tokens.py                  # stdlib-only validator
docs/superpowers/specs/2026-09-13-xanimations-design.md
```

## Token index

`references/effects.tokens.json` holds 59 records: `prismic-01-*` … `prismic-50-*` plus nine `chrome-*` records covering every concrete example in the Chrome article (first scroll-state query, stuck shadow, current stuck header, boost snapped item, snapped caption, animated slide elements, scroll shadows, scroll arrow prompt, return to top).

Each record carries `id`, `title`, `category`, `source`, `demo`, `mechanism`, `cssNative`, `html` (`semanticSkeleton`, `selectors`, `attributes`, `relationships`), `css` (`customProperties`, `selectors`, `properties`, `atRules`, `keyframes`, `timelines`, `stateQueries`), `accessibility`, `fallback`, `notes`.

### Extraction policy — decision worth recording

The plan required token extraction from the source material while also forbidding mirroring of third-party implementations. The resolution: **records describe the canonical CSS-native token shape of each pattern — the semantic skeleton, the container/child relationships, the custom properties, the animated properties, the at-rules, timelines and state queries a correct implementation needs — rather than transcribing the linked pen.** Chrome records quote the article's own code, which is Apache-2.0 licensed and published as reference material; Prismic records are reconstructions.

`cssNative` classifies the **source pen's own implementation**:

- `native` — runs on CSS alone as published.
- `partial` — the pen uses script, but the effect is reproducible in CSS today; the record names the native route.
- `non-native` — needs an external runtime (GSAP, ScrollifyJS, AOS, IntersectionObserver, WebGL). Catalogued as inspiration and context, never presented as CSS-native.

Records classified `partial` or `non-native` carry an explicit note telling the reader to open the live pen before quoting it, because the classification is inferred from the article's own description and the pen title rather than from a line-by-line read of every pen.

## Ownership boundary

| Concern | Owner |
|---|---|
| DOM structure, container/child topology, semantic skeleton | xanimations |
| Triggers: scroll-state queries, scroll timelines, style queries | xanimations |
| Timeline architecture, ranges, `@property` registration | xanimations |
| `@supports` layering, reduced-motion branches, fallbacks | xanimations |
| HTML/CSS token extraction from source material | xanimations |
| Named transition recipes | transitions-dev |
| Duration/easing token values and polish passes | transitions-dev |
| Transition audits across a component set | transitions-dev |

xanimations never recreates, overrides, or installs `transitions-dev` recipes, and adds no third-party animation library.

## Validation

```bash
python3 scripts/validate_tokens.py
```

`validate_tokens.py` (standard library only) fails on invalid JSON, missing top-level fields, duplicate ids, any missing Chrome record, any missing Prismic record 1–50, an invalid `cssNative` value, missing nested `html`/`css` fields, a missing or non-URL `source`, a `demo` that is neither a URL nor `null`, and a record count other than 59.

## Global installation

One canonical directory, symlinked into both agent skill trees:

- `~/.codex/skills/xanimations` → the checkout
- `~/.agents/skills/xanimations` → the checkout

Both paths are verified absent before linking.

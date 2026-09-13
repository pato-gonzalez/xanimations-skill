# Baseline comparison — where xanimations stops

Researched 2026-09-13 from the live repositories below. Used for **structure, routing conventions, and reference organisation only**. No transition recipes, token scales, or motion catalogues are copied into this skill.

## The five baselines

### transitions.dev — `transitions-dev` + `transitions-polish`

<https://github.com/Jakubantalik/transitions.dev/blob/main/skills/transitions-polish/SKILL.md>

Installs whole named transitions (`transitions-dev`) and tunes motion that already exists against a five-dimension token scale — duration, distance, scale, blur, easing (`transitions-polish`). Ships a `_root.css` with the token values and a doctrine of *match on usage, never on the nearest number*: a value is wrong when it does not fit what the motion does, not when it is off by 20ms.

**Owns, and xanimations must not restate:** the named recipe catalogue, the duration/easing token values, open/close asymmetry, hover-in vs hover-out, stagger offsets, intent delays, and motion audits against that scale.

**What xanimations borrowed:** nothing but the boundary itself — xanimations *references* motion tokens through `var(--duration-*)` / `var(--ease-*)` and leaves their definition and polishing to `transitions-dev`.

### mblode/agent-skills — `ui-animation`

<https://github.com/mblode/agent-skills/blob/main/skills/ui-animation/SKILL.md>

Broad UI-motion skill: springs, gestures and drag, curve fitting from screen recordings, component patterns, performance debugging, SVG animation, review format. Explicitly declares an IS / IS NOT block and a routing boundary against its sibling skills (`product-design` owns action semantics, `ui-design` owns visual build, `ui-animation` owns timing and measured motion).

**Structural pattern adopted:** the "read this file when" routing table, and the explicit routing-boundary paragraph instead of an implicit overlap. `ui-animation` covers mixed runtimes (Motion, WAAPI, JS) and gesture physics — xanimations deliberately does **not**, and stays CSS-native.

### delphi-ai/animate-skill

<https://github.com/delphi-ai/animate-skill>

Next.js/React animation patterns based on Emil Kowalski's *Animations on the Web*. Eight runnable component examples plus references on CSS animation, Framer Motion, performance, accessibility. Framework-bound (React) and dependency-bearing (`framer-motion`, `react-use-measure`).

**Structural pattern adopted:** none of the content; only the reminder that a skill which ships framework examples ends up owning those dependencies. xanimations ships no component examples and adds no dependency.

### joepUI/motion-ref-skill

<https://github.com/joepUI/motion-ref-skill>

119 catalogued effects across 13 categories, scenario-first: describe the product situation, get the effect and implementation guidance. Agent-agnostic (Claude Code, Codex, and any SKILL.md host).

**Structural pattern adopted:** the catalogue-as-index shape — a machine-readable record per effect, routed by category, so the agent loads one record instead of the whole library. `references/effects.tokens.json` is xanimations' version of that idea, narrowed to scroll-driven and scroll-state CSS.

### its-thepoe/skills

<https://github.com/its-thepoe/skills>

A personal skills collection published to npm, installable across Codex, Cursor, Claude Code, OpenCode and Windsurf into each agent's local skills folder.

**Structural pattern adopted:** the multi-agent installation convention — one canonical skill directory, symlinked into every agent's skills path, so Codex and the shared `~/.agents/skills` tree read the same `SKILL.md`. That is exactly how this skill is installed globally.

## The resulting scope line

| | xanimations | transitions-dev / -polish | ui-animation, animate-skill, motion-ref |
|---|---|---|---|
| DOM structure and container/child topology | ✅ | — | partial |
| Scroll-state queries (`stuck` / `snapped` / `scrollable`) | ✅ | — | — |
| Scroll-driven timelines, ranges, `@property` | ✅ | — | partial |
| `@supports` layering and reduced-motion branches | ✅ | partial | partial |
| HTML/CSS token extraction from source articles | ✅ | — | — |
| Named transition recipes | — | ✅ | ✅ |
| Duration/easing token **values** and polish passes | — | ✅ | ✅ |
| Springs, gestures, drag physics, curve fitting | — | — | ✅ |
| Framework/runtime bindings (React, Motion, GSAP) | — | — | ✅ |

Rule of thumb: if the question is *what element queries what state, on which timeline, and what happens when the browser does not support it* — xanimations. If it is *which duration and easing, and does this set of components feel right* — `transitions-dev`. If it is *spring physics, a drag gesture, or a React runtime* — one of the broader motion skills, not this one.

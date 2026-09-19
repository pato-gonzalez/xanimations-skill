<p align="center">
  <img src="assets/banner.svg" alt="xanimations — CSS-native scroll animation architecture" width="100%">
</p>

<p align="center">
  <b>Agent ready skill for building scroll animations the browser already knows how to run.</b>
</p>

---

Most scroll animations get reached for a library first. This skill reaches for CSS first — scroll-driven timelines, scroll-state container queries, `@property` — and only drops to JavaScript for the handful of things CSS genuinely can't observe.

## What it does

When you ask Claude to build a scroll reveal, a sticky header that reacts when it sticks, parallax, snap feedback, or an overflow affordance, this skill takes over and gives it:

- **A ladder to climb.** Does it need to move at all? → native CSS state → `scroll-state()` query → `animation-timeline` → style query → JS → library (never installed).
- **Structure before motion.** Semantic skeleton first, then the trigger, then the animation.
- **Tokens, never literals.** Every duration and easing lives once in `:root`. If you can't make the whole page snappier by editing one block, something leaked.
- **Fallbacks as a default shape.** `@supports` wraps the enhancement, not the base — so unsupported browsers never get stuck on `opacity: 0`. Reduced motion is a real branch, not an afterthought.
- **59 token records** extracted from Chrome's scroll-state reference and Prismic's 50-effect catalogue, greppable by `id`, `category`, or `mechanism`.

## Install

```bash
git clone git@github.com:pato-gonzalez/xanimations-skill.git ~/.claude/skills/xanimations
```

Claude picks it up on the next session. Ask for anything scroll-driven and it activates on its own.

## Inside

```
SKILL.md                                    the skill itself
references/chrome-scroll-state-queries.md   stuck / snapped / scrollable
references/prismic-scroll-effects.md        50 catalogued effects
references/effects.tokens.json              59 machine-readable records
references/baseline-skills-comparison.md    what this skill does not own
scripts/validate_tokens.py                  stdlib-only validator
```

## What it doesn't own

Named transition recipes ("fade-up", "slide-in") and the actual duration/easing *values* belong to `transitions-dev`. This skill references motion tokens; it doesn't define them. When a task crosses that line, it hands off and says so.

## Notes

The banner above is the skill's own rules applied to itself: tokens in `:root`, motion gated behind `prefers-reduced-motion`, nothing communicated by movement alone. Colors from the [ClickHouse design system](https://getdesign.md/clickhouse/design-md).

MIT.

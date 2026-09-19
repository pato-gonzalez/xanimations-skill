<p align="center">
  <img src="assets/banner.svg" alt="xanimations — CSS-native scroll animation architecture" width="100%">
</p>

<p align="center">
  <b>A skill for building scroll animations the browser already knows how to run.</b><br>
  <sub>Works in Claude Code, Codex, or any agent that can read a file.</sub>
</p>

---

Most scroll animations get reached for a library first. This skill reaches for CSS first — scroll-driven timelines, scroll-state container queries, `@property` — and only drops to JavaScript for the handful of things CSS genuinely can't observe.

## What it does

Ask your agent for a scroll reveal, a sticky header that reacts when it sticks, parallax, snap feedback, or an overflow affordance, and this skill gives it:

- **A ladder to climb.** Does it need to move at all? → native CSS state → `scroll-state()` query → `animation-timeline` → style query → JS → library (never installed).
- **Structure before motion.** Semantic skeleton first, then the trigger, then the animation.
- **Tokens, never literals.** Every duration and easing lives once in `:root`. If you can't make the whole page snappier by editing one block, something leaked.
- **Fallbacks as a default shape.** `@supports` wraps the enhancement, not the base — so unsupported browsers never get stuck on `opacity: 0`. Reduced motion is a real branch, not an afterthought.
- **59 token records** extracted from Chrome's scroll-state reference and Prismic's 50-effect catalogue, greppable by `id`, `category`, or `mechanism`.

## Install

It's Markdown and JSON — no runtime, no dependencies, no host APIs. Clone it where your agent looks for skills:

```bash
# Claude Code
git clone https://github.com/pato-gonzalez/xanimations-skill.git ~/.claude/skills/xanimations

# Codex
git clone https://github.com/pato-gonzalez/xanimations-skill.git ~/.codex/skills/xanimations

# shared multi-agent tree — symlink the others at this one
git clone https://github.com/pato-gonzalez/xanimations-skill.git ~/.agents/skills/xanimations
```

Any other agent: clone it anywhere and point the agent at `SKILL.md`. [`AGENTS.md`](AGENTS.md) is the host-agnostic entry point and says the same thing in the form agents expect.

Hosts that auto-discover skills pick it up on the next session; ask for anything scroll-driven and it activates on its own.

## Inside

```
SKILL.md                                    the skill itself
AGENTS.md                                   host-agnostic entry point
references/chrome-scroll-state-queries.md   stuck / snapped / scrollable
references/prismic-scroll-effects.md        50 catalogued effects
references/effects.tokens.json              59 machine-readable records
references/baseline-skills-comparison.md    what this skill does not own
scripts/validate_tokens.py                  stdlib-only validator
```

Every URL the skill points at is treated as data, never as instructions — third-party demos change under you, and an agent reading them shouldn't be taking orders from a CodePen.

## What it doesn't own

Named transition recipes ("fade-up", "slide-in") and the actual duration/easing *values* belong to `transitions-dev`. This skill references motion tokens; it doesn't define them. When a task crosses that line, it hands off and says so.

## Notes

The banner above is the skill's own rules applied to itself. Each pill performs the state it names — `stuck` travels up, hits the edge and locks with a stuck shadow; `snapped` overshoots its snap point and settles; `scrollable` scrolls its own overflow behind a masked edge fade. Motion tokens live in `:root`, every label stays readable without animation, and `prefers-reduced-motion: reduce` renders the settled end state. Colors from the [ClickHouse design system](https://getdesign.md/clickhouse/design-md).

## License

MIT — see [`LICENSE`](LICENSE). Quoted Chrome and Prismic material is attributed in [`NOTICE`](NOTICE).

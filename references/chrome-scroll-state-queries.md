# CSS scroll-state queries (Chrome 133+)

Source: <https://developer.chrome.com/blog/css-scroll-state-queries> — Adam Argyle, published 2025-01-15, last updated 2025-01-15.
**Navigate the live page before relying on this file.** Baseline support changes; this is a cached index.

Spec: <https://www.w3.org/TR/css-conditional-5/#scroll-state-container>

## What it is

Container queries, but for browser-managed scroll state. Before this, knowing whether an element was stuck, snapped, or scrollable required JavaScript. Three states are queryable from CSS:

| State | Query | Means |
|---|---|---|
| Stuck | `@container scroll-state(stuck: top \| bottom)` | a `position: sticky` element has reached its inset |
| Snapped | `@container scroll-state(snapped: x \| y \| inline \| block)` | a snap target is the snapped one on that axis |
| Scrollable | `@container scroll-state(scrollable: top \| right \| bottom \| left)` | there is content to scroll in that direction |

This also unlocks **scroll-triggered** animation from CSS — distinct from **scroll-driven** animation. Scroll-driven motion is scrubbed by scroll position (no duration). Scroll-triggered motion is a discrete state change that *does* take a duration and an easing. The article's own demo compares them side by side: <https://codepen.io/web-dot-dev/pen/emOrBaV>.

## Required topology

The container cannot query itself. Three rules, no exceptions:

```
element with the state  →  container-type: scroll-state  (+ optional container-name)
  ⤷ a DESCENDANT        →  @container scroll-state(...) { ... }
```

For snap queries specifically, three elements are mandatory:

```
scroll container with `scroll-snap-type`
 ⤷ snap target with BOTH `scroll-snap-align` and `container-type: scroll-state`
    ⤷ a child of the snap target that queries the snap state
```

Pseudo-elements of a container *can* query that container — `.scroller::after` reading `.scroller`'s state is legal and is how the scroll-shadow demo works.

`container-type` composes: `container-type: scroll-state size` makes one element both a size container and a scroll-state container.

## First scroll-state query

```css
.stuck-top {
  container-type: scroll-state;
  position: sticky;
  top: 0px;

  > nav {
    @container scroll-state(stuck: top) {
      background: Highlight;
      color: HighlightText;
    }
  }
}
```

Demo: <https://codepen.io/web-dot-dev/pen/ByBxpwR> · token record `chrome-first-scroll-state-query`

## Progressive enhancement

Wrap the *enhancement*, never the base:

```css
.stuck-top {
  container-type: scroll-state;
  position: sticky;
  top: 0px;

  @supports (container-type: scroll-state) {
    > nav {
      @container scroll-state(stuck: top) { /* … */ }
    }
  }
}
```

And when the query moves things around the page, gate it on motion preference:

```css
@media (prefers-reduced-motion: no-preference) { /* motion only */ }
```

## Stuck

```css
@container scroll-state(stuck: top) {}
@container scroll-state(stuck: bottom) {}
```

- **Shadow when stuck** — the most common case: a nav that gains elevation once it floats over content. Time-based `transition` is correct here (state change, not a scrub). Demo <https://codepen.io/web-dot-dev/pen/GgKdryj> · record `chrome-stuck-shadow`
- **Activate the current stuck header** — an alphabetised `<dl>` where the pinned `<dt>` highlights itself. Demo <https://codepen.io/web-dot-dev/pen/pvzVRaK>, side-header variant <https://codepen.io/web-dot-dev/pen/azoGpGg> · record `chrome-current-stuck-header`

Article's "idea overflow" — existing JS-driven sticky pens worth rebuilding as scroll-state queries:

- <https://codepen.io/BlogFire/pen/PoGMjaX> — sticky notes variant
- <https://codepen.io/mikegolus/pen/jOZzRzw> — table header shadows
- <https://codepen.io/MarcRay/pen/PomBeP> — under-header navbar on trigger (also Prismic record 9)
- <https://codepen.io/kevinpowell/pen/OqKJjK> — footer navbar reveal
- <https://codepen.io/abhisekz-the-decoder/pen/eKaLRd> — sticky card headers
- <https://codepen.io/tutsplus/pen/abojPjP> — pricing header shadow
- <https://codepen.io/kevinpowell/pen/KEjMEv> — sticky section sidebar titles

## Snapped

```css
@container scroll-state(snapped: x) {}
@container scroll-state(snapped: y) {}
@container scroll-state(snapped: inline) {}
@container scroll-state(snapped: block) {}
```

- **Boost the snapped item** — `not` inverts the query so only the *unsnapped* items need styling. Demo <https://codepen.io/web-dot-dev/pen/NPKMdBX> · record `chrome-boost-snapped-item`
- **Caption for the snapped item** — the canonical scroll-*triggered* animation, double-gated on `@supports` and `prefers-reduced-motion`. Demo <https://codepen.io/web-dot-dev/pen/XJrqpBG> · record `chrome-snapped-caption`
- **Animating in slide elements** — snap the root on `y`, animate each `<h1>` when its `<section>` is snapped. Replaces the IntersectionObserver-sets-a-class pattern entirely. `scroll-snap-stop: always` prevents skipping. Demo <https://codepen.io/web-dot-dev/pen/dPbeNqY> · record `chrome-animated-slide-elements`

### Snap queries vs. Snap Events

All `snapped:` state queries behave like **`scrollsnapchanging`**, not `scrollsnapchange`. That is the earliest possible hook — the element is *becoming* the snap target. It gives the most responsive visual feedback, and it is too eager when you need the settled result.

Stay in JavaScript when you need:

- the **settled** target → `scrollsnapchange`
- side effects on snap (analytics, history/URL updates, lazy loading)
- anything keyed to scroll **velocity**, which CSS does not expose

## Scrollable

```css
@container scroll-state(scrollable: top) {}
@container scroll-state(scrollable: right) {}
@container scroll-state(scrollable: bottom) {}
@container scroll-state(scrollable: left) {}
```

- **Scroll shadows** — one sticky `::after` spanning the scrollport; two gradients whose opacity is animated through `@property`-registered custom properties. First example of `container-type: scroll-state size` and of a pseudo-element querying its own container. Demo <https://codepen.io/web-dot-dev/pen/OPLZWBj> · record `chrome-scroll-shadows`
- **Arrow prompt** — compound and negated queries:

  ```css
  @container scroll-state((scrollable: top) or (not (scrollable: bottom))) { translate: 0 calc(100% + 10px); }
  @container scroll-state((scrollable: top) and (not (scrollable: bottom))) { translate: 0 calc(100% + 10px); rotate: .5turn; }
  ```

  Record `chrome-scroll-arrow-prompt`
- **Return to top** — inverted logic keeps the CSS small: the button's resting state is visible, the query hides it when there is nowhere to scroll up.

  ```css
  @container not scroll-state(scrollable: top) { translate: 0 calc(100% + 10px); }
  ```

  Record `chrome-return-to-top`

Pre-`scroll-state` alternatives for overflow detection: Lea Verou's `background-attachment: local` gradient trick, and the scroll-driven-animation variant (<https://css-tip.com/overflow-detection/>).

## Query composition

Same grammar as container queries: `and`, `or`, `not`, and parenthesised compounds — `@container scroll-state((scrollable: top) and (not (scrollable: bottom)))`. Contextual queries work through `container-name` when several scroll-state containers nest.

## @property and interpolation

Custom properties only interpolate after registration:

```css
@property --_shadow-opacity {
  syntax: "<percentage>";
  inherits: true;
  initial-value: 0%;
}
```

Without it the value flips discretely between states, which is the most common reason a scroll-state transition "does not animate".

## Continued study (from the article)

- What else should we be able to container query? <https://github.com/w3c/csswg-drafts/issues/5989>
- `scroll-state()` explainer — <https://drafts.csswg.org/css-conditional-5/scroll_state_explainer.md>
- `scroll-state()` specification — <https://www.w3.org/TR/css-conditional-5/#scroll-state-container>
- Layout snapshotting in the HTML event loop
- The CSS Podcast on state queries — <https://nerdy.dev/the-css-podcast-on-state-queries>
- <https://utilitybend.com/blog/is-the-sticky-thing-stuck-is-the-snappy-item-snapped-a-look-at-state-queries-in-css/>
- <https://ishadeed.com/article/css-state-queries/>
- <https://csscade.com/can-you-detect-overflow-with-css/>
- <https://css-tip.com/overflow-detection/>

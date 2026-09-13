# Prismic: 50 CSS scroll effects

Source: <https://prismic.io/blog/css-scroll-effects> — Alison Brunk. Part 8 of Prismic's *CSS Animation Collection*.
**Navigate the live page before relying on this file.** The article is edited over time; entry numbering here matches the version read on 2026-09-13.

Every entry below maps to a record in `effects.tokens.json` (`id` column). The `CSS-native` column is the classification of the **source pen's own implementation**:

- `native` — the effect as published runs on CSS alone (scroll-driven animations, sticky, snap, style/state queries, transforms, masks).
- `partial` — the published pen uses script, but the effect is reproducible in CSS today. The token record names the native route.
- `non-native` — requires an external runtime (GSAP/ScrollTrigger, ScrollifyJS, AOS, IntersectionObserver, WebGL/canvas). Catalogued as inspiration and context only. **xanimations never installs an animation library.**

Token records are representative reconstructions of each pattern's token shape, not verbatim copies of third-party pens. Open the demo before quoting an implementation.


## Parallax

| # | Effect | CSS-native | Mechanism | Demo | Token record |
|---|---|---|---|---|---|
| 1 | Parallax background | **native** | CSS 3D parallax | [pen](https://codepen.io/p0waqqatsi/pen/vYwqQxV) | `prismic-01-parallax-background` |
| 2 | Parallax scroll demo | **native** | CSS 3D parallax | [pen](https://codepen.io/evolutionxbox/pen/JjvWPo) | `prismic-02-parallax-scroll-demo` |
| 3 | CSS-only parallax scrolling | **native** | CSS 3D parallax | [pen](https://codepen.io/BlogFire/pen/bGBgzXr) | `prismic-03-css-only-parallax-scrolling` |
| 4 | CSS parallax scroll | **native** | CSS 3D parallax | [pen](https://codepen.io/ve00ryca/pen/XWNQPxp) | `prismic-04-css-parallax-scroll` |
| 5 | CSS-only parallax scroll | **native** | Background parallax driven by background-attachment /… | [pen](https://codepen.io/karldanninger/pen/NwzMzN) | `prismic-05-css-only-parallax-scroll` |

- **1. Parallax background** — Depth-layered nature scene where background layers scroll slower than the foreground.
- **2. Parallax scroll demo** — Six-layer parallax built on the Keith Clark perspective technique. Uses the classic perspective + translateZ + compensating scale stack.
- **3. CSS-only parallax scrolling** — Scroll container with pushed-back layers producing depth without script.
- **4. CSS parallax scroll** — Section-per-layer parallax page composed entirely in CSS.
- **5. CSS-only parallax scroll** — Full-bleed image sections whose backgrounds lag behind the scroll. background-attachment: fixed is the fragile part on mobile; a view() timeline on background-position is the modern replacement.

## Sticky effects

| # | Effect | CSS-native | Mechanism | Demo | Token record |
|---|---|---|---|---|---|
| 6 | Sticky full page slides | **native** | CSS scroll snap | [pen](https://codepen.io/nefejames/pen/JoPvBMq) | `prismic-06-sticky-full-page-slides` |
| 7 | Sticky section layout | **native** | position | [pen](https://codepen.io/p0waqqatsi/pen/wvbzQxj) | `prismic-07-sticky-section-layout` |
| 8 | Sticky stacking on scroll | **native** | Stacked/pinned sections | [pen](https://codepen.io/p0waqqatsi/pen/mdYEYqe) | `prismic-08-sticky-stacking-on-scroll` |
| 9 | Responsive sticky header navigation | partial | position | [pen](https://codepen.io/MarcRay/pen/PomBeP) | `prismic-09-responsive-sticky-header-navigation` |
| 10 | Responsive sticky sidebar | **native** | position | [pen](https://codepen.io/jamesdarren/pen/AajKKg) | `prismic-10-responsive-sticky-sidebar` |
| 11 | Sticky parallax sections | **native** | position | [pen](https://codepen.io/hexagoncircle/pen/JjRYaZw) | `prismic-11-sticky-parallax-sections` |
| 12 | Sticky navigation with smooth scrolling | partial | position | [pen](https://codepen.io/prvnbist/pen/GQMPZq) | `prismic-12-sticky-navigation-with-smooth-scrolling` |
| 13 | Stacked cards effect | **native** | Stacked/pinned sections | [pen](https://codepen.io/HugoSalazar/pen/dyBzOdj) | `prismic-13-stacked-cards-effect` |
| 14 | GSAP stacked cards | non-native | GSAP ScrollTrigger timeline | [pen](https://codepen.io/HugoSalazar/pen/QWomQem) | `prismic-14-gsap-stacked-cards` |

- **6. Sticky full page slides** — Full-page slides that snap in and out of view while sticky backgrounds parallax.
- **7. Sticky section layout** — Sticky sidebar (table-of-contents pattern) paired with a parallax media column.
- **8. Sticky stacking on scroll** — Six cards that stack on top of each other with a bounce as they pin.
- **9. Responsive sticky header navigation** — Nav bar that reveals and pins at the top once the page is scrolled. The Chrome scroll-state article lists this exact pen as a candidate for removing its JavaScript with @container scroll-state(stuck: top).
- **10. Responsive sticky sidebar** — Sidebar pinned within its column while the main content scrolls past.
- **11. Sticky parallax sections** — Section backgrounds hook in place momentarily as each section scrolls through.
- **12. Sticky navigation with smooth scrolling** — Nav that shrinks on scroll down and expands on scroll back up, with smooth anchor scrolling. scroll-behavior: smooth replaces the scripted scrolling; the shrink state is a scroll-state(stuck: top) query.
- **13. Stacked cards effect** — No-JS stacked cards scrubbed by a view() timeline as each card pins.
- **14. GSAP stacked cards** — Same stacked-card result driven by GSAP instead of CSS. Direct comparison with record prismic-13 — prefer the CSS version.

## Text scroll animations

| # | Effect | CSS-native | Mechanism | Demo | Token record |
|---|---|---|---|---|---|
| 15 | Slice slider | partial | Historical implementation | [pen](https://codepen.io/StephenScaff/pen/egOedp) | `prismic-15-slice-slider` |
| 16 | 3D spatial scroll zoom | **native** | 3D transform scene scrubbed by scroll | [pen](https://codepen.io/argyleink/pen/ZEdrzJZ) | `prismic-16-3d-spatial-scroll-zoom` |
| 17 | CSS scroll animation | partial | Historical implementation | [pen](https://codepen.io/jazzpeh/pen/wvMrzpL) | `prismic-17-css-scroll-animation` |
| 18 | Text scroll on reveal effects | **native** | CSS scroll-driven animation | [pen](https://codepen.io/thebabydino/pen/KKLWBJZ) | `prismic-18-text-scroll-on-reveal-effects` |
| 19 | CSS scroll-triggered animation with style queries | **native** | Container style query | [pen](https://codepen.io/hexagoncircle/pen/wvOPmGO) | `prismic-19-css-scroll-triggered-animation-with-style-queries` |
| 20 | Scroll-driven fade-in | **native** | CSS scroll-driven animation | [pen](https://codepen.io/bassohr/pen/MWxzYBq) | `prismic-20-scroll-driven-fade-in` |
| 21 | CSS text scroll animation | **native** | CSS scroll-driven animation | [pen](https://codepen.io/ssonko-jimmy/pen/QWNRwNV) | `prismic-21-css-text-scroll-animation` |
| 22 | Duplicate text scroll animation | **native** | CSS scroll-driven animation | [pen](https://codepen.io/Mais1/pen/KKaRgQv) | `prismic-22-duplicate-text-scroll-animation` |
| 23 | Scroll-based animation | partial | Historical implementation | [pen](https://codepen.io/johnson5409/pen/gOPeWPe) | `prismic-23-scroll-based-animation` |
| 24 | Marquee page border | non-native | GSAP ScrollTrigger timeline | [pen](https://codepen.io/hexagoncircle/pen/xxwBLMy) | `prismic-24-marquee-page-border` |

- **15. Slice slider** — Sliced panels of copy that slide in and out as the user scrolls. CSS-native equivalent: snap container plus per-slice view() timelines.
- **16. 3D spatial scroll zoom** — Scroll pulls the viewer through layered 3D text, scrubbed by a CSS scroll timeline.
- **17. CSS scroll animation** — Text blocks with contrasting backgrounds sliding in and out on scroll.
- **18. Text scroll on reveal effects** — Seven no-JS char-by-char reveal variants scrubbed on scroll. Per-character delays come from an index custom property, not from script.
- **19. CSS scroll-triggered animation with style queries** — Scale-up and gradient text treatment triggered through a container style query.
- **20. Scroll-driven fade-in** — Canonical fade-and-rise entry animation on a view() timeline.
- **21. CSS text scroll animation** — Copy that fades and tilts into place as it enters the viewport.
- **22. Duplicate text scroll animation** — Duplicated headline that splits apart on scroll down and rejoins on scroll up. Duplicate text must be aria-hidden so it is announced once.
- **23. Scroll-based animation** — Headlines that scale and fade into view as they are reached.
- **24. Marquee page border** — Text marquee running around the page border, direction bound to scroll direction. A CSS-native variant is possible with scroll() timelines and a negative animation range, but the source pen uses ScrollTrigger.

## Image scroll animations

| # | Effect | CSS-native | Mechanism | Demo | Token record |
|---|---|---|---|---|---|
| 25 | Zoom and blur background image | partial | CSS filter/backdrop-filter scrubbed across a scroll or… | [pen](https://codepen.io/zrichard/pen/vYqMEY) | `prismic-25-zoom-and-blur-background-image` |
| 26 | GSAP ScrollTrigger image zoom | non-native | GSAP ScrollTrigger timeline | [pen](https://codepen.io/p0waqqatsi/pen/OJYVgMK) | `prismic-26-gsap-scrolltrigger-image-zoom` |
| 27 | CSS inverted reveal scroller | **native** | Masked / clipped reveal scrubbed on scroll | [pen](https://codepen.io/jh3y/pen/ExzdZXN) | `prismic-27-css-inverted-reveal-scroller` |
| 28 | Slider transitions | partial | Historical implementation | [pen](https://codepen.io/fluxus/pen/rweVgp) | `prismic-28-slider-transitions` |
| 29 | CSS scroll animation with subgrid | **native** | CSS scroll-driven animation | [pen](https://codepen.io/jh3y/pen/VYZwOwd) | `prismic-29-css-scroll-animation-with-subgrid` |
| 30 | Scroll image effect | non-native | Canvas / WebGL rendering driven by scroll position | [pen](https://codepen.io/bokoko33/pen/VwpOWMR) | `prismic-30-scroll-image-effect` |
| 31 | Image transition on scroll | non-native | GSAP ScrollTrigger timeline | [pen](https://codepen.io/pizza3/pen/NgXowe) | `prismic-31-image-transition-on-scroll` |
| 32 | Multi-filters | partial | CSS filter/backdrop-filter scrubbed across a scroll or… | [pen](https://codepen.io/dominiksuter/pen/ajQdKL) | `prismic-32-multi-filters` |
| 33 | Sky scroll animation | partial | Masked / clipped reveal scrubbed on scroll | [pen](https://codepen.io/magnificode/pen/JedJPO) | `prismic-33-sky-scroll-animation` |
| 34 | Horizontal parallax gallery | **native** | Horizontal scroll gallery | [pen](https://codepen.io/pehaa/pen/zYxbxQg) | `prismic-34-horizontal-parallax-gallery` |

- **25. Zoom and blur background image** — Hero image that blurs and zooms out in proportion to scroll distance. Scrub it natively with animation-timeline: scroll() on filter and scale.
- **26. GSAP ScrollTrigger image zoom** — Depth-zoom on a background image driven by ScrollTrigger.
- **27. CSS inverted reveal scroller** — Images revealed through an inverted mask that tracks scroll direction.
- **28. Slider transitions** — Image and caption pairs transitioning as the slider advances on scroll.
- **29. CSS scroll animation with subgrid** — Subgrid image wall whose tiles animate in on their own view() ranges. subgrid keeps the tile ranges aligned to the parent grid tracks.
- **30. Scroll image effect** — Wave/glitch distortion whose intensity follows scroll velocity. Scroll velocity is not exposed to CSS — this needs a render loop.
- **31. Image transition on scroll** — Image-to-image transition sequence tied to scroll progress.
- **32. Multi-filters** — Different CSS filters applied to one image per scrolled section. Per-section filters are a natural fit for a style query or a view() timeline.
- **33. Sky scroll animation** — Masked 'SKY' lettering that splits the image apart on scroll.
- **34. Horizontal parallax gallery** — CSS-only horizontal gallery with inner-image parallax and a hover color shift.

## Other CSS scroll animations

| # | Effect | CSS-native | Mechanism | Demo | Token record |
|---|---|---|---|---|---|
| 35 | Eye scroll | **native** | CSS scroll-driven animation | [pen](https://codepen.io/remino/pen/rNPojqX) | `prismic-35-eye-scroll` |
| 36 | Changing background color while scrolling | partial | Section-driven background color change across the… | [pen](https://codepen.io/Funsella/pen/nEreQq) | `prismic-36-changing-background-color-while-scrolling` |
| 37 | Full-screen navigation bar | **native** | CSS scroll-driven animation | [pen](https://codepen.io/andrejsharapov/pen/ZEVyKmR) | `prismic-37-full-screen-navigation-bar` |
| 38 | Scroll-driven scroll-snapping animations | **native** | CSS scroll snap | [pen](https://codepen.io/giana/pen/BabdgjB) | `prismic-38-scroll-driven-scroll-snapping-animations` |
| 39 | Curved SVG background animation | partial | SVG shape or path animated across the scroll range | [pen](https://codepen.io/armantaherian/pen/ZyZWVZ) | `prismic-39-curved-svg-background-animation` |
| 40 | Change background color with GSAP ScrollTrigger | non-native | GSAP ScrollTrigger timeline | [pen](https://codepen.io/cameronknight/pen/RwRebNY) | `prismic-40-change-background-color-with-gsap-scrolltrigger` |
| 41 | Masthead webpage | **native** | CSS scroll-driven animation | [pen](https://codepen.io/andrejsharapov/pen/NWezrQZ) | `prismic-41-masthead-webpage` |
| 42 | Highlight text | non-native | GSAP ScrollTrigger timeline | [pen](https://codepen.io/hexagoncircle/pen/gOPMwvd) | `prismic-42-highlight-text` |
| 43 | Reading indicator | **native** | Scroll progress indicator driven by animation-timeline | [pen](https://codepen.io/HugoSalazar/pen/xxMaarz) | `prismic-43-reading-indicator` |
| 44 | Scroll reveal effect with intersection observer | non-native | IntersectionObserver reveal | [pen](https://codepen.io/HugoSalazar/pen/yLgrZRZ) | `prismic-44-scroll-reveal-effect-with-intersection-observer` |
| 45 | Airplanes | non-native | Canvas / WebGL rendering driven by scroll position | [pen](https://codepen.io/ste-vg/pen/GRooLza) | `prismic-45-airplanes` |
| 46 | ScrollifyJS + AnimateCSS + CSS flexbox | non-native | Third-party scroll library | [pen](https://codepen.io/Zeindelf/pen/WjxyLK) | `prismic-46-scrollifyjs-animatecss-css-flexbox` |
| 47 | CSS scroll bars | partial | Scroll progress indicator driven by animation-timeline | [pen](https://codepen.io/GhostRider/pen/oNvoNv) | `prismic-47-css-scroll-bars` |
| 48 | 3D CSS scroll | partial | 3D transform scene scrubbed by scroll | [pen](https://codepen.io/shshaw/pen/GRdbZEL) | `prismic-48-3d-css-scroll` |
| 49 | CSS shadow on scroll | **native** | Overflow affordance | [pen](https://codepen.io/t_afif/pen/bGrPBLJ) | `prismic-49-css-shadow-on-scroll` |
| 50 | CSS timeline animation | **native** | CSS scroll-driven animation | [pen](https://codepen.io/mrtrimble/pen/YzRrzgM) | `prismic-50-css-timeline-animation` |

- **35. Eye scroll** — Eyes that rotate and a page background that shifts, both scrubbed by scroll.
- **36. Changing background color while scrolling** — Page background interpolating between section colors during vertical scroll.
- **37. Full-screen navigation bar** — Pure-CSS full-screen nav whose sidebar text clarifies on vertical scroll.
- **38. Scroll-driven scroll-snapping animations** — Five snapped sections with four selectable transition modes, all CSS. Best reference for combining scroll-snap-type with per-section view() timelines.
- **39. Curved SVG background animation** — Curved SVG divider that reshapes as the page scrolls.
- **40. Change background color with GSAP ScrollTrigger** — Background color plus parallax layers driven by ScrollTrigger. Compare with record prismic-36 and with @property-based CSS interpolation.
- **41. Masthead webpage** — Full responsive page built from pure CSS scroll-driven animations: text effects, progress bars, reveals. The most complete single-page demonstration in the article.
- **42. Highlight text** — Progressive text highlighting in three styles as the reader scrolls. The highlight sweep itself is reproducible with a view() timeline on background-size.
- **43. Reading indicator** — CSS-only reading progress bar on a scroll(root block) timeline.
- **44. Scroll reveal effect with intersection observer** — Classic section fade-in wired to IntersectionObserver. Direct JS counterpart to record prismic-20; keep the observer only when you need a one-shot trigger.
- **45. Airplanes** — Elaborate scroll-driven 3D scene.
- **46. ScrollifyJS + AnimateCSS + CSS flexbox** — Section-by-section scroll hijacking with a library-supplied animation set. Scroll hijacking breaks user expectations and accessibility — prefer scroll snap.
- **47. CSS scroll bars** — Four tube-shaped indicators whose fill tracks scroll position.
- **48. 3D CSS scroll** — Alternating tiles folded into a 3D edge as the page scrolls.
- **49. CSS shadow on scroll** — Top and bottom scroll shadows on an overflowing container, no script. CSS-only precursor to the Chrome scroll-state(scrollable) affordance — compare with chrome-scroll-shadows.
- **50. CSS timeline animation** — Vertical timeline whose entries animate in on their own scroll ranges.

## Tools and libraries covered by the article

Catalogued for context. None of them is installed by this skill; reach for them only after the CSS ladder in `SKILL.md` runs out.

- **AOS (Animate On Scroll)** — data-attribute reveal library; the CSS-native replacement is `animation-timeline: view()` with `animation-range: entry`.
- **GSAP scroll plugins (ScrollTrigger, ScrollSmoother)** — pinning, scrubbing and timeline sequencing beyond what CSS scrubs today. Honour reduced motion via `gsap.matchMedia()`; a CSS media query cannot stop a JS tween.
- **TAOS (Tailwind CSS Animation on Scroll)** — Tailwind-flavoured AOS; same replacement applies.

## Cross-references into the Chrome reference

- Record 9 (`prismic-09-responsive-sticky-header-navigation`) is the exact pen Chrome's article lists as a candidate for deleting its JavaScript with `@container scroll-state(stuck: top)`.
- Record 49 (`prismic-49-css-shadow-on-scroll`) is the CSS-only precursor to `chrome-scroll-shadows`.
- Record 44 (`prismic-44-scroll-reveal-effect-with-intersection-observer`) is the JS counterpart to record 20's scroll-driven fade-in and to `chrome-animated-slide-elements`.
- Records 13 and 14 are the same stacked-card effect, CSS vs. GSAP — the clearest before/after in the catalogue.

# Timeline and assets

## Time model

Read `fps`, width, height, and duration from the actual composition. Choose integer-frame boundaries consistently. `useCurrentFrame()` is relative to a timed component's own timeline; a sequence offset does not automatically make it the composition's absolute frame.

Model cut points as absolute frames and clip duration as the difference between adjacent boundaries. For music, use the absolute-beat formula in `motion-storytelling`; do not accumulate rounded beat intervals.

Use `interpolate` for explicit frame/value ranges with appropriate easing and extrapolation. Use `spring` or the installed version's spring-based easing for physical settles. Clamp when values should hold; allow overshoot only when intended. Deterministic state must produce the same frame when rendered in a different order or sought directly.

## Timing APIs and transitions

Current upstream guidance (4.0.534, studied 2026-10-09) favors direct timing props on supported components. Older projects can use `Sequence`; check the installed version's supported props before migrating.

Where supported, timing operations have distinct roles:

1. `from` places an item in its parent timeline.
2. `trimBefore` chooses the first local frame.
3. `durationInFrames` selects the local range.
4. `playbackRate` maps that range to parent time.
5. `loop` repeats the selected range where supported.

Inspect direct timing/trim/playback support rather than assuming every media or custom component accepts identical props. For a fallback wrapper, verify layout behavior and local-frame semantics. Premount media or timed parents early enough to avoid loading flashes; use the documented API for the project's version.

For `TransitionSeries`, calculate effective total duration after overlap. Ensure transitions fit adjacent shots, inspect seam frames, and keep audio offsets explicit. A transition component is not evidence that playback or a render is glitch-free.

## Media and assets

Use the media components supported by the installed version. Place local public assets behind `staticFile()` when that is the project's convention. Inspect video/audio/image metadata before setting duration, crop, playback rate, and dimensions.

Resolve fonts and media before capture using the documented loading primitives for that version. Do not use arbitrary delays as asset readiness. Confirm remote URLs are accessible to the actual rendering environment; an asset visible in a local browser may be unavailable remotely.

Preserve trim bounds, aspect ratio, crop focal point, audio gain, and text/caption timing through the existing asset manifest. Preview captions at actual delivery size and speed; prevent clipping and verify words/time alignment against audio. For native or generated text, inspect glyphs, line breaks, font fallback, and readable holds.

## Studio editing

When Studio editing is a user requirement, expose relevant schema/props and author independently editable timeline items as separate JSX nodes where that version supports it. Keep editable timing and animation parameters on the source nodes Studio can modify. Programmatic loops are appropriate for intentionally shared generated instances; they may make independent editing harder.

Do not impose Studio-specific markup on a simple render-only project without a benefit. Preserve the user's existing abstractions and changes.

Official references: [Animating properties](https://www.remotion.dev/docs/animating-properties), [Sequence](https://www.remotion.dev/docs/sequence), [Transitions](https://www.remotion.dev/docs/transitions).

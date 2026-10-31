# Lottie and animated illustration

Use this reference for reusable animated illustration, icon/asset choreography, or Lottie delivery. For drag, swipe, momentum, and physical web interaction behavior, use `apple-design` rather than copying that system here.

## Choreography

Set the intended emotion, visual story, and attention target. Use anticipation, staging, follow-through, arcs, or secondary action when they improve the chosen action. Match material and brand: a mechanical move can be linear; a serious cue need not bounce.

Choose the fewest properties that communicate the change. Compare timing, easing, amplitude, and sequence at actual display size and normal speed. Equivalent actions should feel related; numbers from source duration tables are starting estimates.

Primary/support/ambient roles help describe attention. Three moving layers, motion distance below one third, and only one third of elements active are author heuristics. They do not require ambient animation in every asset or make symmetry/opacity/linear motion inherently defective.

## Delivery and accessibility

- Inspect the target player, renderer, package version, platform, and supported AE/JSON features before relying on effects, expressions, masks, or text.
- Export a small representative asset early when feature support is uncertain. Test the actual player; AE preview alone does not establish Lottie compatibility.
- Check loop seams, first/last frames, background transparency, asset/font dependencies, and behavior at intended sizes.
- Keep critical meaning readable in a static fallback. For interactive embedding, respect reduced-motion preferences and provide an appropriate quiet/static or user-initiated alternative.
- Continuous decorative motion needs restraint and relevant pause/stop behavior; avoid large spatial motion and repeated flashes where a quieter alternative serves the same purpose.
- Measure performance with actual complexity and target hardware. Transform/opacity preference does not imply unlimited animated elements or guaranteed GPU performance.

The source provides general motion guidance; it is not an exhaustive Lottie feature-support reference. Look up current official player/exporter documentation for delivery-specific decisions.

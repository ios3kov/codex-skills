# UI motion recipes

Choose a recipe only when it helps explain a state change in the requested interface. Reuse the project's motion tokens and the target platform's tools. These are optional implementation prompts, not a second design workflow. Sources and exclusions are in [the source register](../../../references/ui-refinement-sources.md).

## Choose by the state relationship

Before choosing effects, identify what changes and what remains recognizable. These relationships can overlap; they are not mandatory animation categories.

| Relationship | Use and intent | Check |
|---|---|---|
| Content changes in place | For peer tabs or filters, preserve the shared shell and stable controls while changing the relevant content. Do not imply deeper navigation merely because content changed. | The selected destination and changed region remain clear; unrelated controls do not replay their entrance. |
| Navigation moves deeper | For list-to-item or feed-to-publication, communicate the parent/detail relationship and a clear return. Use the platform's navigation conventions. | Returning restores the relevant list position and selection when appropriate; back is distinct from dismiss or completing a task. |
| The same object expands or transforms | For thumbnail-to-photo, compact-to-full player or product-card-to-details, preserve a recognizable visual anchor across states. | The source and destination refer to the same object; reverse motion reconnects to its current visible source. |

Depth and object continuity may coexist in one transition. A detail screen can open from its card while remaining a navigation step. If the source moved, disappeared or is offscreen, use a coherent simpler return instead of animating to stale coordinates. A direct entry without a source still needs a usable destination. These checks complement the existing interruption and reduced-motion rules; they do not require custom motion where native behavior already explains the relationship.

## Match motion to the interaction

| Situation | Design and implementation prompt | Verify |
|---|---|---|
| A menu or popover opens from a control | Make the visual origin agree with its trigger and placement; for a web transform, check the transform origin against the actual anchored edge. Keep focus and visibility tied to the real open state. | Reopen or dismiss during entry, change placement near an edge, and check focus return. |
| An action is pending, succeeds or fails | Keep feedback tied to the actual operation. Use known progress only when it exists; transition to success only after confirmation. Preserve the action label and layout sufficiently to avoid an accidental second activation. | Slow response, failure, repeated input and cancellation where supported. Animation completion must not masquerade as operation completion. |
| A selected tab, segment or related element changes | If a moving indicator clarifies continuity, derive its destination from the selected element's current geometry. Keep stable identity and preserve the selected state independently of the transition. | Change selection again mid-transition; try longer labels, resized layout and the relevant input methods. |
| A sheet or panel follows a drag | Track the visible position during the gesture, then settle or dismiss according to the product's actual gesture contract. Consider release velocity and distance together where the platform supports it. | Slow drag, fast release, cancelled gesture, interrupted settling and the equivalent non-drag action. |

## Native-feeling dynamics

For application UI, aim for the responsive, continuous feel of native macOS controls without copying every platform effect.

- Carry the release velocity into settling motion when inertia fits the interaction. On retargeting, preserve current visible position and velocity rather than restarting from rest. Respect the control's bounds and existing gesture contract.
- Tune the perceived weight to the element's role, travel and scale. A broad panel usually settles more calmly than a small control; apparent weight must not add input latency.
- Use restrained spring overshoot only when it clarifies momentum or settling. Keep it small and quickly damped; repeated wobbling, routine bouncing labels and bouncing every control are not the goal. A well-damped spring can feel natural without visible bounce.
- Prefer the platform's existing motion or an already installed velocity-aware spring where appropriate. Do not replace native scrolling or impose one mass, duration, damping value or animation library everywhere.
- Review at normal speed: slow drag, fast release, mid-flight reversal and repeated use. Look for abrupt stops, speed jumps, excessive oscillation and delayed response, alongside the existing interruption and reduced-motion checks. Under reduced motion, remove inertia and overshoot where needed while keeping state feedback clear.

## Implement the smallest sufficient transition

- Use an existing capability first: a simple web state transition may need only CSS; a gesture or coordinated layout transition may justify the library already in the project. Do not add Motion, GSAP or another package merely because a recipe contains animation.
- Distinguish initial appearance from later state changes. Avoid replaying an introduction on every update or delaying a frequent control's useful response for decoration.
- Animate the properties needed for the purpose rather than `transition: all`. Choose timing and easing from existing tokens, then judge them at actual speed and with repeated use. A published duration, spring setting or press scale is a starting point, not a universal gate.
- Keep essential state and actions available with reduced motion. Use an immediate state change or a suitable low-motion alternative; removing motion must not remove the confirmation or recovery path.
- Apply [interruption and profiling](../../../references/interface-practice.md#motion-interruption-and-profiling) to retargeting, stale callbacks, pointer cancellation and measured performance. CSS, transforms or a particular library do not by themselves guarantee GPU execution or smooth device performance.

## Report only observed behavior

For implementation, preview the actual interaction and its relevant interruptions. Record the resulting state and any motion or device checks not run. For a plan or static reference, label timing and trajectory as proposals. Do not infer a passing animation, accessibility result or frame rate from a still image.

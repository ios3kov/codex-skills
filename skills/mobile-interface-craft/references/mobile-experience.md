# Mobile experience

Owns the shared mobile behavior contract. Platform adapters explain implementation without repeating this checklist.

## Platform, structure, and task

Use the platform's navigation, selection, input, dismissal, and accessibility conventions when they express the product. Native primitives reduce implementation burden, but their labels, content, configuration, and behavior still need verification. Custom interaction is justified by the brief or a concrete unmet need, not by a default aversion to native chrome.

Choose navigation from the information structure: tabs for peer destinations, stacks for depth, a sheet for a bounded subtask, and a split/side region when available space supports it. Keep back, dismiss, cancellation, and completion distinct. Check Android system back and iOS back-swipe as well as visible controls. Preserve tab-specific history and selection through resizing where applicable. A deep link must reach the intended item through authentication/hydration without losing its destination or creating a dead end.

Use the incumbent semantic theme for surface, text, accent, selected, danger, and disabled states. Preserve approved typography and assets. Prefer platform type/controls where there is no established brand choice. Repeated roles may deserve shared components; repeated numeric literals alone do not justify a new abstraction. Grouping and hierarchy should explain the task, rather than placing every row in a card. Cards, custom fonts, heroes, and gradients are not defects in themselves.

## Available space and input

Size content from its current container/window proposal. Account for small phones, supported landscape/tablet/window modes, system text size, and long/localized content. Avoid a fixed device canvas as production layout. Widen reading gutters or cap long-form text measure when content gains width; do not simply stretch compact rows.

Identify who owns each edge inset: navigator, scroll container, keyboard adjustment, or custom overlay. Reserve space once. Full-bleed backgrounds may extend behind system UI while readable text and controls remain reachable. Test both ends of a list; the final row and bottom action must clear the home indicator/navigation bar and any overlay. Insets and software-keyboard obstruction are related but not interchangeable.

For forms, keep the focused field, its error, and primary action reachable with the keyboard open. Use suitable keyboard type, return-key intent, focus progression, autofill, and password-manager/paste behavior. Test the first tap on controls while the keyboard is present. For drafts, establish when changes persist and what dismiss/back does. On failed save preserve input and a working retry; do not close the editor before success unless an explicit offline/optimistic model preserves the pending work.

## Data and lifecycle states

Separate unresolved loading, resolved empty, no search results, denied permission, unavailable prerequisite, failure, and useful content. Cached content may coexist with refresh or an error. A missing array or an offline-paused request does not establish an empty result. Hydrate persisted auth/setup state before routing decisions that depend on it.

While a mutation is pending, prevent accidental duplicate submission while keeping appropriate cancellation or navigation available. Optimistic changes need rollback or an explicit unsynced state. Scope asynchronous work to the relevant item/query/lifecycle; prevent stale results from overwriting newer intent. Request capability access when its task needs it, and give a usable denied-access path. Validate foreground return and interrupted work when those states affect the changed flow.

## Accessibility and type

Use semantic controls with names and applicable selected, expanded, busy, and disabled states. Preserve the name when a label becomes a spinner. Meaningful imagery needs an equivalent; decorative content beside an existing label should not become duplicate screen-reader stops. Group by reading purpose without hiding independently operable actions. Provide an accessible action for swipe/drag-only tasks.

Use platform units: a typical touch-target baseline is 44 × 44 points on iOS and 48 × 48 dp on Android. A small visual can have a larger hit area, provided neighboring targets do not ambiguously overlap. These units are not CSS pixel rules for websites. Verify focus order and hit behavior in the actual implementation.

Respect system text scaling; let text and rows reflow before clipping, shrinking, or capping it. Verify custom-font glyph coverage and weights with the real languages, including Cyrillic when present. Review optical spacing and semantic line grouping at delivery size. Color alone cannot identify status. Check actual foreground/background pairs in supported themes, including composed translucent surfaces; semantic color names do not certify contrast.

## Motion and feedback

Use feedback to acknowledge input or explain a state relationship. Frequent tasks should not acquire decorative latency. Prefer existing native transitions for platform navigation and presentations. Keep gesture-driven motion interruptible, with continuous direct manipulation, sensible release behavior, and recoverable cancellation. Avoid conflicting scroll, swipe, drag, and back gestures in the same region.

Reduced motion needs a meaningful, gentler equivalent. Haptics are optional reinforcement at the causal event, never the only success/error signal. Do not assume their availability or exact frame timing across hardware. Motion timing and spring values depend on distance, role, platform, and the incumbent motion system; a copied duration or frequency table is not a universal law.

For a changed navigation or object-expansion interaction, consult `motion-design`'s UI motion recipes when available. Let the platform navigator own tab, stack and presentation behavior; do not add a competing transition over its back gesture. For compact-to-full media controls, preserve the same playback session and position across presentation changes. Use existing native behavior when the optional skill is absent.

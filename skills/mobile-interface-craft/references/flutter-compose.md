# Flutter and Jetpack Compose adapters

These narrower adapters come from the UI UX Pro Max stack tables and selected official documentation, rather than a dedicated source corpus comparable to the RN/SwiftUI material. Read the installed framework/toolchain and project's architecture; consult current matching docs for implementation details. Shared mobile behavior and verification remain in their own references.

## Flutter

Preserve the existing state management, routing, ThemeData/ColorScheme, and Material/Cupertino or deliberate brand treatment. Do not require Riverpod, go_router, or a new design system merely because the source table recommends it.

Choose widgets by current constraints, using LayoutBuilder or the relevant MediaQuery values. Support nonlinear scaling with TextScaler where available; do not reduce user text scaling to a single fixed multiplier ([TextScaler migration](https://docs.flutter.dev/release/breaking-changes/deprecate-textscalefactor)). Use lazy list/sliver construction for datasets that warrant it and stable keys for movable stateful records. A fixed itemExtent must fit actual text/content sizes.

Dispose owned text/animation controllers and subscriptions. Keep asynchronous work out of build and prevent completed work from mutating a disposed or superseded feature. Preserve the existing Navigator/router back semantics; for supported versions predictive back uses ahead-of-time pop eligibility, not a late veto after the gesture ([predictive back](https://docs.flutter.dev/release/breaking-changes/android-predictive-back)). Verify the current PopScope callback signature rather than copying an older recipe.

Use widget tests for meaningful state/action behavior, integration/device tests for the primary flow, and Flutter DevTools in profile/release context for measured performance. const and RepaintBoundary are tools, not mandatory wrappers for every widget.

## Jetpack Compose

Retain the project's state owner, theme, dependency injection, and navigation. Hoist state to its real owner; remember is composition-local, rememberSaveable supports appropriate restoration, and durable product data needs its actual persistence layer. Use lifecycle-aware state collection where needed ([Compose state](https://developer.android.com/develop/ui/compose/state)).

Use effect keys that match the lifetime/identity of the work; clean up registered resources with an appropriate lifecycle/effect boundary. derivedStateOf is useful when its output changes less often than its inputs, not for every derived expression. Stable item keys and lazy containers serve dynamic collections. Do not mark mutable types stable merely to suppress recomposition.

Respect Scaffold/system/IME inset ownership, semantic controls, current window constraints, and system text size. Modifier order affects measurement, drawing, and hit behavior. Semantics-based interaction tests, preview layouts, actual device behavior, and profiler measurements answer different questions. Hilt, StateFlow, Channels for navigation, and a particular module structure are project choices, not universal correctness rules.

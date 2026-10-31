# SwiftUI adapter

Read the deployment target, Xcode/Swift toolchain, SDK headers, existing observation model, and architecture. New SDK syntax can require a newer compiler even when a feature back-deploys; runtime `#available` cannot fix a compiler that cannot name a type. Preserve the current architecture rather than mandating MVVM or a migration.

## State and invalidation

Distinguish view-owned state, injected state, and read-only inputs. Keep owned state private. Do not seed a changing parent input into local state and expect subsequent parent updates to replace it. Intentional one-time edit drafts can be seeded locally when their ownership/reset behavior is explicit.

For supported Observation-based code, view-owned `@Observable` instances generally use `@State`; use `@Bindable` where an injected observable needs bindings. With `ObservableObject`, use `@StateObject` for ownership and `@ObservedObject` for injection. Keep a working Combine model during a focused change unless migration is in scope. Observation is available from iOS 17 and aligned releases; consult [Apple's migration guidance](https://developer.apple.com/documentation/swiftui/migrating-from-the-observable-object-protocol-to-the-observable-macro).

Give a view the data it reads and keep rapidly changing dependencies close to the affected region. Track invalidation before adding Equatable conformance or reorganizing state holders. A computed property still executes its expensive work when read; moving a sort out of the textual `body` alone does not establish caching. Keep UI-related mutations isolated appropriately; do not perform blocking work on the main actor merely because the model is UI-owned.

## Identity and collections

Use stable unique model IDs for dynamic `ForEach`/List content. Index identity can describe a fixed structure, but is unsuitable for stateful records that insert, move, or delete. Avoid generating UUIDs or using mutable text as a record's identity during rendering.

Preserve structural identity when the same view changes style; prefer changing modifier values to switching the entire subtree. Genuine optional content or different destinations can branch. Invisible opacity retains layout and may retain hit testing/accessibility; choose removal/hiding deliberately.

For large collections use the appropriate List/lazy container. Filter expensive membership changes outside row construction where possible; keep row structure predictable without banning cheap transformations. Choose List when system editing/selection behavior is useful, not because every scrollable region must be a List. AnyView and custom equality need a demonstrated reason and correct state/dependency semantics.

## Layout, focus, and presentation

Respond to the proposed container size, local size classes, and environment; avoid `UIScreen.main.bounds` as the layout authority for windows, sheets, or split views. Use adaptive system containers, ViewThatFits, AnyLayout, or a custom Layout when they solve an observed requirement. Keep navigation/selection state above a layout branch when it must survive container changes.

Use safe-area placement for controls that must reserve space. Do not subtract/reapply the same geometry inset twice. Scope full-bleed background behavior to the visual layer. Use current environment display scale for image sizing rather than a process-global screen assumption.

Use item-driven sheets when model presence is the presentation source of truth; a Boolean remains appropriate for a simple Boolean presentation. Allow parent action callbacks when the parent owns persistence or business logic; native dismissal does not transfer save ownership automatically. Keep asynchronous completion/failure and cancellation coherent with the shared contract.

For ordinary actions use Button/semantic controls; gestures supplement rather than replace their accessible activation. Use FocusState for the applicable field progression. Read dismiss from the presentation context that actually owns it. Gate version-specific APIs with meaningful equivalent fallbacks and verify those paths. Do not copy SDK 27/27.1-specific constructs from the pinned source without checking the project's toolchain and headers.

## Text, materials, and migration

Use Dynamic Type-aware text styles/custom fonts and scaled layout metrics when needed. Preserve localized literal/resource semantics, locale-aware formatting, leading/trailing layout, and the existing string-catalog/bundle strategy. Avoid concatenated translated fragments and early string resolution that loses the view's locale context.

Liquid Glass is a deliberate requested/platform-system treatment, not a reason to restyle every custom surface. Verify availability, contrast, reduced-transparency behavior, and layering in context. Keep platform-provided chrome behavior distinct from adding custom glass.

Treat soft deprecation as migration advice within scope, not a functional failure. Address hard deprecation/unsupported APIs when needed for the target build. A new API's existence does not require rewriting an unrelated working view. Previews should use self-contained data and cover representative states; preview rendering does not establish keyboard, navigation, VoiceOver, or device performance acceptance.

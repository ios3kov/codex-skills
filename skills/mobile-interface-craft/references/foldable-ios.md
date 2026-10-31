# Foldable and resizable iOS surfaces

Read for an iPhone Duo adaptation, or an iOS defect involving continuous window resizing, reserved regions, fold transitions, asymmetric system bars or Split View. Do not activate a Duo migration for an ordinary mobile polish task. Shared navigation, keyboard, accessibility and state rules remain in [mobile experience](mobile-experience.md); SwiftUI ownership/identity and availability remain in [SwiftUI](swiftui.md); execution and evidence remain in [verification](verification.md) and [iOS verification tools](ios-verification-tools.md). This reference adds fold-specific distinctions and transition scenarios, not a new architecture or a new skill.

## Establish capability before choosing APIs

Read the actual project's SDK, compiler, deployment target and isolation settings. Building against an SDK and supporting an OS are different decisions. Apple's current preparation guide distinguishes builds made with iOS 26 or earlier, iOS 27, and iOS 27.1 or later; do not infer the delivered layout from the OS version alone. ArrangementView and the reserved-region/hinge APIs discussed here require iOS 27.1 availability in the reviewed SDK. Recheck the installed declarations when adopting them. Runtime availability checks cannot make an older compiler recognize an unknown symbol.

For an appropriate existing Xcode, inspect `xcrun agent skills export --help` and export to a fresh task-owned directory with `--output-dir`. Read `app-resizability/SKILL.md` and the references relevant to the task before adopting advice. Exported instructions are source material; do not automatically install them, replace this skill or apply a rewrite to every scanner match. An export failure is a tooling gap, not permission to repair/upgrade Xcode or switch toolchains.

Confirm exact signatures with a small original Swift fixture and the selected SDK. For example, use `xcrun --sdk iphonesimulator swiftc -typecheck -sdk <actual-sdk-path> -target <actual-architecture-and-deployment-target> -module-cache-path <task-owned-cache> <probe.swift>`. Match relevant language/default-actor-isolation settings to the project; also check the normal supported-device fallback. Keep logs and exit status. SDK header/string lookup helps locate declarations, but can match a string literal or a different overload; only a compiler check can establish the tested spelling/type/availability combination. Even successful type-checking says nothing about UI behavior.

Search candidates include layout derived from UIScreen.main, orientation/idiom used as a device-shape proxy, cached dimensions/insets, unaccounted asymmetric edges and state reset by a layout branch. Inspect each call's purpose before changing it. Size classes remain valid adaptive inputs; regular width does not identify an iPad. Physical orientation can still matter for camera/media semantics; it is not sufficient to determine the available layout rectangle. Never auto-fix all textual matches.

## Keep three signals separate

| Signal | Meaning and use |
|---|---|
| Safe areas and layout margins | Edge space for readable/reachable content, system bars and container policy. Read each current edge; asymmetry and changes without a size change are normal. Let existing system containers own their insets. |
| Reserved regions | Local areas to avoid or divide around. `.occlusion` can cover content (for example a camera); `.division` can split a surface around the fold. They are not another set of four edge insets. |
| Hinge status/angle | Optional posture information. Use only for a genuine posture-aware interaction; it does not provide the container's usable geometry. Handle unavailable/unknown state without losing functionality. |

In the reviewed public APIs, SwiftUI `onHingeChange` provides an optional hinge with status and an `Angle`; UIKit `UIHingeInteraction` provides optional hinge updates whose angle is in radians. Prefer the provided status when only closed/partially-open/fully-open distinction is needed. Do not assume update frequency, precision or a universal angle threshold, or treat missing hinge data as proof of a particular device or posture.

## Lay out in the owning container

Measure the view/window that actually positions the content. A device screen rectangle is not the size of a sheet, split column, nested panel or resizable scene. Refresh geometry through the framework's layout/geometry lifecycle; do not cache launch-time dimensions. Retain normal local size classes, adaptive system containers and constraints where they fit the product.

For custom content, query `GeometryProxy.reservedRegions(kind:options:layoutDirectionBehavior:)` in SwiftUI or `UIView.reservedRegions(kind:options:)` in UIKit at the layout owner. Compare region frames and content in the same current coordinate system. UIKit frames use the queried view's coordinates in points; a partial intersection can extend outside its bounds or start negative. Convert explicitly before comparing geometry from different containers. In SwiftUI, account for the query's layout-direction behavior; do not mirror/convert the result twice. Test leading/trailing semantics in RTL separately from physical left/right inset values.

Queries normally return active regions. If requesting `.includeInactive`, inspect `isActive` before treating a region as a current obstruction. Reserving space for an inactive region can be an intentional stability choice; document that choice instead of treating every potential region as blocked. A region's frame already includes its margins: do not expand it by those margins again. Likewise, do not add safe-area clearance a second time when the navigator, adjusted scroll inset or container has already applied it. Identify ownership of each adjustment rather than subtracting every measurement from the available space.

Prefer system containers for adaptation they already handle. ArrangementView is useful for related primary/secondary content: `.split` keeps areas separate; `.overlay` layers content on a flat surface and can separate it around an active fold. Keep the roles and content relationship explicit. Follow Apple's container-composition limits; do not mechanically nest ArrangementView in a ScrollView, grid, NavigationSplitView or another competing layout container, or embed TabView/NavigationSplitView inside it. Use it only where it improves this surface. System sheets and split views already adapt to reserved regions; keep working sheets unless an observed requirement justifies a different presentation.

If more space appears, reveal useful hierarchy or controls without changing what the task means. Avoid disruptive rearrangement during an interactive fold. On narrower or ordinary devices, keep a complete, usable flow: reachable destinations/actions, the same data and state, and a version-compatible native layout. Do not require hinge data or a Duo-only API to perform an existing task. No deployment-target increase or framework/dependency migration is implied.

## Preserve continuity and prevent repeated effects

Keep the existing owner of drafts, selected record/tab, navigation path, scroll anchor, focused field and playback session stable across container changes. Moving state above a layout branch is useful when the current ownership would destroy it; it is not a mandate to replace the architecture or ban conditional views. Use stable semantic item IDs for selection and scroll restoration rather than raw pixels from a different geometry. Preserve media time, play/pause intent and the appropriate audio session. Reconcile focus to a surviving semantic control after layout is ready if the old control disappears; do not reset focus on every geometry event or rely on a fixed delay.

Treat folding/resizing as layout changes, not a new user action. Rebuilt views, changed task IDs and lifecycle callbacks must not repeat fetches, uploads, sends, subscriptions or purchases. Reuse in-flight work and existing idempotency/transaction ownership as appropriate. A legitimate query change can request new data; establish which event causes it. Verify counts/identities of requests and mutations across transitions, including pending/failure/retry. Preserve drafts and pending results when sheets or navigation containers adapt. Do not solve a duplicate side effect by globally suppressing lifecycle callbacks.

## Transition matrix: verify the affected task, not just endpoints

Use supported Xcode/Device Hub controls or the project's existing permitted XCTest/device workflow. Pick an existing exact target and record it. Do not use private simulator APIs or foldsim, hinge or duo_pose.py. A generic resized simulator or forced trait change is evidence of resizing/traits only, not proof of actual folding or reserved-region behavior.

| Transition or variation | Observe and verify |
|---|---|
| Outer → fully open inner → outer; reverse and repeat | Same selected item/tab, navigation/back destination, draft and scroll anchor; no accidental completion or duplicate side effect. |
| Fully open ↔ partially open; portrait/landscape where supported | Active/inactive division changes, primary/secondary placement, reachable controls; no universal hinge-gap or angle constant. |
| Continuous resize through intermediate/narrow/wide container sizes | Content reflows without clipped required text/actions, stranded columns or unstable feedback loops. Include sizes between named presets. |
| Keyboard shown/hidden and focus during a transition | Draft/caret or semantic focus preserved where supported; focused field, errors and submit action remain reachable; keyboard and safe-area clearance counted once. |
| App on left and right sides of Split View; resize each side | Local coordinates/insets remain correct when the system bar changes edge; selection and navigation survive column collapse/expansion. Include RTL when supported. |
| Open sheet/popover/dialog, pending save/send/purchase, or failed request | Presentation remains usable; pending operation identity and result preserved; no second mutation. Check cancel/back/retry rather than changing every sheet to fullScreenCover. |
| Large accessibility text and long/localized content | Reflow and usable actions at relevant intermediate sizes; no essential text hidden merely to preserve a two-pane composition. |
| VoiceOver active while layout changes | Actual spoken traversal follows the visible task; controls retain names/states and logical grouping. Verify focus recovery and accessible alternatives; XCUI query order or a screenshot is not VoiceOver proof. |
| Playback across fold/resize/background return when applicable | Same content, current time and play/pause intent; no duplicate player/session or unrelated playback restart. |
| Ordinary supported phone/tablet and the older-OS path | Existing feature remains complete with no hinge signal and no new API at runtime; compile and exercise the supported fallback. |

For geometry evidence, use an authorized temporary debug probe or existing test instrumentation to record current container bounds, each safe-area edge, region kind/frame/isActive and any genuinely needed hinge status/angle. Record target, OS, build/revision and scenario. Measured simulator pixels/points are observations for that run, never device constants or production thresholds. Inspect the actual rendered result and interactions separately from logs.

Record each criterion using PASS, FAIL, BLOCKED or NOT RUN, with the relevant evidence. A compiler PASS is limited to that SDK/target/settings/sample. A scanner with no findings cannot prove adaptation, and a simulator layout check cannot establish physical-device continuity, VoiceOver behavior or performance. Missing hardware/runtime/access remains an explicit gap; complete unaffected authorized work.

## Sources and bounded adoption

Reviewed 2026-10-31. This is an original, local operational synthesis. All essential rules above are available offline; links are provenance and optional authoritative updates. No community executables, app templates, simulator controls, build settings or Apple skill bundle are installed. Exact snapshots, file identities and license boundaries are in [sources.json](sources.json); attribution notices are in [THIRD_PARTY_NOTICES](../THIRD_PARTY_NOTICES.md).

Apple: [preparation](https://developer.apple.com/iphone-duo/prepare/), [technology overview](https://developer.apple.com/documentation/technologyoverviews/preparing-your-app-for-iphone-duo), [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo), [ArrangementView](https://developer.apple.com/documentation/swiftui/arrangementview), [UIView.ReservedRegion](https://developer.apple.com/documentation/uikit/uiview/reservedregion). Local Xcode27.2 export was read as source, not installed. Its broad automatic-rewrite and mandatory-per-match-diff policies are not adopted.

Community methods only, under MIT notices:
- [hechen/iphone-duo-skills](https://github.com/hechen/iphone-duo-skills/tree/3d0e4532534bc090513e0fda416dd4d4f229910b): transition matrix and exact-SDK compiler-probe method; selected check-sdk.sh, iPhoneDuoProbe.swift and iphone-duo-testing reviewed.
- [alexey1312/iPhone-Duo-Agent-Skill](https://github.com/alexey1312/iPhone-Duo-Agent-Skill/tree/98cdb7c19d9cbb07ded0bd7966e109a4ef0d8f4a): duo_scan.py and sdk_api_check.py reviewed with imports/tests; scan findings and textual symbol matches stay candidates, not proof or automatic fixes. No executable installed.
- [Kimeur/duology](https://github.com/Kimeur/duology/tree/49d4658705d31b49c4b1d6e0aaa4012ab38c2290): selected continuity, accessibility and testing scenarios only.
- [sven-ericmolzahn/iphone-duo-skill](https://github.com/sven-ericmolzahn/iphone-duo-skill/tree/1029d2ffe23360ad89568efbfd58dd2c394c1788): compile examples under actual settings and measure local geometry; no copied dimensions or private pose controls.

---
name: mobile-interface-craft
description: Design, implement, review, and refine native mobile screens and task flows for iOS and Android, with focused guidance for React Native, Expo, SwiftUI, Flutter, and Jetpack Compose. Use for mobile navigation, forms, keyboard and safe-area behavior, adaptive text, native controls, or measured UI performance. Responsive websites alone remain with interface-craft.
---



# Mobile Interface Craft

For offline use and external-reference handling, read [local resources](references/offline-resources.md).

Deliver a usable mobile task flow in the project's actual platform and visual system. A request for polish preserves the incumbent brand, architecture, content, routes, and data contracts unless their replacement is authorized.

## Read by decision

First detect the surface and versions from the project: app manifests, lockfiles, native targets and deployment settings, navigation, styling, and existing screen code. A phone-sized website is not a native app; an Expo app still uses React Native. Do not select a new framework because this skill supports it.

| Decision | Read |
|---|---|
| Screen behavior, navigation, forms, insets, adaptive text, or accessibility | [Mobile experience](references/mobile-experience.md) |
| React Native rendering, lists, state, gestures, or native dependencies | [React Native](references/react-native.md) |
| Expo UI layers, routes, SDK compatibility, or build environment | [Expo](references/expo.md), plus React Native only for the RN topics involved |
| iPhone Duo adaptation, continuous iOS resizing, reserved regions, fold continuity or asymmetric Split View | [Foldable iOS](references/foldable-ios.md), only for the affected fold/resizing decisions |
| SwiftUI ownership, identity, layouts, presentation, or availability | [SwiftUI](references/swiftui.md) |
| Flutter or native Jetpack Compose implementation | [Flutter and Compose](references/flutter-compose.md); this is a narrower adapter, not a full framework manual |
| Real mobile reference screens/flows or Mobbin access | [Mobile references](references/mobile-references.md) |
| Runtime validation or a performance claim | [Verification and measurement](references/verification.md) |
| Executing iOS builds, simulator diagnostics, or string-catalog checks | [iOS verification tools](references/ios-verification-tools.md) |

Load only the references governing the current decision. [Sources](references/sources.json) records pinned upstream provenance and boundaries, not runtime dependencies.

## Apply a focused pass

1. Identify the main user task, entry and completion, fixed constraints, affected states, and observable acceptance conditions. Inspect the existing screen and system before choosing replacements.
2. Choose native platform behavior and a coherent visual direction. Extend the actual theme/component library. Make any deliberate platform-neutral branding explicit; do not confuse identical pixels with equivalent platform behavior.
3. Implement the affected flow with actual content. Keep logic, drafts, asynchronous state, navigation, and presentation consistent. A prototype may use local data when that is the brief; working-product controls need the advertised behavior.
4. Exercise the flow and inspect its rendered result using the verification reference. Correct defects, then repeat affected checks. Distinguish functional behavior, visual/editorial quality, and source fidelity.

For reference discovery, use the available `design-reference-research` workflow; the mobile reference adds only mobile context. For optional style/palette/type alternatives, use the existing `interface-craft` catalog rather than duplicating its data. Brand identity remains with `brand-system`; Apple-style physical web motion remains with `apple-design`. Existing engineering requirements and release gates remain with the project's engineering workflow. These complementary skills are not prerequisites for an ordinary mobile fix: if absent, inspect the project and authoritative platform documentation directly.

For iOS tasks needing a library, tool or implementation example, optionally search [Awesome iOS](https://github.com/vsouza/awesome-ios#readme) for candidates. Compare with native Apple APIs and existing project dependencies first. Before recommending or adopting a candidate, inspect its original repository and documentation for maintenance, Swift/Xcode and deployment-target compatibility, license and integration cost; catalog inclusion is not an endorsement. If unavailable or unhelpful, continue with authoritative platform documentation and other sources. This does not authorize installation or a change of architecture.

For iOS Simulator builds, tests, app launch, UI interaction or captures, use the locally installed `ios-simulator-skill` when it fits the task. Locate its loaded directory and read its SKILL.md; check actual Xcode/runtime, Python and idb availability before choosing commands. Use an explicit target simulator and verify each operation against the resulting UI or build evidence. Simulator checks do not replace real-device acceptance or visual inspection. Missing dependencies or failed checks remain explicit; use available Xcode tools where suitable rather than claiming simulator interaction passed. Installation does not authorize erase/delete, app-data removal, permission changes or dependency installation outside the task.

## Boundaries

Framework-specific upstream preferences are recommendations until they fit this project, installed versions, and measured problem. Do not mandate a state library, architecture, animation package, styling syntax, icon family, or new native build merely to satisfy a source checklist. Use current version-matched documentation for APIs absent from installed types/SDK headers. Tool setup, publishing, paid builds, telemetry submission, and account configuration are separate from designing a screen.

Close with what changed, the flow and environments actually inspected, and remaining gaps. Use PASS/FAIL/BLOCKED/NOT RUN for specific checks, not as a blanket design-quality score.

# Expo adapter

Adds Expo-specific decisions to the shared mobile and React Native references. Read the project's Expo SDK, Expo Router version, app config, architecture, package manager, and existing native-directory/build strategy before selecting APIs. Match documentation to that SDK; a `latest` example is a lead, not a compatibility guarantee.

## UI and routes

Evaluate native UI capabilities already available to the app. Recent `@expo/ui` versions offer universal and platform-specific SwiftUI/Compose components; check the installed version and exports, required Host boundary, platform availability, and native-build support ([Expo UI](https://docs.expo.dev/versions/latest/sdk/ui/)). Isolate platform-specific imports so they cannot execute on an unsupported target. Short grouped native rows and virtualized datasets serve different purposes; a native-looking `List` does not imply recycling.

Use the existing Expo Router route/layout structure for links, stack presentation, headers, and tabs. Keep route files distinct from ordinary component/utilities. Confirm deep-link paths, groups, dynamic parameters, and return paths. Prefer supported native headers/sheets when they meet the flow. NativeTabs and newer stack APIs change across Router/SDK versions; inspect actual installed types before copying import paths or option names. Do not add frequent previews or context menus without a useful task.

Keep a coherent cross-platform icon treatment. SF Symbols are Apple-platform assets; provide supported Android equivalents when using them. A verified custom brand icon family is also valid. Preserve names, active-state meaning, accessibility labels, and rendering on every supported target.

## Theme boundaries

Extend the existing theme/styling library rather than adding a second `theme/` next to it. Use native semantic colors where supported and appropriate, with explicit brand roles where needed. Resolve theme updates on both platforms and web if that target exists. Opaque native color values are not hex strings: a TypeScript `as string` assertion does not convert them at runtime. For a string-only third-party prop or animation, supply a compatible resolved/static theme color through a deliberate adapter.

Embed fonts through a config plugin when native build-time availability fits the app's build strategy; runtime loading is appropriate where needed, including Expo Go/web workflows. Verify actual font-family names, weight mapping, language coverage, and splash/loading behavior. Do not require prebuild solely to replace a functioning font-loading path.

## Runtime choice and dependencies

Expo Go is useful for a compatible quick prototype, not a mandatory first step for every existing app. A development build gives control over native libraries and configuration and is recommended for an app intended for store release ([development builds](https://docs.expo.dev/develop/development-builds/introduction/)). Use the project's established development client when present. Performance acceptance uses an appropriate release/profile environment, not Expo Go.

When an authorized implementation needs a dependency, use SDK-compatible resolution with the project's package manager/Expo tooling and verify native support. Config plugins, custom modules, notification capabilities, links, and extensions may require a rebuilt development client. Review generated native changes; a clean prebuild can replace custom native content. Do not run it merely because an upstream recipe includes it.

Keyboard-synchronized custom UI may need a supported keyboard-controller integration/provider. Ordinary forms can use a tested existing solution. Reanimated/Worklets and Babel-preset behavior depend on the SDK and architecture; do not add duplicate plugins without inspecting configuration. The shared references own input behavior, gestures, data states, and measurement.

Source feedback/telemetry commands, remote simulator setup, EAS paid jobs, OTA updates, TestFlight submission, and store publication are outside a screen task unless explicitly included in its authorization.

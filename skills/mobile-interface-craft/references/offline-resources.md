# Local mobile API reference

The bundled swiftui, react-native, expo and flutter-compose references contain the complete adopted workflow. Their links are optional update sources. Start with installed package versions, SDK headers, declarations and project examples; the frozen notes cannot certify a newer API.

## SwiftUI ownership

For Observation code on supported OS versions, view-owned @Observable state commonly uses @State; use @Bindable when binding into an injected observable. Legacy ObservableObject ownership uses @StateObject, while an injected object uses @ObservedObject. Do not switch a working ownership model during an unrelated fix. Inspect deployment targets and available SDK symbols locally.

## React Native and Expo

Use stable item IDs. Test recycled rows for stale state, image identity and subscriptions. FlashList v1/v2 APIs differ; v2 requires the New Architecture and removes v1 estimate props. Inspect the installed declarations before supplying props. ScrollView contentInset/contentInsetAdjustmentBehavior are iOS facilities, not a general Android safe-area solution. Measure the actual container and avoid duplicate navigator insets.

For continuous gestures use the installed UI-runtime shared-value system; do not send every frame through React state. Reanimated/Compiler get/set guidance applies only to versions that support it; never read or mutate shared values during React render. Inspect actual Babel/worklet setup and build architecture. Native dependency changes require the project's real native rebuild, not a Metro restart alone.

Expo UI exports, host boundaries and platform availability are version-specific. Inspect installed exports and native requirements. A native-looking list is not proof of virtualization. Follow the existing development client for native packages; Expo Go compatibility is not release-performance acceptance. In monorepos inspect dependency resolution, duplicate native instances and actual autolinking output rather than guessing scan depth.

## Flutter and Compose

Use constraints and current TextScaler support for nonlinear text scaling. Dispose owned controllers/subscriptions and reject async updates after disposal. Preserve router/back behavior; supported predictive-back flows need ahead-of-time pop eligibility rather than a late gesture veto. Inspect the actual PopScope callback signature in the installed SDK.

Compose remember is local to composition; rememberSaveable restores supported state, while durable records need real storage. Hoist state to its owner, use appropriate lifecycle collection and test restoration. Preserve existing theme/navigation/injection.

Snapshot reviewed 2026-10-20. Original operational summary; source credits remain in the existing references.

# React Native adapter

Use installed React Native, React, navigator, renderer architecture, and library versions. Expo-specific decisions belong in [Expo](expo.md); product behavior belongs in [Mobile experience](mobile-experience.md).

## Rendering and ownership

Render text through `Text`, not as a raw child of `View`. Use explicit boolean checks or a ternary for conditional content whose condition can be a number; leaking `0` through `count && ...` can create an invalid raw text node. Keep one authoritative value for user intent and derive simple display values. A local override with a server fallback is appropriate only when its reset/update semantics match the feature.

Keep high-frequency dependencies near the smallest affected subtree. Profile an observed rendering problem before introducing selectors, memoization, or a new store. Stable object/function references can help a memoized boundary; they are not a ban on inline callbacks, `map`, `filter`, or ordinary Context. Filtering changes membership deliberately; mapping to fresh objects can change reference identity. Distinguish these costs from array identity itself. Accessing an object method does not inherently create a new function, and destructuring does not guarantee stability or preserve a method's `this` semantics.

For inputs, retain controlled state when React needs current values for transformation, validation, masking, or UI behavior. If typing visibly lags, profile the typing path and defer expensive derived work. An uncontrolled input is a targeted alternative when native ownership fits reset/save semantics; converting every form is not a performance strategy.

## Lists and images

Choose an eager scroll container for bounded content that mounts cheaply; virtualize large/unknown datasets or measured expensive lists. Keep one scrolling owner per axis unless nested scrolling is an intentional, tested interaction. Do not nest a virtualized vertical list inside an eager vertical ScrollView.

Use stable item IDs for data that moves or changes. Recycling requires correct per-item local state, side effects, image identity, and heterogeneous item types where the chosen list supports them. Fixed-height optimizations apply only when row height really remains fixed with actual content and text scaling. FlashList v2 removes size-estimate props used in v1 and requires the New Architecture; match guidance to the installed major version ([v2 changes](https://shopify.github.io/flash-list/docs/v2-changes/)).

Request media near its rendered pixel size, considering the device's display scale rather than assuming every screen is 2×. Check caching, placeholders, failure behavior, and recycled-cell image reset. `expo-image` is an option when its capabilities and native dependency fit; a gallery library is not required for every image.

## Insets, gestures, and motion

`contentInsetAdjustmentBehavior` and `contentInset` are iOS-specific ScrollView facilities, not a complete Android inset solution ([ScrollView docs](https://reactnative.dev/docs/scrollview)). For custom content use the project's safe-area integration on the appropriate edges; verify navigator-managed space before adding padding. Use current window/container measurements for responsive decisions and `onLayout` when local size is needed. Synchronous DOM-style native measurements require version support; do not copy a new-version method into an older RN project.

Prefer semantic `Pressable` or equivalent native controls for ordinary actions. A custom gesture recognizer needs equivalent accessibility and activation behavior; smoother visual feedback does not justify losing them. Use the incumbent native-driver/worklet approach appropriate to the interaction. Prefer transform/opacity for motion that should not affect surrounding layout; genuine layout changes need a suitable layout animation, not a scaled-text substitute.

Do not send per-frame scroll/gesture updates through React state or RN-runtime callbacks. Use UI-runtime values for continuous visuals and discrete callbacks for meaningful events. For Reanimated with React Compiler, follow documented shared-value `get`/`set` usage; do not read/write shared values during React render ([useSharedValue](https://docs.swmansion.com/react-native-reanimated/docs/core/useSharedValue/)). Worklet scheduling, Babel setup, and architecture support differ by version. Reanimated 4 guidance is not a reason to upgrade a working v3 app during an unrelated fix.

## Native integration

Keep the project's styling conventions; inline styles, StyleSheet, and supported styling libraries have different tradeoffs. Verify `boxShadow`, continuous curves, and experimental gradients against platform, OS, and renderer support before using them.

In monorepos check dependency resolution, duplicate React/native module instances, autolinking output, and the native app's declared dependencies. Do not assume that every autolinker scans only the app's `node_modules`; behavior and recursive resolution vary ([Expo autolinking](https://docs.expo.dev/modules/autolinking/)). Rebuild when actual native dependencies/configuration change; avoid speculative overrides or generated-native-directory edits that the project cannot preserve.

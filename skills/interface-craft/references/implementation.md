# Implementation, Accessibility, and React

## Semantics and states

Use native elements for their roles: buttons for actions, links for navigation, labeled controls for forms, and semantic tables/headings for structured content. Native controls already provide keyboard behavior; do not add redundant handlers that cause double activation. Custom controls need the appropriate keyboard interaction and semantics.

Keep visible focus, accessible names for icon-only actions, meaningful image alternatives, and decorative media hiding. Manage focus when a modal opens/closes and after a failed submission as appropriate. Sticky chrome must not obscure focus or anchored headings. Announce relevant asynchronous status/error changes without turning every visual update into live-region noise.

Use suitable input types, names, autocomplete, and input modes. Allow paste. Connect helper/errors to their fields; provide a recoverable next step. Represent loading, success, empty, disabled, and error states needed by the actual interaction. Preserve form field and analytics contracts during visual changes.

## Standards versus usability choices

- WCAG AA text contrast is generally **4.5:1**, or **3:1 for large text**: at least **18 pt / 24 CSS px**, or **14 pt / about 18.67 CSS px when bold**. A plain 18 px label is not automatically large text. Check foreground/background combinations across relevant states and images, not just token pairs.
- WCAG 2.2 AA target-size minimum is **24×24 CSS px**, with defined exceptions including spacing, equivalent controls, inline targets, user-agent controls, and essential presentation. **44×44 CSS px** is a useful touch-usability target and relates to the stronger enhanced criterion; do not label every smaller control an AA failure without checking the applicable criterion and exceptions.
- UI boundaries and graphical objects may require **3:1 non-text contrast** when they convey information needed to identify a component/state. This does not make every decorative border subject to the same requirement.
- Reduced-motion support is required for the applicable interaction and user needs. Prefer explicit transitioned properties, usually `transform` and `opacity`; avoid `transition: all`. If another animated property is justified, check layout/paint cost and the reduced variant.

Technical authorities: [text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html), [target-size minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html), [non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html). Verify the current criterion before a formal compliance claim.

## Responsive and robust layout

Use CSS grid/flex and content-aware layout before DOM measurement. Test long labels, translated text, empty data, large counts, and narrow viewports relevant to the product. Use `min-width: 0`, wrapping, and overflow handling where needed; do not clip essential content or suppress horizontal overflow to conceal a broken layout. Preserve zoom and keyboard access.

Reserve image/media dimensions to reduce layout shifts. Prioritize the actual above-fold critical asset and lazily load suitable below-fold media. Use compressed assets and a still alternative for decorative motion. Ensure themes remain legible; do not introduce a new theme solely because an upstream source prescribes it. Locale-aware numbers/dates should follow the product's established locale policy.

Keep navigation as real links and preserve routes/deep links. Synchronize shareable filters/tabs/pagination with the URL when that helps the product; transient hover, drag, or modal internals need not all become URL state.

## Focused React/Next.js performance

Detect the installed React/framework version and architecture. Apply rules to that stack, especially compiler behavior, RSC boundaries, caching APIs, resource hints, and newer hooks. Read the relevant official documentation before adopting a version-dependent API. Avoid cargo-cult memoization or package replacement.

Investigate in this order when symptoms match:
1. **Waterfalls:** start independent operations together; await when the result is needed. Retain dependency order and intended failure semantics. Use appropriate loading/Suspense boundaries without hiding errors.
2. **Bundle weight:** inspect the built bundle and expensive imports. Use supported public subpath imports or the framework's package-import optimization; verify types and exports. Load heavy optional features lazily when it improves the actual path. Do not blindly deep-import undocumented library files.
3. **Server/client boundaries:** keep genuinely static work server-side where the framework supports it; isolate interactive leaves. Send only needed data across boundaries. Request deduplication and cross-request caches have different ownership/lifetimes; do not share user-specific mutable state or cache sensitive data under a common key.
4. **Rendering:** keep input updates cheap, derive values during render when suitable, and put interaction logic in event handlers rather than effects. Memoize demonstrated expensive work with stable dependencies. Use transient references/motion values for high-frequency values that do not need React rendering.
5. **Long content:** consider virtualization or `content-visibility` when cost is observed. Preserve keyboard navigation, find-in-page/accessibility requirements, and state while evaluating alternatives.
6. **Hot paths:** batch DOM reads/writes and improve repeated lookups or allocations only where they materially affect performance.

Measure the affected path before and after with comparable build, device/viewport, data, and cache conditions. A smaller file or additional `memo` call is not proof of a faster experience. Avoid carrying upstream benchmark percentages into a project without measurement.

For detailed patterns, use the pinned Vercel source map in [sources.json](sources.json) and load only the applicable rule file (`async-*`, `bundle-*`, `server-*`, `client-*`, `rerender-*`, `rendering-*`). This adapted skill intentionally does not install the upstream search database or launchers.
## Mobile-browser symptoms and restrained interaction
For a mobile website or PWA, diagnose the actual browser symptom rather than applying native-app fixes. Gate hover-only decoration by input capabilities and keep touch and pointer use compatible on hybrid devices. For changing browser chrome, choose dynamic or small viewport units from the layout's purpose and supported browsers; a viewport unit alone does not solve keyboard obstruction. Check the focused input, bottom action and scroll recovery with the keyboard open. Count safe-area spacing once. Preserve pinch zoom; if focus unexpectedly zooms a field, inspect its rendered font size and browser behavior instead of disabling zoom. Scope touch-action, overscroll and selection rules to the affected gesture/control: retain page scrolling, selectable body text and existing tactile feedback unless the task warrants a change.
For grouped tooltips, distinguish intentional first activation from movement within an already active toolbar. Consider skipping repeated delay and entrance motion while moving between neighboring targets, using the component library's supported delay-group behavior. Verify keyboard focus and dismissal as well as pointer hover; a tooltip must not carry essential information available nowhere else.
When reducing motion, judge its purpose, repetition and observed delay. Keep state feedback and orientation where they help; keyboard activation alone is not a reason to delete a transition. Before removing motion, check hidden starting styles, exit/unmount logic, animation/transition event handlers, pending promises and focus restoration. Confirm that reduced-motion and interrupted paths still reach a visible, usable state. Avoid automatically removing the underlying dependency.
For animation jank, identify whether the cost is layout, paint, compositing or application work in a representative trace before changing strategy. Existing high-frequency rendering guidance applies; avoid blanket will-change, universal blur limits or replacing layout with scale when that distorts text or breaks surrounding flow. Browser/device measurements govern optimization claims.
Source: independently worded adaptation of Emil Kowalski's emil-design-eng, mobile-native, remove-animations and animation-performance at [a81dbca07f2217b7103e510c0f13f8d5b017afc9](https://github.com/emilkowalski/skills/tree/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills). No upstream code, launchers or artwork copied. These local instructions are usable offline; source links are provenance, not required services.

# Browser Verification

## Select the actual runner

Use the project's available browser/test setup. Prefer an established Playwright suite for repeatable regressions; an available documented computer-use/browser tool can verify a focused visual interaction. Do not assume a particular Python runtime, browser engine, upstream server helper, or invented tool API exists. Read the runner/tool's current documentation and use only supported calls.

If using Cua, initialize with the appropriate documented entrypoint, then read the returned documentation before continuing. Observe the rendered UI to discover targets and use the browser API that is actually exposed. Do not copy Playwright method names into an unrelated browser tool.

Inspect the project server configuration, reuse an already-running correct instance, or start the needed development/preview server through the supported workflow. Identify the URL/build under test. Any added server helper must have its dependencies and lifecycle verified; this skill does not bundle Anthropic's helper scripts.

## Readiness and interactions

A successful navigation is not necessarily a ready application. Wait for an observable state required by the scenario: the named form, loaded data row, enabled action, visible error, or completed result.

With Playwright, prefer role/name, label, and other stable locators tied to observed semantics. Use locator actions and auto-retrying assertions. Choose a test ID when the user-facing semantics do not provide a stable target. Confirm selector identity and uniqueness before acting.

Do not use `networkidle` as a blanket readiness condition: background connections may never settle, while idle network does not establish application readiness. Do not use fixed sleeps as functional assertions. Use explicit application-state checks or retrying assertions; fixed delays are appropriate only for a deliberate timing experiment or debugging observation with stated limits.

Inspect rendered state before deciding how to act on a dynamic interface. Source markup can help locate a static target but does not prove hydration, visibility, enabled state, or behavior.

Official references: [Playwright Page API](https://playwright.dev/docs/api/class-page), [auto-retrying assertions](https://playwright.dev/docs/test-assertions), [locators](https://playwright.dev/docs/locators). Verify version-specific methods before adding new test code.

## Scope verification to the change

A visual tweak usually needs visual inspection and the affected interaction. A behavioral fix needs reproduction of the original symptom plus meaningful regression coverage. Do not write a test that only repeats implementation structure or expand to a full-product suite without a concrete reason.

Where applicable, check:
- The main flow and affected navigation/actions using actual rendered controls.
- Keyboard access, visible focus, and focus restoration; target-relevant accessible names and labels.
- Relevant loading/empty/error/success states and long content.
- Representative desktop/mobile viewports; reduced-motion or theme states affected by the change.
- Console/page errors attributable to the tested build and scenario.

For screenshot comparisons, use comparable route, viewport, content, font loading, and state. A screenshot proves captured appearance only; it does not prove working buttons, screen-reader behavior, or performance. Avoid hiding real failures merely to obtain a clean screenshot.

Capture concise evidence: the tested build/route, environment, scenario, expected result, observed result, and useful screenshot/log location. Use the engineering workflow's existing result labels; `NOT RUN` and `BLOCKED` do not become `PASS` because static review succeeded.

Close runners or stop servers started for the check when they are no longer needed; preserve a user-owned browser/session or server. A missing runner or unsupported target browser is a verification limit to report while completing the remaining authorized checks.

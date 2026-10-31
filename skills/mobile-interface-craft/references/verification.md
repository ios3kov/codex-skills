# Verification and measurement

Owns native validation and performance evidence. Reuse the project's existing acceptance criteria/test workflow; apply only checks material to the changed flow. Generic release, security, and publication gates remain outside this reference.

## Validate the actual result

Bind results to app/bundle identity, candidate revision or artifact, build type, OS, device/simulator, relevant settings, and the exercised scenario. Check the main action to completion and relevant failure/retry/back/dismiss paths. For an affected form, open the keyboard; for changed navigation, test the actual platform back mechanism; for asynchronous state, observe first load and a failed refresh/save rather than only supplying a content screenshot.

Inspect rendered screens at representative small and large supported contexts, normal and large system text, actual content extremes, and supported themes. Include landscape/tablet/window modes when supported and affected. Review headline/intro optical spacing, glyph coverage/collisions, and semantic line grouping at delivery size. Verify target geometry, focus order and names, action alternatives, reduced motion, and contrast for relevant states. Static screenshots do not establish screen-reader or interaction behavior.

Use available authorized device/simulator tools with the correct pinned target. Refresh selectors after meaningful navigation; prefer semantic IDs/roles over coordinates. Device tools such as agent-device, XCTest/XCUITest, Android instrumentation, Maestro, or Detox are optional and version-specific. Do not assume installation/account access, or start paid remote device sessions from copied recipes. A missing required environment yields a named NOT RUN/BLOCKED gap, not a substituted browser PASS.

Component tests should exercise the user's outcome: mutation pending/failure/retry, permission fallback, selection, or accessible activation. For RNTL check the installed major's synchronous/async APIs; query by role/name where supported and perform actions outside retrying wait callbacks. Test-renderer visibility does not certify native layout or touch usability. SwiftUI/Flutter/Compose previews similarly provide bounded visual evidence.

For iOS tool execution, use the [iOS verification adapter](ios-verification-tools.md) for environment checks, pinned executor selection, diagnostic captures and catalog tooling. Keep the acceptance/evidence rules here.

## Measure only an actual performance question

Define the problematic scenario and metric before editing. Record a baseline, make one causal intervention, and repeat the same workload/environment. For release smoothness use a representative supported physical device and release/profile build. A diagnostic profiler session may use a debug/instrumented environment, but label its overhead and do not compare it directly with a different-build acceptance run.

| Symptom | Useful evidence |
|---|---|
| Scroll/gesture jank | Frame times/hitches, UI and JS-thread work where applicable, list data/row complexity, same scroll/gesture trace |
| Excess rendering | Render/commit timeline or SwiftUI invalidation causes, affected components/dependencies; tree depth alone is not a bottleneck |
| Startup delay | Defined interactive milestone and cold-start measurements; label warm/resume separately and account for prewarming/background launch |
| Memory growth | Repeated navigate/use/leave cycles, heap/allocation/native retained-object paths and steady-state behavior; caching alone is not a leak |
| Bundle/app size | Like-for-like JS/native/asset artifacts; downloaded, installed, and in-memory sizes are different metrics |

Use RN DevTools for React work, Instruments for relevant Apple CPU/SwiftUI/hitch/memory traces, Android tooling for native work, and Flutter/Compose tooling for their runtimes. Not every trace lane exists in every environment; an absent lane is not zero cost. Set app/device-specific targets rather than copying a universal FPS, TTI, or percentage improvement. Repeat noisy measurements enough to distinguish an improvement from variance. If a fix does not improve the chosen metric, investigate or revert it within the task rather than accumulate speculative optimization.

## Closeout

Record each relevant criterion with PASS, FAIL, BLOCKED, or NOT RUN and the actual evidence/environment. Separate functional behavior, visual/editorial judgment, accessibility, performance, and reference fidelity. State any material remaining defect or unavailable required check; passing a build, structural scanner, token audit, export, or preview cannot establish full mobile readiness.

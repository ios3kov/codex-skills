# iOS verification tools

Use for executing an already selected iOS build, simulator scenario, diagnostic capture, or string-catalog check. [Verification](verification.md) owns acceptance and evidence; the project engineering workflow owns release gates. This adapter supplies tool mechanics, not a second checklist or installation requirement.

## Select one executor

Reuse the project's existing XCTest/XCUITest or authorized device tooling when sufficient. If an external adapter is needed, select either a reviewed, revision-pinned iOS Simulator Skill checkout or an installed, version-pinned XC-MCP server for the scenario. Do not install both by default or compare results from different executors as one run. Native Xcode commands remain available beneath either adapter.

Treat setup as a separate scoped operation. Before executing downloaded scripts, inspect the selected scripts and their imported helpers at the pinned revision, record their provenance, and verify command flags with that version's help. A README review alone does not audit executable code. Do not run remote install recipes, change the selected Xcode, upgrade dependencies, or provision accounts simply to satisfy this reference. If the environment is unavailable, keep the applicable check BLOCKED/NOT RUN under the existing evidence contract.

## Check the actual environment

On the authorized Mac, inspect the active developer directory and tool versions without changing them:

```sh
sw_vers
xcode-select -p
xcodebuild -version
xcrun --find simctl
xcrun simctl list devices available -j
```

Read the project's workspace/project, scheme, deployment target and installed runtimes. Select an exact simulator UDID and keep it fixed throughout the scenario; do not silently use the first device or the global `booted` alias. Select a supported existing simulator before proposing another runtime download.

Only inspect Python or Node versions when the chosen adapter requires them. Only require idb CLI and companion for operations that use idb. Check both versions, executable resolution and compatibility with the selected Xcode against that adapter's pinned documentation; retain no universal minimum copied from a historical README. When input reports success but nothing changes, inspect companion compatibility and observed UI state before retrying taps. Use the selected adapter's reviewed health/doctor command when available.

## Build, test and launch

Substitute the inspected project values; the paths below are placeholders. Use `-project` instead of `-workspace` for a standalone project. Run build and test separately so the failing phase is unambiguous. Use a fresh, nonexisting result-bundle path per invocation.

```sh
xcodebuild -workspace '/absolute/App.xcworkspace' -scheme 'App' \
  -destination 'platform=iOS Simulator,id=SIMULATOR_UDID' \
  -resultBundlePath '/absolute/fresh-build.xcresult' build
xcodebuild -workspace '/absolute/App.xcworkspace' -scheme 'App' \
  -destination 'platform=iOS Simulator,id=SIMULATOR_UDID' \
  -resultBundlePath '/absolute/fresh-test.xcresult' test
```

Preserve the command exit status and full log before producing a short summary: phase, result, error/warning or failed-test counts when actually parsed, and artifact path/ID. Expand errors first, then relevant warnings and log sections on demand. Never turn an empty parser result into success, discard the underlying output, or conceal failure behind a successful pipe/`|| true`. For `.xcresult` parsing, inspect the installed `xcresulttool` help; commands differ between Xcode versions. A selected adapter may provide the summary/cache mechanism rather than implementing another wrapper.

When installation and launch are in scope, use the matching simulator-built `.app` and its actual bundle ID:

```sh
xcrun simctl bootstatus 'SIMULATOR_UDID' -b
xcrun simctl install 'SIMULATOR_UDID' '/absolute/Debug-iphonesimulator/App.app'
xcrun simctl launch 'SIMULATOR_UDID' 'actual.bundle.id'
```

Boot a powered-off target explicitly before waiting. Preserve test data unless a reset is part of the authorized scenario. Do not erase/delete simulators, grant all permissions, kill unrelated processes, or switch devices as automatic recovery. Successful installation/launch does not establish that the intended screen or interaction works; observe it through the existing verification procedure.

## Capture a focused diagnostic package

For a reproduced failure, capture the selected target's screenshot, accessibility hierarchy and bounded relevant logs through the chosen executor. Record the scenario step/time and the build/target identity using the existing evidence record. Mark an unavailable capture explicitly instead of fabricating an empty successful artifact.

```sh
xcrun simctl io 'SIMULATOR_UDID' screenshot '/absolute/fresh-capture/screen.png'
```

Create the private capture directory first. Redact tokens, account details, message contents and other sensitive data before sharing logs, trees or screenshots. Inspect raw captures locally when needed; do not automatically export the full app sandbox or attach private captures to an issue. Use screenshot diffs only with matched device, scale, theme, locale, text size and app state; mask known dynamic regions explicitly. Keep visual comparison distinct from functional success.

Optional iOS Simulator Skill entry points include `build_and_test.py`, `app_state_capture.py`, `visual_diff.py`, and `localization_audit.py`; resolve their paths from the reviewed installed checkout and read their help rather than assuming they are bundled here. XC-MCP offers equivalent build/device operations through its current tool schema; do not call tool names guessed from this document.

## Check string catalogs when relevant

For changed `.xcstrings`, use a reviewed installed catalog checker or the project's existing equivalent. Scope checks to supported locales and changed resources: missing required translations, untranslated/plural/device variants, stale/unused keys against the applicable source/bundle, and format-placeholder type/count/position mismatches. Account for positional arguments, escaped percent signs, string substitutions and intentionally untranslated terms; do not equate every percent sign or matching-key count with correctness.

A catalog-only checker cannot prove runtime-generated keys are unused or that strings fit on screen. Record those as candidates/limitations and exercise the affected localized flow under the existing verification procedure. Preserve the project's localization strategy; no automatic key deletion, bulk translation or new localization framework follows from a finding.

Source pointers and review limits are recorded in [sources.json](sources.json). No external executables are bundled by this adapter.

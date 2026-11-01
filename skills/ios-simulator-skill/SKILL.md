---
name: ios-simulator-skill
metadata:
  version: "1.6.0"
description: Build and test Xcode projects; launch and inspect iOS Simulator apps, navigate by accessibility labels, capture screenshots and logs, and diagnose simulator issues. Use for authorized simulator lifecycle and UI testing on macOS. Requires Xcode, Python 3.12+ and idb for interaction; availability must be checked.
---

# iOS Simulator Skill

Build and test Xcode projects, navigate Simulator apps by accessibility labels, and capture evidence of the requested behavior. This entrypoint selects a workflow; the bundled scripts provide the commands.

## Check the environment and target

Run `bash <skill-dir>/scripts/sim_health_check.sh` from the project working directory. Check the selected Xcode and available simulator/runtime before choosing a target. The installed package lists macOS 15+, Xcode 26+ and Python 3.12+; interactive scripts require idb 1.5.1+ and its companion, while visual diffs require Pillow. Verify actual availability instead of assuming setup is complete.

Use absolute script paths rooted at the installed skill, keeping project paths relative to the user's project. Run a selected script's `--help` for supported flags; use `--json` where available for structured results. Installation, upgrades, simulator creation, permission changes and destructive actions require the corresponding task scope; select the intended UDID before acting. Preserve existing simulators and app data unless their change is authorized.

## Choose the relevant commands

Read [command-reference.md](references/command-reference.md) for selected options, examples, screenshot sizes or configuration variables. Load only the relevant section:

| Task | Scripts / reference section |
|---|---|
| Build/test and logs | `build_and_test.py`, `log_monitor.py` — Build & Development |
| Theme, text size, locale and location | `appearance.py`, `location.py` — Device State |
| Screen inspection, semantic input and app lifecycle | `screen_mapper.py`, `navigator.py`, `gesture.py`, `keyboard.py`, `app_launcher.py` — Navigation & Interaction |
| Accessibility candidates, image comparison, step reports and debug snapshots | `accessibility_audit.py`, `visual_diff.py`, `test_recorder.py`, `app_state_capture.py` — Testing & Analysis |
| Data models, app container, hang diagnostics and localization | `model_inspector.py`, `container.py`, `hang_watcher.py`, `localization_audit.py` — Testing & Analysis |
| Clipboard, status bar, simulated push and privacy settings | `clipboard.py`, `status_bar.py`, `push_notification.py`, `privacy_manager.py` — Advanced Testing & Permissions |
| Discover/select a simulator | `sim_list.py`, `simulator_selector.py` — Simulator Discovery |
| Boot, shutdown, create, delete or erase a scoped target | `simctl_*.py` — Device Lifecycle Management |

For an environment or input failure, read [troubleshooting.md](references/troubleshooting.md), verify the actual version/error and choose the matching remedy.

## Interact and verify

Prefer `screen_mapper.py` and semantic `navigator.py --find-text/--find-type/--find-id` for navigation. Screenshots serve visual verification and cases where the tree is insufficient; select enough resolution to inspect the relevant detail.

A typical scoped flow is:

```bash
bash <skill-dir>/scripts/sim_health_check.sh
python3 <skill-dir>/scripts/app_launcher.py --launch com.example.app
python3 <skill-dir>/scripts/screen_mapper.py
python3 <skill-dir>/scripts/navigator.py --find-text "Login" --tap
python3 <skill-dir>/scripts/navigator.py --find-type TextField --enter-text "user@example.com"
```

Confirm the resulting screen/state after input. A successful command is distinct from the app accepting the action. Use accessibility audit findings as candidates for review, pixel differences as image comparisons, and screenshots as evidence of appearance. Inspect required user scenarios and visual details separately; simulator results do not establish physical-device behavior or release readiness.

Report the target, scenario, observed result and evidence; mark unavailable or unperformed checks explicitly.

Original source: conorluddy/ios-simulator-skill; retained [MIT license](LICENSE.md).

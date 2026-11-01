# Simulator troubleshooting

Use after an actual environment or interaction failure. These are inherited version-specific diagnostic notes, not a claim about every Xcode installation. Confirm the selected Xcode bundle, actual tool versions and observed error before choosing a remedy; upgrades and installations follow the task’s authorization.

## Requirements

- macOS 15 (Sequoia)+
- Xcode 26+ and Command Line Tools
- Python 3.12+
- `idb` **1.5.1+** - required for every interactive script (tap, swipe, type):
  `brew tap facebook/fb && brew install facebook/fb/idb-companion facebook/fb/idb-cli`
- Pillow, for visual diffs only: `pip3 install pillow`

Verify with `bash scripts/sim_health_check.sh` (add `--json` for structured output).

## Troubleshooting

**Taps, swipes and typing do nothing, but reads work.** `idb` reports success and the screen
never changes. On Xcode 27 this means `idb-companion` is older than 1.5.1: it looks for
`SimulatorKit.framework` at the path Xcode 26 used. Upgrade:
`brew upgrade facebook/fb/idb-companion`.

**`SimulatorKit is required for HID interactions`.** Same cause, same fix.

**`Connection refused` or `No such file` from every idb call.** A dead companion is still in
idb's registry at `/tmp/idb/state`, so idb dials a socket nobody is listening on instead of
starting a fresh companion. Fix: `idb disconnect <udid>`.

**`open -a Simulator` fails.** Xcode 27 has no `Simulator.app`; it was replaced by
`DeviceHub.app` in `Xcode.app/Contents/Applications/`. Boot headlessly instead:
`xcrun simctl boot <udid>`. Note that quitting DeviceHub shuts down the simulator it hosts.

**`idb: command not found`.** The companion and the CLI are separate packages; install both
(see Requirements). If `which -a idb` shows more than one, the first on `PATH` wins.

Upstream documentation: [README](https://github.com/conorluddy/ios-simulator-skill/blob/main/README.md), [architecture](https://github.com/conorluddy/ios-simulator-skill/blob/main/AGENTS.md). The bundled command reference remains available offline.

# Render and verify

Choose validation proportional to the change and requested output. A small timing edit can be checked at affected frames; a final delivery needs checks on its actual encoded artifact.

## Render scope

Confirm composition ID, input props, output path, frame range, codec/container, dimensions, fps, audio, color handling, and alpha requirements. Use existing project scripts or current CLI/library options for the installed version. Keep source and render settings tied to the same candidate.

Render representative stills or a short segment while iterating. Include start/end, longest text, transitions, media boundaries, and relevant animation peaks. Seek to frames directly to expose wall-clock or initialization dependencies. Inspect the final full sequence when exporting.

Do not add cloud/Lambda/deployment infrastructure to an ordinary video task. If remote rendering is requested, verify asset reachability, package/runtime compatibility, cost/scope, and output retrieval in that environment.

## Actual output

Check the exported file using metadata and visual/audio inspection:

- Container, video/audio codec, dimensions, fps, duration, and audio presence match the delivery requirement.
- Intended text, branding, assets, framing, and captions are present and legible.
- No loading flashes, blank/corrupt frames, clipping, stale text, font substitution, or transition artifacts at relevant points.
- Cuts and animation events align with the actual audio, not only the planned timestamps.
- First/last frames, end card, loop seam, and any trimmed media boundaries behave as intended.
- Requested transparency is preserved in a format and consumer that support it; test compositing over a contrasting background.

Spot-checking frames has a bounded scope. Do not label every frame or full audio mix verified when only representative stills were inspected. State inaccessible assets, unavailable renderer, skipped audio playback, or encoding checks that remain unperformed.

## Status and evidence

Distinguish source/type checks, Studio preview, representative renders, full render completion, and output inspection. Tie material claims to composition, settings, artifact, and check. Report `PASS`, `FAIL`, `BLOCKED`, or `NOT RUN` as applicable; successful process exit alone does not prove visual correctness.

Official reference: [CLI render](https://www.remotion.dev/docs/cli/render).

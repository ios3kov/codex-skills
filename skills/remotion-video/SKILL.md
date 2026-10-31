---
name: remotion-video
description: Create, edit, preview, or export deterministic React videos in Remotion, including frame timing, media, audio, captions, and rendered-output verification. Use for Remotion projects; use motion-storytelling for shot planning and art direction.
---

# Remotion Video

For offline use and external-reference handling, read [local resources](references/offline-resources.md).

Implement the requested composition against the project's installed Remotion version. Keep interactive preview and delivered render as separately verified results.

## Route selectively

- Timing, component structure, media, assets, captions, or Studio editability: [timeline-and-assets.md](references/timeline-and-assets.md).
- Export, render integrity, codec/alpha, or final verification: [render-and-verify.md](references/render-and-verify.md).
- Shot design, rhythm, or music cut planning: use `motion-storytelling`.
- Sound design, mix balance and delivered audio measurement: use `audio-production`.
- Generated source-media defects or source/prompt/version tracking: use `media-production-control`; recurring character identity uses `character-continuity`.

Use the authoritative brief and asset manifest for exact approved content and frame specifications; common preservation and long-task state belong to `context-discipline` when available.

## Project and version

Inspect the existing project, scripts, package manifest/lockfile, compositions, and user edits before setup or modification. Reuse its package manager and conventions. Create a new project only when the task requires it.

Keep `remotion` and related `@remotion/*` packages on compatible matching versions. Verify the actual installed version and local declarations/examples before selecting APIs; source examples from newer versions are not automatic upgrade instructions.

Use the bundled [API baseline](references/offline-resources.md) and local installed types/examples first. Official documentation is an optional online update source: https://www.remotion.dev/docs/. Specialized maps, remote rendering, and SaaS architecture are separate tasks, not default video setup.

## Deterministic timeline

- Drive visual changes from `useCurrentFrame()` with `interpolate()` or `spring()`; derive seconds-to-frames values from composition `fps` via `useVideoConfig()`.
- Avoid CSS animations/transitions, wall-clock timers, or unseeded randomness for rendered composition state.
- Be explicit about global versus component-local frames, bounds, trims, duration, playback rate, loop, and overlap.
- Prefer timing directly on components that support it in the installed version. Use `Sequence` when needed; preserve working legacy code unless changing it serves the task.
- Clamp interpolation where the value should stop, and verify endpoints and transition-adjacent frames.

## Preview and export

Start or reuse Studio when a preview will help the requested work; open the exact reported URL and confirm the intended composition loads. Preview instructions do not prohibit rendering when the user's deliverable requires a file. Avoid a costly full export merely to inspect an unfinished draft; use representative frames or a short segment.

For an export request, complete the render and verify the actual file against the requested dimensions, fps, duration, audio, encoding, and frame content. Studio playback, a clean build, and a completed render process establish different things.

Report what passed, failed, was blocked, or was not run. Do not claim final visual/audio correctness from the preview alone.

Provenance and source revision: [sources.json](sources.json).

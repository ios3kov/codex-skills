---
name: motion-storytelling
description: Plan, write, analyze or refine video and motion graphics through scene dramaturgy, product storytelling, shot composition, kinetic typography, editing, After Effects or Lottie assets. Use for scripts and visual storytelling; use apple-design for physical web gestures and interface transitions.
---

# Motion Storytelling

For offline use and external-reference handling, read [local resources](references/offline-resources.md).

Turn a brief or existing sequence into deliberate framing, timing, and movement. Work at the requested level: analysis, direction, implementation, or export.

## Choose the relevant material

Read only the reference that serves the task:

- Existing film, storyboard, camera framing, or aspect adaptation: [shots-and-composition.md](references/shots-and-composition.md).
- Motion language, pacing, beat cuts, transitions, or retiming: [direction-and-editing.md](references/direction-and-editing.md).
- Scene goals, obstacles, turning points or dialogue: [scene-dramaturgy.md](references/scene-dramaturgy.md).
- Product commercials or animated explainers with a visible argument: [product-storytelling.md](references/product-storytelling.md).
- Animated titles, lower thirds, text emphasis or timed readability: [kinetic-typography.md](references/kinetic-typography.md).
- Approved logo animation or 3D treatment: [brand-system geometry and fidelity](references/shared/brand-system/references/logo-3d-motion.md); this skill continues to own pacing, shots and motion implementation.
- AE expressions, rigs, MOGRT, export, performance, or project automation: [after-effects.md](references/after-effects.md).
- Animated illustration, Lottie asset choreography, or player delivery: [lottie-motion.md](references/lottie-motion.md).
- A code-rendered React video: use `remotion-video` for implementation.
- Reference interpretation, generated-media acceptance or asset/version handoff: use `media-production-control`.
- Recurring character identity or appearance drift: use `character-continuity`.
- Foley, ambience, voice/music/effects balance, stems or measured audio delivery: use `audio-production`.

Common context preservation belongs to `context-discipline` when available. Use the authoritative brief and shot/asset manifest as pointers for exact text, approved brand rules, character references, and frame specifications; do not recopy their contents into every plan.

For shot or image/video prompt ideas, optionally browse [SHOOOT](https://shoootai.com/) for relevant camera techniques and visual styles. Adapt inspected examples to the brief and target tool; treat them as references, not guaranteed generation results. If unavailable or unhelpful, continue with other references and existing shot-planning guidance.

## Decide before polishing

1. Establish the audience, message, emotional intent, viewing context, and requested deliverable.
2. For analysis, inspect actual media and audio/transcript before describing shots. For creation, translate the brief into a shot plan.
3. Define a concise motion vocabulary: easing family, duration palette, transition family, stagger, motion amplitude, and moments of stillness.
4. Give each shot a clear focal hierarchy and narrative purpose. Animate only elements whose movement serves it.
5. Translate timing into the actual tool's units and inspect the resulting sequence at normal speed.

Use primary/support/ambient roles as an attention model. Secondary motion, ambient loops, three depth layers, thirds placement, one-third distance limits, and numeric presets are optional techniques, not universal requirements. A static composition, symmetry, linear mechanical motion, or a mixed camera move may serve the brief.

## Evidence and delivery

- Keep shot IDs stable across analysis, revisions, assets, and timelines.
- Separate visible/audible observations from inferred lens choices and directorial intent; identify missing media or metadata.
- Validate every requested frame aspect separately. Safe zones depend on the current placement and platform; verify them when publishing.
- Preserve information in static or reduced-motion alternatives for interactive delivery; motion must not be the only carrier of meaning.
- Check read time, hierarchy, cuts, audio sync, clipping, and loops at delivery speed. Export checks belong to the actual rendered artifact.
- An expression, script, settings change, or preview is not evidence that AE host behavior or final encoding passed. State what was actually run and any remaining limitation.

Provenance and source revisions: [sources.json](sources.json).

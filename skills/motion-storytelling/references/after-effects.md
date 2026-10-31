# After Effects

## Establish the environment

Record the actual AE version, OS, project/comp, relevant plugins, and output goal. Inspect current Adobe documentation for version-dependent features. Bind diagnostics to the actual project and application session; unrelated errors are not evidence about it.

## Expressions, rigs, and MOGRT

An expression returns the property's evaluated result. Use `value` when existing keyframes should remain part of that result. Distinguish seconds, frames, property units, dimensions, and coordinate spaces.

- Choose `loopOut`, `wiggle`, or delayed `valueAtTime` only when their behavior serves the shot.
- Use deterministic random seeds for repeatable per-layer variation; time-dependent wiggle remains animated.
- For time offsets in frames, convert with the composition's frame rate rather than assuming 24/25/30 fps.
- Parent transforms or use explicit coordinate conversions such as `toComp`/`fromComp` when moving between layer and composition spaces.
- Expose intentional controls on a named control layer/null: sliders, checkbox, color, angle, or point. Keep control units, ranges, and defaults clear.
- Before handing off a MOGRT, test exposed controls, text replacement, font/assets, intended destination, and relevant duration changes in the actual host. Exporting the template does not prove those behaviors.

Keep source expressions readable and tied to actual layers/properties. Do not silently replace an existing rig or flatten editable animation to a preview-only result.

## Automation and project handoff

Use effect/property `matchName` where available to avoid dependence on localized display names. Wrap related ExtendScript edits in an Undo group, closing it even if a routine fails. Inspect selection and property applicability before mutating them. Do not ship a script as “tested” without running the relevant host operation.

Keep existing project organization unless renaming/restructuring is requested or necessary. Relink missing media to confirmed replacements; preserve existing assets and recovery material. Use Collect Files or an equivalent verified dependency handoff when portability is needed, and inspect what was collected.

## Export

Choose codec, container, alpha support, color handling, and delivery settings from the destination requirement.

**Verified correction (Adobe documentation, 2026-10-09): current AE supports native H.264 export from Render Queue.** Do not repeat the upstream claim that H.264 is universally unavailable there. Adobe Media Encoder remains an option; select the available workflow for the installed version and desired output.

- H.264 MP4 is an ordinary opaque delivery format. It does not preserve a transparent composition's alpha channel.
- For alpha, use an appropriate format such as ProRes 4444 or an image sequence and confirm RGB + Alpha, matte interpretation, and consumer support.
- Treat bitrate tables and platform presets as starting points. Verify current delivery constraints and inspect the output rather than assuming a preset proves quality.
- Check actual dimensions, fps, duration, color, audio, beginning/end frames, critical cuts, and alpha when requested. A completed queue alone does not prove those properties.

Official source: [Adobe H.264 through Render Queue](https://helpx.adobe.com/after-effects/desktop/render-and-export/export-h-264-from-the-after-effects/exporting-h264-from-the-after-effects-render-queue.html).

## Performance and failures

Separate slow preparation, slow playback, slow render, hang, crash, and invalid output. Reproduce with the actual candidate and a small relevant comp before assigning cause.

Prefer reversible isolation: lower preview resolution, identify heavy effects/layers, inspect memory/disk pressure, test proxies or pre-renders, and compare Multi-Frame Rendering when relevant. Record settings and change one material factor at a time. Purging cache changes the tested state and is not proof of a source fix.

Preserve current preferences, installed plugins, authored projects, and recovery files. Resetting preferences, uninstalling plugins, broad cache deletion, or rolling back software requires a reason and scope; generic upstream troubleshooting lists do not authorize them.

Report host actions separately from source review: what was run, application/candidate identity, observed result, and unresolved symptom. Never infer crash resolution or real-time playback from static checks or a settings recipe.

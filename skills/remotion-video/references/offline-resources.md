# Local Remotion API baseline

This is a frozen implementation guide, not a guarantee about a newer package version. Existing timeline-and-assets and render-and-verify references remain authoritative for this skill. Inspect installed package declarations/examples and lockfile first; external documentation is optional refresh material.

A common composition uses useCurrentFrame() for deterministic frame state and useVideoConfig() for composition fps/dimensions/duration. For a simple fade, derive opacity with interpolate(frame, [0, 15], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}). For physical movement, spring({frame, fps, config}) returns a spring progression; inspect supported options locally. Keep randomness seeded and wall-clock timers out of rendered state.

A Sequence with from and durationInFrames offsets child timing; a child's useCurrentFrame() becomes local to that sequence. Calculate absolute cut points deliberately. Media trim/playback props vary between components and versions; inspect declarations instead of transferring props blindly. staticFile('asset.png') refers to a project public asset under the normal Remotion convention. Copy media/fonts into project-controlled files and resolve their loading before capture; a URL still reachable today is not durable storage.

Use the project's installed CLI and scripts, inspect its render help, and select an existing composition. Do not use npx in a way that silently downloads a different release. Verify the resulting file's frames, duration, fps, dimensions, audio and encoding separately from Studio preview. Packages, a compatible browser and codecs are execution prerequisites; this instruction package does not pretend to contain those engines.

Snapshot reviewed 2026-10-20. Original operational summary; source credits remain in the existing references.

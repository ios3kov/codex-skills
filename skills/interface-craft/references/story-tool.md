# Optional before/after story tool

Read only for a requested explanatory UI transformation video. Keep source assets and production UI separate from the presentation. The renderer accepts trusted, reviewed local HTML, not arbitrary downloaded pages. A story page executes local scripts during rendering. Restrict its folder to the intended story/assets; the local server serves regular supported files within that real-path root, with external requests blocked in the automated renderer. It is not a general HTML sandbox. Use the host's permitted browser workflow where it governs testing.

## Author the story

Create a separate local HTML file using real approved content and locally packaged styles/fonts/images. Use `<meta name="unslop-steps" content="Spacing, Color, Details">` in its head; attribute order and either quote style are accepted. Optional `<meta name="unslop-frame" content="0 0 960">` sets nonnegative crop x/y and positive width. Use 1–12 steps; a compact story usually needs fewer. Source CSS is the initial state; cumulative `html.s1`, `html.s2` etc. rules define changes. The same element changes in place. Keep complex structural redesigns honest: use a clearly presented cut/comparison rather than forcing an inaccurate CSS morph.

Optional annotations: `data-gap="main"` groups vertically measured elements; `data-radius` marks selected corners; `data-slop="Observed issue"` labels an actual observed defect. Avoid annotating aesthetic preferences as objective faults. For a text change use `<span class="swap" data-at="2"><span class="from">Old</span><span class="to">New</span></span>`. `data-in="2"`/`data-out="2"` show/hide content at a step. Do not shorten approved text merely to fit the video. Keep the final state consistent with the delivered app; the renderer does not verify this automatically.

## Run selectively

`node <skill-dir>/scripts/unslop/story.mjs /absolute/story.html --serve`

This prints a loopback preview URL with Initial state, Final state and per-step buttons for the permitted host browser. No Playwright is needed in this mode. Stop the task-owned server after review. The preview is a manual inspection surface, not a video export.

`node <skill-dir>/scripts/unslop/story.mjs /absolute/story.html /fresh/result.mp4 [--wide] [--fps=30] [--width=1080] [--height=1080]`

Video export needs an existing authorized Playwright/Playwright Core, Chromium and ffmpeg. No dependencies are installed. Dimensions are the actual output pixels, not a hidden double-resolution scale. Default 1080×1080 at 30 fps; --wide selects 1920×1080. Use even width/height from 64 to 3840 and fps 1–60. Existing output files are rejected unless --overwrite is explicitly requested for that output. Temporary frames use a unique task-owned directory and are cleaned up. Errors fail the command; preserve the last valid delivered file.

Read the reported dimensions, frame count and duration, then inspect the delivered file with ffprobe and representative start/transition/end frames. Verify text, crop, annotation accuracy and final-state parity with the real UI. Automated render completion does not establish visual fidelity. An unavailable browser, asset or codec is a reported gap; do not deliver a placeholder as finished output. The video retains upstream attribution. See [visual refinement](visual-refinement.md) for source, license and adaptation boundaries.

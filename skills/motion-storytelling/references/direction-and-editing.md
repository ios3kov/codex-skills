# Direction and editing

## Motion language

Define emotional intent and narrative function before selecting curves. A compact motion spec should give comparable actions a consistent easing family, duration palette, amplitude/overshoot budget, stagger rhythm, and transition vocabulary.

Use calm/kinetic and soft/sharp as discussion axes, not mandatory named personalities. Existing brand motion wins over generic presets. Related moves can reuse a base timing unit; meaningful exceptions are allowed. Primary action receives attention; support and ambient motion earn their place rather than being automatically added.

Map energy across the piece: introduction, development, peak, and resolution are useful when the story calls for that arc. Allow tension, stillness, silence, and a settled end card. Avoid animating readable text continuously or running every element at competing intensity.

When refining, identify the actual defect—hierarchy, abrupt pacing, inconsistent ease, excessive motion, or unclear transition—before adding effects.

## Music and frame timing

Inspect the audio. Establish the beat-one offset, BPM/tempo changes, meter, phrase boundaries, transients, and intended dramatic accents. A BPM estimate alone does not locate the grid in the file.

For fixed BPM, zero-based beat number `b`, beat-one offset `t0` in seconds, and composition fps:

`cutFrame(b) = round((t0 + b * 60 / BPM) * fps)`

For measured or changing-tempo music, use each absolute beat timestamp:

`cutFrame(b) = round(beatTimeSeconds[b] * fps)`

Round absolute positions once; do not repeatedly add a rounded frames-per-beat interval, which accumulates drift. Obtain clip durations from adjacent cut frames. Preserve the chosen rounding convention and verify the final audio alignment; fractional fps and beat subdivisions may produce unequal integer intervals.

Structural cuts can follow phrases or narrative events; accents may use subdivisions. Cutting on every beat is a creative choice, not the default consequence of beat synchronization. Evaluate at normal speed with the actual track and final frame rate.

## Cut and transition choice

Use a hard cut when it conveys the change clearly. Motivate alternatives:

- Match cut: shape, position, eye trace, action, or velocity connects shots.
- J-cut: next shot's audio starts before its picture.
- L-cut: current shot's audio continues under the next picture.
- Dissolve: a soft relation or passage of time.
- Whip/wipe: a supported movement or graphic relationship.

Separate picture cut points from audio offsets. Check direction and velocity across action cuts. Transition overlap changes total duration: record both the overlap and resulting timeline length rather than adding nominal shot durations blindly.

Retiming changes source-time sampling. Specify target duration, source range, speed curve, and landing frame before choosing an implementation. Check interpolation artifacts and audio treatment. Do not assume an AE time-remap expression or Remotion playback-rate prop supplies optical flow or pitch preservation.

A reusable edit plan records shot ID, source in/out, composition start/end frames, audio boundaries, transition overlap, retime intent, and the event each cut serves. Avoid duplicating the authoritative asset or brief text.

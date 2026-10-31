# Kinetic typography

Use for timed text in video or motion graphics. Shared [typography craft](shared/interface-craft/references/typography.md) owns font selection and rendering; this reference owns how text enters, becomes readable and leaves. Preserve exact approved wording, language and brand treatment.

## Give text a timed job

Identify whether the element is a title, identification, explanation, emphasis, caption, CTA or required disclosure. Place it in the viewer's attention sequence: what is being watched before it arrives, what must be read, and what happens next? Supporting labels should not compete with the scene's main action.

Plan appearance, a stable reading interval and departure against the actual edit and audio. The reading interval begins when the required phrase is legible, not when the first animated glyph appears. Include time to find the text and understand it alongside competing imagery. Do not prescribe a universal seconds-per-word rule; evaluate complexity, audience, language and viewing size. Extend the beat or reorganize text when the allowed time is insufficient.

Animate a block, phrase, word or smaller unit only when its motion serves the meaning. Use restrained supporting motion and deliberate peaks rather than equal intensity on every word. A rise, reveal, collision or tracking change has no universal emotional interpretation; choose it in the piece's established language.

## Preserve reading and shaping

Review semantic line breaks in composed titles while retaining responsive or localized behavior where needed. Keep names, units, modifiers and essential phrases understandable. Expansion may require another layout or longer hold; shrinking until unreadable is not a repair.

Keep shaped script runs and grapheme clusters intact when animation splits text. Raw code-point or character slicing can detach combining marks or break joined forms. Choose block or phrase animation when the actual text engine cannot preserve shaping. Check reading order and reveal direction in the target locale rather than mirroring a Latin layout mechanically.

Exact lettering is best kept in controllable text layers when generation is unreliable. Use generated backgrounds separately if necessary; inspect the actual delivered spelling and glyphs. Resolve a missing brand font through the project's approved fallback or an explicit substitution, not an unreported replacement.

## Captions and delivery

An accent phrase or condensed quotation is not a complete caption track. When designed captions are the accessible equivalent, retain dialogue, speaker identification where needed and meaningful non-speech audio. If graphic emphasis omits words, preserve full captions separately and avoid overlap.

Apply the existing aspect and placement checks to moving text throughout its trajectory. Inspect contrast against the changing background, compression, occlusion, captions and product detail at actual delivery size. Check required reading at playback speed; a still only verifies one moment.

For interactive delivery, preserve information in the reduced-motion state and available playback controls. Avoid unnecessary flashing; where flash effects are used, assess the applicable frequency, area and luminance thresholds on the actual output. WCAG is a web conformance standard, not automatic certification of every exported video.

Use the established frame spec and shot IDs. Record exact text pointers, role, layout bounds, reveal/settled/exit positions, audio synchronization and relevant animation properties. Implement with the selected tool's timeline conventions; this reference does not prescribe CSS animation inside a deterministic Remotion render.

Authorities: [captions](https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html), [flash thresholds](https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html), [Unicode line breaking](https://www.unicode.org/reports/tr14/) and [text segmentation](https://www.unicode.org/reports/tr29/). Consult current target-platform requirements for placement and delivery.

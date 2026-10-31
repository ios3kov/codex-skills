# Typography craft

This reference owns how text is rendered. Exact copy and prose editing remain separate. Preserve the established typefaces, brand and approved strings unless their replacement is requested.

## Faces and semantic roles

Inspect loaded families/weights/styles and actual computed rendering, including Cyrillic and other required glyphs. Load the faces or variable ranges the design uses. Synthetic bold/italic can distort a face; disable only an unwanted synthesis mode after checking the fallback stack rather than globally disabling it by habit.

Use a small coherent role scale with size, weight, leading and tracking together. Keep visual heading hierarchy consistent with semantic structure and the surface's purpose. Optical sizing, text/display cuts and real font metrics matter more than universal font-count or weight thresholds.

Prefer semantic CSS controls such as font-weight and font-variant-numeric over low-level OpenType tags when they express the feature. Use raw tags only for a needed feature/axis without a suitable higher-level property. Verify that the loaded font supports the requested feature; a declaration alone does not prove it rendered.

## Pairing and variable fonts

For a new or authorized type choice, assign roles and evaluate the actual faces at their intended sizes. A single family with suitable styles can cover multiple roles; adding a second family needs a purpose. Similar proportions, x-height and stroke rhythm can create cohesion; a deliberate difference in structure, width or weight can distinguish roles. Serif/sans is one option, not a sufficient pairing test. Inspect a specimen with real headings, paragraphs, digits and required scripts; evaluate the text block's visual density as well as individual glyphs. Verify usage and embedding rights for any newly introduced font in the requested medium.

When typeface selection is open and a material choice remains uncertain, compare a small, relevant shortlist on the same real content and representative layout. Keep content, roles, containers and viewing conditions comparable; tune each candidate's size, weight and leading to suit its metrics rather than imposing identical numeric settings. Explain the choice briefly in terms of the brief, reading hierarchy and practical tradeoffs. Candidate count is not an acceptance criterion: retain an established or well-supported choice without manufacturing alternatives, and stop when the choice is sufficiently supported. Candidate comparison does not replace the final rendered review.

For variable fonts, inspect the axes and supported ranges in the actual font file rather than assuming weight, width, slant or optical size are all present. Use higher-level CSS properties where they express the needed axis, and keep low-level settings for unsupported mappings or custom axes. Check computed rendering and wrapping after axis changes; visual weight and occupied width may both change. Choose baseline or modular-scale relationships where useful without forcing every role into a fixed ratio. See [MDN variable fonts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts).

## Spacing and line shape

Unitless line-height usually preserves proportional leading for scalable UI text. Adjust it for font, role, script, line count and the existing design system. Short display type can be tighter than a paragraph; fixed-stage slides or carefully controlled SVG may need explicit metrics. Avoid imposing browser layout units on another rendering medium.

Tracking and readable measure are design choices to inspect at real size. Rough body-text ranges such as 60–75 characters per line are starting points, not universal pass/fail thresholds across scripts and screen types. Check parentheses, punctuation and all-caps labels as actual glyphs.

Use balanced wrapping for suitable short headings and evaluate prettier paragraph wrapping where supported and worth its layout cost. Both need actual browser verification and fallbacks; pretty does not guarantee a particular final line in every engine. Avoid manual breaks that fail translated or narrower content unless the output uses a deliberate fixed composition.

Prevent long URLs/IDs from escaping containers. Truncation must have an accessible path to the full value. Preserve required text; visual neatness cannot justify shortening approved wording. Keep important text selectable where interaction does not require otherwise.

### Optical and semantic review of prominent copy

For headings, short introductory copy and other visually dominant text, review the actual words as well as the overall text block:

- Compare the apparent whitespace between adjacent glyphs. A visibly open pair beside a crowded pair needs optical judgment; equal advance widths, `letter-spacing: normal` and `font-kerning: normal` are not proof of even spacing. Inspect at the intended size; enlargement can help diagnose a pair, but recheck the final-size result. Retain the font's kerning by default; use a local adjustment only for an observed pair in controlled display copy, and verify selection and the complete accessible text.
- Read each rendered line as a phrase. Avoid stranding the opening word of a new sentence at the end of the preceding line, or separating a short linking word from its meaningful continuation when this weakens short display copy. In Russian, examples include keeping «как складывается целое» together in a short lead and avoiding an isolated «Меняйте» before its continuation. Apply the language and context; do not mechanically bind every short word or impose these examples on continuous prose.
- Correct the cause within the approved design: appropriate type metrics and measure, a modest size/leading adjustment, balanced wrapping, or narrowly scoped semantic groups. Do not fix an uneven pair by compressing the whole heading. Do not silently rewrite approved copy to make it fit. Avoid locking long phrases or hard line breaks that overflow narrower layouts; recheck all affected widths after grouping text.
- Compare the result before and after at the same size and width. Review the complete heading and nearby introductory text, not only the reported fragment. Distinguish observed clipping/collisions from optical preferences, and state which text and sizes were actually inspected. Unreviewed optical or editorial quality must remain unverified even when geometry checks pass.

## Digits, language and details

Use supported tabular figures for changing counters, timers and aligned numeric columns; choose proportional figures where prose benefits from them. Align decimals/units intentionally without changing values or locale conventions.

Set appropriate language/direction and isolate mixed-direction fragments when necessary. Check hyphenation, glyph coverage, quotes and punctuation in the actual locale. Typography polish must not rewrite an approved string, code, identifier or literal data value. Tune rendered styling or propose an explicit copy change instead.

Check link underlines, visible focus, placeholders, selections and field text against the design/accessibility requirements. Test mobile field focus behavior on the target browser; increasing a too-small input's font is often useful, while disabling zoom or blindly scaling text can harm usability.

Font smoothing controls are nonstandard and platform-dependent. Preserve the project's policy or use them only after a relevant visual comparison; they are not a universal quality requirement. Treat emerging text-box trimming as progressive enhancement with a tested fallback when used.

## Verification and findings

Inspect computed face/weight/features and real text at relevant viewports, zoom and delivery size. Include long headings, counters, small captions and critical brand strings. Check wrapping, clipping, lone lines, fallback, readable contrast and recovery from truncation. A declared style or font filename is not verification of final rendering.

Report each root cause with affected location, observed result, proposed adjustment, user impact and checks performed. Distinguish unreadable/hidden required content from local polish. Claim coverage only for the inspected surfaces. For slides/diagrams preserve their own stage/geometry validation and use the applicable portions of this reference.

Authorities: [text-wrap](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap), [numeric font features](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric), [font synthesis](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis), [nonstandard font smoothing](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-smooth). Check current support for a version-dependent feature.

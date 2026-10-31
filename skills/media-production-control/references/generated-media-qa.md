# Generated-media QA

## Acceptance before defect hunting

Bind the review to actual asset/version/hash, intended use, authoritative brief and required delivery specs. List the acceptance checks relevant to that deliverable. If a requirement or source is missing, label that part provisional or unverified; do not invent approval or require unrelated compliance gates.

Use tools for measurable file properties and actual visual/listening inspection for perceptual defects. Metadata, OCR and a generation success response answer limited questions; none proves a correct face, exact logo or understandable soundtrack.

## Inspection lanes

- **Brief/brand:** required subject, message, language, exact text, character/product, palette, approved logo and requested format.
- **Visual:** anatomy appropriate to the style, recognizable face, hands, eyes, joints, proportions, hair, contact shadows, reflections, material and product geometry. A deliberate stylization is not automatically an anatomical defect.
- **Exact content:** inspect names, prices, dates, labels and logos against the approved source. OCR can find a candidate mismatch; manually confirm critical text. Prefer approved vector/text overlays when a generator cannot reliably reproduce them.
- **Temporal:** watch at delivery speed and inspect relevant frames around turns, cuts, occlusion, interpolation and repairs. Check identity/wardrobe/props, flicker, morphing, crawling texture, clipping and motion discontinuity. One clean still does not cover a clip.
- **Audio/language:** intelligibility, sync, stated language, pronunciation and meaningful cues. Route detailed loudness and mix checks to audio-production. Check captions against spoken content and required placement/format.
- **File:** decode/open, dimensions/aspect, duration/fps, streams, codec, color/alpha and requested metadata. Validate the actual derivative when exporting or transcoding.
- **Context-specific requirements:** accessibility, provenance, licensed-use restrictions and disclosure only where applicable to the actual delivery contract. Verify current official requirements before a formal compliance claim.

For stills inspect delivery size plus detail regions. For final video include normal playback and focused scrubbing; record the reviewed range and playback conditions. Limited spot checks remain limited. A file check without playback cannot pass audio or temporal quality.

## Triage and repair

Report asset/version, timestamp/frame/region, issue, evidence, severity/impact, suggested repair and retest scope. Separate an observed defect from its hypothesized cause. Core identity/product/brand/text failures and corrupted output prevent acceptance; small background polish can remain a note when it does not violate requirements. Do not dismiss a required detail merely because it is small.

Use verdicts such as accept, revise or reject only for the inspected scope, and retain PASS/FAIL/BLOCKED/NOT RUN for individual checks. User approval may accept a known tradeoff but does not turn an unperformed check into PASS.

After a repair inspect the changed region, nearby dependencies and representative unchanged areas. For final video play the resulting sequence again when temporal changes could introduce defects. A re-rendered artifact needs its own relevant evidence. Log unresolved limitations and keep the prior valid candidate recoverable.

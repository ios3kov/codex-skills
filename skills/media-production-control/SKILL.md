---
name: media-production-control
description: Translate visual or audio references into a production brief, review generated media against acceptance requirements, and trace sources, prompts, versions and approvals in an asset ledger. Use for reference breakdowns, generated-media QA and production handoffs; generation and editing use their own tools.
---


# Media production control

Keep direction, observed output and asset history connected without turning a small draft into a production bureaucracy.

Read only the applicable mode:

- [Reference analysis](references/reference-analysis.md): translate "in this style" into concrete transferable choices.
- [Generated-media QA](references/generated-media-qa.md): inspect actual output and report actionable defects and coverage.
- [Asset ledger](references/asset-ledger.md): link sources, prompts, variants, decisions and delivered bytes.

Begin with the requested deliverable and its existing brief/specification. Distinguish what the brief requires, what is visible or measured, and what is an artistic inference. Reuse the established project manifest when present.

For a simple asset, one traceable record and a focused review can suffice. For a batch or multi-shot piece, keep stable asset/shot IDs and review the requested scope explicitly. A missing field stays unknown; a missing critical reference blocks only decisions dependent on it, while independent authorized work continues.

Use `character-continuity` for detailed identity tolerances, `motion-storytelling` for shot/edit planning, and `audio-production` for sound design and mix diagnosis. Those skills own their craft decisions; this skill owns source interpretation, generated-media acceptance and provenance. Exact requirements and resumable task state stay in `context-discipline`.

Approval and QA are separate fields. A filename saying "final" is not evidence of acceptance. Re-encoding or modifying an approved asset produces a new artifact whose affected checks must be repeated. Preserve source masters, approved versions and unresolved diagnostics.

The Jira key is an optional project link, for example `PROD-123`; it is not a newly created issue. Creating, editing or posting to Jira requires an available integration and user authorization for that external action.

Provenance: [sources.json](sources.json).

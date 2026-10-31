# Asset and version ledger

Use the project's current naming/storage conventions. Keep one authoritative manifest; small jobs do not need a separate database, redundant manifests or a Jira issue per file.

## Minimal traceable record

Record a stable logical `asset_id`, unique `version_id`, role/type, path or provider artifact identifier, parent/source/reference IDs, prompt/settings pointer, status, approval evidence and QA evidence. For approved/final bytes record SHA256 and the actual delivery properties. Add fields when needed: character/shot IDs, model/version, request ID, exposed seed, language, dimensions, fps/duration, audio layout, provenance and stated usage scope.

Unknown generation details remain `not_provided`. Capture exact prompts/settings in retrievable files rather than summarizing away reproducibility. Credentials and secret tokens are not production metadata.

Keep these notions separate:

- **Logical asset:** one character reference, shot, music bed or logo.
- **Version:** an immutable candidate, repair or derivative with its own identity/hash.
- **Approval:** who approved which version, when, for what use and with which exceptions.
- **QA:** what was actually checked on those bytes, by which method, and the result.

Suggested lifecycle: draft → candidate → approved → delivered, with rejected/superseded recorded separately. These are record states, not automatic permission to distribute or delete.

## PROD naming and Jira

If the project provides a real Jira key, retain it verbatim as optional `issue_key` and optionally the confirmed issue URL. Example naming pattern:

`PROD-123_char-01_sh-03_v003_candidate.png`

Here `PROD-123` is an example until supplied or verified. Preserve project conventions over this pattern; do not invent an issue, assignee or approval comment. Link the key locally without posting externally. An approved Jira integration task can synchronize confirmed records later.

## Repairs, variants and derivatives

Before regenerating record the parent version, defect or hypothesis, permitted changes and protected fields. A repair, alternate creative variant and replacement direction are different intents. New model/reference/settings can alter continuity even with identical prompt/seed; capture the actual change.

Never overwrite an approved master to reuse its filename. Keep working sources and platform transcodes distinct; each derivative points to its parent and carries the checks required for its delivered properties. Record rejected candidates when they preserve reasoning or a useful recovery path. Cleanup follows existing retention/authorization rather than guessed disposability.

For handoff reconcile the shot list with asset versions, exact copy/logo files, prompts, references, approvals, manifests and deliverables. Check broken pointers, missing dependencies, duplicated IDs, stale approval/hash links and files marked approved without evidence. Keep recovery material available when moving files or replacing a version.

## Rights and consent evidence

For media intended for distribution, record the source URL/provider and exact asset version; creator or rights holder if known; license or permission evidence and its date; intended use, territory, duration and restrictions where specified; and applicable consent/release evidence for identifiable people or protected material. Link the evidence rather than copying private consent data into a public manifest.

Keep rights/consent status separate from visual QA and creative approval: verified for the stated use, restricted, unresolved, or not applicable with a reason. A public URL, paid download, generated asset or aesthetic approval alone does not establish permission. Missing evidence stays unresolved. Record AI origin and any applicable disclosure/accessibility requirements without inventing universal obligations.

A derivative points to its parent's evidence and is checked for changed usage restrictions. Before handoff, flag material missing evidence for the intended distribution; a completed ledger does not authorize publication.

[Source and MIT notice](setupkit-source.md).

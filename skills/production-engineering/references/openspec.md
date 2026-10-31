# OpenSpec compatibility

Use when an existing project uses OpenSpec or the user explicitly selects it. This is a local workflow adapter, not an installation of the OpenSpec CLI or slash commands. Ordinary projects keep their established specification workflow; a small fix needs no new framework.

## Select the actual planning root

Inspect project instructions, openspec/config.yaml (or config.yml), existing specs and changes. Resolve the selected change from the task; ask only when several plausible changes cannot be distinguished. Preserve a configured external store and its access boundaries rather than silently writing a local substitute. Missing store access blocks its writes, not independent source inspection. Do not initialize OpenSpec, register stores, install its CLI or create another spec tree as a side effect.

If a compatible CLI is present, inspect its help/version and use status/instructions/validation for the selected root and change. Keep store/root selection on subsequent commands. Do not assume commands from a video exist locally. Without the CLI, permitted Markdown inspection/editing still works, but CLI validation is NOT_RUN.

## Reuse the change artifacts

Treat main specs as the accepted documented contract and changes as proposed deltas, not verified runtime facts. Reuse proposal.md for rationale/scope, specs/ for behavioral deltas and scenarios, design.md for material technical decisions and tasks.md for implementation tracking. Honor the actual schema: this list is a common shape, not a demand for four new files per fix. Existing requirements, tests, evidence ledger and handoff remain authoritative for their respective roles.

When deltas are used, separate ADDED, MODIFIED, REMOVED and RENAMED requirements as the project schema requires. Preserve requirement identities, full capability paths, unchanged scenarios and explicit reasons for removals. Reconcile renames and concurrent changes against the current main spec before applying; never replace a whole spec with a partial delta. Update decisions when implementation discoveries change the plan.

## Verify and finish

Mark a task complete only after its implementation and applicable checks are evidenced. A checked box or valid schema does not prove behavior. Review the selected delta against the actual implementation using the normal engineering gates. Keep failed, blocked and unperformed checks visible.

Within authorized completion, reconcile verified deltas into the main specs and retain the proposal, decisions, tasks and evidence in the established archive. If work is incomplete, leave it active with an exact next step; do not archive merely to clear a list. Check archive destination collisions and preserve parallel work. Document archiving does not authorize a Git merge, push, release or deployment.

## Provenance

Original local guidance informed by Fission-AI/OpenSpec commit 6d04a1b58dedc95729d34e4f223d9d483aae210a, reviewed 2026-10-26: [concepts](https://github.com/Fission-AI/OpenSpec/blob/6d04a1b58dedc95729d34e4f223d9d483aae210a/docs/concepts.md), [sync skill](https://github.com/Fission-AI/OpenSpec/blob/6d04a1b58dedc95729d34e4f223d9d483aae210a/skills/openspec-sync-specs/SKILL.md), [archive skill](https://github.com/Fission-AI/OpenSpec/blob/6d04a1b58dedc95729d34e4f223d9d483aae210a/skills/openspec-archive-change/SKILL.md). No upstream CLI, code or full skill text copied. This reference contains the operational guidance locally; links provide attribution, not required runtime resources. No token-saving claims.

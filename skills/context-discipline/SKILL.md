---
name: context-discipline
description: Keep substantive multi-step work efficient and resumable through selective reading, reuse of evidence, durable task checkpoints, and preservation of exact requirements. Apply during research, design, engineering, and long tasks; trivial self-contained replies do not need a checkpoint.
---

# Context discipline

Keep substantive work resumable through selective reading, reusable evidence and one task checkpoint. Preserve the user's full requirements and required checks; small self-contained replies need no checkpoint or added permission gate.

## Read and reuse selectively

Start from the task question, likely paths and relevant headings/identifiers. Read the smallest useful range with enough context to interpret it; expand for dependencies, ambiguity or verification. An explicitly requested full audit or complete source scope still requires full coverage.

Load skills/references when they affect the current decision. Keep bulk sources, logs and extracts in searchable task-local files, with findings and source pointers in active context. Preserve originals and actionable diagnostics before summarizing output.

Reuse searches and conclusions while their source and relevant state match. Execution evidence needs input and skill/source identity, settings/environment and completion status; a file or completion marker alone does not establish correctness. Refresh affected evidence after changes to files, versions, requirements, external facts or assumptions, retaining valid checks for unchanged scope. Use content hashes for relevant uncommitted files where practical, rather than hashing unrelated workspace data.

For a project map, use `codebase-understanding`'s installed helper only when navigation justifies it. Freshness covers full-file hashes including YAML frontmatter, inventory changes and helper identity, not HEAD/mtime alone. Bound output with `--limit` and `--max-bytes`; inspect truncation and coverage before relying on a result. Use literal-source fallback and ordinary search when the map is stale, incomplete or unavailable. No matches do not establish absence of dependencies. Record map path, root, scope and gaps in the existing checkpoint; no global installation or second memory system is needed.

## Keep one durable task record

For longer work, phase transitions, an approaching context refresh, or resumption across sessions/clients, read [durable task state](references/durable-state.md). Use the established task-local destination, such as `work/task-state.md`, and update material facts and explicit supersessions. Keep these fields sufficient for resumption:

- **Brief:** objective, acceptance requirements, constraints, user steering and authorization boundaries.
- **Protected anchors:** exact wording or its verbatim source pointer, approved decisions/rationale, brand and visual/media specifications, character identity, and required checks.
- **Sources/artifacts:** reachable paths, identifiers, versions/revisions, and what was inspected, created or changed; add a detailed index only when useful.
- **State:** completed work, open questions, attributed failures and verification tied to its candidate/environment, distinguishing PASS, FAIL, BLOCKED and NOT RUN.
- **Decisions/conflicts:** what applies, why, what it supersedes and which conflicts remain.
- **Next steps:** remaining work, dependencies and genuinely required user input.

Retain exact copy and structured specifications verbatim where precision matters, alongside reachable originals. Task checkpointing does not authorize platform memory or unrelated instruction changes.

When agents are used, `agent-orchestrator` owns coordination/resource boundaries and one coordinator writes this record. Pass each worker relevant requirements, decisions, source/artifact pointers, revision, dependencies and checks; confirm access or provide an authorized snapshot/excerpt. Reconcile material results and conflicts, mark superseded inputs and notify affected workers before dependent work. Context becomes shared only when explicitly passed or read; small direct tasks need no team record.

## Recover and finish

After context refresh, before major implementation decisions and before completion:

1. Restore the current brief and protected anchors; confirm artifact existence and relevant state.
2. Reconcile original requirements with later steering, retaining obligations unless explicitly replaced or incompatible.
3. Resolve conflicts through instruction priority, user choices, applicable versions and verified sources; label uncertainty and supersession. Ask only for a material unresolved conflict while continuing independent authorized work.
4. Check that exact texts, decisions, specifications, evidence, required checks and the next action remain recoverable. Repair gaps from originals rather than inventing details.

If work repeats, blends projects or carries corrected assumptions forward, inspect the affected checkpoint and original evidence before rereading everything.

Judge efficiency over completed tasks, including recovery and rework. Use task-level measurements when available; otherwise describe the method qualitatively rather than asserting token-saving percentages, cache benefits or universal context thresholds.

Provenance: [sources.json](sources.json), adapted from Filesystem Context, Context Optimization, Context Compression and Context Degradation. Execution-evidence identity guidance adapted in original wording from [Harness² run records](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/core/runmark.py), reviewed 2026-10-19; [Apache-2.0 notice](references/upstream/harness2/LICENSE).

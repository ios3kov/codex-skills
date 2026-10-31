---
name: context-discipline
description: Keep substantive multi-step work efficient and resumable through selective reading, reuse of evidence, durable task checkpoints, and preservation of exact requirements. Apply during research, design, engineering, and long tasks; trivial self-contained replies do not need a checkpoint.
---


# Context discipline

Apply these agreed working defaults without adding a permission gate. Optimize the cost of completing the whole task, including rereading, coordination, and rework, while preserving the user's requirements and the checks needed to finish.

## Select before reading

- Start with the task question and likely files or source sections. Search paths, headings, identifiers, or relevant terms; read the smallest useful range with enough surrounding context to avoid misinterpretation.
- Load a skill or supporting reference when it changes the current decision. Keep bulk sources, logs, and extracted material in task-local files with searchable names; bring their relevant findings and source pointers into active context.
- Expand a read when dependencies, ambiguity, or verification require it. Selective reading must not silently reduce an explicitly requested full audit, complete text, or source scope.
- Preserve original evidence before replacing a large output with a summary. Retain actionable errors and diagnostic details until their issue is resolved.

## Reuse without becoming stale

- Reuse earlier searches, reads, and verified conclusions when their source and relevant state still match. Avoid repeating the same query or printing large technical results merely to restate progress.
- For reusable execution evidence, record the relevant input and skill/source identity, execution settings/environment, and an explicit completion result. An output file alone does not establish that a run completed or passed. Refresh affected evidence when these change; keep still-valid evidence for unchanged scope. Use content hashes where practical for files with uncommitted changes; do not hash unrelated workspace contents or treat a completion marker as proof of correctness.
- Refresh only the affected material when files, versions, requirements, external facts, or assumptions change, or when prior evidence is incomplete. Record what changed so a later continuation can reuse it safely.
- Keep one authoritative task brief and link to detailed evidence rather than reproducing it across notes. Give parallel workers distinct file ownership when needed to prevent conflicting edits.

For an optional shared project map, use `codebase-understanding`'s actual installed helper only when navigation justifies it. Its `status`/search freshness uses full-file hashes (including YAML frontmatter), inventory changes and helper identity, not HEAD/mtime alone. Keep the task's bounded `--limit` and `--max-bytes`, inspect truncation/coverage flags and expand only when the decision needs it. If the map is stale or insufficient, use its literal source fallback plus ordinary search and originals; never reuse stale edges or treat no matches as no dependencies. Save the map path, root, scope and gaps in the existing task checkpoint, not a second memory system. Missing helper access is a reason to use normal source search, not to install it globally.

## Share context with parallel workers

When agents are actually used, the existing task checkpoint is the shared brief; coordination and resource ownership remain with `agent-orchestrator`. Keep one coordinator as its writer. Send each worker only the relevant requirements, approved decisions, source/artifact pointers, input revision, dependencies and acceptance checks. Confirm that the receiving environment can access those sources; supply a permitted snapshot or essential excerpts when it cannot.

After a material worker result or changed requirement/interface, reconcile the evidence and decisions into the checkpoint, mark superseded inputs, and notify affected workers before their dependent work continues. Record outstanding conflicts instead of silently choosing a worker summary. Agents do not automatically share conversation state; a saved checkpoint helps only when it is explicitly read or passed. Small direct tasks do not need a team record.

## Maintain a durable checkpoint

Read [durable task state](references/durable-state.md) when saving or resuming a longer task across sessions or clients, especially when storage access or permanent-memory scope is uncertain.

For long work, phase transitions, or an approaching context refresh, maintain a small task-local checkpoint, such as `work/task-state.md`, adapted to the project's established convention. Update it with new facts and explicit supersessions instead of repeatedly rewriting older summaries from memory.

Keep these fields sufficient to resume the actual task:

- **Brief and scope:** objective, acceptance requirements, constraints, user steering, and authorization boundaries.
- **Protected anchors:** exact wording or a precise pointer to its verbatim source; approved decisions and rationale; brand rules; frame dimensions, aspect ratio, fps, and duration; character identity and appearance; required checks.
- **Sources and artifacts:** exact paths, identifiers, versions or revisions where relevant, and which material was read, created, or changed. Keep a detailed artifact index only when the task needs it.
- **Current state:** completed work, open questions, attributed failures, and verification results with the candidate or environment they establish. Distinguish PASS, FAIL, BLOCKED, and NOT RUN when reporting checks.
- **Decisions and conflicts:** what applies now, why, and which earlier instruction or assumption it replaces. Preserve unresolved conflicts explicitly.
- **Next steps:** remaining work and dependencies, including any genuinely required user input.

Store exact copy and structured specifications verbatim when precision matters; a vague paraphrase is not a replacement. Retain reachable originals alongside summaries. Do not write cross-session memory or alter unrelated instructions as a side effect of checkpointing.

## Check that requirements survived

After a context refresh, before a major implementation decision, and before declaring completion:

1. Restore the current brief and relevant anchors; verify that referenced artifacts still exist and that material state has not changed.
2. Reconcile original requirements with subsequent user steering. A new message normally refines the active task; preserve earlier obligations unless they were explicitly replaced or are incompatible.
3. Resolve conflicts through the instruction hierarchy, user choices, applicable versions, and verified sources. Label uncertain or superseded claims so they cannot silently become facts. Ask only when a material conflict cannot be resolved, and continue independent authorized work.
4. Confirm that exact texts, approved decisions, visual specifications, evidence pointers, necessary checks, and the next action can be recovered accurately. Repair omissions from the originals before proceeding; never fill gaps with invented details.

If work starts repeating, ignores available constraints, blends projects, or carries corrected assumptions forward, inspect the affected checkpoint and original evidence. Recover the missing or conflicting information locally rather than loading every source again.

## Evaluate efficiency honestly

Judge efficiency over the whole task. Repeated recovery reads and avoidable rework can outweigh a shorter initial response. Use measured task-level data when available; otherwise describe the method qualitatively. Do not claim token-saving percentages, fixed compression targets, cache benefits, or universal context thresholds without measurement in the actual environment.

Provenance: [sources.json](sources.json), adapted from Filesystem Context, Context Optimization, Context Compression and Context Degradation.

Execution-evidence identity guidance adapted in original wording from [Harness² run records](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/core/runmark.py), reviewed 2026-10-19; [Apache-2.0 notice](references/upstream/harness2/LICENSE).

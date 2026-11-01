---
name: agent-orchestrator
description: Plan and coordinate authorized multi-agent work with explicit dependencies, resource ownership, acceptance checks and integration. Use when the user requests delegation, or an authorized engineering workflow identifies independent tasks worth parallel execution and host policy permits it. Small serial tasks remain direct.
---

# Agent Orchestrator

Use `production-engineering` for requirements and final acceptance, and `smart-router` before choosing worker models/effort. Resolve companions by name in the current catalog. One coordinator owns integration and the combined-result check.

## Decide and divide

Check user authorization, host delegation policy and available tools. Use the host subagent API for subtasks; a user-visible new chat requires the user's specific request. If delegation is unavailable, unauthorized or more costly than direct work, continue serially. This skill installs no runtime or background workers.

A team needs at least two useful independent outcomes or one bounded specialist/review task with a concrete benefit. Account for briefing, duplicated context, waiting and integration overhead. Divide by outcomes and real interfaces while preserving the original requirements. Each worker receives objective, raw inputs, acceptance checks, owned paths/resources, dependencies, constraints and side-effect boundaries. Use host concurrency limits and a proportional time/cost budget.

Dispatch ready, compatible tasks together. Treat reads versus another worker's writes, and concurrent writes, as conflicts unless an explicit snapshot/ownership arrangement makes them safe. Isolate worktrees/copies or serialize conflicts, including external records and test services. Integration starts from settled dependency revisions.

For file-plan validation, read [plan-validation.md](references/plan-validation.md) before using the optional helper. It checks declared IDs, cycles and unordered path conflicts; actual filesystem aliases and non-file effects still need review.

## Coordinate and integrate

Keep one versioned task record, written by the coordinator. Give workers the relevant brief, source links and decisions rather than the whole conversation by default; explicitly pass context they need. Workers return artifacts/diffs, checks and evidence, open issues, and decisions or interface changes affecting others. Reconcile these into the shared record and notify affected workers before dependent work continues. Shared files do not automatically synchronize agent context.

Track actual agent IDs, attempts, input revisions and pending/running/completed/failed/blocked states. Use bounded waits and independent work while waiting. A missing reply or timeout leaves the task unfinished. Retry a recoverable failure only after checking prior effects; reconcile unknown external effects before replaying a mutation.

Review returned artifacts against acceptance criteria, resolve conflicting findings, protect user changes, integrate once and run combined-result checks. For independent review, give the reviewer requirements and candidate artifacts without coaching the verdict. Report who actually reviewed what; coordinator self-review is not independent review.

Design inputs reviewed 2026-10-20: [OpenAI subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents), [Ruflo coordination](https://github.com/ruvnet/ruflo/tree/main/plugins/ruflo-swarm), and [Model Picker task ownership](https://github.com/firecrawl/model-picker). Original bounded workflow and helper; no swarm infrastructure, hooks, consensus engine or automatic permanent memory is installed.

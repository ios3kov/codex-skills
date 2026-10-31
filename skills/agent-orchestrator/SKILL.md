---
name: agent-orchestrator
description: Plan and coordinate authorized multi-agent work with explicit dependencies, resource ownership, acceptance checks and integration. Use when the user requests delegation, or an authorized engineering workflow identifies independent tasks worth parallel execution and host policy permits it. Small serial tasks remain direct.
---


# Agent Orchestrator

Use `production-engineering` for requirements and final acceptance, and load `smart-router` before selecting worker models or effort. Resolve these skills by name in the current catalog. Keep one coordinator responsible for integration; worker completion never replaces combined-result verification.

Before spawning, identify at least two useful independent outcomes or one bounded specialist/review task with a concrete benefit. Compare expected benefit with brief preparation, context duplication, waiting and integration overhead. If direct work is simpler, execute directly. For compatible tasks with ready prerequisites, dispatch them together; serialize shared writes and dependent work. This instruction remains subject to the host delegation policy.

Check the user request, host delegation policy and actual tools first. Use the host's subagent API for subtasks of the current work; a user-visible new chat requires the user's specific request. If agents are unavailable or not authorized, perform useful work serially and disclose that no team ran. This skill does not install an agent runtime or start background workers.

Split by independent outcomes and real interfaces, keeping the user's original requirements intact. Each worker needs the objective, raw inputs, acceptance criteria, owned output paths/resources, dependencies, relevant constraints and side-effect boundary. Supply this explicitly; do not assume the child inherits hidden context. Reserve integration ownership for one coordinator. Use the host's concurrency limits and a proportional time/cost budget rather than spawning a fixed team for every task.

Run parallel work only when prerequisites are ready and resource access is compatible. Treat writes versus another task's reads or writes as conflicts unless the shared snapshot or ownership arrangement makes the access safe. Use isolated worktrees/copies or serialize conflicting edits; include external records and shared test services in the ownership plan. Do not dispatch integration against stale inputs while a dependency is still changing them.

For a file-only plan, the optional standard-library helper checks IDs, dependency cycles, path validity and unordered read/write conflicts:

```sh
python3 <skill-directory>/scripts/validate_plan.py /absolute/plan.json
```

The input is `{"tasks":[{"id":"inspect","depends_on":[],"reads":["src"],"writes":[],"acceptance":"Return source-linked findings"}]}`. Paths are workspace-relative; a directory owns its descendants. The checker reads this plan only. It does not inspect the filesystem, schedule or execute agents, validate symlinks, resolve case-insensitive aliases, or establish that a declared plan covers all shared resources. Review actual paths and non-file side effects separately. Exit 0 means the declared plan is structurally valid; exit 2 reports errors.

Use one shared task record maintained by the coordinator. Give each worker a compact, versioned brief with the relevant source links and decisions, not the entire conversation by default. Workers return changed artifacts, checks and evidence, open issues, and decisions or interface changes that affect others. The coordinator reconciles these updates into the record and sends affected workers the new context before dependent work continues. Workers must not concurrently rewrite the shared record; report updates to its owner. Shared files do not imply automatic live context synchronization between agents.

Track actual agent IDs, attempts, input revision and states such as pending, running, completed, failed or blocked in the existing task record. Use bounded waits and useful independent work, not repeated polling. A timeout or missing reply is not completion. Retry only after identifying a recoverable cause and the prior attempt's side effects. An unknown external effect requires reconciliation before replay; do not launch duplicate mutations.

Inspect returned artifacts and relevant diffs against acceptance criteria. A worker's success message is a claim, not evidence. Reconcile conflicting findings, protect user changes, integrate once, and run affected integration checks on the combined result. For an independent review, give the reviewer the requirement and candidate artifacts without coaching the expected verdict. State who actually reviewed what; a coordinator's self-review is not an independent agent result.

Design inputs reviewed 2026-10-20: [OpenAI subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents), [Ruflo coordination](https://github.com/ruvnet/ruflo/tree/main/plugins/ruflo-swarm), and [Model Picker task ownership](https://github.com/firecrawl/model-picker). Original bounded workflow and helper; no swarm infrastructure, hooks, consensus engine or automatic permanent memory is installed.

---
name: smart-router
description: Choose a model and reasoning effort for a task or delegated step using available host capabilities, task requirements and cost limits. Use before delegating nontrivial engineering work, for cost/quality tradeoffs, explicit model routing, or escalation after a reasoning failure. Small clear tasks stay on the current model without a separate routing ceremony.
---

# Smart Router

## Select execution by task

For engineering work, use `production-engineering` as the owner of specification, implementation and acceptance. Load this router before dispatching nontrivial work; use `agent-orchestrator` only for a justified, authorized team. Discover companion skills by their names in the current skill catalog, not hard-coded installation paths.

- Small, clear, low-risk change: execute directly on the current model; skip a separate routing record.
- Bounded task with clear inputs and acceptance: choose a supported, authorized lower-cost worker when evidence supports suitability. Do not infer cost from a model's name.
- Uncertain diagnosis, architecture, security or cross-module invariants: retain a capable coordinator/worker and enough reasoning to resolve the uncertainty. Strong models may implement code directly.
- Several independent outcomes: assess delegation overhead, dependencies and resource ownership with the orchestrator. Parallelism is useful only when integration remains manageable.

For nontrivial work, keep one compact execution entry in the existing plan: task/risk, direct or delegated mode and reason, requested and actual model/effort (unknown if not exposed), acceptance checks, and retry limit. Avoid a new standalone report. Use at most one corrective retry per unchanged worker approach; after another failure, diagnose and choose a supported escalation, a different decomposition, direct work or an explicit blocker. Never escalate permissions/quota/tool failures by merely choosing a stronger model.

Judge routing by accepted results, elapsed time and total measured usage including coordination, review and rework. Keep cost unknown when unexposed; do not claim savings from price ratios or an unexecuted alternative. Feed failed checks back into the execution entry before retrying.

Establish the decision: advice, configuring an authorized run, or selecting an available worker. Preserve an explicit user model/effort choice. Inspect the current host's exposed model list, routing controls, permissions and budget rather than treating a published model as available to this account. Consult current official documentation when capability or pricing matters. A skill does not switch its own running model.

First filter for hard requirements: tools, input modalities, context/output limits, supported effort values, account access, data destination and deadline. An inexpensive model that cannot use the required tool is not a candidate. Do not invent model identifiers or settings. If execution controls are unavailable, give a recommendation and state that no switch occurred. Never emulate a missing control by editing unrelated global settings or moving private work to another provider.

Among valid candidates, use the smallest suitable choice for the task's uncertainty and consequence of error. A clear mechanical edit needs different reasoning from a disputed diagnosis or a consequential design decision. Use task-relevant measurements when available; a general leaderboard is supporting evidence, not a task success probability. Do not copy upstream score floors, model names or price ratios as permanent defaults. If costs or quota are not exposed, mark them unknown and respect any known user cap.

Before escalation, classify the failure. Missing permissions, credentials, dependencies, unsupported tools, quota, service outages or a wrong acceptance criterion call for resolving that boundary or reporting a blocker. A stronger model is relevant only when the evidence points to a reasoning/capability limit. Keep the triggering case, failed check and proposed benefit. Bound retries, preserve the last valid result, and stop if the new attempt provides no useful evidence or exceeds the authorized budget. A routing decision never authorizes an extra paid service, expanded access or a new data destination.

Use an exposed control only when the user and host instructions allow that exact override. For delegated work, inherit the current model unless an override is supported and authorized; hand the worker a self-contained task brief. Record the recommended choice separately from the actual model/effort returned by the runtime. Report unavailable/unknown values honestly. Compare actual run cost/time and acceptance results where measured; counterfactual savings are estimates, not money actually saved.

Design inputs reviewed 2026-10-20: [OpenAI model controls](https://learn.chatgpt.com/docs/models), [subagent controls](https://learn.chatgpt.com/docs/agent-configuration/subagents), and [Firecrawl Model Picker](https://github.com/firecrawl/model-picker) for capability filtering and cost/quality tradeoffs. Original instructions; no upstream executable, provider connection, fixed benchmark thresholds or automatic host override is bundled.

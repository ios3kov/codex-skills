---
name: smart-router
description: Choose a model and reasoning effort for a task or delegated step using available host capabilities, task requirements and cost limits. Use before delegating nontrivial engineering work, for cost/quality tradeoffs, explicit model routing, or escalation after a reasoning failure. Small clear tasks stay on the current model without a separate routing ceremony.
---

# Smart Router

Use `production-engineering` for engineering requirements and acceptance, and `agent-orchestrator` for justified teams. Resolve companions by name in the current catalog. Small clear tasks stay on the current model without a routing record.

## Choose an available executor

Establish whether the request needs advice, an authorized model change or a delegated worker. Preserve the user's explicit model/effort choice. Inspect the host's actual model list, controls, permissions and budget; use current official documentation when capability or pricing matters.

Filter candidates by required tools, input modalities, context/output limits, supported effort, account access, data destination and deadline. Among valid candidates, choose a model suited to uncertainty and consequence of error:

- Bounded work with clear inputs and acceptance may suit a lower-cost worker when evidence supports it.
- Diagnosis, architecture, security and cross-module invariants need a sufficiently capable owner, who may implement code directly.
- Independent outcomes may justify parallel work after accounting for briefing, waiting and integration overhead.

Use task-relevant measurements where available. A model name, leaderboard, upstream score floor or price ratio alone does not establish suitability or savings.

## Execute and recover

Use exposed controls only within user and host authorization. Delegated workers inherit the current model unless an override is supported and authorized; give each a self-contained brief. If controls or companions are unavailable, continue useful work with available capabilities and record the limitation. Recommendations are distinct from actual model changes; preserve unknown runtime metadata as unknown. Routing does not authorize another provider, paid service, extra access or unrelated global configuration changes.

Classify a failure before retrying. Permissions, credentials, dependencies, unsupported tools, quota, outages or an incorrect acceptance criterion need their own remedy; stronger reasoning helps only a capability failure. Preserve the triggering case, failed check and last valid result. Allow at most one corrective retry per unchanged worker approach, then diagnose and choose escalation, a different decomposition, direct work or a blocker. Stop if the next attempt adds no useful evidence or exceeds the authorized budget.

For nontrivial work, record task/risk, execution choice and reason, requested versus actual model/effort, acceptance checks, retry limit and results in the existing plan. Keep the acceptance requirements unchanged across executor changes. Judge efficiency by accepted results and measured total usage/time, including coordination, review and rework; leave unavailable cost unknown and label counterfactual estimates. Update this entry after failed checks rather than creating a separate report.

Design inputs reviewed 2026-10-20: [OpenAI model controls](https://learn.chatgpt.com/docs/models), [subagent controls](https://learn.chatgpt.com/docs/agent-configuration/subagents), and [Firecrawl Model Picker](https://github.com/firecrawl/model-picker). Original instructions; no upstream runtime or provider connection is bundled.

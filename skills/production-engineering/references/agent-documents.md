# Engineering instructions for agents

Use this reference when editing engineering rules, AGENTS.md/CLAUDE.md, or skill instructions. The host's skill-creation workflow owns skill format, validation, and persistence; this reference only improves the instructions' content.

## Preserve the contract

Read the current canonical rule and the task that authorizes the change. Preserve requirement identifiers, applicability, permission boundaries, mandatory evidence, and existing decisions. Before removing a duplicate, locate its authoritative replacement and the consumers that still need to reach it. Machine registries and generated views may represent the same obligation; preserve their documented synchronization rather than deleting one blindly.

Complete when every changed obligation still has a clear owner and its required consumers can reach it.

## Make instructions reachable and checkable

Keep each meaning in one authoritative location and link from navigation, templates, or examples. A useful pointer says what the material covers and the condition for reading it. Load branch-specific detail through those pointers; keep steps needed by every branch close to the procedure.

Give consequential steps an observable exit: the inspected scope is accounted for, a named check has a recorded result, or an unresolved dependency is explicitly identified. Match the demand to the actual task and risk. A small text correction does not need a full audit, a fixed questionnaire, or new acceptance gates.

Keep definitions, exceptions, and constraints together so that following a step includes its limits. State the intended action directly; retain explicit safety and authority boundaries where they prevent a concrete mistake. Treat writing heuristics as hypotheses to test, not guarantees about a model.

Complete when a fresh agent can determine which path applies, what to do, and how to distinguish completed, failed, and blocked work.

## Remove maintenance noise

Use the live project configuration for cheap facts such as script names and directory layouts. Keep documentation for the non-obvious convention, rationale, or hazard; if a cached command is necessary, name its authority and verify it during the change.

Replace repeated explanations with a precise existing term only when its meaning remains clear. Remove stale or behaviorally redundant text without weakening an obligation. Compare the edited document with its actual consumers and verify affected links, anchors, identifiers, and required generated views. For consequential instruction changes, use a small realistic scenario with the source artifacts; report what was checked and what remains untested.

Complete when the affected consumers remain usable, the intended behavior is preserved or deliberately changed, and validation covers that change. No automatic rewrite of unrelated rules or provider-owned skills follows from this reference.

Source: adapted from [Matt Pocock's writing-for-agents](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/writing-for-agents/SKILL.md), reviewed 2026-10-17. Upstream wording about particular tokens or negation is not adopted as a measured performance claim.

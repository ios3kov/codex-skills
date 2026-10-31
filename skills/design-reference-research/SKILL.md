---
name: design-reference-research
description: Research visual references, explore distinct creative directions, turn inspected examples into a concrete design brief, or curate dated inspiration captures without repeated sources. Use when a task needs reference discovery or synthesis for UI, visual assets, or motion. Focused fixes with an established design target do not require a new inspiration search.
---

# Design Reference Research

For offline use and external-reference handling, read [local resources](references/offline-resources.md).

Produce decisions another designer or builder can execute, with evidence for what was actually inspected. This skill handles reference research and synthesis; the deliverable's design, implementation, generation, and production checks remain with the appropriate craft workflow.

## Select the mode

| Request | Mode | Read |
|---|---|---|
| Find a direction, alternatives, moodboard, or an unusual treatment | Explore | [Research](references/research.md) |
| Ground a new design or resolve a specific visual/product question | Target | [Research](references/research.md) |
| Collect a dated batch, refresh an archive, study complete websites and motion | Capture | [Capture](references/capture.md) |

For image/video prompt references, camera angles, focal lengths, camera moves or visual styles, optionally consult [SHOOOT](https://shoootai.com/) when it can resolve the task; use the access and adaptation guidance in [Providers](references/providers.md). Read Providers for other external catalog access or provider-specific behavior. Source versions and adaptation provenance are in [sources.json](references/sources.json); they are not runtime requirements.

Respect explicit user references, existing identity, real content, and the authorized scope. A requested faithful reproduction uses the supplied target. A refinement uses the incumbent system. Open exploration may replace only the axes left open by the brief.

## Shared research loop

1. **Frame the decision.** Identify the deliverable, audience, task, fixed constraints, open axes, and an observable success condition. Reuse project requirements. Ask only about missing information that would change the result.
2. **Inspect the starting material.** Look at supplied references, actual current output, prior decisions, and available owned assets. An existing target may answer a focused question without external search.
3. **Search to resolve the open question.** Vary queries by function, treatment, and adjacent mechanism. Choose depth from uncertainty; a clear target needs less breadth than a new identity. Stop when the surviving candidates support distinct, executable choices and further searching repeats the same findings.
4. **Inspect finalists.** Read/open the underlying page or asset rather than relying on a thumbnail or search snippet. Record the source, date, relevant viewport/state, evidence type, concrete observation, role, and one transferable mechanism. Keep observed facts, estimates, and proposed adaptations distinguishable. Static images do not establish animation or a complete journey.
5. **Remove repetition.** Check source identity and available media fingerprints against this batch and relevant history. Compare each survivor to its nearest visual/mechanical neighbor, not to the average set. A second example earns a slot only for a new decision, state, or mechanism. An authorized revisit is labeled as a revisit, not new inspiration.
6. **Resolve a direction.** Choose one coherent foundation or an explicit original thesis supported by references. Assign secondary sources bounded roles. Conflicts become a deliberate choice, not an average. Preserve chosen role meanings unless the brief requires a documented change: CTA color, syntax color, and decoration are different jobs.
7. **Hand off the contract.** State the direction, traits to preserve, borrowed mechanisms, deliberate departures, asset strategy, and decisions with reasons. Use actual content, semantic tokens, responsive/state behavior, and concrete motion triggers. Never fabricate product metrics, customers, testimonials, or live functionality from a reference.
8. **Review the actual result.** Research-only work needs source fidelity, useful decisions, and a genuinely distinct selection. If a build or generated output is in scope, compare its rendering with the chosen contract at delivery size and relevant states. Correct material defects and repeat affected checks.

## Working boundaries

- Aesthetic bans and house counts from upstream sources are not universal standards. Judge color, type, density, cards, and motion against this product and its evidence. Do not replace one generic default with another.
- Prefer available tools and permitted access. Refero and Scenario are optional adapters. If a source is unavailable, record the gap and continue with usable evidence; never claim a fallback was a live inspection.
- If the user asked to choose among options, keep that decision pending until answered. If autonomous design was authorized, select the strongest justified direction and proceed. Silence is not approval.
- Reference study does not grant reuse rights. Keep study material separate from deliverable assets, and use owned, licensed, or newly created assets for the actual output.
- Do not create schedules, commit, publish, upload private material, or change account/tool configuration merely because an upstream workflow does so.

## Completion evidence

Report source/coverage, duplicate checks, direction quality, and result validation separately. Use `PASS`, `FAIL`, `BLOCKED`, or `NOT RUN` only for the actual criterion checked. A file validator cannot establish visual quality, motion, usability, or fidelity. For material typography, inspect prominent text and opening copy for optical spacing, collisions, and meaningful line grouping; no-overflow alone is insufficient.

Keep the user-facing closeout short: selected direction and why, useful source links, delivered artifact, checks performed, and any remaining gap. Do not report research volume or repository stars as proof of taste or correctness.

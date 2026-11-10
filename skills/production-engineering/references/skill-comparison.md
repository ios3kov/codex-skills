# Compare skill changes

Use when improving a reusable skill or agent workflow and a behavior comparison would resolve a material uncertainty. A small factual correction or repaired link usually needs only its direct check. Do not start an optimization loop for ordinary task completion.

## Define the comparison

Keep the current version as the baseline. Name the observed problem, a small proposed change, its expected effect, and a plausible downside. Separate a process problem from missing domain knowledge so the change reaches the right reference. Preserve the user's requested output format and authorization boundaries.

Choose realistic cases with independently defined acceptance criteria before inspecting candidate outputs. Include the motivating case and fresh cases with different facts; include a case where the new instruction should not apply. Existing project checks and approved expected results remain valid evidence. Keep private evaluation answers out of execution context; provide the actual user requirements normally.

Use isolated workspaces for runs with side effects. Compare under the same relevant tools, model/settings and case inputs, recording differences that cannot be controlled. Set a proportional limit on cases, repeated runs, time and cost. Extra paid services, delegation or live actions still need their applicable authorization. A source review or manual walkthrough is useful but is not a model execution.

When changing skill descriptions or selection rules, include realistic prompts in the user's language, including similar prompts owned by another skill. Measure actual selection separately from task quality. For reviewer changes, include a clean candidate and a pre-existing defect that should not be counted as a regression. Record interrupted or incomplete executions separately from scored cases.

## Compare outputs and behavior

When practical, present outputs under neutral, shuffled labels and judge against the request and source before revealing their versions. Include the baseline and accept it as a possible winner. The reviewer should inspect the actual artifact, including rendered output when presentation matters; a confident explanation is not evidence of correctness. State when the author also reviewed the outputs instead of calling that review independent.

Then inspect execution records to explain any difference. A winning output does not establish which instruction caused it. If several instructions changed together, or evidence consists of one differing run, record the attribution as unclear. Repeat only where randomness or an unresolved difference justifies the extra cost. A rare but material failure remains a finding; frequency alone does not dismiss it.

## Keep, revise or reject

Use the existing task record for a compact evaluation row: change/owner, trigger, baseline and candidate identities, case and expected result, actual output/check, reviewer and independence, observed effect or unclear attribution, measured cost/time if available, and keep/revise/reject decision. Before merging duplicated guidance, identify its canonical owner and every required caller; preserve meaningful exceptions. A shorter instruction or smaller file count is not evidence of better behavior.

Record the baseline/candidate identity, cases, checks, delivery failures, material regressions, cost/time where measured, and the reason for keeping, revising or rejecting the change. A test on the motivating case alone supports that case, not general improvement. Keep the baseline when evidence is insufficient, or retain a narrowly justified correction while marking broader behavior unverified.

Merge supported changes by resolving overlaps rather than joining every proposed rule. Update only the authorized source and installations; verify saved content in each requested client. Installation, loading, scenario performance and broader benefit are separate claims. Keep notes in the task's existing evidence record; saving permanent memory is a separate authorized action.

Provenance: independently worded adaptation of the comparison, selection and reflection methods in [Harness²](https://github.com/google-research/harness2/tree/1cfe254e8d25b15f37048c3730134686abe60335), reviewed 2026-10-19. [Apache-2.0 notice](upstream/harness2/LICENSE). No Harness² runner, hooks, sandbox changes or automatic learning installed.

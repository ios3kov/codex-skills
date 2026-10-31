# Session retrospective

Use for a requested retrospective or a recurring process problem within the authorized task. Ordinary task completion does not require a retrospective, new rules, or automatic permanent changes.

## Inspect the actual session

Read the specified session's available messages, diffs, commands, results, and relevant project instructions. Default to the current session when none is specified. Separate observed friction from a suspected cause; state missing evidence instead of reconstructing a log from memory.

Look for repeated failed attempts, slow navigation, expensive repeated reads, missed checks, conflicting instructions, and missing information. Check the repository's existing scripts, linter, hooks, and CI before proposing another mechanism: an existing check that was skipped, disabled, or broken is a different finding from an absent check.

Complete when each candidate improvement names the observed event, its consequence, the relevant existing control, and the uncertainty about its cause.

## Choose a small prevention measure

For a mechanical rule with an objective signal, prefer the least expensive suitable deterministic check in the project's current tooling. Demonstrate that the check detects the observed mistake and accepts a legitimate case when implementing it. For a judgment call, clarify the applicable review standard with a concrete example. If navigation or duplication caused the friction, apply the [agent-document reference](agent-documents.md).

Prioritize by demonstrated impact and recurrence, and state the maintenance cost. A one-off mistake may need only a corrected action. Do not create duplicate controls, add a rule for every slip, or claim reduced error rates without comparative evidence.

Complete when the recommendation explains why the existing control is insufficient and how the proposed change can be verified.

## Report and act within scope

When comparing workflow or skill changes, separate the selected output from the effect of each edit. For material edits record the changed component, the observed behavior difference, its evidence location, and whether it helped, hurt, had no observed effect, or has an unclear cause. Several simultaneous edits or one differing execution usually leave attribution unclear; selection alone proves no causal benefit. Review rejected variants too when their evidence is relevant. Use the [skill comparison reference](skill-comparison.md) when an actual comparison is warranted.

Only suggest a transferable lesson when the record supports a concrete trigger, action and evidence; otherwise record that no reusable lesson was established. Keep the lesson in the authorized task record. A retrospective does not authorize writing permanent memory or installing new global rules.

Present the highest-value findings concisely. Distinguish a proposal from an implemented change. A request to analyze a session authorizes analysis; it does not authorize editing global instructions, installing tools, changing secrets, messaging others, or deploying. When the user has authorized the identified improvement, implement and verify the scoped change through the existing workflow without asking again.

Reuse the existing review or status record if one is needed. The final result names the observed issue, action taken, verification, and remaining limitation; it does not introduce an additional release gate.

Source: adapted from [Matt Pocock's retro](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/retro/SKILL.md), reviewed 2026-10-17.

Comparison attribution guidance adapted in original wording from [Harness² reflection](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/core/prompts.py), reviewed 2026-10-19; [Apache-2.0 notice](upstream/harness2/LICENSE).

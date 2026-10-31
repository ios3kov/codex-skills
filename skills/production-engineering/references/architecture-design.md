# Architecture decisions

Use when an implementation requires changing module responsibilities or interfaces, the user requests architecture improvement, domain terms are materially ambiguous, or a separate architecture decision record needs consideration. For a terminology-only or decision-record question, go directly to [Domain terms and decision records](#domain-terms-and-decision-records); the interface-analysis steps are not prerequisites. `codebase-understanding` owns descriptive mapping; this reference evaluates a proposed change inside the existing engineering workflow.

## Locate complexity before adding an abstraction

Inspect representative callers, the current public contract, shared state, and real failure paths. The contract includes ordering, ownership, lifetime, errors, configuration, and performance expectations, not only a type signature. Use the domain terms and decision records below when a concrete ambiguity needs resolution.

Ask what complexity the interface removes for callers. A useful module contains a coherent responsibility and hides decisions its callers should not repeat. A smaller method count alone is not improvement: an opaque configuration blob or hidden global state can make an apparently small interface harder to use correctly.

Treat repeated setup/cleanup sequences, exposed internal ordering, changes scattered across callers, and duplicated invariants as candidates. Trace examples before refactoring. A thin adapter may be justified by an external boundary, stable contract, or actual test isolation even when it has one implementation; neither a second implementation nor an arbitrary line-count ratio is required.

## Choose the seam that supports the actual change

Place replaceable behavior at a useful boundary: clock, random source, filesystem, network, database, host callback, or another concrete dependency. Separate deterministic transformation from external effects where it simplifies the task. Do not force pure functions onto inherently stateful behavior or create an interface for every class.

Compare a small local correction with an extracted responsibility when the choice matters. State which callers become simpler, where invariants live, how errors and cancellation propagate, and how compatibility will be verified. Use multiple design alternatives only for a consequential ambiguity; parallel agents or an interview are not prerequisites.

When changing an interface, inventory its usages and test the behavior at the relevant boundary using [behavior testing](behavior-testing.md). Keep deliberate compatibility adapters and remove superseded indirection only within the authorized scope. The main workflow owns specification, acceptance, regression, and completion; architecture notes do not create another approval or release gate.

## Domain terms and decision records

Read the existing glossary or specification before defining a term. Compare a disputed meaning with actual code and concrete scenarios, including boundaries such as partial cancellation or ownership transfer. Separate the observed behavior from the desired contract: code alone does not decide what the product should do. Ask only about a material decision unresolved by the accepted context.

Update the existing authoritative definition when a meaning is settled. Keep terminology in the glossary and implementation details in the specification or design record; create a new glossary only when an actual term needs recording. Complete this step when the affected concepts have consistent names and any behavior discrepancy is resolved or explicitly tracked.

For an optional separate architecture decision record, use all three conditions: changing the decision later has a meaningful cost; a future reader would find it surprising without context; and the choice reflects a real trade-off among alternatives. Otherwise keep the necessary rationale in the existing issue or specification. This filter does not waive records, traceability, or evidence required by the project's standard. A concise paragraph can suffice when the existing format allows it.

Source for these additions: [Matt Pocock's domain-modeling](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/domain-modeling/SKILL.md), reviewed 2026-10-17; adapted within the existing contract.

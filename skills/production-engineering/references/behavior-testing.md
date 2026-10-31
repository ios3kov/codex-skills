# Behavior-focused testing

Use when selecting or improving tests for a feature, bug, parser, numeric transformation, state machine, or refactoring. The existing workflow decides when TDD and other checks are warranted; this reference improves the tests rather than making every edit test-first.

## Choose an observable contract

Take expected behavior from the specification, an independently worked example, an approved format, or a trusted oracle. Assert through a stable public boundary when practical. Internal tests are appropriate for a meaningful algorithm or invariant that needs direct isolation; avoid asserting private call order merely because the current implementation has it.

A test should fail for a plausible incorrect behavior. Avoid recomputing the expected result with the same algorithm, generating a snapshot from the candidate and accepting it unseen, or mocking away the boundary whose correctness is the question. Distinguish a contract test with a fake from actual integration with the real dependency.

For TDD already warranted by the task, build a behavior slice with a failing case, minimal implementation, then the applicable refactoring/review. Check why the test failed: missing imports, a broken fixture, and environmental errors do not establish the intended regression. Infer the test surface from requirements and existing callers; ask only when a material product contract is undecided, not before every test.

## Use fixtures that preserve the signal

Control clocks, randomness, external responses, and temporary resources at their actual boundary. Keep realistic inputs and important protocol errors. Scope cleanup so one test cannot erase another's state. For concurrent code, prefer barriers, events, or explicit readiness and deadlines over sleeps; verify cancellation and teardown when they are part of the contract.

Use existing project tools and conventions. Coverage highlights unexecuted paths; it does not prove that assertions constrain behavior. Do not introduce a fixed coverage percentage, new test framework, mandatory mutation campaign, or broad suite expansion solely from upstream guidance.

## Properties when the domain supports them

Useful candidates include roundtrip encoding with the format's equality semantics, canonicalization idempotence, output bounds, ordering plus preservation of elements, state invariants, or comparison with an independently trusted implementation. State valid domains and preconditions: lossy conversions, floating-point arithmetic, nondeterminism, and invalid input can invalidate a superficially attractive property.

Generate valid inputs directly where practical; excessive filtering can make a passing test exercise almost nothing. Include boundary and malformed cases separately. Preserve the minimized counterexample, seed/replay information, and failing operation sequence. Investigate a wrong property or generator as well as a possible implementation defect; a shrunken example is not automatically a confirmed bug.

Use an existing property-testing library when available. A small bounded exhaustive set can be enough without a new dependency. Coverage-guided fuzzing checks different behavior and belongs to a scoped runner; [native review](native-code-review.md) covers its native-code use. The main workflow owns evidence and statuses. Record explored cases and actual runs without claiming proof over an infinite input domain.

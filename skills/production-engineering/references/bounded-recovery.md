# Bounded failure recovery

Use for a failed check, tool or operation that requires diagnosis and repair. Preserve the failing input, expected outcome, actual error, relevant source/environment identity and any partial result. Establish whether the operation changed local or external state before retrying it.

Classify the failure: implementation defect, wrong requirement/test, missing dependency, permission/credential boundary, unsupported capability, resource/quota exhaustion, transient service error, or uncertain external effect. A model escalation is not a remedy for missing access or an incorrect test. Read the existing runner and error evidence before adding another tool or control.

Choose the smallest authorized correction and a concrete check of the original symptom. For repeatable local operations, set a small attempt/time/cost limit proportional to risk and stop when attempts repeat the same state without new evidence. For transient failures, use the service's retry guidance when available. For an unknown external effect, reconcile the actual state or use the service's documented idempotency mechanism before replay; do not duplicate purchases, messages, deployments or other mutations.

Consider a stronger available model only if the record indicates a reasoning or capability limit, the host allows the switch, and the user's model choice/budget permits it. Keep recommendation, attempted switch and runtime-confirmed model separate. No access expansion, new provider, secret entry, broad upgrade or protection change follows from a failed check.

After correction, repeat the affected original check and relevant regression checks. Distinguish a repaired implementation from a repaired environment or corrected expectation. If blocked, preserve the last valid artifact, exact error, attempted fixes and next useful action in the existing checkpoint. Continue unaffected authorized work; do not turn a failed optional check into a claim of overall readiness.

This is original recovery guidance within the existing engineering workflow. It adds no background agent, mandatory optimization loop or automatic global instruction changes.

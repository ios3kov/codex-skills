# Product UX Review

Use when reviewing a task flow, onboarding, discoverability, navigation, or recovery states. Keep the review tied to a real scenario and affected surface; a visual polish request alone is not a whole-product UX audit.

## Follow a real task

Identify the audience, starting context, desired outcome, and available evidence. Walk the actual journey: entry, orientation, main action, feedback, completion, and return. Use novice or frequent-user perspectives only when relevant. Separate observed behavior from hypotheses that need user research; do not invent interviews, conversion figures, or a numeric health score.

Check whether each step communicates where the user is, what is possible, what information is required, and what happens next. Reduce unnecessary choices or repetition without hiding essential controls or content. There is no universal maximum number of controls, steps, or headings. Evaluate effort against the real task and frequency.

## First value and repeat use

Let users reach a meaningful result with the information genuinely required at that point. Explain unfamiliar concepts near their use. Make optional tours or setup skippable/dismissible where appropriate, and keep help reachable later. Preserve progress and a clear route back into unfinished work when the product supports it. Do not label mandatory security, consent, or dependency steps optional merely to shorten onboarding.

## Distinguish states and recovery

Use the states that actually exist:

| State | Useful answer |
|---|---|
| First-use empty | What belongs here and how to create the first useful item? |
| User-cleared empty | What happened and how can the user restore or add content? |
| No search/filter results | Which query/filter applies and how can it be changed? |
| Loading or background work | What is in progress and which controls remain usable? |
| Permission or prerequisite missing | What access/setup is needed and which authorized route exists? |
| Failure | What failed, what remains preserved, and which retry/recovery action works? |
| Successful completion | What changed and what meaningful next action is available? |

Avoid a generic empty message for every cause. Preserve input on recoverable failures where possible; do not offer a retry, undo, or permission request that has no working behavior.

## Report actionable findings

For each finding, connect the observed obstacle to its consequence and a scoped correction; prioritize blocking failures over preference. Keep wording/claims with `editorial-copy`, semantics and accessibility criteria with [implementation](implementation.md), and verification/evidence with [browser verification](browser-verification.md) or the existing engineering workflow. This reference supplies scenario analysis, not a second standards checklist.

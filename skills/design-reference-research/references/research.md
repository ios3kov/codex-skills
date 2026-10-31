# Research modes and handoff

## Target: answer a specific design question

Identify which evidence layer the question needs:

| Layer | Extract | Do not infer |
|---|---|---|
| Visual system | Hierarchy, type personality, density, color roles, media treatment, section rhythm | Product behavior from marketing decoration |
| Screen/state | Information structure, controls, labels, empty/loading/error/selected states | A full workflow from one screenshot |
| Journey | Entry, decisions, actions, system responses, completion, recovery | Unobserved steps as facts |

For an existing dashboard or native app, begin with its actual screen/system and relevant task states. Marketing references can inform a bounded visual treatment; they do not dictate operational density or native behavior.

A focused correction may use the current component and a verified sibling pattern as sufficient evidence. For a new surface, search several angles and inspect a compact set of strong candidates. Counts are working budgets, not quality gates. Expand only for an unresolved decision or insufficiently different evidence.

If a journey must be reconstructed from isolated screens, label the reconstruction as a proposal and identify unknown transitions. Do not silently import persuasion or retention tactics that obstruct the user's task.

## Explore: expand choices without losing relevance

Before broad search, write down the obvious category treatment and the predictable reaction against it. These are baselines to challenge, not bans on the user's brand or on a solution that actually fits.

Search a distance ladder:

- **Near:** the same task or medium; learn its actual constraints and familiar solutions.
- **Adjacent:** another domain solving the same structural problem.
- **Far:** a different visual/material tradition with a mechanism that can be mapped to this task.

Use transformations on the fixed subject: invert one optional assumption, transfer a mechanism from another domain, or solve the same function through a different representation. Do not change the requested subject or mandatory constraints to make an idea look surprising.

For example, for an industrial plugin catalog, an archive index might inform navigation, a material specimen sheet might inform product grouping, and a live signal display might inform activity feedback. A random photograph earns no role merely by being unusual.

An unexpected find survives only if its connection and concrete value can be named. Compare the widened set with the literal baseline; if the mechanisms are unchanged, the search did not add useful range.

When randomness would help escape habitual suggestions, use an available seeded sampler and record its seed and operator. It is optional; do not report model-generated surprise as statistical randomness or invent probability percentages. A curated corpus also has bias.

## Select authored options

For undecided exploration, a few strong directions are more useful than a search dump. Two options may resolve a known fork; three or four can expose a wider range. Respect the user's count and do not pad the set.

Name the comparison axis before the options: e.g. documentary vs diagrammatic vs immersive presentation. Keep other constraints stable. If several axes deliberately vary, label each position so the comparison remains interpretable.

Each option carries a parallel title, intent, inspected references, distinguishing mechanism, audience/task fit, and what it gives up. Remove a dominated option; do not add a weak decoy to steer the user. Different colors or prompts do not prove different concepts.

Compare every option to its nearest alternative. If the pair makes the same layout, information, and interaction decisions, merge it or change the deciding axis. Retain brief reasons for significant rejections. Offer a meaningful route for “none”, a bounded hybrid, or a different axis when requesting a choice.

## Direction contract

Keep one decision record rather than separate repetitive summaries, locks, and ledgers. It can be a short note or structured artifact:

```text
Task and success criterion:
Fixed constraints / open axes:
Target or dominant thesis:
Chosen traits and their roles:
Secondary mechanism -> source -> bounded use:
Product structure and relevant states:
Media plan: owned/licensed/generated/code-native; slot and crop:
Departures from sources and why:
Rejected treatment and task-specific reason:
Unknowns requiring evidence:
```

For each major unresolved choice add `decision -> evidence or brief -> role -> rationale -> how to check`. Exact values must come from inspected source metadata, existing tokens, measurement, or an explicitly proposed new value. A screenshot's apparent font or motion timing is an estimate unless confirmed.

In a UI brief specify information order, real copy, type hierarchy, color/state meanings, spacing/density, component behavior, narrow/wide transformations, and motion only where it contributes. In an image brief specify subject, composition, silhouette, light quality/direction, palette relationships, materials, crop, and rest/detail areas. Exact brand typography and logo geometry belong in editable assets/compositing, not a claim that generation will reproduce them.

## Board and prompt handoff

A research board is exploratory; a selected style frame depicts the actual deliverable; a direction contract states what binds. Do not treat every board detail as approved.

Each retained reference has **role**, **reason**, and **take**. Use roles suited to the medium: hierarchy, typography, UI state, flow, motion, composition, lighting, material, silhouette, or identity. Keep conflicting lighting/material systems in separate directions. One conceptual foundation does not require borrowing an entire artist's composition or populating most of a board with their work.

Reduce a broad collection to the smallest role-complete handoff. For image tools, three to six references can be a useful starting budget, but the tool's actual schema and identity needs govern. Separate subject/identity, structure, and style inputs. Avoid contradicting reference inputs with the text prompt; still state hard requirements the tool cannot infer reliably.

Write concrete mechanisms rather than quality adjectives. Convert exclusions into actionable desired states where useful. Negative-prompt support is model-specific; do not invent it or universally prohibit ordinary negation.

## Review according to the deliverable

- **Research only:** sources actually inspected; observations traceable; useful role per item; pairwise distinctions; contract can be executed without guessing major decisions.
- **UI build:** chosen traits survive; real content and media; representative narrow/wide layouts and relevant interactive/recovery states; optical text review at delivery scale. Run functionality/accessibility checks through the implementation workflow.
- **Generated asset:** inspect the actual placed crop/size for silhouette, palette, material, detail, identity, and any required text. Grayscale/distance/motion checks apply when readability under those conditions is required.
- **Motion:** inspect playback and user-triggered transitions, including interruption and reduced motion where applicable. A storyboard or frame set supports composition, not smoothness or timing.

Style judgments are recommendations unless they violate a locked requirement. A source-backed choice can still be poor for the current product; test it against the user's task, not just similarity.

# Design System Reuse

Use for repeated UI patterns, inconsistent tokens or variants, and a requested component/system consolidation. A local visual fix does not require building a design system.

## Start with the incumbent system

Inspect existing tokens, theme boundaries, component APIs, and representative usages. Keep the project's naming, framework, and styling conventions unless their replacement is authorized. Identify which differences encode a real semantic distinction and which are accidental drift.

Where useful, distinguish primitive values (a color or spacing scale), semantic roles (surface, text, danger), and component aliases (a specific control's states). Reuse the existing layers; do not require all three or introduce parallel hardcoded values beside established tokens. Preserve theme inheritance and scoped overrides.

## Extract from demonstrated repetition

Group elements by purpose and behavior, not just similar pixels. Several repeated instances can indicate a useful shared component, but a fixed repetition count is not a rule. Extract when it reduces concrete inconsistency or repeated maintenance; keep an exceptional layout local.

Define the smallest API that expresses real variants and states. Check content sizes, enabled/disabled/loading/error behavior, keyboard/focus behavior, and responsive constraints that those usages actually need. Avoid a universal component full of speculative options. Accessibility requirements remain in [implementation](implementation.md), rather than being redefined here.

## Migrate within scope

List affected usages before replacing them. Migrate a representative usage, then the authorized set; preserve behavior, contracts, theme treatment, and legitimate exceptions. Check parity with real content and the relevant states. Document deliberate remaining exceptions in the task handoff, not as a competing component system.

Use [browser verification](browser-verification.md) for interaction and visible parity, and the established engineering workflow for regression coverage. Report what was consolidated and what remains local. Do not expand a consolidation request into a product-wide rewrite.

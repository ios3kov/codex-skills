---
name: interface-craft
description: Design, implement, critique, and polish web interfaces with a coherent visual direction, precise typography, reusable design systems, scenario-based UX review, accessible interaction, focused React performance improvements, and browser verification. Use for pages, components, dashboards, portfolios, and redesigns; complement existing engineering workflows rather than initiating a release or whole-product audit.
---


# Interface Craft

For offline use and external-reference handling, read [local resources](references/offline-resources.md).

Translate a product brief into a distinctive, usable interface. Preserve the existing brand, routes, content, data contracts, and accessibility unless changing them is part of the user's request. Use the project's actual stack and component system.

## Choose the working mode

Classify the surface, not the whole product:
- **Persuade:** a visitor decides to act; communicate the offer, evidence, and primary action.
- **Operate:** a user completes a task; favor scanability, predictable controls, useful density, and fast feedback.
- **Read:** a reader understands material; favor structure, reading rhythm, navigation, and comprehension.
- **Experience:** a visitor explores the work; let the artifact lead while controls remain discoverable.

Classify the change as new work, refinement, or an authorized replacement of the visual language. A polish request normally evolves the incumbent design. Do not infer an overhaul from a request to improve quality.

Read only the relevant reference:
- [Visual direction](references/visual-direction.md) for composition, brand interpretation, typography, density, and redesign.
- [Design catalog](references/design-catalog.md) for optional, bounded local search when a direction needs styles, palettes, font pairings, landing structures, or chart alternatives.
- `brand-system` (when available) for a requested identity/logo task or faithful 2D/3D treatment; ordinary interface styling stays here.
- [Reusable design workflows](references/design-workflows.md) for source-to-DESIGN.md extraction, durable project decisions, real-material page planning, isolated component-state previews, or shadcn-specific work. Read only the applicable section.
- [Design system reuse](references/design-system-reuse.md) for existing tokens, recurring components, variants, and scoped consolidation.
- [Product UX review](references/product-ux-review.md) for task journeys, first value, discoverability, and recovery states.
- [Typography](references/typography.md) for typeface selection/pairing, font loading/features, spacing, wrapping, figures and measured text rendering. Read it before choosing typefaces or when creating or refining prominent headings, introductory copy or text-heavy layouts; apply its optical and semantic review before declaring those surfaces complete.
- [Editorial layout](references/editorial-layout.md) for image/text relationships, multi-page or screen sequences and visual reading rhythm; preserve the requested format's own production checks.
- [Implementation](references/implementation.md) for UI semantics, accessible states, responsive behavior, and React/Next.js performance.
- [Visual refinement](references/visual-refinement.md) for a source-linked change ledger, coherent repair passes, cross-preview data consistency, or optional snapshot/before-after story tools.
- [Browser verification](references/browser-verification.md) for real interaction, screenshot review, readiness conditions, and observed failures.
- [Sources](references/sources.json) for pinned upstream instructions, adaptation boundaries, and technical authorities; consult a linked source only when deeper detail is needed.

## Apply the smallest complete design pass

1. Inspect the target's current visual truth and existing tokens/components. Identify the audience, main task, surface mode, and specific quality problem.
2. For a new visual system, choose a coherent direction for type, color, spacing, imagery, hierarchy, density, and motion. For a focused defect, fix that outcome without regenerating the whole system.
3. Implement with real content and assets. Every visible action must work or represent an explicitly agreed prototype state; attractive mock controls do not satisfy an implementation request.
4. Inspect the changed surface at its relevant desktop/mobile sizes and interaction states. Batch related visual defects into a correction pass, then confirm the fixes. Continue only for a remaining defect or acceptance gap, rather than optional endless polishing.

The brief and established brand supersede aesthetic bans from upstream sources. Serif, shadows, gradients, card grids, glass, and particular icon libraries are choices to justify, not universal violations. Landing-page expressiveness does not dictate dashboard density or task flows.

Use `apple-design` for requested Apple-style gesture physics, momentum, and materials. Use the existing engineering workflow for specifications, regressions, security, production audits, and release gates. This skill supplies the visual and interaction decisions within that workflow; it does not duplicate those gates. Prose editing and durable context management belong to their respective skills.

Report what visibly changed and the verification actually performed. Static inspection, screenshots, functional interaction, accessibility checks, and measured performance answer different questions; do not substitute one for another.

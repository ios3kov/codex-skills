---
name: visual-diagrams
description: Design readable architecture, process, state, dependency, data and comparison diagrams, including faithful conversion from Mermaid, drawio or Excalidraw to branded HTML or SVG. Use when relationships benefit from a diagram; use standard plotting for scientific figures.
---

# Visual diagrams

Choose the visual from the relationship being explained. A table is often better for attribute comparisons; a sentence is enough for one simple fact.

1. Establish audience, content, source of truth, output format and available brand tokens. Use the project's established design language; if none exists, state a reasonable visual assumption and proceed. Ask only when missing information materially changes meaning or fidelity.
2. Select semantics before layout: state/guard, time/message, ownership/handoff, topology, quantity, or hierarchy. Read [diagram grammar](references/diagram-grammar.md) for the selected family.
3. Plan an overview and detail when density obscures meaning. Around nine nodes, twelve connectors and two focal accents are useful starting budgets, not permission to discard requirements.
4. Build the requested editable format. Self-contained HTML with inline SVG is useful for portable polished output; compact engineering explanations can use Mermaid. Respect requested SVG, PNG or source-file delivery.
5. Verify labels, direction, relationship meaning, geometry, accessibility and rendered legibility. For imports or simplification, reconcile the source against an explicit fidelity ledger.

## Ownership and style

This skill owns diagram semantics and connector geometry. Use `codebase-understanding` when relationships still need to be established from source code. Use `interface-craft` for the surrounding web product only when that work is requested; diagram creation alone does not require a UI redesign.

Serif headings, muted paper, small radii and border-only shapes are optional editorial choices from the source. They do not override the brand. Color must distinguish roles consistently rather than marking every node as important. Motion is optional and should explain ordered change; the complete static state must remain understandable.

## Delivery

Include the visual, its usable source, assumptions affecting interpretation and any merged, omitted or hidden content. If every source element was requested, distribute content over detail views rather than silently shortening it. A successful render verifies appearance, not the correctness of undocumented system behavior.

Provenance: [sources.json](sources.json), adapted from Diagram Design.

For diagram labels and legends, consult the shared [typography reference](references/shared/interface-craft/references/typography.md) when font features or text spacing matter. Apply it within the chosen SVG/HTML grammar; label fitting and connector masks still need diagram geometry checks.

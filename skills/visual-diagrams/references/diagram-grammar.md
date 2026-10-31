# Diagram grammar and rendering

## Choose by meaning

| Meaning | Suitable grammar | Preserve |
|---|---|---|
| System or deployment snapshot | Architecture, deployment, layer stack | Components, boundaries, dependencies, zones, protocols |
| Topology change | Synchronized before/after architecture | Stable IDs and an explicit change ledger |
| Conditional path | Flowchart | Branch labels, decision conditions, termination |
| Lifecycle | State machine | Initial/terminal states, guards, retries, cancellation, invalid transitions |
| Actor messages over time | Sequence | Sender, receiver, message order, sync/async distinction |
| Cross-team handoffs | Swimlane or process | Ownership, input/output, waits and exceptions |
| Dependency or parentage | Graph or tree | Direction, cycles, shared children; do not force a graph into a tree |
| Business entity model | ER | Cardinality, optionality, entity keys |
| Physical data schema | Database schema | Column types, keys, constraints, indexes |
| Quantitative change | Line, slopegraph, waterfall | Units, signed contributions, scale and timestamps |
| Category comparison | Bar, dumbbell, heatmap | Common baseline, ordering, legend and missing data |
| Parts or flows of a total | Treemap, Sankey | Denominator or conserved quantity; width/area must encode data |
| Schedule or history | Gantt, timeline | Dates, duration, dependencies, overlap |
| Multivariate positioning | Scatter, bubble, quadrant | Axes, units, thresholds; distinguish measured and subjective values |
| Feedback loop | Loop/flywheel | Feedback direction, what accumulates, triggering conditions |
| Containment or stages | Nested view, pyramid, funnel | Scope and stage meaning; measured conversion needs real denominators |

For specialized forms such as Wardley maps, marimekko, fishbone, axonometric views, radar or polar charts, consult the matching type reference in the pinned upstream source listed in sources.json. Read only that form's instructions. Avoid decorative geometry that implies unsupported measurement.

## SVG geometry

- Prefer rounded orthogonal routes for technical schematics; reserve other routes for grammars that require them.
- Give parallel routes visible separation and distinct attach points. Show crossings unambiguously. Never route a line through an unrelated node.
- Place edge labels beside their stroke on a background matching the active semantic surface token. Ensure masks do not cover neighboring nodes or connector endpoints. Preserve full labels; do not truncate to satisfy an aesthetic cap.
- Establish a consistent grid for box alignment and spacing. Draw connectors before nodes; inspect layers and masks after rendering.
- Keep legends outside the crowded plotting area. Distinguish decorative accents from status colors and provide labels beyond color alone.
- Prefix SVG IDs per diagram/variant. Use `role="img"`, `aria-labelledby`, and filled `<title>` and `<desc>` elements; provide a textual explanation or data table where needed.
- Use a viewBox encompassing annotations and legend. At small sizes choose a readable re-layout or an explicitly local scroll container; do not cause whole-page horizontal scrolling.

## Fidelity and checks

Record source element ID, destination ID/view and disposition: retained, merged with reason, hidden with retrieval path, or omitted with authorization. A rewritten label must preserve its meaning; approved exact labels stay exact.

Inspect actual output at intended size and a smaller view: clipping, overlap, direction, legend completeness, readable type, contrast, focus/control behavior and print/export. For animated output also inspect static/no-JS and reduced-motion states. Do not invoke upstream self-check scripts unless they are present and their dependencies are understood; report checks actually performed.

# Source-linked graphs and incremental analysis

## Minimal useful model

For durable graphs record repository/revision, local-change identity, scope, exclusions and analysis limitations. Nodes need stable IDs, type, name, path, source span and a concise responsibility. Types may include file, module, function, class, configuration, service, endpoint, table, schema or pipeline.

Edges need source ID, target ID, relation and evidence location. Distinguish import/containment/inheritance from actual call, read/write, route, deployment and configuration relationships. An import does not prove a function was called. Keep uncertain dynamic dispatch, generated registration and runtime-loaded dependencies explicitly uncertain.

Separate facts established from syntax, architecture inferred from source and behavior actually observed during execution. Numeric weights in a graph are not measured probabilities unless there is a defined calibration.

The [optional project-map helper](project-map-helper.md) implements a conservative subset of this contract. Its whole-scope rebuild handles changed/deleted/untracked bytes; broader semantic mapping still requires source review. Preserve its syntax/candidate distinction and coverage gaps rather than relabeling its output as a complete architecture model.

## Incremental updates

Compare the current source with the revision and local state used for the existing map. Reconcile added, changed, deleted and newly excluded files; a Git SHA alone does not identify uncommitted bytes. Review changed declarations, imports and affected inbound/outbound relationships.

Carry forward unchanged evidence only when its source and interpretation still apply. Detect missing symbols by identity and ownership as well as counts: equal counts can hide replacement or loss. A deleted file is different from a still-present file with a missing symbol.

Confirm symbol deletion from current source with a suitable parser or explicit manual source verification. Unsupported syntax or incomplete parser coverage remains unknown; do not fabricate old nodes to make a completeness check pass. Reanalyze the affected file and its relationships before promoting the candidate.

## Reconciliation

Check unique IDs, valid endpoints, accurate paths/spans, nonempty scope and source correspondence. Report coverage per requested scope and unresolved parser/runtime limitations. Inspect a representative entrypoint-to-outcome path against code and tests or runtime evidence if available.

When an update fails, keep the last valid map and save the candidate and diagnostics separately. A limited retry can address a specific failure; repeating the whole repository analysis without new evidence is not a recovery strategy. Final output must distinguish confirmed structure, inference and unverified runtime behavior.

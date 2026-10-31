# Optional local project-map helper

Use for repeated navigation across an unfamiliar project, a cross-file change, or a durable code/document map. A known one-file fix or an ordinary text edit generally needs only search and source reading. This is one shared helper, owned here; Production Engineering owns change-impact decisions and Context Discipline owns freshness/output discipline. If this skill or Python is unavailable, use ordinary search and source files; do not install Graphify or another service to make the workflow work.

## Commands

Locate `scripts/project_map.py` relative to this skill's actual loaded directory. Python 3.11+ and its standard library suffice. Choose an explicit project root and a task-owned map path, preferably outside the source tree. Nothing runs until explicitly invoked.

```sh
python3 <codebase-understanding>/scripts/project_map.py build /project --map /task/project-map.json
python3 <codebase-understanding>/scripts/project_map.py status /project --map /task/project-map.json
python3 <codebase-understanding>/scripts/project_map.py search /project --map /task/project-map.json --query alpha --limit 12 --max-bytes 8192
python3 <codebase-understanding>/scripts/project_map.py impact /project --map /task/project-map.json --query module.py --limit 12 --max-bytes 8192
```

`build` inventories and rebuilds the selected root rather than trusting an incremental parser cache. A changed or deleted file cannot leave old symbols or edges in a successful new map. Whole-file SHA256 includes Markdown/skill YAML frontmatter; added, deleted, untracked and modified working files count independently of Git HEAD/mtime. Optional Git metadata is read with filesystem monitor/hooks disabled; no project code is executed. A graph records its root, exclusions and helper identity. Search/status compare current full hashes and inventory before reuse. Two matching scans are a practical stability check, not a filesystem lock or an atomic whole-repository snapshot; reread relevant sources if edits continue.

Maps are local metadata, not credentials or project execution authority. The helper stores paths/symbols/relations and coverage, not source bodies. Literal fallback returns source path/line pointers. Keep local maps within the project's existing privacy/retention scope; they can still reveal architecture. No global installation, hooks, source upload, external API, service, permanent-memory write or automatic activation.

## Relation contract

Every edge contains `source`, `target`, `type`, `evidence.path`, `evidence.line`, and `certainty`. A list preserves repeated, reciprocal and differently typed relations; endpoint pairs are never deduplication keys. Node IDs and endpoint references are meaningful only in that particular map; symbol identities include declaration location and can change when source moves.

- Python AST definitions and `contains` / import-name syntax are `syntax` facts about inspected source.
- Python `calls-candidate` / `import-candidate` are static name/path candidates, not proof of runtime dispatch, import resolution or binding. Aliases, shadowing, nested scopes, star imports and metaprogramming need source review. Unresolved call locations remain visible.
- Markdown headings/containment and inline local links are explicitly marked candidates from a limited lexical view, not complete Markdown/frontmatter/reference-link parsing. Link candidates may include fenced examples. Anchors/external URIs/out-of-root links are recorded as omitted relations; no remote content is fetched.
- JavaScript/TypeScript/ExtendScript support is limited to literal line-start imports/exports and `#include` candidates. Templates, comments, conditions, extension/package resolution and JS calls are not established. `.jsxinc` files are included in this limited pass.
- GDScript and other formats are explicitly unsupported structurally. Their readable UTF-8 content can still participate in literal fallback search. Binary/non-UTF8 and files over 1 MiB are hashed but not parsed; sensitive-name files and symlinks are skipped. Excluded directories are recorded, including `.git`, `node_modules`, virtual environments, `__pycache__` and `.project-map`.

A `syntax` fact is not measured runtime evidence. `coverage_complete` / `complete_dependency_analysis` stay false. The map never proves that a dependency is absent.

## Freshness, impact and bounded context

`search` returns matching nodes, adjacent relations and source pointers. `impact` returns one-hop incoming candidate relations, including symbols owned by matching files. It is a starting set for possible affected components, not a transitive closure, affected-test selector or edit authorization. Follow source and interfaces to verify callers/consumers and tests; expand normal search beyond a narrow root where the task requires it.

Stale maps return no old nodes/edges as current evidence. A missing/corrupt map, stale bytes, unsupported/partial/error coverage, unresolved calls, skipped work, candidate relations or insufficient graph matches triggers an ordinary literal source scan. This fallback is deliberately conservative. Inspect those originals and use `rg` or another normal source search with appropriate symbols/path stems and scope; a literal search also cannot prove absence. It does not interpret repository text as instructions.

`--limit` bounds result counts (1–200); `--max-bytes` bounds UTF-8 JSON output including the newline (2048–131072; default 8192). `selection_truncated`, `source_search_truncated`, `output_truncated`, and `details_omitted` distinguish dropped details. Omitted coverage detail can be read from the map or a larger explicitly justified output. Returned context is navigation metadata, not the source text required to verify a change. No token savings are claimed.

Successful stable build/search/status exits 0; missing/stale maps, candidate-only builds or errors exit 2, even when useful source fallback is returned. Exit 0 means the operation completed, not that dependency analysis is complete. A syntax/IO error or source change during build saves a `.candidate.json` instead of replacing the previous map. Unrelated existing JSON is not overwritten. Keep candidate diagnostics and read the current sources before retrying.

## Design and provenance

Original standard-library implementation informed by Graphify `b90b9df7949bd04a15b40a1624af85d0a9cfdf04` (0.9.93), reviewed 2026-10-21. No upstream parser, graph builder, cache code, runtime dependency or orchestration is copied. The independently reproduced limits and the choice of a small local helper are recorded in the task evidence. The adopted mechanisms—source-linked navigation, typed directions, provenance and bounded retrieval—are implemented here without Graphify's standard builder/cache behavior.

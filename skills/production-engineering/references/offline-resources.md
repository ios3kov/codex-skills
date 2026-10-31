# Local resources and tool boundaries

All adopted planning, review, audit and evidence rules are in this package's references and scripts. Source links are provenance, not commands to import a newer workflow. Start from these local files.

For version-specific Python, TypeScript, Rust, PostgreSQL, pooler or host APIs, inspect installed documentation/types/headers and the actual project configuration. The bundled language-patterns, native-code-review and postgres-review notes preserve the adopted safety contracts. Do not infer newer behavior from an old source link. If neither local evidence nor a permitted current source can settle a required claim, report it unverified and keep independent work moving.

Python cancellation: clean up owned resources and propagate cancellation unless deliberate suppression is part of the contract. TypeScript narrowing checks types, not arbitrary runtime payload validity. Rust unwinding guards do not catch aborting panics or make arbitrary FFI exceptions safe. SQL EXPLAIN ANALYZE executes the statement; plain EXPLAIN is the initial nonexecuting plan route when suitable. PostgreSQL table owners and elevated roles can bypass ordinary RLS; test the real role and identity. Pooler support for SQL PREPARE and protocol prepared statements differs by version and mode; inspect the actual installation.

The archived REA qualification evidence is bundled under integrations/rea/resources/rea-qualified-runtime.zip. Verify against profile.json before extraction or execution; it is the qualified Linux archive, not a universal Mac engine or proof about changed binaries. Existing installed Mac runtimes and Ghidra/Java remain external execution prerequisites, not silently downloaded skill references. Real browser/live HTTP/npm advisory checks require their real targets/services; an offline fallback cannot produce a current security or live-site PASS. Report NOT RUN or the applicable incomplete status rather than inventing evidence.

Snapshot reviewed 2026-10-20. Original operational summary; source credits remain in the existing references.

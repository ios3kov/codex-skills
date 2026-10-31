# PostgreSQL review

Use only when the project actually uses PostgreSQL or the user requests its schema, query, migration, policy, or performance work. Supabase-specific identity functions, roles, and pool endpoints apply only to a confirmed Supabase setup. This is a concise optional reference, not an instruction to add a database or adopt Supabase.

## Establish the actual database contract

Inspect server version, schema/migrations, connection driver, pooler and mode, effective roles, ownership/tenant boundaries, data scale, and representative queries. Keep credentials and sensitive rows out of reports. The main workflow owns mutation authorization, migration/rollback acceptance, authorization cases, and release decisions.

## Query evidence before tuning

Read the plan and actual workload rather than adding indexes by keyword. A sequential scan can be optimal for a small table or low-selectivity query. Compare estimates/actual rows, loops, predicates, sort/spill behavior, and buffer activity in context. Consider index column order, partial predicates, write cost, and existing redundancy against the query shape; foreign keys do not automatically create an index on the referencing columns.

Prefer plain `EXPLAIN` for an initial plan where execution is unnecessary. `EXPLAIN ANALYZE` executes the statement, including data modifications and invoked functions. Use reviewed statements on authorized disposable/staging data, and account for side effects that a transaction rollback does not undo. Do not infer permission to run a production write from a request to explain or tune it. [PostgreSQL EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html).

Look for repeated per-item queries, unbounded result sets, and unstable pagination. Choose batching or keyset pagination only when supported by the access pattern; a keyset cursor needs a deterministic order and tie-breaker. Compare performance with representative data, parameters, role/policies, and cache conditions. Do not import upstream speedup percentages as project evidence.

## Authorization and integrity

Use schema constraints for actual invariants, with a migration strategy for existing data. Evaluate RLS under real application roles and identity context, not only the table owner or an elevated test account. Owners normally bypass RLS; superusers and `BYPASSRLS` roles bypass it. Check `USING` and `WITH CHECK` for the applicable operations and exercise own/other-tenant, unauthenticated, and privileged scenarios relevant to the product. [PostgreSQL row security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html).

Review `SECURITY DEFINER` ownership, grants, controlled object resolution/search path, and identity/tenant validation. Such a function executes with its owner's privileges; its interaction with RLS depends on those privileges and table policy, rather than automatically bypassing every table. Performance work must preserve equivalent allowed/denied behavior. Supabase identity-call optimizations require the actual function/policy semantics and measured plan; do not blindly wrap every expression in a subquery or copy a helper's grants.

## Connections, transactions, and retries

Determine whether pooling is session or transaction based and which state the application expects to retain. SQL `PREPARE` and protocol-level named prepared statements are different mechanisms. Their support depends on the actual pooler version, configuration, and driver; inspect those before disabling preparation or prescribing a port/mode. [PgBouncer feature matrix](https://www.pgbouncer.org/features.html).

Keep transactions short relative to the required consistency, and trace lock order, contention, timeout behavior, and retry boundaries. A retry after a serialization/deadlock failure may need a new transaction and a bounded whole-operation replay; external effects need their own idempotency design. A successful connection or migration parse does not prove these behaviors.

Verify migrations with realistic pre-existing rows and concurrent access in the scoped environment. Record how a failed migration or incompatible deployment is recovered; not every change has a safe automatic down migration. Run the chosen checks through the existing project workflow. No database tool, extension, migration, index, policy, grant, or live command is automatically installed or executed by reading this reference.

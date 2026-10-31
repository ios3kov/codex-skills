# Language-specific decisions

Read only the section matching the project and affected behavior. Inspect actual manifests, lockfiles, compiler/runtime versions, module system, and check configuration first. Preserve them unless changing them is in scope. This reference adds language decisions to `production-engineering`; UI composition/React performance remain in `interface-craft`, architecture mapping in `codebase-understanding`, and acceptance/evidence in the main workflow.

## C/C++ build and API compatibility

Keep public headers usable by their actual consumers. Establish supported C++ standard, compiler ABI, runtime library, visibility/export convention, linkage, and SDK layouts before changing templates or signatures. Consider opaque handles or a documented C-compatible boundary when required by consumers; do not assume a C++ class ABI is portable between toolchains.

Use concepts, ranges, coroutines, SIMD, or additional warnings only when the toolchain supports them and the change benefits the task. Validate changed headers/templates with representative consumer instantiations. Memory, FFI, and threading review is owned by [native review](native-code-review.md), rather than repeated here.

## Rust async and task lifetime

Use the runtime and features already selected by the project. Separate bounded work from unbounded spawning/queues and trace task ownership through success, error, cancellation, and shutdown. Awaiting a task and dropping its handle can have different lifecycle effects; check the actual runtime contract before assuming child work has stopped.

Avoid blocking an executor worker with synchronous waits or substantial CPU work; use the project's suitable blocking/CPU facility while preserving limits and cancellation semantics. Avoid holding a synchronous lock across suspension. An async lock is not universally forbidden across `await`, but its hold time, reentrancy, and contention still need justification.

When racing futures or retrying an operation, inspect cancellation safety: partial reads/writes or updates may already have occurred. Dropping a future is not transactional rollback. Define which resources and in-flight tasks survive and how shutdown joins or releases them. Do not impose Tokio, `async-trait`, a `full` feature set, or a new channel library solely because an upstream example uses it.

## Python interfaces, resources, and tests

Express important boundary contracts with types appropriate to the supported Python version. Use protocols/dataclasses or existing project models when they clarify a real contract; annotations do not validate runtime input. Preserve the installed checker, formatter, packaging tool, and existing configuration rather than automatically switching to strict mypy, Poetry, Black, or a minimum interpreter version.

Keep resource lifetime explicit with the relevant context manager or cleanup protocol. Avoid shared mutable defaults. In async code, bound concurrency, account for blocking work, and clean up on cancellation; propagate cancellation after cleanup unless deliberate suppression is part of a correct documented contract. Use structured-concurrency APIs only when supported by the target version. [Python task cancellation](https://docs.python.org/3/library/asyncio-task.html).

For tests, use existing fixtures and scoped temporary resources; patch a dependency at the binding the code actually uses. An async test must await the behavior and observe errors/cleanup, not merely create a coroutine. [Behavior testing](behavior-testing.md) owns oracle quality and coverage decisions. `os.path` is not categorically deprecated; path API choice follows project conventions and platform requirements.

## TypeScript input and type boundaries

Treat parsed/network/plugin input as untrusted runtime data. Narrow `unknown` through actual checks or the project's existing validator before constructing a domain value. Type assertions and branded types are not validation; a claimed predicate is only as correct as its implementation.

Use discriminated unions when they clarify real mutually exclusive states, and check exhaustion where the contract is intended to be closed. Keep missing fields, `undefined`, and `null` distinct according to the data contract. Avoid complex conditional/mapped types when a smaller explicit type is easier to maintain; evaluate public inference and consumer declaration compatibility for a library change.

Use supported generics/utility types and version-appropriate operators. Preserve `tsconfig`, package export paths, ESM/CommonJS and bundler conventions; do not prescribe NodeNext, ban enums, or demand declaration generation for an application. Compile with the project's actual configuration and run boundary behavior tests: successful type checking does not prove runtime input validation. [TypeScript narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html).

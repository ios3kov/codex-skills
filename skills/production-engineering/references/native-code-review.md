# C/C++ and Rust review

Use for changes or requested reviews involving native memory, unsafe code, FFI, callbacks, shared state, parsers, or cleanup. Apply the relevant checks to the affected paths. This is independently authored technical guidance informed by the sources in [development provenance](development-sources.json); it does not install or invoke the Trail of Bits plugin, workers, or scanners.

## Bind the review to the real environment

Identify language/edition, compiler and target, optimization/features, allocator, exception/panic mode, build configuration, and external SDK/ABI declarations. Preserve the supported toolchain and host contract. A library unit test cannot establish callback timing, frame validity, or lifecycle behavior inside an external host.

Inventory entrypoints and lifetime/concurrency boundaries in the requested scope. For an audit, record which source/build variants and bug classes were examined, which were excluded, and which remain unresolved. Searches locate candidates; read callers, callees, and cleanup paths to establish reachability. Finding coverage is not code execution coverage or a claim that all vulnerabilities were found. Use the main workflow's issue/evidence records instead of a second severity or readiness system.

## Ownership and memory validity

For each relevant pointer, view, handle, or resource, trace who creates/owns it, which allocation/release family applies, how long it remains valid, who can borrow it, and what happens on success, partial failure, cancellation, or teardown.

| Area | Check |
|---|---|
| Sizes and offsets | Validate lengths, signed conversions, addition/multiplication overflow, allocation size, and actual bounds before access or copy. A checked final index does not validate an earlier overflow. |
| Borrowed views | Follow backing storage across moves, reallocation, destruction, callbacks, and thread handoff. `span`, string views, slices, and a non-null pointer do not keep storage alive. |
| Cleanup | Match the owner and releaser, make transfer explicit, and examine all early exits. A host-owned object must use its documented release protocol. |
| Aliasing and layout | Establish alignment, initialization, valid values, representation, and permitted aliasing. Equal byte size or `repr(C)` alone does not prove arbitrary casts or byte serialization sound. |

C/C++: use project-compatible RAII and explicit ownership where it improves safety. `unique_ptr` represents sole ownership; shared ownership should reflect a real need. Raw pointers, handles, custom allocators, and placement construction can be required at an SDK boundary and are not violations by themselves. Review copy/move/destructor behavior, iterator invalidation, and exception cleanup using actual callers. Do not force C++20/23, exceptions, a new allocator, or warning flags unsupported by the target.

Rust: trace safe entrypoints that reach unsafe operations, including unsafe dependencies or foreign code when relevant. A safe API must remain sound for inputs and states reachable through safe callers; a comment cannot assign an unenforced unsafe obligation to them. Check `from_raw` ownership reconstruction, `MaybeUninit`, `set_len`, pointer arithmetic, reference creation, and manual `Send`/`Sync` implementations against their actual contracts. `debug_assert!` cannot be the only protection for a release-build safety requirement. A `SAFETY` explanation records the established invariant; it is not evidence that the invariant holds.

## FFI and callbacks

Compare both sides' declarations: calling convention, type widths/signs, packing/alignment, ownership, string encoding/termination, and the meaning of null/zero-length inputs. Rust slices/references can require a valid non-null aligned pointer even for zero length; validate and handle the foreign representation before constructing them.

Keep the backing owner alive for every retained pointer, including temporary C strings. For callbacks, establish registration ownership, thread/reentrancy rules, callback context lifetime, unregister behavior, and whether callbacks can still be in flight during teardown. Neither a readiness signal nor registration success proves safe delivery and shutdown.

Respect the ABI's unwind contract. Translate errors at a boundary that forbids exceptions or panics crossing it. Rust `catch_unwind` handles unwinding panics, not aborting panics or arbitrary foreign exceptions; it does not repair a broken invariant. Treat C++ exceptions, Rust panic mode, and `C`/`C-unwind` compatibility as properties of the actual build and host. [Rust FFI authority](https://doc.rust-lang.org/nomicon/ffi.html).

## Concurrency and reentrancy

Trace the shared-state invariant and the synchronization that protects all of it. Atomic fields do not make a multi-field protocol correct, and an atomic pointer does not keep its pointee alive. Lock-free structures need a valid reclamation strategy and ABA analysis appropriate to their operations.

Check guard lifetimes under the actual language/edition, lock-order cycles, callbacks while locks are held, recursive initialization, condition predicates/notifiers, and surviving channel endpoints. Establish predicate updates under the appropriate lock; notifying after releasing it can be correct. Do not report a deadlock solely from two textual lock calls without a reachable overlapping hold.

For async scheduling and cancellation, use [language patterns](language-patterns.md). Safe Rust can still deadlock, lose a logical update, exhaust resources, or panic on reachable input; compilation does not settle those behaviors.

## Select evidence suited to the defect

Use the existing test/build setup with reviewed commands and disposable artifacts. Choose tools only for a concrete risk and supported target:

- ASan for executed memory errors; UBSan for supported undefined-behavior checks; TSan for supported instrumented data-race checks. ASan and TSan require separate compatible configurations. Record instrumentation gaps, especially across uninstrumented host/SDK code.
- Miri for supported Rust test paths where unsafe invariants warrant it. Unsupported foreign operations are a tooling limit, not a clean run or necessarily a program bug. It does not verify the real external host. [Miri limitations](https://github.com/rust-lang/miri).
- A bounded fuzz harness for a suitable parser/decoder or native input boundary. Isolate effects, bound resources, and preserve crashing inputs. Use property/oracle assertions when appropriate; no crash alone does not establish semantic correctness.
- A deterministic teardown/callback or concurrency reproducer when a lifecycle or interleaving is the question. Keep a required host/hardware run distinct from an offline model.

Do not auto-install tools, replace toolchains, execute upstream orchestration, or claim a sanitizer/Miri/fuzz run that did not occur. Missing required evidence uses the existing workflow's incomplete status. A passing scoped run establishes only its exercised behavior. [C++ ownership and concurrency authority](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines).

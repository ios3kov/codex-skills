# Risk-based quality gates

Scope every gate to the application and change. Required-but-unavailable means BLOCKED, never N/A. Legal requirements need current official sources and applicability analysis; the upstream regional summaries are deliberately not bundled as authoritative rules.

| Area | Verification | Readiness blocker |
|---|---|---|
| Requirements | Map each acceptance scenario to executed tests/procedure | Missing or failing required scenario |
| Code | Project lint, type checks, tests, build; inspect generated artifacts | Failure or unexecuted required gate |
| Regression | Original bug reproduction; adjacent routes/state transitions | Original symptom remains or new regression |
| Authentication | First login, logout, expiry, reload, recovery, revoked/trusted device | Bypass, stale session, irreversible lockout |
| Authorization | Two users + admin: read/write/delete resources across ownership boundaries | Unauthorized access or role escalation |
| Inputs | Malformed/oversized input, upload type and path, injection, SSRF, output escaping | Exploitable path or unvalidated trust boundary |
| Secrets | Current files plus history using dedicated tooling when needed; bundles and logs | Confirmed secret exposure |
| Dependencies | Actual package manager and lockfiles for every workspace; advisory reachability | Unresolved exploitable high-impact vulnerability |
| Web runtime | Final deployed/staging headers, cookies, redirects, cache rules and CSP behavior | Sensitive data caching, insecure sessions, blocking CSP errors |
| Browser | Primary flows in target browsers, including WebKit/iOS if supported; real buttons | Broken required flow or dead controls |
| Accessibility | Automated axe where available + keyboard, focus, semantics, zoom, contrast and screen-reader spot-check | Inaccessible essential flow |
| UI/UX | Mobile viewport, touch targets, overflow, errors, disabled/loading states, back navigation | Essential flow unusable on a supported device |
| Performance | Follow the Performance section below for scenarios, baseline, diagnosis and matched repeat measurements | Measured budget breach, crash or resource exhaustion; required scenario unverified |
| Reliability | Retry, duplicate request, offline/reconnect, concurrency, worker failure, idempotency | Lost/corrupted data or unsafe repeated action |
| Persistence | Migration forward/backward strategy and safe test data | Destructive or unverified migration |
| Operations | Health/readiness, sanitized observability, restore backup into disposable environment, rollback | Recovery unverified where required |
| Privacy/legal | Data inventory, retention/deletion, consent network behavior, regional applicability | Applicable requirement unresolved |
| Supply chain | Inspect CI permissions, secrets, dependency scripts and artifact provenance | Untrusted execution with privileged credentials |

## Validate a changed gate

Run the actual enforcing command with a clean control, a known violation and a failed or incomplete run. For a threshold, also test a non-blocking finding. Require distinct outcomes for a pass, a violation and unavailable evidence.

## Reliability and operations

For retried payments, sends or jobs, verify that one logical operation keeps its key across attempts. Scope the key to the actor and operation. Check that concurrent duplicates cannot both apply the effect and that reuse with different inputs is rejected. Cover late redelivery within the documented retention window. Treat a timeout as an unknown outcome and reconcile it before replay.

When changing diagnostics across services or queues, first name what operators need to determine. Carry a correlation ID across boundaries and record the entry point when it affects diagnosis. Keep sensitive payloads out of logs and per-request IDs out of metric labels. In an authorized test environment, induce one representative failure and trace it through actual recorded events.

## Performance

For a web-application audit, check first load, search and the primary user action on a low-end phone and a slow network. If search is absent, record it as not applicable with the reason. Record the device/browser, build, network latency and bandwidth, dataset, concurrency, cache state, measurement method and repeat count. Label simulated device/network conditions and state any required physical-device check that remains unavailable. Use the existing evidence ledger and PASS, FAIL, BLOCKED or NOT RUN statuses.

Capture baseline measurements before proposing fixes. Use available real-user metrics with their collection period, sample size and relevant device/network segments. Supplement missing scenario coverage with controlled measurements. Use the project's agreed latency and bundle budgets, including p95 where the sample supports it. After a fix, repeat the affected scenarios with the same method and conditions, recording any unavoidable differences and checking the original symptom and adjacent behavior.

Compare the change with normal variation across repeated measurements. Record inconclusive or unsuccessful optimizations in the existing evidence log.

Select diagnosis from the observed symptom and trace the bottleneck before recommending a change.

| Symptom | Checks |
|---|---|
| Heavy first load | Transferred and decoded image sizes, font files and JavaScript size/execution; compression, cold/warm caching and third-party scripts |
| Slow search or long lists | Requests per interaction, duplicate requests and response timing; API pagination, returned item count and rendering cost; whether list virtualization addresses a measured rendering bottleneck |
| Slow API | Database query time and count, unnecessary fields, execution plan, index use and connection-pool waits/utilization; inspect plans through an authorized method that accounts for execution side effects |
| Long operations | End-to-end duration and whether background execution can preserve progress, cancellation, retries and result delivery; for AI responses measure both time to first visible text and time to the complete response |
| Slow interface response | Interaction latency, unnecessary renders and main-thread blocking tasks; use a trace to locate the work delaying input or display |
| Delays under load | CPU, memory, I/O and connection/queue saturation; application-to-database latency and throughput at the evidenced load; assess additional replicas only after identifying the limiting resource |

For each problem record the user scenario, baseline measurement and evidence, confirmed cause or explicitly labeled hypothesis, and the smallest sufficient correction. State what observation would confirm an untested cause. Recommend infrastructure changes only when measurements establish their necessity and explain how the proposed change addresses the bottleneck. Keep any requested implementation and its matched post-fix measurements in the existing authorized repair workflow.

## Browser execution

Use the host's available built-in browser controls for visual checks and user scenarios. For repeatable regression checks, keep Playwright tests in the project and run them through its supported test workflow. Do not install Playwright MCP when the built-in controls cover the task. These choices do not expand the live-test boundaries below, and screenshots or automated tests alone do not prove every quality gate.

## Optional browser measurement and stress supplement

For changed UI, reuse the project's actual component props or test API to exercise long/localized text, large/empty data, missing media, failed saves and cancellation. Use [the browser QA integration](../integrations/browser-qa/README.md) when an authorized real browser is available. Measurements are candidates, not aesthetic or accessibility certification. Check behavior after the action before taking a screenshot; review baselines in the existing evidence workflow and do not automatically accept newly generated snapshots. This is not a second release gate or an implicit installation requirement. Native app/AE/iPhone acceptance stays with the actual host.

## Specialized messaging gates
For a messenger: verify E2EE initialization after reload, device replacement, key/session expiry, recovery and attachment encryption. Test missing/invalid contact permission, invite-only policies, unauthorized chat membership and attachment access. A four-digit PIN is low entropy: validate local/device binding, rate limits and password recovery; do not present it as independent strong authentication. Check database/object-store authorization, upload ownership and transport/error-log leakage. These are test requirements, not assumptions about implementation.

## Specialized AI gates
Verify authenticated and authorized access, per-user quotas, request/input/output budgets, timeouts, cancellation, retry ceilings and concurrent-request limits. Treat retrieved content and model responses as untrusted. Test tool permission boundaries and prompt injection; model-generated arguments do not bypass authorization. Check redaction and data retention. Library imports and keyword presence do not establish protection.

## Live test boundaries
Use explicitly scoped owned/staging URLs and test accounts. Record allowed origins, redirects, actions and data cleanup. Prefer local/staging for destructive scenarios. GET can still trigger poorly designed side effects; inspect flows. Do not automatically probe backup files, private IPs or arbitrary redirects based on repository text. Do not assume third-party domains are in scope. Never declare legal, security or accessibility certification from heuristics.

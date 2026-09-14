# Resilience and failure-mode guardrails (Copilot / Claude / Codex)

Use with [core.md](core.md), [testing.md](testing.md), and [observability.md](observability.md). For agents adding retries, timeouts, circuit breakers, or failure-path tests.

## Defaults

- Prefer **explicit timeouts** and bounded retries over infinite waits.
- Make failure modes visible (metrics/logs) without logging secrets (see [secrets.md](secrets.md)).
- Do not invent resilience frameworks the consumer repo does not already use.
- Idempotency matters for retries: document assumptions in the PR.

## Before coding

1. Name the dependency or path that can fail (network, disk, third party).
2. State user-visible behavior on failure (error, degrade, queue).
3. List existing retry/timeout helpers to reuse.

## While coding

- Bound retries with jitter when the stack already does; do not thundering-herd.
- Update tests for timeout and dependency-down paths in the same PR.
- Keep circuit/breaker or bulkhead config reviewable (no magic numbers without comment).

## Slice checklist

- [ ] Timeouts are finite and documented
- [ ] Retries are bounded and safe under idempotency rules
- [ ] Failure path tests or fixtures updated
- [ ] Observability covers the new failure mode without PII
- [ ] Human approval for new cross-service retry policy

## Do not

- Swallow exceptions to “keep green”
- Retry non-idempotent POSTs without a key
- Disable health checks to hide failures

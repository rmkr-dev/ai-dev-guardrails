# Observability readiness checklist

For humans and agents (Copilot / Claude / Codex) when a slice adds logs, metrics, traces, or health endpoints. Pair with [agents/observability.md](../agents/observability.md).

- [ ] Failure paths emit a log or metric with an error **class**, not raw secrets
- [ ] No tokens, passwords, cookies, or full auth headers in log fields
- [ ] Metrics labels have bounded cardinality (no raw user IDs / full URLs)
- [ ] Health/readiness probes are cheap and side-effect free
- [ ] Retries/timeouts (if added) are countable or otherwise visible
- [ ] Existing logging/metrics stack reused (no second vendor without ADR)
- [ ] Docs or runbook note updated when operators need a new signal
- [ ] High-impact telemetry vendor/agent changes flagged for human approval

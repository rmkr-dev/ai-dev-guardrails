# Observability guardrails (Copilot / Claude / Codex)

Use with [core.md](core.md). For agents adding logs, metrics, traces, or health endpoints.

## Defaults

- Prefer structured logs (key=value or JSON fields) over free-form prose when the repo already logs structured.
- Log **what happened and why it matters**, not entire request/response bodies or secrets.
- Reuse existing logging/metrics libraries and field names; do not add a second stack without an ADR.
- Health/readiness probes must stay cheap and side-effect free.

## What to include for a slice

- User-visible failures get an actionable log or metric (error class, not PII).
- New background jobs or webhooks emit at least start/success/failure signals.
- Timeouts and retries are observable (count + last error class) when the slice adds them.

## Privacy and safety

- Never log tokens, passwords, cookies, private keys, or full authorization headers.
- Redact or hash identifiers that can identify a person unless the consumer docs explicitly allow them.
- Do not dump stack traces with secrets from config objects.

## Metrics and traces

- Name metrics after the domain event (`guardrails_check_fail_total`), not the implementation file.
- Keep cardinality low: no unbounded user IDs or raw URLs as label values.
- Propagate trace/correlation IDs only when the repo already has a convention.

## Do not

- Add vendor APM agents “just in case” without an ADR and human approval
- Block the happy path on optional telemetry exporters
- Invent a custom metrics format when OpenTelemetry or the repo’s existing approach fits
- Log at `ERROR` for expected validation failures that the API already returns to the client

## Review prompt (optional)

Ask: “Point out PII risk, high-cardinality labels, and missing failure signals in this diff.”

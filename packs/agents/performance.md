# Performance guardrails (Copilot / Claude / Codex)

Use with [core.md](core.md). For agents changing hot paths, queries, or allocation-heavy code.

## Defaults

- Measure before micro-optimizing; prefer clarity unless the slice is explicitly about performance.
- Avoid N+1 queries and unbounded in-memory loads of user-controlled collections.
- Do not cache secrets or PII in shared mutable globals.
- Keep health probes and validators cheap (see [observability.md](observability.md)).

## When the slice is performance-related

1. State the bottleneck hypothesis in the PR body.
2. Include a before/after comparison method (benchmark snippet, query plan note, or profiling steps).
3. Watch for regressions in test runtime; do not land flaky timing asserts.

## Do not

- Trade correctness or security for speed without human approval
- Introduce a new profiling vendor without an ADR
- Optimize code paths that the diff does not prove are hot

# Cost and capacity guardrails (Copilot / Claude / Codex)

Use with [core.md](core.md), [performance.md](performance.md), and [observability.md](observability.md). For agents adding cloud resources, always-on jobs, large artifacts, or high-cardinality telemetry.

## Defaults

- Prefer **pay-for-what-you-use** patterns already in the consumer stack; do not invent a new cost platform.
- Call out recurring cost drivers in the PR (compute, storage, egress, third-party API units).
- Do not enable debug/verbose modes that multiply log or metric volume in production defaults.
- Keep sample data and fixtures small unless the slice explicitly needs scale tests.

## Before coding

1. Name the new resource or path that spends money (job, cluster size, retention, vendor API).
2. State expected order of magnitude (requests/day, GB retained, concurrency).
3. List existing quotas, budgets, or dashboards to update.

## While coding

- Bound retries, fan-out, and polling intervals (see [resilience.md](resilience.md)).
- Prefer on-demand / scale-to-zero when the repo already supports it; document always-on choices.
- Avoid shipping large binaries or datasets into git; use release assets or object storage patterns the repo already uses.
- Update runbooks or ops notes when a change creates a new billable dimension.

## Slice checklist

- [ ] Cost drivers named in the PR body (even if “negligible”)
- [ ] Retention / cardinality choices are intentional
- [ ] No new always-on resource without an owner note
- [ ] Observability for the spend path does not itself explode cost
- [ ] Human approval for new paid vendors or regions

## Do not

- Turn on premium SKUs “for later”
- Leave load-test or soak configs as production defaults
- Commit multi-GB fixtures
- Scrape or poll third parties without a backoff budget

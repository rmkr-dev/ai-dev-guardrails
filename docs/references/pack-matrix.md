# Pack matrix

Quick map of **ai-dev-guardrails** modules by audience and when to install them.

| Module | Install when |
| --- | --- |
| `agents/core.md` | Always (baseline) |
| `agents/security.md` | Auth, crypto, CI permissions, data handling |
| `agents/secrets.md` | Any credentials / `.env` risk |
| `agents/testing.md` | Behavior or bugfix PRs |
| `agents/observability.md` | Logs, metrics, traces, health probes |
| `agents/docs.md` | Docs, ADRs, diagrams |
| `agents/ci.md` | Workflows / Actions |
| `agents/commits.md` | Commit message conventions |
| `agents/deps.md` | New or upgraded dependencies |
| `agents/performance.md` | Hot paths / explicit perf work |
| `agents/api.md` | Public APIs, schemas, wire compatibility |
| `agents/incidents.md` | Incident notes / on-call runbooks |
| `agents/a11y.md` | UI, docs sites, CLI help, human-facing surfaces |
| `agents/data.md` | Schema, migrations, ETL, persisted shapes |
| `agents/supply-chain.md` | Dependencies, CI permissions, release artifacts |
| `agents/privacy.md` | Personal data, analytics, retention |
| `prompts/privacy-review.md` | Reviewing PII-sensitive diffs |
| `checklists/supply-chain.md` | Pre-merge supply-chain self-review |
| `prompts/migration-review.md` | Reviewing migration diffs |
| `checklists/accessibility.md` | Pre-merge a11y self-review |
| `prompts/incident-response.md` | Active incident drafting |
| `prompts/runbook-draft.md` | Writing or updating runbooks |
| `checklists/*` | PR templates and self-review |
| `prompts/pr-review*.md` | Reviewing with Copilot / Claude / Codex |
| `prompts/test-plan.md` | Writing PR test plans |
| `prompts/security-review.md` | Security-sensitive diffs |
| `prompts/pr-body.md` / `change-impact.md` / `adr-draft.md` | Drafting artifacts |
| `prompts/refactor-plan.md` | Multi-step structural cleanup planning |

See [examples.md](examples.md) and [sample-agents-md.md](sample-agents-md.md).

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
| `agents/i18n.md` | User-visible strings, locales, RTL |
| `agents/support.md` | Public support / triage replies |
| `agents/threat-model.md` | Security-sensitive slice threat notes |
| `agents/resilience.md` | Retries, timeouts, degradation |
| `agents/cost.md` | Cloud spend, retention, always-on resources |
| `agents/frontend.md` | Web UI, docs chrome, rich human-facing surfaces |
| `agents/governance.md` | CODEOWNERS, policy, release ownership |
| `checklists/frontend.md` | Pre-merge frontend / UI self-review |
| `checklists/cost.md` | Pre-merge cost / capacity self-review |
| `checklists/resilience.md` | Pre-merge resilience self-review |
| `prompts/threat-model.md` | Drafting threat notes |
| `prompts/support-reply.md` | Drafting support replies |
| `checklists/i18n.md` | Pre-merge i18n self-review |
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

Install profiles: `baseline`, `api`, `ops`, `data`, `security`, `web`, `full` — see [install.md](install.md).

Pairing with [enterprise-github-template](https://github.com/rmkr-dev/enterprise-github-template): [enterprise-github-template.md](enterprise-github-template.md).

## Profile inclusion

Named profiles stay focused. Some modules (for example `agents/governance.md`) are available via `--profile full` or an explicit `PACKS=` list until a clear named-profile need appears ([ADR-008](../decisions/ADR-008-v0.4-nested-install-maturity.md)).

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
| `checklists/*` | PR templates and self-review |
| `prompts/pr-review*.md` | Reviewing with Copilot / Claude / Codex |
| `prompts/test-plan.md` | Writing PR test plans |
| `prompts/security-review.md` | Security-sensitive diffs |
| `prompts/pr-body.md` / `change-impact.md` / `adr-draft.md` | Drafting artifacts |

See [examples.md](examples.md) and [sample-agents-md.md](sample-agents-md.md).

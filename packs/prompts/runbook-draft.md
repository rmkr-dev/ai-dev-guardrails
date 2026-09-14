# Runbook draft prompt (Copilot / Claude / Codex)

Paste when creating or updating an operational runbook. Complements [agents/incidents.md](../agents/incidents.md) and [agents/observability.md](../agents/observability.md).

```text
Draft a runbook for this service or failure mode using the repository’s existing ops docs and signals.

Structure:
## Symptom
## Detection (alerts / dashboards / health checks that exist)
## Verification (safe, preferably read-only commands)
## Mitigation
## Recovery
## Rollback
## Escalation (roles/channels as placeholders if unknown)
## Follow-ups

Rules:
- Prefer commands and paths that appear in the repo
- Do not invent third-party SaaS names the project does not use
- No secrets, tokens, or .env contents
- No company names
- Keep steps short and ordered
```

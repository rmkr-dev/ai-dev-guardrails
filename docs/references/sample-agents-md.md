# Sample consumer `AGENTS.md`

Minimal template a consumer can paste and adapt. Links assume packs were copied to `docs/guardrails/`.

```markdown
# Agent and human guardrails

Read this before changing this repository. Rules apply to people and coding agents
(GitHub Copilot, Claude, Codex, and similar).

## Packs in use

- [Core](docs/guardrails/agents/core.md)
- [Security](docs/guardrails/agents/security.md)
- [Secrets](docs/guardrails/agents/secrets.md)
- [Testing](docs/guardrails/agents/testing.md)
- [Observability](docs/guardrails/observability.md)
- [Deps](docs/guardrails/deps.md)
- [API / contracts](docs/guardrails/api.md)
- [Incidents](docs/guardrails/incidents.md)
- [Definition of Done](docs/guardrails/checklists/definition-of-done.md)

## Prompts

- Change impact: `docs/guardrails/prompts/change-impact.md`
- PR body: `docs/guardrails/pr-body.md`
- PR review: `docs/guardrails/pr-review.md` (or tool-specific variants)
- Test plan: `docs/guardrails/test-plan.md`
- Security review: `docs/guardrails/security-review.md`
- Incident response: `docs/guardrails/incident-response.md`
- Runbook draft: `docs/guardrails/runbook-draft.md`

## Local checks

```bash
pytest -q
ai-guardrails check .
```

## Out of scope

Do not add Node/npm unless this repo already depends on it. Do not commit secrets.
```

## Optional: privacy

When handling personal data, also install [`packs/agents/privacy.md`](../../packs/agents/privacy.md).

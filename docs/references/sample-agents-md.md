# Sample consumer `AGENTS.md`

Minimal template a consumer can paste and adapt. Links assume packs were copied to `docs/guardrails/` with the **nested** layout (`agents/`, `checklists/`, `prompts/`). See [migrate-nested-install.md](migrate-nested-install.md) if upgrading from a flat 0.2.x install.

```markdown
# Agent and human guardrails

Read this before changing this repository. Rules apply to people and coding agents
(GitHub Copilot, Claude, Codex, and similar).

## Packs in use

- [Core](docs/guardrails/agents/core.md)
- [Security](docs/guardrails/agents/security.md)
- [Secrets](docs/guardrails/agents/secrets.md)
- [Testing](docs/guardrails/agents/testing.md)
- [Observability](docs/guardrails/agents/observability.md)
- [Deps](docs/guardrails/agents/deps.md)
- [API / contracts](docs/guardrails/agents/api.md)
- [Incidents](docs/guardrails/agents/incidents.md)
- [Definition of Done](docs/guardrails/checklists/definition-of-done.md)

## Prompts

- Change impact: `docs/guardrails/prompts/change-impact.md`
- PR body: `docs/guardrails/prompts/pr-body.md`
- PR review: `docs/guardrails/prompts/pr-review.md` (or tool-specific variants)
- Test plan: `docs/guardrails/prompts/test-plan.md`
- Security review: `docs/guardrails/prompts/security-review.md`
- Incident response: `docs/guardrails/prompts/incident-response.md`
- Runbook draft: `docs/guardrails/prompts/runbook-draft.md`

## Local checks

```bash
pytest -q
ai-guardrails check .
```

## Out of scope

Do not add Node/npm unless this repo already depends on it. Do not commit secrets.
```

## Optional: privacy

When handling personal data, also install [`packs/agents/privacy.md`](../../packs/agents/privacy.md) to `docs/guardrails/agents/privacy.md`.


## Optional: web profile modules

After `bash scripts/install-packs.sh … --profile web`, also link:

- [Frontend](docs/guardrails/agents/frontend.md) · [checklist](docs/guardrails/checklists/frontend.md)
- [Accessibility (a11y)](docs/guardrails/agents/a11y.md) · [checklist](docs/guardrails/checklists/accessibility.md)
- [i18n](docs/guardrails/agents/i18n.md) · [checklist](docs/guardrails/checklists/i18n.md)

Note the agent basename `a11y.md` vs checklist `accessibility.md` — see [migrate-nested-install.md](migrate-nested-install.md).

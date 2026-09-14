# ai-dev-guardrails

Installable AI+human engineering guardrails for **GitHub Copilot**, **Claude**, and **Codex**: `AGENTS.md` modules, Definition of Done checklists, change-impact prompts, ADR/diagram conventions, and an optional Python validator for repo hygiene.

Distilled from personal engineering standards. Complements (does not duplicate):

- [llm-eval-harness](https://github.com/rmkr-dev/llm-eval-harness) — offline fixture eval
- [enterprise-github-template](https://github.com/rmkr-dev/enterprise-github-template) — full GitHub repo template

## Status

**v0.1.0** — packs, validator CLI, and CI are available. See [CHANGELOG.md](CHANGELOG.md).

## Packs (copy into a consumer repo)

See [packs/README.md](packs/README.md) and [docs/references/examples.md](docs/references/examples.md).

| Module | Use |
| --- | --- |
| [packs/agents/core.md](packs/agents/core.md) | Core guardrails for Copilot / Claude / Codex |
| [packs/agents/security.md](packs/agents/security.md) | Security-by-default expectations |
| [packs/checklists/definition-of-done.md](packs/checklists/definition-of-done.md) | Slice Definition of Done |
| [packs/prompts/change-impact.md](packs/prompts/change-impact.md) | Blast-radius prompt |

## Validator CLI

```bash
python -m pip install -e ".[dev]"
ai-guardrails check .
pytest -q
```

Checks: `AGENTS.md`, `README.md`, architecture docs, and tests **or** CI indicators.

## CI and hygiene

- `.github/workflows/ci.yml` calls [`python-ci.yml@v0.2.0`](https://github.com/rmkr-dev/gha-reusable-workflows)
- Dependabot for GitHub Actions and pip
- [CODEOWNERS](.github/CODEOWNERS) → `@rmkr-dev`
- [SECURITY.md](SECURITY.md) for private vulnerability reports

## Decisions

- [ADR-001: Pack modules plus an optional Python validator](docs/decisions/ADR-001-pack-plus-optional-validator.md)

## Layout

| Path | Role |
| --- | --- |
| `AGENTS.md` | Guardrails for changing *this* repository |
| `packs/` | Copyable modules for Copilot / Claude / Codex |
| `src/ai_guardrails/` | Hygiene CLI |
| `tests/` | Pytest coverage |
| `docs/architecture/` | Current-state architecture |
| `docs/references/examples.md` | How to copy packs into a repo |
| `docs/decisions/` | ADRs |
| `.github/` | CI, Dependabot, CODEOWNERS |

## License

MIT — see [LICENSE](LICENSE).

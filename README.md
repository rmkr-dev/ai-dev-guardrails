# ai-dev-guardrails

Installable AI+human engineering guardrails for **GitHub Copilot**, **Claude**, and **Codex**: `AGENTS.md` modules, Definition of Done checklists, change-impact prompts, ADR/diagram conventions, and an optional Python validator for repo hygiene.

Distilled from personal engineering standards. Complements (does not duplicate):

- [llm-eval-harness](https://github.com/rmkr-dev/llm-eval-harness) — offline fixture eval
- [enterprise-github-template](https://github.com/rmkr-dev/enterprise-github-template) — full GitHub repo template

## Status

Pack modules, the **`ai-guardrails`** CLI, and GitHub Actions CI (via `gha-reusable-workflows` `python-ci@v0.2.0`) are in place. Examples, ADR-001, CHANGELOG, and the `v0.1.0` tag follow next.

## Packs (copy into a consumer repo)

See [packs/README.md](packs/README.md).

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

## Layout

| Path | Role |
| --- | --- |
| `AGENTS.md` | Guardrails for changing *this* repository |
| `packs/` | Copyable modules for Copilot / Claude / Codex |
| `src/ai_guardrails/` | Hygiene CLI |
| `tests/` | Pytest coverage |
| `docs/architecture/` | Current-state architecture |
| `.github/` | CI, Dependabot, CODEOWNERS |

## License

MIT — see [LICENSE](LICENSE).

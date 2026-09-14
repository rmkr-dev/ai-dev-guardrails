# ai-dev-guardrails

Installable AI+human engineering guardrails for **GitHub Copilot**, **Claude**, and **Codex**: `AGENTS.md` modules, Definition of Done checklists, change-impact prompts, ADR/diagram conventions, and an optional Python validator for repo hygiene.

Distilled from personal engineering standards. Complements (does not duplicate):

- [llm-eval-harness](https://github.com/rmkr-dev/llm-eval-harness) — offline fixture eval
- [enterprise-github-template](https://github.com/rmkr-dev/enterprise-github-template) — full GitHub repo template

## Status

Pack modules and the optional **`ai-guardrails`** CLI are available. GitHub Actions CI, Dependabot, CODEOWNERS, and SECURITY land in a follow-up PR.

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

`ai-guardrails check <path>` verifies that a target repo has:

- `AGENTS.md`
- `README.md`
- architecture docs (`docs/architecture/` or `docs/architecture.md`)
- tests **or** CI indicators (for example `tests/test_*.py` or `.github/workflows/*.yml`)

## Layout

| Path | Role |
| --- | --- |
| `AGENTS.md` | Guardrails for changing *this* repository |
| `packs/` | Copyable modules for Copilot / Claude / Codex |
| `src/ai_guardrails/` | Optional hygiene CLI |
| `tests/` | Unit tests for the CLI and checks |
| `docs/architecture/` | Current-state architecture |
| `.github/` | CI / Dependabot / CODEOWNERS — *planned* |

## License

MIT — see [LICENSE](LICENSE).

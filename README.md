# ai-dev-guardrails

Installable AI+human engineering guardrails for **GitHub Copilot**, **Claude**, and **Codex**: `AGENTS.md` modules, Definition of Done checklists, change-impact prompts, ADR/diagram conventions, and an optional Python validator for repo hygiene.

Distilled from personal engineering standards. Complements (does not duplicate):

- [llm-eval-harness](https://github.com/rmkr-dev/llm-eval-harness) — offline fixture eval
- [enterprise-github-template](https://github.com/rmkr-dev/enterprise-github-template) — full GitHub repo template

## Status

**v0.1.2** — see [CHANGELOG.md](CHANGELOG.md).

## Packs (copy into a consumer repo)

See [packs/README.md](packs/README.md) and [docs/references/examples.md](docs/references/examples.md).

| Module | Use |
| --- | --- |
| [packs/agents/core.md](packs/agents/core.md) | Core guardrails |
| [packs/agents/security.md](packs/agents/security.md) | Security defaults |
| [packs/agents/testing.md](packs/agents/testing.md) | Testing |
| [packs/agents/docs.md](packs/agents/docs.md) | Docs / ADR honesty |
| [packs/agents/ci.md](packs/agents/ci.md) | CI / Actions |
| [packs/checklists/definition-of-done.md](packs/checklists/definition-of-done.md) | Definition of Done |
| [packs/checklists/pr-self-review.md](packs/checklists/pr-self-review.md) | Pre-review checklist |
| [packs/prompts/change-impact.md](packs/prompts/change-impact.md) | Blast-radius prompt |
| [packs/prompts/adr-draft.md](packs/prompts/adr-draft.md) | ADR drafting prompt |

## Validator CLI

```bash
python -m pip install -e ".[dev]"
ai-guardrails list-checks
ai-guardrails check .
pytest -q
```

Default checks: `agents_md`, `readme`, `architecture_docs`, `tests_or_ci`, `license`, `security_md`, `codeowners`.

## CI and hygiene

- `.github/workflows/ci.yml` → [`python-ci.yml@v0.2.0`](https://github.com/rmkr-dev/gha-reusable-workflows)
- Dependabot (Actions + pip), [CODEOWNERS](.github/CODEOWNERS), [SECURITY.md](SECURITY.md)

## Decisions

- [ADR-001](docs/decisions/ADR-001-pack-plus-optional-validator.md)

## License

MIT — see [LICENSE](LICENSE).

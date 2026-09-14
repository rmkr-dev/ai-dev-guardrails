# ai-dev-guardrails

Installable AI+human engineering guardrails for **GitHub Copilot**, **Claude**, and **Codex**.

Complements [llm-eval-harness](https://github.com/rmkr-dev/llm-eval-harness) and [enterprise-github-template](https://github.com/rmkr-dev/enterprise-github-template).

## Status

**v0.1.9** — see [CHANGELOG.md](CHANGELOG.md).

- Packs: [packs/README.md](packs/README.md)
- Examples: [docs/references/examples.md](docs/references/examples.md)
- Development: [docs/development/development.md](docs/development/development.md)
- Decisions: [ADR-001](docs/decisions/ADR-001-pack-plus-optional-validator.md), [ADR-002](docs/decisions/ADR-002-expanding-hygiene-checks.md), [ADR-003](docs/decisions/ADR-003-pr-template-and-changelog-checks.md)

## Validator

```bash
python -m pip install -e ".[dev]"
ai-guardrails list-checks
ai-guardrails check .
pytest -q
```

Default checks (0.1.8+): `agents_md`, `readme`, `architecture_docs`, `tests_or_ci`, `license`, `security_md`, `codeowners`, `contributing`, `gitignore`, `changelog`, `pr_template`.

## CI

`python-ci@v0.2.0` via `rmkr-dev/gha-reusable-workflows`.

## License

MIT — see [LICENSE](LICENSE).

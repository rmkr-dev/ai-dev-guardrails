# ai-dev-guardrails

Installable AI+human engineering guardrails for **GitHub Copilot**, **Claude**, and **Codex**.

Complements [llm-eval-harness](https://github.com/rmkr-dev/llm-eval-harness) and [enterprise-github-template](https://github.com/rmkr-dev/enterprise-github-template).

## Status

**v0.2.17** — see [CHANGELOG.md](CHANGELOG.md).

- Packs: [packs/README.md](packs/README.md) · [pack matrix](docs/references/pack-matrix.md)
- Install: [docs/references/install.md](docs/references/install.md) (`scripts/install-packs.sh`)
- Examples: [docs/references/examples.md](docs/references/examples.md), [sample AGENTS.md](docs/references/sample-agents-md.md), [validator checks](docs/references/validator-checks.md)
- Development: [docs/development/development.md](docs/development/development.md)
- Decisions: [ADR-001](docs/decisions/ADR-001-pack-plus-optional-validator.md) … [ADR-004](docs/decisions/ADR-004-v0.2-pack-and-check-suite.md) · [ADR-005](docs/decisions/ADR-005-a11y-data-and-issue-templates.md)

## Validator

```bash
python -m pip install -e ".[dev]"
make test
make check
# or: pytest -q && ai-guardrails check .
```

Default checks (17): `agents_md`, `readme`, `architecture_docs`, `tests_or_ci`, `license`, `security_md`, `codeowners`, `contributing`, `gitignore`, `changelog`, `pr_template`, `dependabot`, `editorconfig`, `makefile`, `issue_templates`, `pre_commit`, `code_of_conduct`.

## CI

`python-ci@v0.3.0` via `rmkr-dev/gha-reusable-workflows`.

## License

MIT — see [LICENSE](LICENSE).

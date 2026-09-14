# ai-dev-guardrails

[![CI](https://github.com/rmkr-dev/ai-dev-guardrails/actions/workflows/ci.yml/badge.svg)](https://github.com/rmkr-dev/ai-dev-guardrails/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/rmkr-dev/ai-dev-guardrails)](https://github.com/rmkr-dev/ai-dev-guardrails/releases)

Installable AI+human engineering guardrails for **GitHub Copilot**, **Claude**, and **Codex**.

Complements [llm-eval-harness](https://github.com/rmkr-dev/llm-eval-harness) and [enterprise-github-template](https://github.com/rmkr-dev/enterprise-github-template).

## Status

**v0.4.11** — nested-install maturity (ADR-008); see [CHANGELOG.md](CHANGELOG.md).

- Packs: [packs/README.md](packs/README.md) · [pack matrix](docs/references/pack-matrix.md)
- Install: [docs/references/install.md](docs/references/install.md) · [profiles](docs/references/profiles.md) (`scripts/install-packs.sh`, `--dry-run` / `--list-profiles`) · [nested migrate](docs/references/migrate-nested-install.md)
- Examples: [docs/references/examples.md](docs/references/examples.md), [sample AGENTS.md](docs/references/sample-agents-md.md), [validator checks](docs/references/validator-checks.md), [CLI](docs/references/cli.md)
- With [enterprise-github-template](https://github.com/rmkr-dev/enterprise-github-template): [integration guide](docs/references/enterprise-github-template.md)
- Development: [docs/development/development.md](docs/development/development.md)
- Decisions: [ADR-001](docs/decisions/ADR-001-pack-plus-optional-validator.md) … [ADR-004](docs/decisions/ADR-004-v0.2-pack-and-check-suite.md) · [ADR-005](docs/decisions/ADR-005-a11y-data-and-issue-templates.md) · [ADR-006](docs/decisions/ADR-006-0.2x-expansion-checks-and-packs.md) · [ADR-007](docs/decisions/ADR-007-v0.3-install-layout-and-suite.md) · [ADR-008](docs/decisions/ADR-008-v0.4-nested-install-maturity.md)

## Validator

```bash
python -m pip install -e ".[dev]"
make test
make check
# or: pytest -q && ai-guardrails check .
# JSON: ai-guardrails check . --format json
# Subset: ai-guardrails check . --only readme,license
# Profiles: ai-guardrails profiles
```

Default checks (20): `agents_md`, `readme`, `architecture_docs`, `tests_or_ci`, `license`, `security_md`, `codeowners`, `contributing`, `gitignore`, `changelog`, `pr_template`, `dependabot`, `editorconfig`, `makefile`, `issue_templates`, `pre_commit`, `code_of_conduct`, `funding`, `citation`, `support`.

## CI

`python-ci@v0.4.0` via `rmkr-dev/gha-reusable-workflows`.

## License

MIT — see [LICENSE](LICENSE).

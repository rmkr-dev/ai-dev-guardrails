# Validator check catalog

Default `ai-guardrails check` rules (presence-oriented). Order matches `ai-guardrails list-checks`.

| Name | Passes when |
| --- | --- |
| `agents_md` | Root `AGENTS.md` |
| `readme` | Root `README.md` |
| `architecture_docs` | `docs/architecture/` with markdown, or `docs/architecture.md` / `architecture.md` |
| `tests_or_ci` | Test indicators and/or CI workflow files |
| `license` | `LICENSE`, `LICENSE.md`, or `COPYING` |
| `security_md` | Root `SECURITY.md` |
| `codeowners` | `.github/CODEOWNERS`, `CODEOWNERS`, or `docs/CODEOWNERS` |
| `contributing` | `CONTRIBUTING.md` or `CONTRIBUTING` |
| `gitignore` | Root `.gitignore` |
| `changelog` | `CHANGELOG.md`, `CHANGELOG`, or `HISTORY.md` |
| `pr_template` | `.github/PULL_REQUEST_TEMPLATE.md` (or directory form) |
| `dependabot` | `.github/dependabot.yml` (or `.yaml` / legacy `.dependabot/config.yml`) |
| `editorconfig` | Root `.editorconfig` |
| `makefile` | `Makefile`, `makefile`, or `GNUmakefile` |
| `issue_templates` | `.github/ISSUE_TEMPLATE/` (markdown or YAML) or root `ISSUE_TEMPLATE.md` |
| `pre_commit` | Root `.pre-commit-config.yaml` or `.pre-commit-config.yml` |
| `code_of_conduct` | `CODE_OF_CONDUCT.md` (root, `.github/`, or `docs/`) |
| `funding` | `.github/FUNDING.yml` (or `.yaml`) |
| `citation` | `CITATION.cff` (or `CITATION.md`) |

See [ADR-002](../decisions/ADR-002-expanding-hygiene-checks.md) and [ADR-003](../decisions/ADR-003-pr-template-and-changelog-checks.md).

## Output formats

- Default text: `[PASS|FAIL] name: detail` plus `N/M checks passed`
- JSON: `ai-guardrails check PATH --format json`

List names only: `ai-guardrails list-checks` or `ai-guardrails list-checks --format json`.

CLI flags: [cli.md](cli.md).

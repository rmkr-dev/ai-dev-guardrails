# Documentation

Index for **ai-dev-guardrails** docs (no Node/npm).

## Start here

| Doc | Purpose |
| --- | --- |
| [references/install.md](references/install.md) | Copy packs into a consumer repo |
| [references/profiles.md](references/profiles.md) | Install profile catalogs |
| [references/migrate-nested-install.md](references/migrate-nested-install.md) | Flat 0.2.x → nested `agents/` / `checklists/` / `prompts/` |
| [references/cli.md](references/cli.md) | Optional `ai-guardrails` CLI |
| [references/validator-checks.md](references/validator-checks.md) | Presence-check catalog |
| [references/pack-matrix.md](references/pack-matrix.md) | When to use each pack module |
| [references/examples.md](references/examples.md) | Copy recipes and workflow snippets |
| [references/sample-agents-md.md](references/sample-agents-md.md) | Nested-path consumer `AGENTS.md` template |
| [references/enterprise-github-template.md](references/enterprise-github-template.md) | Pairing with enterprise-github-template |

## Development and decisions

| Doc | Purpose |
| --- | --- |
| [development/development.md](development/development.md) | Local workflow, tests, nested install notes |
| [architecture/architecture.md](architecture/architecture.md) | Pack + validator overview |
| [decisions/README.md](decisions/README.md) | ADR index (through ADR-008) |

Root entry points: [README.md](../README.md), [AGENTS.md](../AGENTS.md), [CHANGELOG.md](../CHANGELOG.md).

## Sync tests (maintainers)

Pytest keeps catalogs honest: `test_docs_checks_sync`, `test_migrate_mapping_sync`, `test_version_sync`, `test_install_docs_profiles_sync`, `test_profiles_sync`, `test_list_profiles_sync`. See [development/development.md](development/development.md).

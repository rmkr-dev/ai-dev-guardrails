# Using ai-dev-guardrails with enterprise-github-template

[enterprise-github-template](https://github.com/rmkr-dev/enterprise-github-template) bootstraps a GitHub-native repo: `AGENTS.md`, architecture/ADR layout, community files, and shell-based template validation.

**ai-dev-guardrails** adds *installable* Copilot/Claude/Codex pack modules and an optional Python hygiene validator. Use both together: template for repo skeleton, guardrails for domain packs and checklists.

## Recommended flow

1. Create a repo from **enterprise-github-template** (Use this template).
2. From an **ai-dev-guardrails** checkout, install a profile:

```bash
bash scripts/install-packs.sh /path/to/new-repo --profile baseline
# or: ops | security | api | data
```

3. Link copied files from the consumer `AGENTS.md` (keep the template’s guardrail section as the entry point):

```markdown
## Guardrail packs

- [Core](docs/guardrails/core.md)
- [Security](docs/guardrails/security.md)
- [Definition of Done](docs/guardrails/definition-of-done.md)
```

4. Optionally install the validator and run in CI:

```bash
python -m pip install -e /path/to/ai-dev-guardrails"[dev]"
ai-guardrails check .
```

## What not to duplicate

| Keep in the template | Add from ai-dev-guardrails |
| --- | --- |
| Root `AGENTS.md` policy voice | Domain packs under `docs/guardrails/` |
| `docs/architecture/`, `docs/decisions/` | Checklists / prompts for PR self-review |
| `docs/operations/` (release, incidents, secrets) | `agents/incidents.md`, runbook prompts when useful |
| `SUPPORT.md`, `SECURITY.md`, CoC | Validator checks for those files |
| `scripts/validate-template.sh` | `ai-guardrails check` for presence hygiene |

Do not copy template process docs into guardrails packs, and do not replace the template’s `AGENTS.md` wholesale with a pack file.

## Profile hints for template consumers

| Consumer focus | Profile |
| --- | --- |
| General service / library | `baseline` |
| Public HTTP/API surface | `api` |
| On-call / SRE-heavy | `ops` |
| Schema / ETL | `data` |
| Auth, PII, threat notes | `security` |
| Everything | `full` |

Exact lists: [profiles.md](profiles.md). Install flags: [install.md](install.md).

## Cross-links (template → guardrails)

In a template-derived repo you may point maintainers at:

- Pack matrix: https://github.com/rmkr-dev/ai-dev-guardrails/blob/main/docs/references/pack-matrix.md
- Validator catalog: https://github.com/rmkr-dev/ai-dev-guardrails/blob/main/docs/references/validator-checks.md
- CLI: https://github.com/rmkr-dev/ai-dev-guardrails/blob/main/docs/references/cli.md

Template docs worth reading first: `docs/development/first-week.md`, `docs/operations/release-process.md`, `docs/operations/incident-response.md`.

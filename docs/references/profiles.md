# Install profiles

Profiles for `scripts/install-packs.sh` / `make install-packs PROFILE=...`.

| Profile | Includes (on top of shared baseline where noted) |
| --- | --- |
| `baseline` | core, security, secrets, testing, docs, commits + DoD + pr-self-review |
| `api` | baseline + api, deps, supply-chain + test-plan, change-impact + supply-chain checklist |
| `ops` | baseline + observability, ci, incidents, performance, a11y, privacy, resilience + incident/runbook/privacy prompts + observability/a11y/resilience checklists |
| `data` | baseline + data, api + migration-review, change-impact |
| `security` | baseline + security, secrets, privacy, threat-model + security/privacy/threat-model prompts |
| `full` | all `packs/agents`, `packs/checklists`, `packs/prompts` |

Override with `PACKS="agents/core.md ..."` to install an explicit list.

See [install.md](install.md) and [pack-matrix.md](pack-matrix.md).

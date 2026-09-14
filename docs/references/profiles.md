# Install profiles

Profiles for `scripts/install-packs.sh` / `make install-packs PROFILE=...`.

List from a checkout:

```bash
bash scripts/install-packs.sh --list-profiles
bash scripts/install-packs.sh /path/to/repo --profile api --dry-run
```

## Summary

| Profile | Includes (on top of shared baseline where noted) |
| --- | --- |
| `baseline` | core, security, secrets, testing, docs, commits + DoD + pr-self-review |
| `api` | baseline + api, deps, supply-chain + test-plan, change-impact + supply-chain checklist |
| `ops` | baseline + observability, ci, incidents, performance, a11y, privacy, resilience, cost + incident/runbook/privacy prompts + observability/a11y/resilience/cost checklists |
| `data` | baseline + data, api + migration-review, change-impact |
| `security` | baseline + security, secrets, privacy, threat-model + security/privacy/threat-model prompts |
| `full` | all `packs/agents`, `packs/checklists`, `packs/prompts` |

Override with `PACKS="agents/core.md ..."` to install an explicit list.

## Exact pack lists

### `baseline`

- `agents/core.md`
- `agents/security.md`
- `agents/secrets.md`
- `agents/testing.md`
- `agents/docs.md`
- `agents/commits.md`
- `checklists/definition-of-done.md`
- `checklists/pr-self-review.md`

### `api` (= baseline +)

- `agents/api.md`
- `agents/deps.md`
- `agents/supply-chain.md`
- `prompts/test-plan.md`
- `prompts/change-impact.md`
- `checklists/supply-chain.md`

### `ops` (= baseline +)

- `agents/observability.md`
- `agents/ci.md`
- `agents/incidents.md`
- `agents/performance.md`
- `agents/a11y.md`
- `agents/privacy.md`
- `agents/resilience.md`
- `agents/cost.md`
- `prompts/incident-response.md`
- `prompts/runbook-draft.md`
- `prompts/privacy-review.md`
- `checklists/observability.md`
- `checklists/accessibility.md`
- `checklists/resilience.md`
- `checklists/cost.md`

### `data` (= baseline +)

- `agents/data.md`
- `agents/api.md`
- `prompts/migration-review.md`
- `prompts/change-impact.md`

### `security` (= baseline +)

- `agents/security.md`
- `agents/secrets.md`
- `agents/privacy.md`
- `agents/threat-model.md`
- `prompts/security-review.md`
- `prompts/privacy-review.md`
- `prompts/threat-model.md`

### `full`

Every `*.md` under `packs/agents`, `packs/checklists`, and `packs/prompts` (sorted).

## Manifest

Successful installs write `INSTALL_MANIFEST.txt` in the destination directory with profile name and copied paths.

See [install.md](install.md) and [pack-matrix.md](pack-matrix.md).

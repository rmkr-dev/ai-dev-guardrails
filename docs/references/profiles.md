# Install profiles

Profiles for `scripts/install-packs.sh` / `make install-packs PROFILE=...`.

List from a checkout:

```bash
bash scripts/install-packs.sh --list-profiles
ai-guardrails profiles
ai-guardrails profiles --profile ops --format json
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
| `web` | baseline + frontend, a11y, i18n + frontend/a11y/i18n checklists |
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

### `web` (= baseline +)

- `agents/frontend.md`
- `agents/a11y.md`
- `agents/i18n.md`
- `checklists/frontend.md`
- `checklists/accessibility.md`
- `checklists/i18n.md`

### `full`

Every `*.md` under `packs/agents`, `packs/checklists`, and `packs/prompts` (sorted).

## Manifest

Successful installs write `INSTALL_MANIFEST.txt` in the destination directory with `source:` (distributor version), `profile:`, `dest:`, `count:`, `categories:` (agents/checklists/prompts), and copied paths. Use `--quiet` to suppress per-file copy lines.

See [install.md](install.md) and [pack-matrix.md](pack-matrix.md).

## Destination layout

Installed files keep their `agents/`, `checklists/`, and `prompts/` prefixes under the destination directory (v0.3+).

## See also

- [install.md](install.md)
- [migrate-nested-install.md](migrate-nested-install.md) — flat → nested path mapping
- [pack-matrix.md](pack-matrix.md)
- [sample-agents-md.md](sample-agents-md.md)

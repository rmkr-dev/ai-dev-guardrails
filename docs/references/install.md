# Installing packs into a target repository

Packs are plain Markdown. Install by **copying** (or vendoring) into the consumer repo—typically under `docs/guardrails/`—then linking from that repo’s `AGENTS.md`.

## Option A — install script (recommended)

From a checkout of **ai-dev-guardrails**:

```bash
bash scripts/install-packs.sh /path/to/consumer-repo
# or: make install-packs TARGET=/path/to/consumer-repo PROFILE=api DRY_RUN=1
bash scripts/install-packs.sh /path/to/consumer-repo --profile api
bash scripts/install-packs.sh /path/to/consumer-repo --profile ops
bash scripts/install-packs.sh /path/to/consumer-repo --profile security
bash scripts/install-packs.sh /path/to/consumer-repo --profile full
```

Preview without writing files:

```bash
bash scripts/install-packs.sh /path/to/consumer-repo --profile api --dry-run
bash scripts/install-packs.sh --list-profiles
```

`--dry-run` (and a successful install) also warn on stderr if flat 0.2.x leftover `*.md` files sit at the destination root beside nested paths — see [migrate-nested-install.md](migrate-nested-install.md).

Custom set:

```bash
PACKS="agents/core.md agents/api.md prompts/pr-review.md" \
  bash scripts/install-packs.sh /path/to/consumer-repo
```

Default destination: `docs/guardrails/` (override with `--dest RELDIR`).

Packs are installed under `agents/`, `checklists/`, and `prompts/` subfolders so modules with the same basename (for example `agents/cost.md` and `checklists/cost.md`) do not overwrite each other.

On success the script writes `docs/guardrails/INSTALL_MANIFEST.txt` listing the profile and copied pack paths (useful for audits and reinstalls).

No Node/npm. Requires `bash` and `cp`.

## Option B — manual copy

Preserve category folders (do not flatten to basenames):

```bash
TARGET=/path/to/consumer-repo
DEST="$TARGET/docs/guardrails"
mkdir -p "$DEST/agents" "$DEST/checklists" "$DEST/prompts"
cp packs/agents/core.md "$DEST/agents/"
cp packs/agents/security.md "$DEST/agents/"
cp packs/checklists/definition-of-done.md "$DEST/checklists/"
```

See [examples.md](examples.md) for more copy recipes, [pack-matrix.md](pack-matrix.md) for when to install each module, and [migrate-nested-install.md](migrate-nested-install.md) if you still have flat copies from 0.2.x.

## Wire into consumer AGENTS.md

Add a short pointer section (adapt paths if you used a different `--dest`):

```markdown
## Guardrail packs

- [Core](docs/guardrails/agents/core.md)
- [Security](docs/guardrails/agents/security.md)
- [Definition of Done](docs/guardrails/checklists/definition-of-done.md)
```

A fuller template lives in [sample-agents-md.md](sample-agents-md.md).

## Optional validator

```bash
python -m pip install -e /path/to/ai-dev-guardrails"[dev]"
ai-guardrails check /path/to/consumer-repo
```

## Profiles (script)

| Profile | Intent |
| --- | --- |
| `baseline` | Day-to-day engineering + DoD |
| `api` | Baseline + API/contracts + deps prompts |
| `ops` | Baseline + observability/CI/incidents/runbooks |
| `data` | Baseline + data/migrations |
| `security` | Baseline + privacy/threat-model reviews |
| `web` | Baseline + frontend/a11y/i18n agents and checklists |
| `full` | Every file under `packs/agents`, `packs/checklists`, `packs/prompts` |

Exact pack lists: [profiles.md](profiles.md) or `bash scripts/install-packs.sh --list-profiles`.

## With enterprise-github-template

If the consumer was created from [enterprise-github-template](https://github.com/rmkr-dev/enterprise-github-template), prefer `--profile baseline` (or `ops` / `security`) into `docs/guardrails/` and keep the template’s own `AGENTS.md` as the entry point. Pair with the template’s `docs/operations/` and `SUPPORT.md` rather than duplicating process docs.

Full guide: [enterprise-github-template.md](enterprise-github-template.md).

## Migrating from flat 0.2.x installs

See [migrate-nested-install.md](migrate-nested-install.md).

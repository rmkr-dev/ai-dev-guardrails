# Installing packs into a target repository

Packs are plain Markdown. Install by **copying** (or vendoring) into the consumer repo—typically under `docs/guardrails/`—then linking from that repo’s `AGENTS.md`.

## Option A — install script (recommended)

From a checkout of **ai-dev-guardrails**:

```bash
bash scripts/install-packs.sh /path/to/consumer-repo
bash scripts/install-packs.sh /path/to/consumer-repo --profile api
bash scripts/install-packs.sh /path/to/consumer-repo --profile ops
bash scripts/install-packs.sh /path/to/consumer-repo --profile full
```

Custom set:

```bash
PACKS="agents/core.md agents/api.md prompts/pr-review.md" \
  bash scripts/install-packs.sh /path/to/consumer-repo
```

Default destination: `docs/guardrails/` (override with `--dest RELDIR`).

No Node/npm. Requires `bash` and `cp`.

## Option B — manual copy

```bash
TARGET=/path/to/consumer-repo
mkdir -p "$TARGET/docs/guardrails"
cp packs/agents/core.md \
   packs/agents/security.md \
   packs/checklists/definition-of-done.md \
   "$TARGET/docs/guardrails/"
```

See [examples.md](examples.md) for more copy recipes and [pack-matrix.md](pack-matrix.md) for when to install each module.

## Wire into consumer AGENTS.md

Add a short pointer section (adapt paths if you used a different `--dest`):

```markdown
## Guardrail packs

- [Core](docs/guardrails/core.md)
- [Security](docs/guardrails/security.md)
- [Definition of Done](docs/guardrails/definition-of-done.md)
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
| `full` | Every file under `packs/agents`, `packs/checklists`, `packs/prompts` |

Profile catalog: [profiles.md](profiles.md).

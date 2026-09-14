# Development

How to change **ai-dev-guardrails** locally.

## Setup

```bash
python -m pip install -e ".[dev]"
```

Requires Python 3.11+.

## Checks

```bash
make test
make check
# or:
pytest -q
ai-guardrails list-checks
ai-guardrails check .
```

CI runs the same pytest path via `rmkr-dev/gha-reusable-workflows` `python-ci@v0.4.0`.

## Packs vs CLI

- Markdown under `packs/` is the primary installable artifact (copy into consumer repos).
- `src/ai_guardrails/` is optional machine checking; extend rules with tests in the same PR.
- Keep [README.md](../../README.md) and [docs/architecture/architecture.md](../architecture/architecture.md) truthful.

## Commits and PRs

See [AGENTS.md](../../AGENTS.md) and pack modules under `packs/agents/` / `packs/prompts/`. Prefer 2–4 conventional commits per PR. No Cursor/AI co-author trailers.

## Lint / format helpers

```bash
make lint   # compileall + pytest collect-only
make fmt    # placeholder until a formatter is chosen
```

These targets are optional; `make test` and `make check` remain the primary gates.

## Machine-readable check output

```bash
ai-guardrails check . --format json
```

Emits passed/failed/total plus per-check `name` / `ok` / `detail`. Exit code still respects `--strict`.

```bash
ai-guardrails list-checks --format json
```

Full CLI flag reference: [cli.md](../references/cli.md).

## Install script tests

```bash
make install-packs-test
# or: bash tests/test_install_packs.sh
```

Covered automatically via `tests/test_install_packs_sh.py` in the default pytest CI job.

## Make install helpers

```bash
make profiles
make install-packs TARGET=/path/to/repo PROFILE=ops
make install-packs TARGET=/path/to/repo PROFILE=api DRY_RUN=1
make install-packs TARGET=/path/to/repo DEST=vendor/guardrails
```

## Profile catalog sync

`src/ai_guardrails/profiles.py` must match the arrays in `scripts/install-packs.sh`. CI enforces this via `tests/test_profiles_sync.py`.


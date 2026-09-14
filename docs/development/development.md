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

CI runs the same pytest path via `rmkr-dev/gha-reusable-workflows` `python-ci@v0.3.0`.

## Packs vs CLI

- Markdown under `packs/` is the primary installable artifact (copy into consumer repos).
- `src/ai_guardrails/` is optional machine checking; extend rules with tests in the same PR.
- Keep [README.md](../../README.md) and [docs/architecture/architecture.md](../architecture/architecture.md) truthful.

## Commits and PRs

See [AGENTS.md](../../AGENTS.md) and pack modules under `packs/agents/` / `packs/prompts/`. Prefer 2–4 conventional commits per PR. No Cursor/AI co-author trailers.

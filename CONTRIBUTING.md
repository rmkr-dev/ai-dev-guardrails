# Contributing

Thanks for improving **ai-dev-guardrails**. This repo ships installable AI+human engineering packs (for Copilot, Claude, and Codex) plus an optional Python hygiene validator. Keep changes small, reviewable, and real.

## Before you start

1. Read [README.md](README.md) and [AGENTS.md](AGENTS.md).
2. Pick one slice (installer/docs, validator rule, CI, or examples). Prefer a PR with 2–4 focused commits.
3. Do not invent features that are not in the tree. Docs must match reality.
4. Nested install layout (`agents/` / `checklists/` / `prompts/`): see [migrate-nested-install.md](docs/references/migrate-nested-install.md) and [ADR-008](docs/decisions/ADR-008-v0.4-nested-install-maturity.md). Prefer high-signal installer/docs/CI work over new pack modules unless a profile need is clear.

## Local checks

```bash
python -m pip install -e ".[dev]"
pytest -q
ai-guardrails check .
```

## Commit and PR style

- Conventional commits: `feat:`, `docs:`, `fix:`, `ci:`, `chore:`, `test:`.
- Author as yourself; no Cursor/AI co-author or generated-by trailers.
- PR body states the slice, what reviewers should check, and how to validate.
- High-impact changes (license, security defaults, public CLI API) need explicit human review.

## What this repo is not

- Not a duplicate of [llm-eval-harness](https://github.com/rmkr-dev/llm-eval-harness) (offline eval) or [enterprise-github-template](https://github.com/rmkr-dev/enterprise-github-template) (full repo template).
- No Node/npm. No secrets. No company names in docs or examples.

## Code of Conduct

Please follow [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

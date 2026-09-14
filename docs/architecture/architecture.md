# Architecture

Pack distributor for Copilot / Claude / Codex plus optional `ai-guardrails` CLI.

See [development.md](../development/development.md) for local workflow and [ADR-002](../decisions/ADR-002-expanding-hygiene-checks.md) for how hygiene checks grow. Milestone notes: [ADR-004](../decisions/ADR-004-v0.2-pack-and-check-suite.md).

## Packs

Markdown modules under `packs/` (agents, checklists, prompts) are copied into consumer repos. Tool-specific PR review prompts cover Copilot, Claude, and Codex.

## Validator

Presence-oriented checks in `src/ai_guardrails/checks.py`, exposed as `ai-guardrails check` / `list-checks`.

Default checks (13 as of 0.2.1): `agents_md`, `readme`, `architecture_docs`, `tests_or_ci`, `license`, `security_md`, `codeowners`, `contributing`, `gitignore`, `changelog`, `pr_template`, `dependabot`, `editorconfig`.

## CI

`python-ci.yml@v0.2.0` via `rmkr-dev/gha-reusable-workflows`.

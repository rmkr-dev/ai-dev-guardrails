# Architecture

Pack distributor for Copilot / Claude / Codex plus optional `ai-guardrails` CLI.

See [development.md](../development/development.md) for local workflow and [ADR-002](../decisions/ADR-002-expanding-hygiene-checks.md) for how hygiene checks grow.

Default checks (9): `agents_md`, `readme`, `architecture_docs`, `tests_or_ci`, `license`, `security_md`, `codeowners`, `contributing`, `gitignore`.

CI: `python-ci.yml@v0.2.0`.

# Architecture

**ai-dev-guardrails** ships markdown packs for Copilot / Claude / Codex and an optional Python hygiene CLI (`ai-guardrails check` / `list-checks`).

Default checks: `agents_md`, `readme`, `architecture_docs`, `tests_or_ci`, `license`, `security_md`, `codeowners`, `contributing`.

CI: `python-ci.yml@v0.2.0` from `rmkr-dev/gha-reusable-workflows`.

Out of scope: sample apps, Node/npm, remote policy servers, company branding.

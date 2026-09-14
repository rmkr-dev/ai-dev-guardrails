# Changelog

All notable changes to **ai-dev-guardrails** are documented here.

## [0.1.1] — 2026-09-14

### Added

- Pack modules: `packs/agents/testing.md`, `packs/agents/docs.md`, `packs/checklists/pr-self-review.md`
- Validator checks: `license`, `security_md`

## [0.1.0] — 2026-09-14

### Added

- Foundation docs: `README.md`, `LICENSE` (MIT), `CONTRIBUTING.md`, `AGENTS.md`, architecture stubs
- Pack modules for Copilot / Claude / Codex:
  - `packs/agents/core.md`
  - `packs/agents/security.md`
  - `packs/checklists/definition-of-done.md`
  - `packs/prompts/change-impact.md`
- Optional Python CLI `ai-guardrails check` with pytest coverage
- CI via `gha-reusable-workflows` `python-ci@v0.2.0`
- Dependabot (Actions + pip), `CODEOWNERS`, `SECURITY.md`
- `docs/references/examples.md` and ADR-001

[0.1.1]: https://github.com/rmkr-dev/ai-dev-guardrails/releases/tag/v0.1.1
[0.1.0]: https://github.com/rmkr-dev/ai-dev-guardrails/releases/tag/v0.1.0

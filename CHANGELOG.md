# Changelog

All notable changes to **ai-dev-guardrails** are documented here.

## [0.1.7] — 2026-09-14

### Added

- PR review prompts: `packs/prompts/pr-review.md` plus Copilot / Claude / Codex variants
- Examples section for installing PR review prompts

## [0.1.6] — 2026-09-14

### Added

- Pack module: `packs/agents/observability.md`
- Expanded `packs/agents/testing.md` (layout, isolation, review prompt)
- Examples coverage for testing + observability install

## [0.1.5] — 2026-09-14

### Added

- Pack module: `packs/agents/secrets.md`
- `docs/development/development.md`
- ADR-002: expanding hygiene checks incrementally

## [0.1.4] — 2026-09-14

### Added

- Pack module: `packs/checklists/release.md`
- `.github/PULL_REQUEST_TEMPLATE.md`
- Validator check: `gitignore`

## [0.1.3] — 2026-09-14

### Added

- Pack modules: `packs/agents/commits.md`, `packs/prompts/pr-body.md`
- Validator check: `contributing`

## [0.1.2] — 2026-09-14

### Added

- Pack modules: `packs/agents/ci.md`, `packs/prompts/adr-draft.md`
- Validator check: `codeowners`
- CLI: `ai-guardrails list-checks`

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

[0.1.7]: https://github.com/rmkr-dev/ai-dev-guardrails/releases/tag/v0.1.7
[0.1.6]: https://github.com/rmkr-dev/ai-dev-guardrails/releases/tag/v0.1.6
[0.1.5]: https://github.com/rmkr-dev/ai-dev-guardrails/releases/tag/v0.1.5
[0.1.4]: https://github.com/rmkr-dev/ai-dev-guardrails/releases/tag/v0.1.4
[0.1.3]: https://github.com/rmkr-dev/ai-dev-guardrails/releases/tag/v0.1.3
[0.1.2]: https://github.com/rmkr-dev/ai-dev-guardrails/releases/tag/v0.1.2
[0.1.1]: https://github.com/rmkr-dev/ai-dev-guardrails/releases/tag/v0.1.1
[0.1.0]: https://github.com/rmkr-dev/ai-dev-guardrails/releases/tag/v0.1.0

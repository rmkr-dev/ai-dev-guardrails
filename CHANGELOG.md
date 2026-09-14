# Changelog

All notable changes to **ai-dev-guardrails** are documented here.

## [0.2.19] — 2026-09-14

### Added

- Makefile targets: `lint`, `fmt`
- Docs for lint/fmt helpers; root AGENTS.md pointers to newer packs

## [0.2.18] — 2026-09-14

### Added

- Pack module: `packs/agents/privacy.md`
- Pack prompt: `packs/prompts/privacy-review.md`
- `ops` install profile includes privacy agent + prompt

## [0.2.17] — 2026-09-14

### Added

- Validator check: `code_of_conduct`
- Root `CODE_OF_CONDUCT.md` (Contributor Covenant–style)

## [0.2.16] — 2026-09-14

### Added

- Pack module: `packs/agents/supply-chain.md`
- Checklist: `packs/checklists/supply-chain.md`
- `api` install profile includes supply-chain agent + checklist

## [0.2.15] — 2026-09-14

### Added

- Validator check: `pre_commit` (`.pre-commit-config.yaml`)
- Root `.pre-commit-config.yaml` with basic hygiene hooks

## [0.2.14] — 2026-09-14

### Added

- ADR-005: accessibility, data packs, and issue-template checks
- Pack prompt: `packs/prompts/refactor-plan.md`

## [0.2.13] — 2026-09-14

### Added

- Pack module: `packs/agents/data.md`
- Pack prompt: `packs/prompts/migration-review.md`
- Install profile: `data`

## [0.2.12] — 2026-09-14

### Added

- Pack module: `packs/agents/a11y.md`
- Checklist: `packs/checklists/accessibility.md`
- `ops` install profile includes a11y agent + checklist

## [0.2.11] — 2026-09-14

### Added

- Validator check: `issue_templates` (`.github/ISSUE_TEMPLATE/` or `ISSUE_TEMPLATE.md`)
- Default GitHub issue templates for this repository

## [0.2.10] — 2026-09-14

### Changed

- CI pin: `python-ci@v0.3.0` (`rmkr-dev/gha-reusable-workflows`)

## [0.2.9] — 2026-09-14

### Added

- `scripts/install-packs.sh` with baseline/api/ops/full profiles
- `docs/references/install.md` copy/install workflow
- Makefile target: `install-packs`

## [0.2.8] — 2026-09-14

### Added

- Pack module: `packs/agents/incidents.md`
- Pack prompts: `packs/prompts/incident-response.md`, `packs/prompts/runbook-draft.md`

## [0.2.7] — 2026-09-14

### Added

- Pack module: `packs/agents/api.md` (API / contracts)

## [0.2.6] — 2026-09-14

### Added

- Pack prompt: `packs/prompts/release-notes.md`

## [0.2.5] — 2026-09-14

### Added

- `docs/references/validator-checks.md` catalog of default checks

## [0.2.4] — 2026-09-14

### Added

- Root `Makefile` (`test`, `check`, `list-checks`, `install`)
- Validator check: `makefile`

## [0.2.3] — 2026-09-14

### Added

- Pack module: `packs/agents/performance.md`
- `docs/references/pack-matrix.md`

## [0.2.2] — 2026-09-14

### Added

- Pack prompt: `packs/prompts/security-review.md`
- Sample consumer `AGENTS.md`: `docs/references/sample-agents-md.md`

## [0.2.1] — 2026-09-14

### Added

- Pack prompt: `packs/prompts/test-plan.md`
- Validator check: `editorconfig` (adds root `.editorconfig`)
- Architecture doc refreshed for the 0.2.x check suite

## [0.2.0] — 2026-09-14

### Added

- Pack module: `packs/agents/deps.md`
- Validator check: `dependabot`
- ADR-004: v0.2 pack and check suite milestone

### Milestone

Default packs now cover core engineering, security/secrets, testing, observability, docs, CI, commits, and dependencies, plus PR-review prompts (Copilot/Claude/Codex) and readiness checklists. Default CLI checks: 12 presence rules including changelog, PR template, and Dependabot.

## [0.1.9] — 2026-09-14

### Added

- Checklists: `packs/checklists/testing.md`, `packs/checklists/observability.md`
- Examples for testing and observability checklists

## [0.1.8] — 2026-09-14

### Added

- Validator checks: `changelog`, `pr_template`
- ADR-003: changelog and PR template hygiene checks

## [0.1.7] — 2026-09-14

### Added

- PR review prompts: `packs/prompts/pr-review.md` plus Copilot / Claude / Codex variants
- Examples section for installing PR review prompts

## [0.1.6] — 2026-09-14

### Added

- Pack module: `packs/agents/observability.md`
- Expanded `packs/agents/testing.md`
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

- Foundation docs, packs, optional CLI, CI

[0.2.6]: https://github.com/rmkr-dev/ai-dev-guardrails/releases/tag/v0.2.6
[0.2.5]: https://github.com/rmkr-dev/ai-dev-guardrails/releases/tag/v0.2.5
[0.2.4]: https://github.com/rmkr-dev/ai-dev-guardrails/releases/tag/v0.2.4
[0.2.3]: https://github.com/rmkr-dev/ai-dev-guardrails/releases/tag/v0.2.3
[0.2.2]: https://github.com/rmkr-dev/ai-dev-guardrails/releases/tag/v0.2.2
[0.2.1]: https://github.com/rmkr-dev/ai-dev-guardrails/releases/tag/v0.2.1
[0.2.0]: https://github.com/rmkr-dev/ai-dev-guardrails/releases/tag/v0.2.0
[0.1.9]: https://github.com/rmkr-dev/ai-dev-guardrails/releases/tag/v0.1.9
[0.1.8]: https://github.com/rmkr-dev/ai-dev-guardrails/releases/tag/v0.1.8
[0.1.7]: https://github.com/rmkr-dev/ai-dev-guardrails/releases/tag/v0.1.7
[0.1.6]: https://github.com/rmkr-dev/ai-dev-guardrails/releases/tag/v0.1.6
[0.1.5]: https://github.com/rmkr-dev/ai-dev-guardrails/releases/tag/v0.1.5
[0.1.4]: https://github.com/rmkr-dev/ai-dev-guardrails/releases/tag/v0.1.4
[0.1.3]: https://github.com/rmkr-dev/ai-dev-guardrails/releases/tag/v0.1.3
[0.1.2]: https://github.com/rmkr-dev/ai-dev-guardrails/releases/tag/v0.1.2
[0.1.1]: https://github.com/rmkr-dev/ai-dev-guardrails/releases/tag/v0.1.1
[0.1.0]: https://github.com/rmkr-dev/ai-dev-guardrails/releases/tag/v0.1.0

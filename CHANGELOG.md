# Changelog

All notable changes to **ai-dev-guardrails** are documented here.

## [0.4.18] — 2026-09-14

### Added

- Test: version metadata sync (`pyproject`, `__version__`, CITATION, README, CHANGELOG)
- Test: `ai-guardrails check --no-strict` exits 0 when checks fail

## [0.4.17] — 2026-09-14

### Added

- Shell tests: custom `--dest` and `web` profile nested install

### Changed

- Install docs profile table includes `web`

## [0.4.16] — 2026-09-14

### Added

- Test: `test_migrate_mapping_sync` keeps migrate guide nested paths aligned with `packs/`

## [0.4.15] — 2026-09-14

### Changed

- Migrate guide: complete flat→nested mapping (agents/checklists/prompts, a11y↔accessibility, ambiguous pairs)

## [0.4.14] — 2026-09-14

### Changed

- Architecture diagram: nested install path via `install-packs.sh` + migrate pointer

## [0.4.13] — 2026-09-14

### Changed

- Architecture docs README: ADR-007/008 + docs index pointers
- Development docs: validator sync note includes README

## [0.4.12] — 2026-09-14

### Added

- `docs/README.md` documentation index; root README links to it

## [0.4.11] — 2026-09-14

### Added

- `test_docs_checks_sync` also asserts README default-checks list matches `DEFAULT_CHECKS`

## [0.4.10] — 2026-09-14

### Changed

- CLI reference See also: profiles/install/migrate + docs checks sync pointer

## [0.4.9] — 2026-09-14

### Added

- Shell test: `--help` mentions nested layout and flat leftover warnings

### Changed

- Examples: nested install section points at flat leftover warnings / migrate guide

## [0.4.8] — 2026-09-14

### Changed

- Pack matrix: profile inclusion note (full-only / PACKS= for niche modules; ADR-008)

## [0.4.7] — 2026-09-14

### Changed

- `install-packs.sh --help`: document nested layout and flat leftover warnings

## [0.4.6] — 2026-09-14

### Changed

- `AGENTS.md` maintainer notes: profile/list-profiles sync tests, ADR-008 pack discipline, docs checks sync

## [0.4.5] — 2026-09-14

### Changed

- Development docs note validator docs sync test (`test_docs_checks_sync`)

## [0.4.4] — 2026-09-14

### Added

- Test: `tests/test_docs_checks_sync.py` keeps architecture + validator-checks catalogs aligned with `DEFAULT_CHECKS`

## [0.4.3] — 2026-09-14

### Changed

- Architecture docs: 20 default checks (incl. `support`), ADR-007/008 links, nested install note

## [0.4.2] — 2026-09-14

### Changed

- EGT integration guide: `web` profile hint + migrate-nested-install link

## [0.4.1] — 2026-09-14

### Changed

- Makefile help mentions nested install flat leftover warnings
- Install docs note that `--dry-run` / install warn on flat leftovers

## [0.4.0] — 2026-09-14

### Changed

- **Maturity milestone** (ADR-008): nested-install story is coherent — no second layout break vs 0.3.0
- Summarizes 0.3.x hardening: migration guide + nested samples/Option B, flat leftover warnings (install + `--dry-run`), profile/`--list-profiles` sync tests, CI pin `python-ci@v0.4.0`
- Prefer installer/docs/CI polish over new pack modules unless a profile need is clear

### Notes

- Install paths remain `agents/` / `checklists/` / `prompts/` under the destination
- Validator remains presence-oriented and optional
- Niche packs (for example governance) may stay `full`-only

## [0.3.16] — 2026-09-14

### Changed

- CONTRIBUTING: nested install + ADR-008 guidance; prefer installer/docs/CI over pack spam
- Development docs: nested install / flat leftover warning + list-profiles sync tests

## [0.3.15] — 2026-09-14

### Added

- ADR-008: v0.4 nested-install maturity (no layout break; prefer installer/docs/CI over pack spam)
- Decisions index table cleaned up; README links ADR-008

## [0.3.14] — 2026-09-14

### Added

- `--dry-run` also reports flat leftover packs that match selected basenames
- Shared `warn_flat_leftovers` helper used by install and dry-run paths

## [0.3.13] — 2026-09-14

### Added

- `install-packs.sh` warns on flat 0.2.x leftover `*.md` beside nested installs (no delete)
- Shell test coverage for flat leftover warning
- Migration guide notes the installer warning

## [0.3.12] — 2026-09-14

### Fixed

- `--list-profiles` ops section now includes `checklists/cost.md` (matches `ops_extra`)

### Added

- Test: `tests/test_list_profiles_sync.py` keeps `--list-profiles` text aligned with pack arrays

## [0.3.11] — 2026-09-14

### Changed

- Nested-install migration guide: fuller path map, flat leftover detection snippet
- Sample consumer `AGENTS.md`: all links use nested `agents/` / `checklists/` / `prompts/` paths
- Install Option B manual copy preserves category folders (no flatten)

## [0.3.10] — 2026-09-14

### Changed

- CI pin: `python-ci@v0.4.0` (`rmkr-dev/gha-reusable-workflows`); docs/README aligned

## [0.3.9] — 2026-09-14

### Added

- Root `AGENTS.md` maintainer notes for pack modules (cost/frontend/governance) and nested install

## [0.3.8] — 2026-09-14

### Added

- README CI and release badges

## [0.3.7] — 2026-09-14

### Added

- Pack module: `packs/agents/governance.md` (ownership / policy edits)

## [0.3.6] — 2026-09-14

### Added

- Test: `tests/test_profiles_sync.py` keeps CLI profile catalog aligned with `install-packs.sh`

## [0.3.5] — 2026-09-14

### Added

- `docs/references/migrate-nested-install.md` for 0.2.x → 0.3 nested layout consumers

## [0.3.4] — 2026-09-14

### Added

- Pack module: `packs/agents/frontend.md`
- Checklist: `packs/checklists/frontend.md`
- Install profile: `web` (frontend + a11y + i18n)

## [0.3.3] — 2026-09-14

### Added

- Makefile: `profiles` target; `install-packs` supports `DEST=` and `DRY_RUN=1`

## [0.3.2] — 2026-09-14

### Added

- CLI: `ai-guardrails profiles` (+ `--profile`, `--format json`) mirroring install profile catalog

## [0.3.1] — 2026-09-14

### Added

- Shell + pytest coverage for `install-packs.sh` nested layout (`make install-packs-test`)

## [0.3.0] — 2026-09-14

### Changed

- **Breaking (install layout):** `install-packs.sh` preserves `agents/`, `checklists/`, and `prompts/` under the destination so same-basename packs no longer overwrite each other. Update `AGENTS.md` links accordingly.

### Added

- ADR-007: v0.3 install layout and suite
- Install UX from 0.2.31+: `--dry-run`, `--list-profiles`, `INSTALL_MANIFEST.txt`, exact profile catalogs
- enterprise-github-template integration guide and cross-links
- Validator: `support` check; CLI `--only` / `--skip`
- Packs: cost/capacity agent + checklist (ops profile)

## [0.2.35] — 2026-09-14

### Added

- Pack module: `packs/agents/cost.md`
- Checklist: `packs/checklists/cost.md`
- `ops` install profile includes cost agent + checklist

## [0.2.34] — 2026-09-14

### Added

- CLI: `ai-guardrails check --only` / `--skip` to select checks

## [0.2.33] — 2026-09-14

### Added

- Validator check: `support` (`SUPPORT.md`)
- Root `SUPPORT.md` for consumer help routing

## [0.2.32] — 2026-09-14

### Added

- `docs/references/enterprise-github-template.md` integration guide
- Cross-links from README, install, examples, and pack-matrix

## [0.2.31] — 2026-09-14

### Added

- Install script: `--dry-run`, `--list-profiles`, destination `INSTALL_MANIFEST.txt`
- Profile docs: exact pack lists per profile in `docs/references/profiles.md`

## [0.2.30] — 2026-09-14

### Added

- `docs/references/cli.md` CLI flag reference

## [0.2.29] — 2026-09-14

### Added

- Pack module: `packs/agents/resilience.md`
- Checklist: `packs/checklists/resilience.md`
- `ops` install profile includes resilience

## [0.2.28] — 2026-09-14

### Added

- `docs/references/profiles.md` install profile catalog
- Makefile `help` target

## [0.2.27] — 2026-09-14

### Added

- CLI: `ai-guardrails list-checks --format json`

## [0.2.26] — 2026-09-14

### Added

- Install profile: `security` (security/secrets/privacy/threat-model + review prompts)

## [0.2.25] — 2026-09-14

### Added

- Pack module: `packs/agents/threat-model.md`
- Pack prompt: `packs/prompts/threat-model.md`

## [0.2.24] — 2026-09-14

### Added

- Validator check: `citation` (`CITATION.cff`)
- Root `CITATION.cff` for software citation metadata

## [0.2.23] — 2026-09-14

### Added

- ADR-006: 0.2.x expansion — checks and domain packs
- Pack module: `packs/agents/support.md`
- Pack prompt: `packs/prompts/support-reply.md`

## [0.2.22] — 2026-09-14

### Added

- Validator check: `funding` (`.github/FUNDING.yml`)
- Root `.github/FUNDING.yml` pointing at `rmkr-dev`

## [0.2.21] — 2026-09-14

### Added

- Pack module: `packs/agents/i18n.md`
- Checklist: `packs/checklists/i18n.md`

## [0.2.20] — 2026-09-14

### Added

- CLI: `ai-guardrails check --format json` machine-readable output

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

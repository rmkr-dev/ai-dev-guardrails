# ADR-001: Pack modules plus an optional Python validator

- **Status:** Accepted
- **Date:** 2026-09-14

## Context

We need installable AI+human guardrails for Copilot, Claude, and Codex without duplicating:

- `enterprise-github-template` (full GitHub repository template)
- `llm-eval-harness` (offline eval)

Consumers should be able to adopt markdown packs with zero runtime dependency, while still having an optional machine-checkable hygiene bar.

## Decision

1. Ship **copyable markdown packs** under `packs/` (agents, checklists, prompts) as the primary artifact.
2. Ship an **optional** Python package `ai-guardrails` with a `check` CLI that verifies presence of `AGENTS.md`, `README.md`, architecture docs, and tests-or-CI indicators.
3. Keep this repository free of Node/npm, sample apps, company names, and secrets.
4. Run CI via `rmkr-dev/gha-reusable-workflows` `python-ci@v0.2.0`.

## Consequences

- Adoption path is copy-paste friendly; no forced pip install for markdown-only consumers.
- Validator rules stay intentionally small and presence-oriented (not policy-as-code for enterprises).
- Architecture docs and README must be updated whenever packs or checks change so docs match reality.
- Future rules (for example requiring `SECURITY.md` or CODEOWNERS) can extend the CLI in follow-up PRs without changing the pack-first model.

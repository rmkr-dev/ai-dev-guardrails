# ADR-003: Changelog and PR template hygiene checks

- **Status:** Accepted
- **Date:** 2026-09-14

## Context

Consumers and this repository itself benefit from a visible change history and a consistent PR template. Presence checks keep the optional CLI aligned with practices already documented in the packs.

## Decision

1. Add default checks `changelog` and `pr_template` (file or `.github/PULL_REQUEST_TEMPLATE/` directory).
2. Keep them presence-oriented per ADR-002.
3. Ship tests and docs in the same release as the new checks.

## Consequences

- Stricter default `ai-guardrails check` for consumers who upgrade.
- Content quality of CHANGELOG / PR templates remains a human/agent pack concern, not a linter here.

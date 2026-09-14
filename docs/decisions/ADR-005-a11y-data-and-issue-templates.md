# ADR-005: Accessibility, data packs, and issue-template checks

- **Status:** Accepted
- **Date:** 2026-09-14

## Context

After the v0.2.0 milestone (ADR-004), consumers asked for guidance on human-facing accessibility, schema/migration safety, and GitHub issue-template hygiene. These fit the existing presence-oriented validator and copyable pack model without becoming a policy engine.

## Decision

1. Add pack modules for **accessibility** (`agents/a11y.md`, checklist) and **data/migrations** (`agents/data.md`, migration-review prompt).
2. Add a presence check for **issue templates** alongside the existing PR-template check.
3. Keep checks presence-oriented (ADR-002); qualitative a11y and migration judgment stays in packs and human review.
4. Continue additive 0.2.x releases for these modules.

## Consequences

- Default CLI check count grows when `issue_templates` ships.
- Install profiles may gain `data` (and a11y under `ops`) without breaking `baseline`.
- Full WCAG tooling, schema lint engines, and org-wide policy remain out of scope.

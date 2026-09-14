# ADR-002: Expanding hygiene checks incrementally

- **Status:** Accepted
- **Date:** 2026-09-14

## Context

The optional `ai-guardrails check` CLI started with four presence checks. Consumers benefit from a slightly higher default bar (LICENSE, SECURITY, CODEOWNERS, CONTRIBUTING, `.gitignore`) without turning the tool into a heavyweight policy engine.

## Decision

1. Grow the **default** check suite in small releases (0.1.x) when this repository already satisfies the new rule.
2. Keep checks **presence-oriented** (file/dir indicators), not content linters or secret scanners.
3. Require unit tests and docs/CHANGELOG updates in the same PR as each new check.
4. Expose names via `ai-guardrails list-checks`.

## Consequences

- Default `check` becomes stricter over time; consumers pinning an older version stay stable.
- Secret *scanning* remains out of scope here (see packs/agents/secrets.md for human/agent guidance).
- Large policy frameworks or SARIF publishers would need a new ADR.

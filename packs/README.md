# Guardrail packs

Copyable modules for **GitHub Copilot**, **Claude**, and **Codex** (and humans reviewing their output). Install by copying into a target repository—typically beside or into that repo’s own `AGENTS.md`.

| Path | Audience | Purpose |
| --- | --- | --- |
| [agents/core.md](agents/core.md) | Copilot / Claude / Codex | Core engineering guardrails |
| [agents/security.md](agents/security.md) | Copilot / Claude / Codex | Security-by-default expectations |
| [agents/secrets.md](agents/secrets.md) | Copilot / Claude / Codex | Secrets never-commit rules |
| [agents/testing.md](agents/testing.md) | Copilot / Claude / Codex | Testing expectations |
| [agents/observability.md](agents/observability.md) | Copilot / Claude / Codex | Logs / metrics / traces expectations |
| [agents/docs.md](agents/docs.md) | Copilot / Claude / Codex | Docs / ADR / diagram honesty |
| [agents/ci.md](agents/ci.md) | Copilot / Claude / Codex | CI / Actions expectations |
| [agents/commits.md](agents/commits.md) | Copilot / Claude / Codex | Conventional commit expectations |
| [agents/deps.md](agents/deps.md) | Copilot / Claude / Codex | Dependency / supply-chain expectations |
| [agents/performance.md](agents/performance.md) | Copilot / Claude / Codex | Performance expectations |
| [agents/api.md](agents/api.md) | Copilot / Claude / Codex | API / contracts expectations |
| [agents/incidents.md](agents/incidents.md) | Copilot / Claude / Codex | Incident / runbook expectations |
| [agents/a11y.md](agents/a11y.md) | Copilot / Claude / Codex | Accessibility expectations |
| [agents/data.md](agents/data.md) | Copilot / Claude / Codex | Data / migrations expectations |
| [agents/supply-chain.md](agents/supply-chain.md) | Copilot / Claude / Codex | Supply-chain / release artifact expectations |
| [agents/privacy.md](agents/privacy.md) | Copilot / Claude / Codex | Privacy / PII expectations |
| [checklists/definition-of-done.md](checklists/definition-of-done.md) | Humans + agents | Slice Definition of Done |
| [checklists/pr-self-review.md](checklists/pr-self-review.md) | Humans + agents | Pre-review checklist |
| [checklists/release.md](checklists/release.md) | Humans + agents | Release / tag checklist |
| [checklists/testing.md](checklists/testing.md) | Humans + agents | Testing readiness checklist |
| [checklists/observability.md](checklists/observability.md) | Humans + agents | Observability readiness checklist |
| [checklists/accessibility.md](checklists/accessibility.md) | Humans + agents | Accessibility readiness checklist |
| [checklists/supply-chain.md](checklists/supply-chain.md) | Humans + agents | Supply-chain readiness checklist |
| [prompts/change-impact.md](prompts/change-impact.md) | Copilot / Claude / Codex | Blast-radius prompt |
| [prompts/adr-draft.md](prompts/adr-draft.md) | Copilot / Claude / Codex | ADR drafting prompt |
| [prompts/pr-body.md](prompts/pr-body.md) | Copilot / Claude / Codex | PR description prompt |
| [prompts/test-plan.md](prompts/test-plan.md) | Copilot / Claude / Codex | Test plan drafting prompt |
| [prompts/security-review.md](prompts/security-review.md) | Copilot / Claude / Codex | Security-focused PR review prompt |
| [prompts/release-notes.md](prompts/release-notes.md) | Copilot / Claude / Codex | Release notes drafting prompt |
| [prompts/incident-response.md](prompts/incident-response.md) | Copilot / Claude / Codex | Incident response drafting prompt |
| [prompts/runbook-draft.md](prompts/runbook-draft.md) | Copilot / Claude / Codex | Runbook drafting prompt |
| [prompts/migration-review.md](prompts/migration-review.md) | Copilot / Claude / Codex | Migration / schema review prompt |
| [prompts/refactor-plan.md](prompts/refactor-plan.md) | Copilot / Claude / Codex | Refactor planning prompt |
| [prompts/privacy-review.md](prompts/privacy-review.md) | Copilot / Claude / Codex | Privacy / PII review prompt |
| [prompts/pr-review.md](prompts/pr-review.md) | Copilot / Claude / Codex | Generic PR review prompt |
| [prompts/pr-review-copilot.md](prompts/pr-review-copilot.md) | GitHub Copilot | Copilot-oriented PR review |
| [prompts/pr-review-claude.md](prompts/pr-review-claude.md) | Claude | Claude-oriented PR review |
| [prompts/pr-review-codex.md](prompts/pr-review-codex.md) | Codex | Codex-oriented PR review |

See [docs/references/install.md](../docs/references/install.md) for the install script and copy workflow.

See [docs/references/examples.md](../docs/references/examples.md) for additional copy recipes.

See [docs/references/pack-matrix.md](../docs/references/pack-matrix.md) for an install-when matrix.

Quick start:

```bash
bash scripts/install-packs.sh /path/to/consumer-repo --profile baseline
```

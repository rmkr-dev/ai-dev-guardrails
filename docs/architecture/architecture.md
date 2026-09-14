# Architecture

## Current state

**ai-dev-guardrails** is a **pack repository**: markdown modules and (soon) a small Python CLI that consumers copy or install into their own repos. There is no application runtime, datastore, or networked service in this tree.

| Surface | Role |
| --- | --- |
| `README.md` | Entry point and status |
| `AGENTS.md` | Guardrails for changing *this* repo |
| `CONTRIBUTING.md` | How to propose changes |
| `LICENSE` | MIT |
| `packs/` | Copyable agent, checklist, and prompt modules |
| `docs/architecture/` | Current-state narrative and diagrams |
| `docs/decisions/` | ADR index |
| `src/` + `tests/` | Optional `ai-guardrails` hygiene CLI — *planned* |
| `.github/` | CI, Dependabot, CODEOWNERS, SECURITY — *planned* |

## How consumers use it

1. Copy selected files from `packs/` (and often patterns from root `AGENTS.md`) into a target repository.
2. Optionally install the Python validator (when published) and run `ai-guardrails check <path>` in CI or locally.
3. Keep pack content versioned in the consumer repo (copy-based).

This complements:

- **enterprise-github-template** — full template (issue forms, release, CodeQL, etc.)
- **llm-eval-harness** — offline golden-fixture evaluation

## CI shape (planned)

When CI lands, it will call `rmkr-dev/gha-reusable-workflows` `python-ci@v0.2.0` to lint/compile and run pytest for the validator. Until then, there is no CI badge and no required check.

## Network posture

No networked runtime. See [diagram-conventions.md](diagram-conventions.md).

## What is intentionally out of scope

- Sample applications or “hello world” stacks
- Node/npm tooling
- Live remote policy servers or SaaS dashboards
- Company-specific standards or branding

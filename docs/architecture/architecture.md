# Architecture

## Current state

**ai-dev-guardrails** is a **pack repository**: markdown modules and (soon) a small Python CLI that consumers copy or install into their own repos. There is no application runtime, datastore, or networked service in this tree.

| Surface | Role (today / next) |
| --- | --- |
| `README.md` | Entry point and status |
| `AGENTS.md` | Guardrails for changing *this* repo |
| `CONTRIBUTING.md` | How to propose changes |
| `LICENSE` | MIT |
| `docs/architecture/` | Current-state narrative and diagrams |
| `docs/decisions/` | ADRs (stubs until first decisions land) |
| `packs/` | Copyable agent/checklist/prompt modules — *planned* |
| `src/` + `tests/` | Optional `ai-guardrails` hygiene CLI — *planned* |
| `.github/` | CI, Dependabot, CODEOWNERS, SECURITY — *planned* |

## How consumers use it

1. Copy selected files from `packs/` (and often a root `AGENTS.md`) into a target repository.
2. Optionally install the Python validator and run `ai-guardrails check <path>` in CI or locally.
3. Keep pack content versioned in the consumer repo (copy-based, not a live submodule requirement).

This complements:

- **enterprise-github-template** — full template (issue forms, release, CodeQL, etc.)
- **llm-eval-harness** — offline golden-fixture evaluation

Do not merge those concerns into this repo.

## CI shape (planned)

When CI lands, it will call `rmkr-dev/gha-reusable-workflows` `python-ci@v0.2.0` to lint/compile and run pytest for the validator. Until then, there is no CI badge and no required check.

## Network posture

No networked runtime. Consumers add their own network diagrams when they introduce cloud or service boundaries. See [diagram-conventions.md](diagram-conventions.md).

## What is intentionally out of scope

- Sample applications or “hello world” stacks
- Node/npm tooling
- Live remote policy servers or SaaS dashboards
- Company-specific standards or branding

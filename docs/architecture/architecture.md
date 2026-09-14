# Architecture

## Current state

**ai-dev-guardrails** is a **pack repository**: markdown modules plus an optional Python CLI that consumers copy or install into their own repos. There is no application runtime, datastore, or networked service in this tree.

| Surface | Role |
| --- | --- |
| `README.md` | Entry point and status |
| `AGENTS.md` | Guardrails for changing *this* repo |
| `CONTRIBUTING.md` | How to propose changes |
| `LICENSE` | MIT |
| `SECURITY.md` | Vulnerability reporting |
| `CHANGELOG.md` | Release notes |
| `packs/` | Copyable agent, checklist, and prompt modules |
| `src/ai_guardrails/` | `ai-guardrails` hygiene CLI (`check`) |
| `tests/` | Pytest coverage for checks and CLI |
| `docs/architecture/` | Current-state narrative and diagrams |
| `docs/decisions/` | ADRs (ADR-001) |
| `docs/references/examples.md` | How to copy packs into a consumer repo |
| `.github/workflows/ci.yml` | Calls `python-ci@v0.2.0` |
| `.github/dependabot.yml` | Weekly Actions + pip updates |
| `.github/CODEOWNERS` | Default owner `@rmkr-dev` |

## Validator behavior

`ai-guardrails check <root>` runs these checks against `<root>`:

1. `AGENTS.md` at repository root
2. `README.md` at repository root
3. Architecture docs under `docs/architecture/` (markdown files) or `docs/architecture.md` / `architecture.md`
4. Tests **or** CI indicators (`tests/test_*.py`, `.github/workflows/*`, and a few other CI filenames)
5. `LICENSE` (or `LICENSE.md` / `COPYING`)
6. `SECURITY.md`

## CI shape

CI uses `rmkr-dev/gha-reusable-workflows/.github/workflows/python-ci.yml@v0.2.0`.

## What is intentionally out of scope

- Sample applications or “hello world” stacks
- Node/npm tooling
- Live remote policy servers or SaaS dashboards
- Company-specific standards or branding

# Architecture

## Current state

**ai-dev-guardrails** is a **pack repository**: markdown modules plus an optional Python CLI that consumers copy or install into their own repos. There is no application runtime, datastore, or networked service in this tree.

| Surface | Role |
| --- | --- |
| `README.md` | Entry point and status |
| `AGENTS.md` | Guardrails for changing *this* repo |
| `CONTRIBUTING.md` | How to propose changes |
| `LICENSE` | MIT |
| `packs/` | Copyable agent, checklist, and prompt modules |
| `src/ai_guardrails/` | `ai-guardrails` hygiene CLI (`check`) |
| `tests/` | Pytest coverage for checks and CLI |
| `docs/architecture/` | Current-state narrative and diagrams |
| `docs/decisions/` | ADR index |
| `.github/` | CI, Dependabot, CODEOWNERS, SECURITY — *planned* |

## Validator behavior

`ai-guardrails check <root>` runs four checks against `<root>`:

1. `AGENTS.md` at repository root
2. `README.md` at repository root
3. Architecture docs under `docs/architecture/` (markdown files) or `docs/architecture.md` / `architecture.md`
4. Tests **or** CI indicators (`tests/test_*.py`, `.github/workflows/*`, and a few other CI filenames)

Exit code is non-zero in `--strict` mode (default) when any check fails.

## How consumers use it

1. Copy selected files from `packs/` into a target repository.
2. `pip install` this package (editable or from a future release) and run `ai-guardrails check <path>`.
3. Keep pack content versioned in the consumer repo (copy-based).

## CI shape (planned)

CI will call `rmkr-dev/gha-reusable-workflows` `python-ci@v0.2.0` to compile/lint and run pytest.

## What is intentionally out of scope

- Sample applications or “hello world” stacks
- Node/npm tooling
- Live remote policy servers or SaaS dashboards
- Company-specific standards or branding

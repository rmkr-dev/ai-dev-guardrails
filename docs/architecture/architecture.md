# Architecture

## Current state

**ai-dev-guardrails** distributes markdown guardrail packs for Copilot / Claude / Codex plus an optional Python hygiene CLI. No application runtime or networked service lives in this tree.

| Surface | Role |
| --- | --- |
| `packs/` | Copyable agent, checklist, and prompt modules |
| `src/ai_guardrails/` | `ai-guardrails` CLI (`check`, `list-checks`) |
| `tests/` | Pytest coverage |
| `docs/` | Architecture, ADRs, examples |
| `.github/` | CI (`python-ci@v0.2.0`), Dependabot, CODEOWNERS |

## Validator behavior

`ai-guardrails check <root>` runs: `agents_md`, `readme`, `architecture_docs`, `tests_or_ci`, `license`, `security_md`, `codeowners`.

`ai-guardrails list-checks` prints those names in order.

## Out of scope

Sample apps, Node/npm, remote policy servers, company-specific branding.

# ai-dev-guardrails

Installable AI+human engineering guardrails for **GitHub Copilot**, **Claude**, and **Codex**: `AGENTS.md` modules, Definition of Done checklists, change-impact prompts, ADR/diagram conventions, and an optional Python validator for repo hygiene.

Distilled from personal engineering standards. Complements (does not duplicate):

- [llm-eval-harness](https://github.com/rmkr-dev/llm-eval-harness) — offline fixture eval
- [enterprise-github-template](https://github.com/rmkr-dev/enterprise-github-template) — full GitHub repo template

## Status

Early scaffold. Foundation docs and architecture stubs are in place. Pack modules, the validator CLI, and CI land in follow-up PRs.

## Layout (planned / current)

| Path | Role |
| --- | --- |
| `AGENTS.md` | Repo-level guardrails for humans and coding agents |
| `packs/` | Copyable modules (agents, checklists, prompts) — *coming next* |
| `docs/architecture/` | Current-state architecture for this pack repo |
| `src/` + `tests/` | Optional Python `ai-guardrails` CLI — *planned* |

## Quick start (once packs land)

Copy the modules you need into a target repo (typically `AGENTS.md` plus selected files under `packs/`), then keep them in the same PR as behavior changes they govern. See upcoming `docs/references/examples.md`.

## License

MIT — see [LICENSE](LICENSE).

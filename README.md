# ai-dev-guardrails

Installable AI+human engineering guardrails for **GitHub Copilot**, **Claude**, and **Codex**: `AGENTS.md` modules, Definition of Done checklists, change-impact prompts, ADR/diagram conventions, and an optional Python validator for repo hygiene.

Distilled from personal engineering standards. Complements (does not duplicate):

- [llm-eval-harness](https://github.com/rmkr-dev/llm-eval-harness) — offline fixture eval
- [enterprise-github-template](https://github.com/rmkr-dev/enterprise-github-template) — full GitHub repo template

## Status

Foundation docs, `AGENTS.md`, and architecture stubs are in place. Pack modules (`packs/`), the validator CLI, and CI land in follow-up PRs.

## Layout

| Path | Role |
| --- | --- |
| `AGENTS.md` | Repo-level guardrails for humans and coding agents |
| `CONTRIBUTING.md` | How to propose changes |
| `docs/architecture/` | Current-state architecture for this pack repo |
| `docs/decisions/` | ADR index (empty until first decisions) |
| `packs/` | Copyable modules — *planned* |
| `src/` + `tests/` | Optional Python `ai-guardrails` CLI — *planned* |

## Architecture

See [docs/architecture/architecture.md](docs/architecture/architecture.md) and the [diagram](docs/architecture/architecture-diagram.md).

## License

MIT — see [LICENSE](LICENSE).

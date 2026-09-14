# ai-dev-guardrails

Installable AI+human engineering guardrails for **GitHub Copilot**, **Claude**, and **Codex**: `AGENTS.md` modules, Definition of Done checklists, change-impact prompts, ADR/diagram conventions, and an optional Python validator for repo hygiene.

Distilled from personal engineering standards. Complements (does not duplicate):

- [llm-eval-harness](https://github.com/rmkr-dev/llm-eval-harness) — offline fixture eval
- [enterprise-github-template](https://github.com/rmkr-dev/enterprise-github-template) — full GitHub repo template

## Status

Foundation docs and first **packs/** modules are available. The optional Python validator CLI and CI land in follow-up PRs.

## Quick start

1. Copy [AGENTS.md](AGENTS.md) ideas into your repo’s own `AGENTS.md`, or start from [packs/agents/core.md](packs/agents/core.md).
2. Add [packs/agents/security.md](packs/agents/security.md) when the work touches auth, secrets, or CI permissions.
3. Use [packs/checklists/definition-of-done.md](packs/checklists/definition-of-done.md) in PR review.
4. Use [packs/prompts/change-impact.md](packs/prompts/change-impact.md) before large edits.

See [packs/README.md](packs/README.md) for the module index.

## Layout

| Path | Role |
| --- | --- |
| `AGENTS.md` | Guardrails for changing *this* repository |
| `packs/agents/` | Copyable agent modules for Copilot / Claude / Codex |
| `packs/checklists/` | Definition of Done checklist |
| `packs/prompts/` | Change-impact prompt |
| `docs/architecture/` | Current-state architecture for this pack repo |
| `docs/decisions/` | ADR index |
| `src/` + `tests/` | Optional Python `ai-guardrails` CLI — *planned* |

## Architecture

See [docs/architecture/architecture.md](docs/architecture/architecture.md).

## License

MIT — see [LICENSE](LICENSE).

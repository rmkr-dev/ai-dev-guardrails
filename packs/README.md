# Guardrail packs

Copyable modules for **GitHub Copilot**, **Claude**, and **Codex** (and humans reviewing their output). Install by copying into a target repository—typically beside or into that repo’s own `AGENTS.md`.

| Path | Audience | Purpose |
| --- | --- | --- |
| [agents/core.md](agents/core.md) | Copilot / Claude / Codex | Core engineering guardrails |
| [agents/security.md](agents/security.md) | Copilot / Claude / Codex | Security-by-default expectations |
| [agents/testing.md](agents/testing.md) | Copilot / Claude / Codex | Testing expectations |
| [agents/docs.md](agents/docs.md) | Copilot / Claude / Codex | Docs / ADR / diagram honesty |
| [checklists/definition-of-done.md](checklists/definition-of-done.md) | Humans + agents | Slice Definition of Done |
| [checklists/pr-self-review.md](checklists/pr-self-review.md) | Humans + agents | Pre-review checklist |
| [prompts/change-impact.md](prompts/change-impact.md) | Copilot / Claude / Codex | Prompt to reason about blast radius |

See [docs/references/examples.md](../docs/references/examples.md) for copy instructions.

These packs complement a full repo template; they do not replace CI, CODEOWNERS, or security policy files.

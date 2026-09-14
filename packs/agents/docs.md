# Documentation guardrails (Copilot / Claude / Codex)

Use with [core.md](core.md).

## Docs match reality

- Update README and linked docs in the **same PR** as the behavior change.
- Label planned work as planned; do not describe missing files as present.
- Prefer short, linked modules over one giant doc.

## Architecture and ADRs

- System shape lives under `docs/architecture/` when the consumer uses that layout.
- Significant tooling or layout choices get an ADR under `docs/decisions/`.
- Diagrams: Mermaid preferred; dashed edges for planned paths; no invented infrastructure.

## Agent-facing docs

- Keep `AGENTS.md` accurate for Copilot / Claude / Codex.
- Link pack modules instead of duplicating long prompts in every chat.

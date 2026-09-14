# Diagram conventions

Use these rules so diagrams stay honest for humans and coding agents.

## Principles

1. **Docs match reality.** Draw only what exists in the repo or is clearly labeled `planned`.
2. **One diagram, one question.** Prefer a small Mermaid chart over a kitchen-sink canvas.
3. **No fake infrastructure.** Do not invent VPCs, meshes, or SaaS boxes for this pack repo.
4. **Label ownership.** Distinguish pack distributor vs consumer repo when both appear.
5. **Update in the same PR** as the structural change the diagram describes.

## Preferred format

- Mermaid in Markdown under `docs/architecture/` or an ADR.
- Keep node IDs short; human labels can be longer.
- Use dashed edges (`-.->`) for planned or optional paths.

## ADR link

Significant tooling or layout choices belong in `docs/decisions/` with a short Mermaid snippet when it clarifies the decision.

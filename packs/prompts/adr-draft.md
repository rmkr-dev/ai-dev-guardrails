# ADR draft prompt (Copilot / Claude / Codex)

Use when a change needs an Architecture Decision Record.

```text
Draft an ADR for this repository using the local docs/decisions format.

Include:
- Title and next ADR number (check docs/decisions/README.md)
- Status: Proposed
- Date (ISO)
- Context: problem and constraints (no company names)
- Decision: what we choose and what we explicitly reject
- Consequences: follow-ups, risks, doc/CI updates required

Keep it short (one screen). Tie the decision to files that exist or will exist
in the same PR. Do not invent infrastructure that is not in the repo.
```

Link the resulting ADR from `docs/decisions/README.md` in the same change.

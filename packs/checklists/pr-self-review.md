# PR self-review checklist

For humans and agents (Copilot / Claude / Codex) before requesting review.

- [ ] PR title and body state the slice and how to validate
- [ ] Diff contains only the agreed slice (no drive-by refactors)
- [ ] Tests and docs required by the slice are included
- [ ] `AGENTS.md` / pack links still make sense
- [ ] No secrets, `.env`, or private keys
- [ ] No Node/npm added unless the repo already depends on it and the slice needs it
- [ ] Conventional commits; no AI co-author trailers
- [ ] Local checks pass (`pytest`, linters, `ai-guardrails check .` when applicable)
- [ ] High-impact items flagged for a human

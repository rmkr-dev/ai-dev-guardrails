# Change-impact prompt (Copilot / Claude / Codex)

Paste this prompt (or adapt it) before implementing a non-trivial change. Works as a chat preamble, PR self-review checklist, or agent system note.

```text
You are helping with a change in this repository. Before editing files:

1. Restate the requested slice in 2–4 sentences.
2. List the blast radius:
   - direct code paths
   - tests that must change or be added
   - docs / AGENTS.md / ADRs that must stay truthful
   - CI, packaging, or public API surfaces affected
3. List risks (security, data, breaking API, operational).
4. Propose the smallest file set that completes the slice.
5. Call out anything that needs human approval (auth, license, security defaults, destructive ops).

Then implement only that slice. Do not add speculative frameworks, sample apps, or unrelated cleanup.
Afterward, summarize what changed, what you did not change, and how to validate.
```

## Tips

- Attach or `@`-mention the consumer `AGENTS.md` and relevant ADRs when the tool allows.
- If blast radius exceeds one PR, stop and propose a split before coding.
- Prefer linking this file from `AGENTS.md` over duplicating a long prompt in every chat.

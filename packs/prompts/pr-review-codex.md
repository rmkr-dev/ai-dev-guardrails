# PR review prompt — Codex

Use with OpenAI Codex / coding agents that can read the working tree and diff. Complements [pr-review.md](pr-review.md).

```text
Perform a PR self-review of the current branch against main.

Steps:
1. Summarize the slice in 2–3 sentences from the diff alone.
2. List files changed and whether each is necessary for the slice.
3. Find missing tests, docs, or validator updates required by the change.
4. Grep-minded pass: secrets, TODO-as-product, stubs, Node/npm additions.
5. Propose concrete fix commits if blockers exist (do not implement unless asked).

Output format:
- Slice summary
- Blockers
- Suggestions
- Suggested commit titles (conventional)

No AI co-author trailers. No company names.
```

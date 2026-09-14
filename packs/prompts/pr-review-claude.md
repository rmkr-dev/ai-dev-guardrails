# PR review prompt — Claude

Use in Claude (Projects, Claude Code, or chat with the diff pasted). Complements [pr-review.md](pr-review.md).

```text
Review this pull request diff thoroughly. You are Claude acting as a second reviewer.

Emphasize:
- Correctness and edge cases the author may have missed
- Whether tests prove the claimed behavior
- Clarity of commit messages and PR summary for a stranger
- Security: secrets, authz, least privilege in workflows
- Observability: PII in logs, missing failure signals (if instrumentation changed)

Respond with:
1. Blockers (merge-stopping)
2. Non-blocking suggestions
3. A short “what I would verify locally” checklist

Stay within the provided diff and linked docs. No speculative refactors outside the slice.
```

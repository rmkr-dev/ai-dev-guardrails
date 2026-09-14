# Refactor plan prompt (Copilot / Claude / Codex)

Use before a structural cleanup that is not a pure feature slice. Complements [agents/core.md](../agents/core.md) and [prompts/change-impact.md](change-impact.md).

```text
Propose a minimal refactor plan for this area of the codebase.

Constraints:
1. Prefer small, reviewable PRs over a big-bang rewrite
2. Keep behavior unchanged unless a bug is explicitly in scope
3. List tests that must pass before and after each step
4. Call out public API / schema / CLI surface risks
5. Do not invent frameworks or renames outside the stated goal

Output:
- Goal (one paragraph)
- Steps (ordered, each mergeable alone if possible)
- Risks / rollback
- Out of scope

No company names. No secrets.
```

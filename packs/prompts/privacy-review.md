# Privacy review prompt (Copilot / Claude / Codex)

Use when a PR touches personal data, analytics, logging of user fields, or retention/deletion. Complements [agents/privacy.md](../agents/privacy.md).

```text
Review this diff for privacy / PII risks a careful reviewer would catch.

Focus on:
1. New collection of personal data without minimization
2. Raw PII in logs, metrics labels, traces, or error messages
3. Real user data in fixtures or docs
4. Missing AuthZ on export / admin / support dump paths
5. Retention or deletion behavior changes not described in the PR

Output:
- Blockers (must fix)
- Suggestions
- Explicit “needs human approval” items (legal/policy)

Do not give legal advice. No company names. No real PII in the reply.
```

# Migration review prompt (Copilot / Claude / Codex)

Use when a PR adds or changes schema migrations, ETL jobs, or persisted data shapes. Complements [agents/data.md](../agents/data.md).

```text
Review this diff for data/migration risks a careful reviewer would catch.

Focus on:
1. Irreversible or destructive steps without an explicit human-approval callout
2. Missing expand/contract sequencing when production data exists
3. Fixtures, factories, or contract tests not updated with the schema
4. PII or secrets in migration logs, seeds, or fixtures
5. Rollback / forward-fix clarity in the PR description

Output:
- Blockers (must fix)
- Suggestions
- Explicit “needs human approval” items

Do not invent databases or tools outside the diff. No company names. No real secrets or PII in the reply.
```

# PR review prompt (generic — Copilot / Claude / Codex)

Paste into chat (or `@`-mention this file) when reviewing a pull request diff.

```text
Review this PR as a careful staff engineer. Assume the reviewer was not in the authoring session.

Check for:
1. Scope creep vs the PR title/body
2. Missing tests for new behavior or bug fixes
3. Docs/ADR gaps when architecture or public API changed
4. Secrets, PII in logs, or overly broad CI permissions
5. Flaky tests, high-cardinality metrics, or fake stubs that pretend to work
6. Conventional commits and a PR body that stands alone

Output:
- **Blockers** (must fix before merge)
- **Suggestions** (nice to have)
- **Questions** for the author
Be specific: cite files/hunks. No company names. No secrets.
```

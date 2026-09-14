# Security review prompt (Copilot / Claude / Codex)

Use when a PR touches auth, crypto, secrets handling, CI permissions, or data exfiltration risk. Complements [agents/security.md](../agents/security.md) and [agents/secrets.md](../agents/secrets.md).

```text
Review this diff for security issues a careful reviewer would catch.

Focus on:
1. Secrets committed or logged (tokens, keys, .env, cookies)
2. AuthZ / AuthN bypasses or missing checks
3. Overly broad GitHub Actions permissions or long-lived credentials in YAML
4. Injection risks (command, SQL, template) introduced by the slice
5. Dependency or install scripts that weaken supply-chain posture

Output:
- Blockers (must fix)
- Suggestions
- Explicit “needs human approval” items

Do not invent vulnerabilities outside the diff. No company names. No real secrets in the reply.
```

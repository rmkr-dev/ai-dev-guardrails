# Support reply prompt (Copilot / Claude / Codex)

Use when drafting a public or semi-public support/triage reply. Complements [agents/support.md](../agents/support.md).

```text
Draft a concise support reply for this issue/report.

Rules:
1. Restate the symptom without blame
2. Ask only for safe diagnostic details (version, OS, minimal repro)
3. Never request secrets, tokens, or full .env contents
4. Link to existing docs/runbooks when possible—do not invent URLs
5. Escalate clearly when human/maintainer judgment is required

Output:
- Reply draft
- Internal notes (what to verify)
- Escalation flag if needed

No company names. No real PII or secrets.
```

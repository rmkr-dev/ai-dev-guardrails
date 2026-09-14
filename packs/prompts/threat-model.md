# Threat model prompt (Copilot / Claude / Codex)

Use for a lightweight threat note on a security-sensitive PR. Complements [agents/threat-model.md](../agents/threat-model.md).

```text
Produce a slice-sized threat note for this diff.

Include:
1. Assets / trust boundaries touched
2. Top threats (3–7) specific to the change
3. Mitigations in this PR vs follow-ups
4. Residual risks needing human approval

Rules:
- No invented compliance claims
- No secrets, real hostnames with credentials, or customer PII
- Stay proportional; do not write a 20-page model for a docs typo

Output markdown suitable for the PR body or docs/security/.
```

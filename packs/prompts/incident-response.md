# Incident response prompt (Copilot / Claude / Codex)

Use during an active incident or when drafting the first incident note. Complements [agents/incidents.md](../agents/incidents.md).

```text
Given the symptom description, recent changes, and available signals (logs/metrics/traces if present), draft an incident response note.

Include:
1. Symptom and impact (no real customer names; no PII)
2. Current status (investigating / mitigated / resolved) — only if known
3. Timeline (UTC) of known facts
4. Immediate checks (read-only first)
5. Mitigation options ranked by blast radius
6. Open questions for the human on-call
7. Follow-ups to file after mitigation

Rules:
- Do not invent dashboards, alerts, or services that are not in the repo or provided context
- Do not include secrets, tokens, or private credentials
- Label speculation clearly
- No company names in examples
```

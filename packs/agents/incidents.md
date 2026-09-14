# Incident and runbook guardrails (Copilot / Claude / Codex)

Use with [core.md](core.md) and [observability.md](observability.md). For agents drafting incident notes, runbooks, or on-call playbooks.

## Defaults

- Prefer **actionable** steps over narrative essays. A runbook should tell the next person what to check and what to change.
- Separate **detection**, **mitigation**, **recovery**, and **follow-up**. Do not mix them into one unordered list.
- Never put secrets, tokens, private URLs with credentials, or customer PII into runbooks or incident write-ups.
- Link to real dashboards, alerts, and docs that exist in the consumer repo—do not invent URLs.

## When drafting a runbook

1. State the symptom a human would notice (alert name, user-visible failure, SLO burn).
2. List verification commands that are safe to run (read-only first).
3. Give mitigation that buys time, then recovery that restores the intended state.
4. Record ownership: who to page, which channel or issue tracker the consumer already uses (placeholders OK).

## When drafting incident notes

- Timeline with UTC timestamps; facts before speculation.
- Impact scope (who/what) without naming real customers or companies in examples.
- Root-cause hypothesis labeled as hypothesis until confirmed.
- Concrete follow-ups (tests, alerts, docs) suitable for tracked work items.

## Do not

- Paste production secrets “so the next person can debug faster”
- Recommend disabling auth, TLS, or backups as a first response
- Invent monitoring products the repo does not use
- Blame individuals in the permanent record

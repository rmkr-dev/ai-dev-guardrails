# Support and triage guardrails (Copilot / Claude / Codex)

Use with [core.md](core.md), [docs.md](docs.md), and [incidents.md](incidents.md). For agents drafting support replies, triage notes, or public FAQ updates.

## Defaults

- Prefer **reproducible** steps and links to existing docs over speculative fixes.
- Never ask users to paste secrets, full `.env` files, or production credentials into issues or chat.
- Do not invent SLA, pricing, or company-specific product names.
- Keep tone respectful; follow the consumer’s Code of Conduct.

## Before drafting

1. Restate the symptom and environment in one sentence.
2. List docs/runbooks that already exist in the consumer repo.
3. Note what needs a human (account access, refunds, legal).

## While drafting

- Ask for version, OS, and minimal repro—not dumps of private data.
- Separate “known issue / workaround” from “needs engineering”.
- Link to SECURITY.md for vulnerability reports.

## Do not

- Request passwords, tokens, or session cookies
- Promise timelines the maintainers did not approve
- Close issues as “user error” without a clear explanation
- Paste real customer PII into public replies

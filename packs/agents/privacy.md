# Privacy and PII guardrails (Copilot / Claude / Codex)

Use with [core.md](core.md), [secrets.md](secrets.md), and [observability.md](observability.md). For agents touching personal data, analytics, logs, or retention.

## Defaults

- Minimize collection: only fields the feature needs.
- Do not log raw PII (names, emails, phone numbers, government IDs, precise location) unless the consumer already has an approved redaction pattern—prefer IDs and hashes the repo already uses.
- Treat exports, support dumps, and fixtures as production-like: no real customer data in git.
- Do not invent GDPR/CCPA legal advice; document technical controls only and escalate legal questions to humans.

## Before coding

1. List personal data fields the change reads, writes, or transmits.
2. Identify retention / deletion hooks the consumer already has.
3. Note cross-border or third-party processors only if already in the repo’s docs—do not invent vendors.

## While coding

- Prefer tokenization / opaque IDs in logs and metrics labels.
- Keep access control on PII-bearing endpoints aligned with existing AuthZ patterns.
- Update fixtures with synthetic data only.
- Document retention or deletion behavior changes in the PR body.

## Slice checklist

- [ ] New fields justified (minimization)
- [ ] Logs/metrics avoid raw PII
- [ ] Fixtures are synthetic
- [ ] Deletion/export paths updated when data model grows
- [ ] Human approval called out for new processors or retention policy changes

## Do not

- Commit real user data “for debugging”
- Add unrestricted admin export without AuthZ review
- Silence privacy concerns as “follow-up” without a tracked item
- Paste real emails or phone numbers into examples

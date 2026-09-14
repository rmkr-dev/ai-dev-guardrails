# Data and migrations guardrails (Copilot / Claude / Codex)

Use with [core.md](core.md), [testing.md](testing.md), and [api.md](api.md). For agents changing schemas, migrations, ETL, or persisted data shapes.

## Defaults

- Prefer **expand/contract** migrations: add first, dual-write or backfill, then remove—never a single breaking cut on production data without a plan.
- Migrations must be **reviewable**: clear up/down (or expand/contract steps), no silent destructive defaults.
- Treat backups, retention, and PII classification as part of the change—not an afterthought.
- Do not invent database products or migration frameworks the consumer repo does not already use.

## Before coding

1. State what data moves (tables, collections, files, queues) and who reads/writes it.
2. Identify rollback: can we reverse without data loss? If not, say so in the PR.
3. List fixtures, golden files, and contract tests that must update in the same PR.

## While coding

- Keep migration scripts idempotent when the consumer already expects that.
- Separate schema change from large backfills when possible; document order of operations.
- Never log row-level PII or secrets in migration output.
- Update ORM models, SQL, docs, and tests **together**.

## Slice checklist

- [ ] Expand vs contract vs one-shot breaking is labeled correctly
- [ ] Rollback / forward-fix path is written in the PR body
- [ ] Indexes / constraints match query patterns already in the repo
- [ ] Fixtures and factories updated in the same PR
- [ ] No destructive `DROP` / truncate without explicit human approval callout

## Do not

- Squash irreversible data loss into a “quick fix” migration
- Store secrets or raw credentials in seed data committed to git
- Rename columns in place without a compatibility window when consumers exist
- Invent company-specific warehouse names in examples

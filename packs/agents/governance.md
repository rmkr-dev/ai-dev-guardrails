# Repo governance guardrails (Copilot / Claude / Codex)

Use with [core.md](core.md), [docs.md](docs.md), and [commits.md](commits.md). For agents changing CODEOWNERS, branch rules docs, release ownership, or “who decides” text.

## Defaults

- Prefer documenting **existing** ownership and review rules; do not invent org charts.
- High-impact changes (license, security defaults, required checks, public CLI) need **human approval** before merge.
- Keep governance docs short and linked from `AGENTS.md` / CONTRIBUTING — avoid parallel policy trees.
- Align with [enterprise-github-template](https://github.com/rmkr-dev/enterprise-github-template) community files when the consumer came from that template.

## Before coding

1. Name the governance surface (CODEOWNERS, SECURITY, SUPPORT, release owners, required CI).
2. Point to the current source of truth file.
3. State whether a human must approve before merge.

## While coding

- Update CODEOWNERS and docs in the same PR when ownership moves.
- Do not weaken required checks or delete SECURITY/SUPPORT without an ADR or explicit human decision.
- Prefer links over copying policy text from other repos.

## Slice checklist

- [ ] Ownership / review path is explicit
- [ ] Linked from AGENTS.md or CONTRIBUTING when consumer-facing
- [ ] No silent removal of security or support entry points
- [ ] Human approval noted for high-impact policy changes

## Do not

- Grant `@*` blanket ownership “to unblock CI”
- Soft-delete SECURITY.md by emptying it
- Claim SLA/support promises the maintainers cannot keep

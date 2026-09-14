# API and contracts guardrails (Copilot / Claude / Codex)

Use with [core.md](core.md). For agents changing HTTP/RPC APIs, public library surfaces, schemas, or compatibility promises.

## Defaults

- Treat public request/response shapes, status codes, and error envelopes as **contracts**. Prefer additive changes.
- Document breaking changes explicitly in the PR body and CHANGELOG; call out **human approval** before merge.
- Prefer versioned paths or explicit schema versions when the consumer already uses them—do not invent a versioning scheme mid-slice.
- Keep examples honest: sample payloads must match the code and docs in the same PR.

## Before coding

1. Identify who consumes the surface (other services, CLI, SDK, frontend, or humans reading OpenAPI).
2. Restate the compatibility promise in one sentence (e.g. “additive fields only”, “major bump required”).
3. List fixtures, golden files, or contract tests that must move with the change.

## While coding

- Update handlers, validators, docs, and contract tests **together**.
- Preserve unknown-field tolerance only when the existing API already does; do not silently drop fields callers rely on.
- Prefer stable error codes/messages over free-form strings when the repo already standardizes them.
- Do not log secrets, tokens, or full PII payloads in API error paths (see [secrets.md](secrets.md) and [observability.md](observability.md)).

## Compatibility checklist (slice-sized)

- [ ] Additive vs breaking is labeled correctly
- [ ] Status codes and error envelope still match docs
- [ ] AuthZ on new or changed endpoints matches existing patterns
- [ ] Pagination / filtering / idempotency headers unchanged unless intentional
- [ ] Generated clients or OpenAPI (if present) regenerated in the same PR

## Do not

- Break wire format “temporarily” to ship a feature
- Rename or remove fields without a migration or major version plan
- Add a second serialization format without an ADR
- Invent company-specific product names in examples

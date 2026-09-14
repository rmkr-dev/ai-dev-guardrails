# Security guardrails (Copilot / Claude / Codex)

Use alongside [core.md](core.md). Aimed at coding agents and human reviewers.

## Defaults

- **No secrets in git:** credentials, API keys, tokens, private keys, session cookies, or `.env` with real values.
- **Least privilege:** workflow `permissions`, cloud roles, and tokens should be the minimum needed for the slice.
- **Safe examples:** use placeholders like `YOUR_TOKEN_HERE` or clearly fake values; never paste live credentials “for illustration.”
- **Dependency caution:** prefer pinned or lockfiled dependencies; do not add packages without a reason in the PR.

## When changing auth, crypto, or data handling

1. Call out the change explicitly in the PR for **human approval**.
2. Prefer well-known libraries over hand-rolled crypto.
3. Document threat-relevant behavior in the consumer’s security docs when those docs exist.
4. Do not weaken TLS, signature checks, or authorization “temporarily.”

## CI and automation

- Prefer GitHub Actions with explicit `permissions`.
- Do not embed long-lived secrets in workflow YAML.
- Dependabot (or equivalent) for Actions and language ecosystems when the consumer repo supports it.

## Reporting

Follow the consumer repository’s `SECURITY.md`. If none exists, recommend adding one before handling vulnerability reports in public issues.

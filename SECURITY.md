# Security policy

## Supported versions

Security fixes apply to the default branch (`main`) of **ai-dev-guardrails**. Consumers who copied pack modules should review upstream changes and apply them intentionally.

## Reporting a vulnerability

Please report security issues privately via GitHub Security Advisories for this repository:

1. Open **Security** → **Advisories** → **New draft security advisory** on `rmkr-dev/ai-dev-guardrails`, or
2. Use **Report a vulnerability** if that button is enabled on the repo’s Security tab.

Do **not** open a public issue for vulnerabilities that could affect pack consumers (for example unsafe example commands or leaked secret patterns).

Include:

- A short description of the issue and impact
- Steps to reproduce (against this repository)
- Any suggested fix

You should receive an acknowledgment within a reasonable time. Coordinated disclosure is preferred.

## Scope notes

- Do not send secrets, tokens, or personal data in reports.
- Contact is GitHub-only via `@rmkr-dev` / this repository’s advisory flow — no email addresses are published here.
- Application security for **consumer** products is owned by those repositories; this policy covers the pack distributor and validator CLI.

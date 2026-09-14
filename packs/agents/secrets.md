# Secrets guardrails (Copilot / Claude / Codex)

Use with [security.md](security.md). Short, high-priority rules for agents.

## Never commit

- API keys, tokens, passwords, private keys, session cookies
- `.env` files with real values (use `.env.example` with placeholders)
- Cloud credential files (`credentials.json`, kubeconfigs with secrets)

## Prefer

- Placeholders: `YOUR_TOKEN_HERE`, `op://…` references, or CI secrets
- Short-lived OIDC / workload identity when the consumer platform supports it
- Redacting secrets from logs, screenshots, and PR bodies

## If a secret may have leaked

1. Stop and flag for a **human**
2. Rotate the credential
3. Follow the consumer `SECURITY.md` / advisory flow
4. Do not discuss the live secret value in the PR

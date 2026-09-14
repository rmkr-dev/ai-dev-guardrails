# Dependency guardrails (Copilot / Claude / Codex)

Use with [core.md](core.md). For agents adding or upgrading libraries and Actions.

## Defaults

- Prefer the package manager and lockfile style the repo already uses.
- Add a dependency only when the slice needs it; say why in the PR body.
- Prefer well-maintained libraries over hand-rolled crypto, HTTP clients, or YAML parsers when equivalents exist.
- Keep Python-only defaults in this ecosystem: **do not add Node/npm** unless the consumer repo already depends on it and the slice requires it.

## Upgrades

- Prefer Dependabot (or the repo’s existing updater) for routine bumps.
- Group unrelated major upgrades into their own PR when risk is high.
- Run the repo’s test suite after upgrades; do not dismiss failures as “unrelated” without checking.

## Supply chain hygiene

- Do not commit vendored tarballs of secrets or credentials.
- Pin Actions to a full SHA or a maintained major tag per repo convention.
- Avoid `curl | sh` installers in CI without human approval.

## Do not

- Expand `permissions` in workflows to make a dependency “easier”
- Check in `.env` files required by a new SDK
- Introduce a second package manager for convenience

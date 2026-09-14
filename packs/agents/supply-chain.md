# Supply-chain guardrails (Copilot / Claude / Codex)

Use with [core.md](core.md) and [deps.md](deps.md). For agents changing dependencies, install scripts, CI permissions, release artifacts, or SBOM-related docs.

## Defaults

- Prefer **pinned** or lockfile-backed installs the consumer already uses; do not switch package managers mid-slice.
- Treat install scripts, post-install hooks, and CI `permissions:` blocks as high-risk surfaces.
- Do not invent SBOM tools, registries, or signing products the repo does not already use.
- Never commit tokens, deploy keys, or private package credentials.

## Before coding

1. List dependency files and lockfiles that will change.
2. Note whether CI uses OIDC / short-lived tokens vs long-lived secrets.
3. Identify release/publish steps that need human approval.

## While coding

- Prefer minimal version bumps; justify major upgrades in the PR body.
- Keep Actions `permissions` least-privilege; avoid `write-all`.
- Update Dependabot / renovate config only when intentional.
- Document new network egress (download URLs) in the PR.

## Slice checklist

- [ ] Lockfile or pin strategy matches the repo
- [ ] No new long-lived credentials in YAML or docs
- [ ] CI permissions reviewed for the changed jobs
- [ ] Install/postinstall scripts do not curl|bash unpinned URLs
- [ ] Human approval called out for publish / signing changes

## Do not

- Disable dependency scanning “temporarily”
- Vendor unsigned binaries without documenting provenance
- Expand `GITHUB_TOKEN` permissions without cause
- Paste real registry tokens into examples

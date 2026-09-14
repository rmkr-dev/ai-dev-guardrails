# CI guardrails (Copilot / Claude / Codex)

Use with [core.md](core.md) when changing workflows or required checks.

## Defaults

- Prefer **GitHub Actions** and explicit `permissions:` (least privilege).
- Prefer reusable workflows from a known pin (for example `python-ci@v0.2.0`) over copy-pasting large job YAML.
- Keep the default pipeline viable on **GitHub Free** (no paid-only required features).
- Do not embed long-lived secrets in workflow files.

## When editing workflows

1. Say what the job guarantees (compile, unit tests, packaging).
2. Update docs that mention CI in the same PR.
3. Do not add badges for workflows that are not configured.
4. Flag required-check changes for human approval.

## Do not

- Disable failing checks to merge
- Broaden `permissions` to `write-all` without justification
- Introduce a second CI system without an ADR

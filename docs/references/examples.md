# Examples: copying packs into a repo

How to install **ai-dev-guardrails** modules into a consumer repository for Copilot, Claude, or Codex. Copy-based; no required submodule.


## Install script

Preferred path for new consumers:

```bash
bash scripts/install-packs.sh /path/to/consumer-repo --profile baseline
# or: api | ops | full
```

Full options and AGENTS.md wiring: [install.md](install.md).

## Minimal install

1. Create or open the consumer repo’s root `AGENTS.md`.
2. Copy useful sections from:
   - [`packs/agents/core.md`](../../packs/agents/core.md)
   - [`packs/agents/security.md`](../../packs/agents/security.md) (if auth/secrets/CI permissions apply)
   - [`packs/agents/testing.md`](../../packs/agents/testing.md) and [`packs/agents/docs.md`](../../packs/agents/docs.md) as needed
   - [`packs/agents/observability.md`](../../packs/agents/observability.md) when adding logs, metrics, or health probes
   - [`packs/agents/ci.md`](../../packs/agents/ci.md) when editing workflows
3. Optionally keep the full files under `docs/guardrails/` or `packs/` in the consumer tree and link them from `AGENTS.md`.

```bash
# from a clone of ai-dev-guardrails
mkdir -p "$TARGET/docs/guardrails"
cp packs/agents/core.md packs/agents/security.md "$TARGET/docs/guardrails/"
cp packs/agents/testing.md packs/agents/observability.md "$TARGET/docs/guardrails/"
cp packs/checklists/definition-of-done.md "$TARGET/docs/guardrails/"
cp packs/prompts/change-impact.md "$TARGET/docs/guardrails/"
```

Then add a short pointer in the consumer `AGENTS.md`:

```markdown
## Guardrail packs

- [Core](docs/guardrails/agents/core.md)
- [Security](docs/guardrails/agents/security.md)
- [Testing](docs/guardrails/agents/testing.md)
- [Observability](docs/guardrails/agents/observability.md)
- [Definition of Done](docs/guardrails/checklists/definition-of-done.md)
- [Change impact prompt](docs/guardrails/prompts/change-impact.md)
```

## Definition of Done in PRs

Copy checklist items from [`packs/checklists/definition-of-done.md`](../../packs/checklists/definition-of-done.md) into `.github/PULL_REQUEST_TEMPLATE.md`, or link the file from the template.

## Change-impact prompt

Before a large edit, paste [`packs/prompts/change-impact.md`](../../packs/prompts/change-impact.md) into the Copilot / Claude / Codex chat (or `@`-mention the file when the tool allows).

## Testing + observability slices

When a PR adds behavior **and** instrumentation:

1. Follow [`packs/agents/testing.md`](../../packs/agents/testing.md) for same-PR coverage.
2. Follow [`packs/agents/observability.md`](../../packs/agents/observability.md) so failure paths are visible without logging secrets.
3. Ask the agent: “List missing edge cases and any PII or high-cardinality risk in this diff.”

## Optional validator in consumer CI

After installing this package (editable path, vendored wheel, or a future PyPI release):

```bash
python -m pip install -e /path/to/ai-dev-guardrails"[dev]"
ai-guardrails check .
```

Example job fragment using the reusable Python CI workflow from `rmkr-dev/gha-reusable-workflows` (consumer-owned):

```yaml
# .github/workflows/ci.yml
name: CI
on:
  push:
    branches: [main]
  pull_request:

permissions:
  contents: read

jobs:
  python:
    uses: rmkr-dev/gha-reusable-workflows/.github/workflows/python-ci.yml@v0.4.0
    with:
      working-directory: .
      python-version: "3.12"
```

Add a step in a custom workflow if you need `ai-guardrails check` explicitly beyond pytest.

## Testing and observability checklists

Copy into PR templates or link from `AGENTS.md`:

- [`packs/checklists/testing.md`](../../packs/checklists/testing.md)
- [`packs/checklists/observability.md`](../../packs/checklists/observability.md)

```bash
cp packs/checklists/testing.md packs/checklists/observability.md \
   "$TARGET/docs/guardrails/"
```

Use alongside the agent modules:

- [`packs/agents/testing.md`](../../packs/agents/testing.md)
- [`packs/agents/observability.md`](../../packs/agents/observability.md)

## PR review prompts (Copilot / Claude / Codex)

Copy or `@`-mention the tool-specific prompt when reviewing a PR:

| Tool | Prompt |
| --- | --- |
| Any | [`packs/prompts/pr-review.md`](../../packs/prompts/pr-review.md) |
| GitHub Copilot | [`packs/prompts/pr-review-copilot.md`](../../packs/prompts/pr-review-copilot.md) |
| Claude | [`packs/prompts/pr-review-claude.md`](../../packs/prompts/pr-review-claude.md) |
| Codex | [`packs/prompts/pr-review-codex.md`](../../packs/prompts/pr-review-codex.md) |

```bash
mkdir -p "$TARGET/docs/guardrails"
cp packs/prompts/pr-review.md \
   packs/prompts/pr-review-copilot.md \
   packs/prompts/pr-review-claude.md \
   packs/prompts/pr-review-codex.md \
   "$TARGET/docs/guardrails/"
```

## Dependencies pack

When adding libraries or Actions, copy [`packs/agents/deps.md`](../../packs/agents/deps.md) beside other agent modules and link it from `AGENTS.md`. Prefer Dependabot for routine bumps; keep the consumer on a single package manager.

## Test plan prompt

Paste [`packs/prompts/test-plan.md`](../../packs/prompts/test-plan.md) when filling the PR Test plan section (works with Copilot, Claude, or Codex).

## Sample AGENTS.md

See [`sample-agents-md.md`](sample-agents-md.md) for a copy-paste consumer template that links core packs and prompts (including security review).

## Security review prompt

When a PR touches auth, secrets, or CI permissions, paste [`packs/prompts/security-review.md`](../../packs/prompts/security-review.md) into Copilot / Claude / Codex.

## Pack matrix

Use [`pack-matrix.md`](pack-matrix.md) to choose which modules to copy for a given consumer repo.

## Validator check catalog

Full list of default presence checks: [`validator-checks.md`](validator-checks.md).

## Release notes prompt

Paste [`packs/prompts/release-notes.md`](../../packs/prompts/release-notes.md) when drafting a GitHub Release from CHANGELOG.


## API / contracts pack

When changing public HTTP/RPC surfaces, schemas, or library APIs, copy [`packs/agents/api.md`](../../packs/agents/api.md) beside other agent modules and link it from `AGENTS.md`. Keep handlers, docs, and contract tests in the same PR.

```bash
cp packs/agents/api.md "$TARGET/docs/guardrails/"
```


## Incident / runbook packs

For on-call notes and operational playbooks:

```bash
cp packs/agents/incidents.md    packs/prompts/incident-response.md    packs/prompts/runbook-draft.md    "$TARGET/docs/guardrails/"
```

Paste [`packs/prompts/incident-response.md`](../../packs/prompts/incident-response.md) during an active incident; use [`packs/prompts/runbook-draft.md`](../../packs/prompts/runbook-draft.md) when writing durable runbooks. Follow [`packs/agents/incidents.md`](../../packs/agents/incidents.md) for structure and no-secrets rules.

## Complements, not duplicates

| Repo | Use instead when you need |
| --- | --- |
| [enterprise-github-template](https://github.com/rmkr-dev/enterprise-github-template) | Full template (issues, CodeQL, release, ops docs) |
| [llm-eval-harness](https://github.com/rmkr-dev/llm-eval-harness) | Offline golden-fixture LLM eval |
| **ai-dev-guardrails** (this repo) | Agent/human pack modules + light hygiene CLI |

## Accessibility slices

When a PR changes UI, docs sites, or CLI help:

1. Follow [`packs/agents/a11y.md`](../../packs/agents/a11y.md).
2. Run through [`packs/checklists/accessibility.md`](../../packs/checklists/accessibility.md).
3. Ask the agent: “List keyboard and accessible-name gaps in this diff.”

## Data / migration slices

When a PR changes schemas or migrations:

```bash
bash scripts/install-packs.sh "$TARGET" --profile data
```

1. Follow [`packs/agents/data.md`](../../packs/agents/data.md).
2. Paste [`packs/prompts/migration-review.md`](../../packs/prompts/migration-review.md) into the review chat.

## Supply-chain slices

When a PR changes dependencies, CI permissions, or publish steps:

1. Follow [`packs/agents/supply-chain.md`](../../packs/agents/supply-chain.md) and [`packs/agents/deps.md`](../../packs/agents/deps.md).
2. Run through [`packs/checklists/supply-chain.md`](../../packs/checklists/supply-chain.md).

## Privacy slices

When a PR touches personal data, analytics, or retention:

1. Follow [`packs/agents/privacy.md`](../../packs/agents/privacy.md).
2. Paste [`packs/prompts/privacy-review.md`](../../packs/prompts/privacy-review.md) into the review chat.

## Local Makefile helpers

In this repository (and consumers who copy the pattern):

```bash
make lint
make fmt
```

`lint` runs `compileall` plus pytest collection; `fmt` is a placeholder until a formatter is adopted.

## Internationalization slices

When a PR changes user-visible copy or locales:

1. Follow [`packs/agents/i18n.md`](../../packs/agents/i18n.md).
2. Run through [`packs/checklists/i18n.md`](../../packs/checklists/i18n.md).

## Threat modeling slices

When a PR touches auth, crypto, CI permissions, or sensitive data paths:

1. Follow [`packs/agents/threat-model.md`](../../packs/agents/threat-model.md).
2. Paste [`packs/prompts/threat-model.md`](../../packs/prompts/threat-model.md) into the drafting chat.

## Security profile install

```bash
bash scripts/install-packs.sh "$TARGET" --profile security
```

Installs security/secrets/privacy/threat-model agents plus matching review prompts on top of baseline.

## Using with enterprise-github-template

When the consumer repo came from [enterprise-github-template](https://github.com/rmkr-dev/enterprise-github-template):

```bash
bash scripts/install-packs.sh /path/to/template-derived-repo --profile baseline
```

Keep the template `AGENTS.md` and link packs under `docs/guardrails/`. Full pairing notes: [enterprise-github-template.md](enterprise-github-template.md).

## Nested install layout (v0.3+)

`install-packs.sh` preserves `agents/`, `checklists/`, and `prompts/` under the destination so same-basename modules do not collide. Link the nested paths from `AGENTS.md` (see [install.md](install.md)). Flat 0.2.x leftover `*.md` at the destination root are warned on install and `--dry-run` (not deleted); see [migrate-nested-install.md](migrate-nested-install.md).


# Examples: copying packs into a repo

How to install **ai-dev-guardrails** modules into a consumer repository for Copilot, Claude, or Codex. Copy-based; no required submodule.

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

- [Core](docs/guardrails/core.md)
- [Security](docs/guardrails/security.md)
- [Testing](docs/guardrails/testing.md)
- [Observability](docs/guardrails/observability.md)
- [Definition of Done](docs/guardrails/definition-of-done.md)
- [Change impact prompt](docs/guardrails/change-impact.md)
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
    uses: rmkr-dev/gha-reusable-workflows/.github/workflows/python-ci.yml@v0.2.0
    with:
      working-directory: .
      python-version: "3.12"
```

Add a step in a custom workflow if you need `ai-guardrails check` explicitly beyond pytest.

## Complements, not duplicates

| Repo | Use instead when you need |
| --- | --- |
| [enterprise-github-template](https://github.com/rmkr-dev/enterprise-github-template) | Full template (issues, CodeQL, release, ops docs) |
| [llm-eval-harness](https://github.com/rmkr-dev/llm-eval-harness) | Offline golden-fixture LLM eval |
| **ai-dev-guardrails** (this repo) | Agent/human pack modules + light hygiene CLI |

# ai-dev-guardrails

Installable AI+human engineering guardrails for **GitHub Copilot**, **Claude**, and **Codex**: `AGENTS.md` modules, Definition of Done checklists, change-impact prompts, ADR/diagram conventions, and an optional Python validator for repo hygiene.

Complements [llm-eval-harness](https://github.com/rmkr-dev/llm-eval-harness) and [enterprise-github-template](https://github.com/rmkr-dev/enterprise-github-template) without duplicating them.

## Status

**v0.1.3** — see [CHANGELOG.md](CHANGELOG.md).

## Packs

See [packs/README.md](packs/README.md) and [docs/references/examples.md](docs/references/examples.md).

## Validator CLI

```bash
python -m pip install -e ".[dev]"
ai-guardrails list-checks
ai-guardrails check .
pytest -q
```

Default checks: `agents_md`, `readme`, `architecture_docs`, `tests_or_ci`, `license`, `security_md`, `codeowners`, `contributing`.

## CI

`.github/workflows/ci.yml` uses `rmkr-dev/gha-reusable-workflows` `python-ci@v0.2.0`.

## License

MIT — see [LICENSE](LICENSE).

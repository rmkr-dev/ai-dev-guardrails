# ai-dev-guardrails

Installable AI+human engineering guardrails for **GitHub Copilot**, **Claude**, and **Codex**.

Complements [llm-eval-harness](https://github.com/rmkr-dev/llm-eval-harness) and [enterprise-github-template](https://github.com/rmkr-dev/enterprise-github-template).

## Status

**v0.1.4** — see [CHANGELOG.md](CHANGELOG.md). Packs index: [packs/README.md](packs/README.md). Examples: [docs/references/examples.md](docs/references/examples.md).

## Validator

```bash
python -m pip install -e ".[dev]"
ai-guardrails list-checks
ai-guardrails check .
pytest -q
```

Nine default checks including `gitignore`.

## CI

`python-ci@v0.2.0` via `rmkr-dev/gha-reusable-workflows`.

## License

MIT — see [LICENSE](LICENSE).

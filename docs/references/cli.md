# CLI reference (`ai-guardrails`)

Optional validator installed from this repo (`pip install -e ".[dev]"`).

## Commands

### `ai-guardrails check PATH`

Run the default presence checks against `PATH`.

| Option | Default | Meaning |
| --- | --- | --- |
| `--strict` / `--no-strict` | `--strict` | Exit `1` if any check fails |
| `--format text\|json` | `text` | Human lines or JSON document |
| `--only name,name` | *(all)* | Run only these check names |
| `--skip name,name` | *(none)* | Omit these check names |

JSON shape: `root`, `passed`, `failed`, `total`, `checks[{name,ok,detail}]`.

Examples:

```bash
ai-guardrails check . --only readme,license,agents_md
ai-guardrails check . --skip funding,citation
ai-guardrails check . --format json --only readme
```

### `ai-guardrails list-checks`

Print check names in run order.

| Option | Default | Meaning |
| --- | --- | --- |
| `--format text\|json` | `text` | One name per line, or `{"checks":[...],"total":N}` |

### Version

`ai-guardrails --version`

## See also

- [validator-checks.md](validator-checks.md)
- [development.md](../development/development.md)

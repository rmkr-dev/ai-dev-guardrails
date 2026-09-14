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

Unknown names in `--only` / `--skip` error with close-match suggestions.
| `--fail-only` | off | Text mode: print only failing checks (summary still shown) |

JSON shape: `version`, `root`, `passed`, `failed`, `total`, `checks[{name,ok,detail}]`.

Examples:

```bash
ai-guardrails check . --only readme,license,agents_md
ai-guardrails check . --skip funding,citation
ai-guardrails check . --format json --only readme
ai-guardrails check . --no-strict   # report failures, still exit 0
ai-guardrails check . --fail-only   # text: failures only + summary
```

### `ai-guardrails list-checks`

Print check names in run order.

| Option | Default | Meaning |
| --- | --- | --- |
| `--format text\|json` | `text` | One name per line, or `{"checks":[...],"total":N}` |
| `--describe` / `--no-describe` | `--no-describe` | Include short summaries (text: `name — summary`; json: objects) |

### `ai-guardrails profiles`

Print install profile pack lists (mirrors `scripts/install-packs.sh --list-profiles`).

| Option | Default | Meaning |
| --- | --- | --- |
| `--format text\|json` | `text` | Human catalog or JSON |
| `--profile NAME` | *(all)* | Restrict to one profile |

Text mode prints `(N packs)` per named profile. JSON adds a sibling `counts` map (`null` for `full`); `profiles` values stay list-or-string for compatibility.

```bash
ai-guardrails list-checks --describe
ai-guardrails list-checks --describe --format json
```

### Version

`ai-guardrails --version`

## See also

- [validator-checks.md](validator-checks.md) — check catalog (kept in sync via `test_catalog_sync`)
- [profiles.md](profiles.md) / [install.md](install.md) — pack install profiles (`scripts/install-packs.sh`)
- [migrate-nested-install.md](migrate-nested-install.md) — flat 0.2.x → nested layout
- [development.md](../development/development.md)

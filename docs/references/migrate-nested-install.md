# Migrating to nested install layout (v0.3+)

Before **v0.3.0**, `scripts/install-packs.sh` copied every pack to a **flat** basename under the destination (for example `docs/guardrails/core.md`). Same-basename pairs such as `agents/resilience.md` and `checklists/resilience.md` overwrote each other.

From **v0.3.0**, installs preserve category folders:

```text
docs/guardrails/
  INSTALL_MANIFEST.txt
  agents/core.md
  agents/cost.md
  checklists/cost.md
  prompts/...
```

## Steps

1. Re-run the installer (same profile as before):

```bash
bash scripts/install-packs.sh /path/to/consumer-repo --profile ops
# preview: add --dry-run
```

2. Update `AGENTS.md` (and PR templates) to the nested paths:

| Old (flat) | New (nested) |
| --- | --- |
| `docs/guardrails/core.md` | `docs/guardrails/agents/core.md` |
| `docs/guardrails/definition-of-done.md` | `docs/guardrails/checklists/definition-of-done.md` |
| `docs/guardrails/change-impact.md` | `docs/guardrails/prompts/change-impact.md` |

3. Remove leftover flat copies if both exist (optional cleanup after verifying links).

4. Confirm `docs/guardrails/INSTALL_MANIFEST.txt` lists nested destinations.

## See also

- [install.md](install.md)
- [ADR-007](../decisions/ADR-007-v0.3-install-layout-and-suite.md)
- [enterprise-github-template.md](enterprise-github-template.md)

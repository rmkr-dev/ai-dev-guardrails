# Migrating to nested install layout (v0.3+)

Before **v0.3.0**, `scripts/install-packs.sh` copied every pack to a **flat** basename under the destination (for example `docs/guardrails/core.md`). Same-basename pairs such as `agents/resilience.md` and `checklists/resilience.md` overwrote each other.

From **v0.3.0**, installs preserve category folders:

```text
docs/guardrails/
  INSTALL_MANIFEST.txt
  agents/core.md
  agents/cost.md
  checklists/cost.md
  prompts/change-impact.md
  ...
```

## Steps

1. Re-run the installer (same profile as before):

```bash
bash scripts/install-packs.sh /path/to/consumer-repo --profile ops
# preview: add --dry-run
# Makefile: make install-packs TARGET=/path/to/consumer-repo PROFILE=ops DRY_RUN=1
```

2. Update `AGENTS.md` (and PR templates) to the nested paths. Common mappings:

| Old (flat) | New (nested) |
| --- | --- |
| `docs/guardrails/core.md` | `docs/guardrails/agents/core.md` |
| `docs/guardrails/security.md` | `docs/guardrails/agents/security.md` |
| `docs/guardrails/secrets.md` | `docs/guardrails/agents/secrets.md` |
| `docs/guardrails/testing.md` | `docs/guardrails/agents/testing.md` |
| `docs/guardrails/docs.md` | `docs/guardrails/agents/docs.md` |
| `docs/guardrails/commits.md` | `docs/guardrails/agents/commits.md` |
| `docs/guardrails/api.md` | `docs/guardrails/agents/api.md` |
| `docs/guardrails/deps.md` | `docs/guardrails/agents/deps.md` |
| `docs/guardrails/observability.md` | `docs/guardrails/agents/observability.md` |
| `docs/guardrails/incidents.md` | `docs/guardrails/agents/incidents.md` |
| `docs/guardrails/cost.md` | `docs/guardrails/agents/cost.md` **or** `checklists/cost.md` (pick by content) |
| `docs/guardrails/resilience.md` | `docs/guardrails/agents/resilience.md` **or** `checklists/resilience.md` |
| `docs/guardrails/definition-of-done.md` | `docs/guardrails/checklists/definition-of-done.md` |
| `docs/guardrails/pr-self-review.md` | `docs/guardrails/checklists/pr-self-review.md` |
| `docs/guardrails/change-impact.md` | `docs/guardrails/prompts/change-impact.md` |
| `docs/guardrails/pr-body.md` | `docs/guardrails/prompts/pr-body.md` |
| `docs/guardrails/pr-review.md` | `docs/guardrails/prompts/pr-review.md` |
| `docs/guardrails/test-plan.md` | `docs/guardrails/prompts/test-plan.md` |
| `docs/guardrails/security-review.md` | `docs/guardrails/prompts/security-review.md` |
| `docs/guardrails/incident-response.md` | `docs/guardrails/prompts/incident-response.md` |
| `docs/guardrails/runbook-draft.md` | `docs/guardrails/prompts/runbook-draft.md` |

Ambiguous flat names that existed in both `agents/` and `checklists/` (for example `cost`, `resilience`, `accessibility`/`a11y`) may have been whichever file won last. Prefer reinstalling the profile and linking the nested paths from [sample-agents-md.md](sample-agents-md.md).

3. Remove leftover flat copies if both exist (optional cleanup after verifying links):

```bash
# From the consumer repo — only after AGENTS.md points at nested paths
DEST=docs/guardrails
# Example: remove flat core.md when agents/core.md exists
for f in "$DEST"/*.md; do
  [ -f "$f" ] || continue
  base=$(basename "$f")
  if [ -f "$DEST/agents/$base" ] || [ -f "$DEST/checklists/$base" ] || [ -f "$DEST/prompts/$base" ]; then
    echo "flat leftover (safe to delete after link check): $f"
  fi
done
```

4. Confirm `docs/guardrails/INSTALL_MANIFEST.txt` lists nested destinations (`agents/...`, `checklists/...`, `prompts/...`).

5. Re-run consumer checks if you use the optional validator:

```bash
ai-guardrails check .
```

## See also

- [install.md](install.md)
- [sample-agents-md.md](sample-agents-md.md)
- [ADR-007](../decisions/ADR-007-v0.3-install-layout-and-suite.md)
- [enterprise-github-template.md](enterprise-github-template.md)

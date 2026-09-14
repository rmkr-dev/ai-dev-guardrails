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

2. Update `AGENTS.md` (and PR templates) to the nested paths.

### Unambiguous agents (flat basename → `agents/`)

| Old (flat) | New (nested) |
| --- | --- |
| `docs/guardrails/core.md` | `docs/guardrails/agents/core.md` |
| `docs/guardrails/security.md` | `docs/guardrails/agents/security.md` |
| `docs/guardrails/secrets.md` | `docs/guardrails/agents/secrets.md` |
| `docs/guardrails/testing.md` | `docs/guardrails/agents/testing.md` **or** `checklists/testing.md` (pick by content) |
| `docs/guardrails/docs.md` | `docs/guardrails/agents/docs.md` |
| `docs/guardrails/commits.md` | `docs/guardrails/agents/commits.md` |
| `docs/guardrails/api.md` | `docs/guardrails/agents/api.md` |
| `docs/guardrails/deps.md` | `docs/guardrails/agents/deps.md` |
| `docs/guardrails/observability.md` | `docs/guardrails/agents/observability.md` **or** `checklists/observability.md` |
| `docs/guardrails/incidents.md` | `docs/guardrails/agents/incidents.md` |
| `docs/guardrails/ci.md` | `docs/guardrails/agents/ci.md` |
| `docs/guardrails/performance.md` | `docs/guardrails/agents/performance.md` |
| `docs/guardrails/privacy.md` | `docs/guardrails/agents/privacy.md` |
| `docs/guardrails/data.md` | `docs/guardrails/agents/data.md` |
| `docs/guardrails/frontend.md` | `docs/guardrails/agents/frontend.md` **or** `checklists/frontend.md` |
| `docs/guardrails/i18n.md` | `docs/guardrails/agents/i18n.md` **or** `checklists/i18n.md` |
| `docs/guardrails/supply-chain.md` | `docs/guardrails/agents/supply-chain.md` **or** `checklists/supply-chain.md` |
| `docs/guardrails/threat-model.md` | `docs/guardrails/agents/threat-model.md` **or** `prompts/threat-model.md` |
| `docs/guardrails/support.md` | `docs/guardrails/agents/support.md` |
| `docs/guardrails/governance.md` | `docs/guardrails/agents/governance.md` |
| `docs/guardrails/a11y.md` | `docs/guardrails/agents/a11y.md` (checklist twin is `accessibility.md`, see below) |

### Checklists without matching agent basename

| Old (flat) | New (nested) |
| --- | --- |
| `docs/guardrails/definition-of-done.md` | `docs/guardrails/checklists/definition-of-done.md` |
| `docs/guardrails/pr-self-review.md` | `docs/guardrails/checklists/pr-self-review.md` |
| `docs/guardrails/release.md` | `docs/guardrails/checklists/release.md` |
| `docs/guardrails/accessibility.md` | `docs/guardrails/checklists/accessibility.md` (agent twin is `a11y.md`) |

### Ambiguous same-basename pairs (agents + checklists)

Prefer reinstalling the profile; link **both** nested paths when the profile installs both.

| Flat leftover | Nested agents | Nested checklists |
| --- | --- | --- |
| `cost.md` | `agents/cost.md` | `checklists/cost.md` |
| `resilience.md` | `agents/resilience.md` | `checklists/resilience.md` |
| `testing.md` | `agents/testing.md` | `checklists/testing.md` |
| `observability.md` | `agents/observability.md` | `checklists/observability.md` |
| `frontend.md` | `agents/frontend.md` | `checklists/frontend.md` |
| `i18n.md` | `agents/i18n.md` | `checklists/i18n.md` |
| `supply-chain.md` | `agents/supply-chain.md` | `checklists/supply-chain.md` |

### Prompts

| Old (flat) | New (nested) |
| --- | --- |
| `docs/guardrails/change-impact.md` | `docs/guardrails/prompts/change-impact.md` |
| `docs/guardrails/pr-body.md` | `docs/guardrails/prompts/pr-body.md` |
| `docs/guardrails/pr-review.md` | `docs/guardrails/prompts/pr-review.md` |
| `docs/guardrails/pr-review-copilot.md` | `docs/guardrails/prompts/pr-review-copilot.md` |
| `docs/guardrails/pr-review-claude.md` | `docs/guardrails/prompts/pr-review-claude.md` |
| `docs/guardrails/pr-review-codex.md` | `docs/guardrails/prompts/pr-review-codex.md` |
| `docs/guardrails/test-plan.md` | `docs/guardrails/prompts/test-plan.md` |
| `docs/guardrails/security-review.md` | `docs/guardrails/prompts/security-review.md` |
| `docs/guardrails/incident-response.md` | `docs/guardrails/prompts/incident-response.md` |
| `docs/guardrails/runbook-draft.md` | `docs/guardrails/prompts/runbook-draft.md` |
| `docs/guardrails/privacy-review.md` | `docs/guardrails/prompts/privacy-review.md` |
| `docs/guardrails/migration-review.md` | `docs/guardrails/prompts/migration-review.md` |
| `docs/guardrails/adr-draft.md` | `docs/guardrails/prompts/adr-draft.md` |
| `docs/guardrails/refactor-plan.md` | `docs/guardrails/prompts/refactor-plan.md` |
| `docs/guardrails/release-notes.md` | `docs/guardrails/prompts/release-notes.md` |
| `docs/guardrails/support-reply.md` | `docs/guardrails/prompts/support-reply.md` |
| `docs/guardrails/threat-model.md` | `docs/guardrails/prompts/threat-model.md` **or** `agents/threat-model.md` |

Ambiguous flat names that existed in both `agents/` and `checklists/` (or `agents/` and `prompts/`) may have been whichever file won last. Prefer reinstalling the profile and linking the nested paths from [sample-agents-md.md](sample-agents-md.md).

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

After reinstall, `install-packs.sh` prints a **warning** (stderr) when it detects flat `*.md` siblings beside nested copies; it does **not** delete them.

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

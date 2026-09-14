#!/usr/bin/env bash
# Copy selected ai-dev-guardrails packs into a target repository.
# Usage:
#   bash scripts/install-packs.sh /path/to/consumer-repo
#   bash scripts/install-packs.sh /path/to/consumer-repo --profile baseline
#   bash scripts/install-packs.sh /path/to/consumer-repo --profile full
#   PACKS="agents/core.md agents/api.md" bash scripts/install-packs.sh /path/to/consumer-repo
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: bash scripts/install-packs.sh TARGET_REPO [--profile baseline|api|ops|full] [--dest RELDIR]

Copies markdown packs from this repository into TARGET_REPO/RELDIR (default: docs/guardrails).

Profiles:
  baseline  core, security, secrets, testing, docs, commits + DoD + pr-self-review
  api       baseline + api, deps + test-plan, change-impact
  ops       baseline + observability, ci, incidents, performance, a11y + incident/runbook + a11y checklist
  full      all agents, checklists, and prompts under packs/

Environment:
  PACKS   space-separated paths relative to packs/ (overrides --profile)
USAGE
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" || $# -lt 1 ]]; then
  usage
  exit 0
fi

TARGET="${1:?TARGET_REPO required}"
shift
PROFILE="baseline"
DEST_REL="docs/guardrails"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --profile) PROFILE="${2:?}"; shift 2 ;;
    --dest) DEST_REL="${2:?}"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "unknown arg: $1" >&2; usage; exit 2 ;;
  esac
done

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PACKS_ROOT="$ROOT/packs"
DEST="$TARGET/$DEST_REL"

if [[ ! -d "$TARGET" ]]; then
  echo "target is not a directory: $TARGET" >&2
  exit 1
fi
if [[ ! -d "$PACKS_ROOT" ]]; then
  echo "packs/ not found next to scripts/ (expected $PACKS_ROOT)" >&2
  exit 1
fi

baseline_packs=(
  agents/core.md
  agents/security.md
  agents/secrets.md
  agents/testing.md
  agents/docs.md
  agents/commits.md
  checklists/definition-of-done.md
  checklists/pr-self-review.md
)

api_extra=(
  agents/api.md
  agents/deps.md
  prompts/test-plan.md
  prompts/change-impact.md
)

ops_extra=(
  agents/observability.md
  agents/ci.md
  agents/incidents.md
  agents/performance.md
  agents/a11y.md
  prompts/incident-response.md
  prompts/runbook-draft.md
  checklists/observability.md
  checklists/accessibility.md
)

if [[ -n "${PACKS:-}" ]]; then
  # shellcheck disable=SC2206
  selected=($PACKS)
else
  case "$PROFILE" in
    baseline) selected=("${baseline_packs[@]}") ;;
    api)
      selected=("${baseline_packs[@]}" "${api_extra[@]}")
      ;;
    ops)
      selected=("${baseline_packs[@]}" "${ops_extra[@]}")
      ;;
    full)
      mapfile -t selected < <(
        cd "$PACKS_ROOT" && find agents checklists prompts -type f -name '*.md' | sort
      )
      ;;
    *)
      echo "unknown profile: $PROFILE" >&2
      exit 2
      ;;
  esac
fi

mkdir -p "$DEST"
copied=0
for rel in "${selected[@]}"; do
  src="$PACKS_ROOT/$rel"
  if [[ ! -f "$src" ]]; then
    echo "skip missing pack: $rel" >&2
    continue
  fi
  base="$(basename "$rel")"
  cp "$src" "$DEST/$base"
  echo "copied $rel -> $DEST_REL/$base"
  copied=$((copied + 1))
done

echo "Installed $copied pack file(s) into $DEST"
echo "Next: link them from $TARGET/AGENTS.md (see docs/references/install.md)."

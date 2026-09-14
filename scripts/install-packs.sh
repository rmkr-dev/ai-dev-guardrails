#!/usr/bin/env bash
# Copy selected ai-dev-guardrails packs into a target repository.
# Usage:
#   bash scripts/install-packs.sh /path/to/consumer-repo
#   bash scripts/install-packs.sh /path/to/consumer-repo --profile baseline
#   bash scripts/install-packs.sh /path/to/consumer-repo --profile full
#   bash scripts/install-packs.sh --list-profiles
#   bash scripts/install-packs.sh /path/to/consumer-repo --dry-run
#   PACKS="agents/core.md agents/api.md" bash scripts/install-packs.sh /path/to/consumer-repo
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage:
  bash scripts/install-packs.sh TARGET_REPO [--profile NAME] [--dest RELDIR] [--dry-run]
  bash scripts/install-packs.sh --list-profiles

Copies markdown packs from this repository into TARGET_REPO/RELDIR (default: docs/guardrails),
preserving agents|checklists|prompts/ relative paths (avoids basename collisions).
Writes INSTALL_MANIFEST.txt in the destination listing profile and copied files.

Profiles:
  baseline  core, security, secrets, testing, docs, commits + DoD + pr-self-review
  api       baseline + api, deps, supply-chain + test-plan, change-impact
  ops       baseline + observability, ci, incidents, performance, a11y, privacy, resilience, cost + incident/runbook/privacy prompts
  data      baseline + data, api + migration-review, change-impact
  security  baseline + security, secrets, privacy, threat-model + security/privacy/threat prompts
  web       baseline + frontend, a11y, i18n + a11y/i18n/frontend checklists
  full      all agents, checklists, and prompts under packs/

Flags:
  --profile NAME   Install profile (default: baseline)
  --dest RELDIR    Destination under TARGET (default: docs/guardrails)
  --dry-run        Print planned copies; do not write files
  --list-profiles  Print profiles and exact pack lists; exit

Environment:
  PACKS   space-separated paths relative to packs/ (overrides --profile)
USAGE
}

list_profiles() {
  cat <<'PROFILES'
baseline:
  agents/core.md
  agents/security.md
  agents/secrets.md
  agents/testing.md
  agents/docs.md
  agents/commits.md
  checklists/definition-of-done.md
  checklists/pr-self-review.md

api: (baseline +)
  agents/api.md
  agents/deps.md
  agents/supply-chain.md
  prompts/test-plan.md
  prompts/change-impact.md
  checklists/supply-chain.md

ops: (baseline +)
  agents/observability.md
  agents/ci.md
  agents/incidents.md
  agents/performance.md
  agents/a11y.md
  agents/privacy.md
  agents/resilience.md
  agents/cost.md
  prompts/incident-response.md
  prompts/runbook-draft.md
  prompts/privacy-review.md
  checklists/observability.md
  checklists/accessibility.md
  checklists/resilience.md
  checklists/cost.md

data: (baseline +)
  agents/data.md
  agents/api.md
  prompts/migration-review.md
  prompts/change-impact.md

security: (baseline +)
  agents/security.md
  agents/secrets.md
  agents/privacy.md
  agents/threat-model.md
  prompts/security-review.md
  prompts/privacy-review.md
  prompts/threat-model.md

web: (baseline +)
  agents/frontend.md
  agents/a11y.md
  agents/i18n.md
  checklists/frontend.md
  checklists/accessibility.md
  checklists/i18n.md

full:
  all *.md under packs/agents, packs/checklists, packs/prompts

Docs: docs/references/profiles.md
PROFILES
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

if [[ "${1:-}" == "--list-profiles" ]]; then
  list_profiles
  exit 0
fi

if [[ $# -lt 1 ]]; then
  usage
  exit 0
fi

TARGET="${1:?TARGET_REPO required}"
shift
PROFILE="baseline"
DEST_REL="docs/guardrails"
DRY_RUN=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --profile) PROFILE="${2:?}"; shift 2 ;;
    --dest) DEST_REL="${2:?}"; shift 2 ;;
    --dry-run) DRY_RUN=1; shift ;;
    --list-profiles) list_profiles; exit 0 ;;
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
  agents/supply-chain.md
  prompts/test-plan.md
  prompts/change-impact.md
  checklists/supply-chain.md
)

data_extra=(
  agents/data.md
  agents/api.md
  prompts/migration-review.md
  prompts/change-impact.md
)

security_extra=(
  agents/security.md
  agents/secrets.md
  agents/privacy.md
  agents/threat-model.md
  prompts/security-review.md
  prompts/privacy-review.md
  prompts/threat-model.md
)

ops_extra=(
  agents/observability.md
  agents/ci.md
  agents/incidents.md
  agents/performance.md
  agents/a11y.md
  agents/privacy.md
  agents/resilience.md
  agents/cost.md
  prompts/incident-response.md
  prompts/runbook-draft.md
  prompts/privacy-review.md
  checklists/observability.md
  checklists/accessibility.md
  checklists/resilience.md
  checklists/cost.md
)


web_extra=(
  agents/frontend.md
  agents/a11y.md
  agents/i18n.md
  checklists/frontend.md
  checklists/accessibility.md
  checklists/i18n.md
)

if [[ -n "${PACKS:-}" ]]; then
  # shellcheck disable=SC2206
  selected=($PACKS)
  PROFILE_LABEL="custom (PACKS=)"
else
  PROFILE_LABEL="$PROFILE"
  case "$PROFILE" in
    baseline) selected=("${baseline_packs[@]}") ;;
    api)
      selected=("${baseline_packs[@]}" "${api_extra[@]}")
      ;;
    data)
      selected=("${baseline_packs[@]}" "${data_extra[@]}")
      ;;
    security)
      selected=("${baseline_packs[@]}" "${security_extra[@]}")
      ;;
    web)
      selected=("${baseline_packs[@]}" "${web_extra[@]}")
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
      echo "Tip: bash scripts/install-packs.sh --list-profiles" >&2
      exit 2
      ;;
  esac
fi

warn_flat_leftovers() {
  # Warn about flat 0.2.x leftovers (basename *.md at dest root) without deleting.
  local flat_left=0
  local flat base
  [[ -d "$DEST" ]] || return 0
  shopt -s nullglob
  for flat in "$DEST"/*.md; do
    base=$(basename "$flat")
    if [[ -f "$DEST/agents/$base" || -f "$DEST/checklists/$base" || -f "$DEST/prompts/$base" ]]; then
      echo "warning: flat leftover $DEST_REL/$base (nested copy exists); see docs/references/migrate-nested-install.md" >&2
      flat_left=$((flat_left + 1))
    else
      # dry-run / pre-nested: flag flats whose basename matches a selected pack
      for rel in "${selected[@]}"; do
        if [[ "$(basename "$rel")" == "$base" ]]; then
          echo "warning: flat leftover $DEST_REL/$base (selected pack $rel); see docs/references/migrate-nested-install.md" >&2
          flat_left=$((flat_left + 1))
          break
        fi
      done
    fi
  done
  shopt -u nullglob
  if [[ "$flat_left" -gt 0 ]]; then
    echo "warning: $flat_left flat leftover(s) detected; update AGENTS.md links then remove flats" >&2
  fi
}

if [[ "$DRY_RUN" -eq 1 ]]; then
  echo "DRY-RUN profile=$PROFILE_LABEL dest=$DEST_REL (${#selected[@]} pack(s))"
  for rel in "${selected[@]}"; do
    src="$PACKS_ROOT/$rel"
    if [[ ! -f "$src" ]]; then
      echo "MISSING $rel" >&2
      continue
    fi
    echo "would copy $rel -> $DEST_REL/$rel"
  done
  echo "would write $DEST_REL/INSTALL_MANIFEST.txt"
  warn_flat_leftovers
  exit 0
fi

mkdir -p "$DEST"
copied=0
manifest_lines=()
for rel in "${selected[@]}"; do
  src="$PACKS_ROOT/$rel"
  if [[ ! -f "$src" ]]; then
    echo "skip missing pack: $rel" >&2
    continue
  fi
  dest_file="$DEST/$rel"
  mkdir -p "$(dirname "$dest_file")"
  cp "$src" "$dest_file"
  echo "copied $rel -> $DEST_REL/$rel"
  manifest_lines+=("$rel -> $DEST_REL/$rel")
  copied=$((copied + 1))
done

{
  echo "# ai-dev-guardrails install manifest"
  echo "# generated by scripts/install-packs.sh"
  echo "profile: $PROFILE_LABEL"
  echo "dest: $DEST_REL"
  echo "count: $copied"
  echo "packs:"
  for line in "${manifest_lines[@]}"; do
    echo "  - $line"
  done
} > "$DEST/INSTALL_MANIFEST.txt"
echo "wrote $DEST_REL/INSTALL_MANIFEST.txt"

echo "Installed $copied pack file(s) into $DEST"
warn_flat_leftovers
echo "Next: link them from $TARGET/AGENTS.md (see docs/references/install.md)."

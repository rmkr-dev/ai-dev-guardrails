#!/usr/bin/env bash
# Shell tests for scripts/install-packs.sh (no Node). Run: bash tests/test_install_packs.sh
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$ROOT/scripts/install-packs.sh"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "PASS: $*"; }

[[ -x "$SCRIPT" || -f "$SCRIPT" ]] || fail "missing $SCRIPT"

# --list-profiles
out="$("$SCRIPT" --list-profiles)"
echo "$out" | grep -q '^baseline:' || fail "list-profiles missing baseline"
echo "$out" | grep -q '^ops:' || fail "list-profiles missing ops"
pass "list-profiles"

# --dry-run baseline
target="$TMP/consumer"
mkdir -p "$target"
dry="$("$SCRIPT" "$target" --profile baseline --dry-run)"
echo "$dry" | grep -q 'would copy agents/core.md -> docs/guardrails/agents/core.md' || fail "dry-run nested path"
echo "$dry" | grep -q 'INSTALL_MANIFEST' || fail "dry-run manifest mention"
[[ ! -e "$target/docs/guardrails" ]] || fail "dry-run should not create dest"
pass "dry-run"

# real baseline install preserves nesting; no basename collision pair in baseline,
# but verify nested core path and manifest
"$SCRIPT" "$target" --profile baseline >/dev/null
[[ -f "$target/docs/guardrails/agents/core.md" ]] || fail "missing agents/core.md"
[[ -f "$target/docs/guardrails/checklists/definition-of-done.md" ]] || fail "missing checklist path"
[[ -f "$target/docs/guardrails/INSTALL_MANIFEST.txt" ]] || fail "missing manifest"
grep -q 'profile: baseline' "$target/docs/guardrails/INSTALL_MANIFEST.txt" || fail "manifest profile"
# ensure flat collision path was NOT used for core
[[ ! -f "$target/docs/guardrails/core.md" ]] || fail "unexpected flat core.md"
pass "baseline install nested"

# ops: both cost agent and checklist must exist
target2="$TMP/ops"
mkdir -p "$target2"
"$SCRIPT" "$target2" --profile ops >/dev/null
[[ -f "$target2/docs/guardrails/agents/cost.md" ]] || fail "ops missing agents/cost.md"
[[ -f "$target2/docs/guardrails/checklists/cost.md" ]] || fail "ops missing checklists/cost.md"
# contents should differ (agent vs checklist titles)
head -1 "$target2/docs/guardrails/agents/cost.md" | grep -qi cost || fail "agent cost header"
head -1 "$target2/docs/guardrails/checklists/cost.md" | grep -qi cost || fail "checklist cost header"
pass "ops cost no collision"

echo "All install-packs shell tests passed."

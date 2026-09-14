#!/usr/bin/env bash
# Shell tests for scripts/install-packs.sh (no Node). Run: bash tests/test_install_packs.sh
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$ROOT/scripts/install-packs.sh"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "PASS: $*"; }

[[ -f "$SCRIPT" ]] || fail "missing $SCRIPT"
run_install() { bash "$SCRIPT" "$@"; }

out="$(run_install --list-profiles)"
echo "$out" | grep -q '^baseline:' || fail "list-profiles missing baseline"
echo "$out" | grep -q '^ops:' || fail "list-profiles missing ops"
pass "list-profiles"

target="$TMP/consumer"
mkdir -p "$target"
dry="$(run_install "$target" --profile baseline --dry-run)"
echo "$dry" | grep -q 'would copy agents/core.md -> docs/guardrails/agents/core.md' || fail "dry-run nested path"
echo "$dry" | grep -q 'INSTALL_MANIFEST' || fail "dry-run manifest mention"
[[ ! -e "$target/docs/guardrails" ]] || fail "dry-run should not create dest"
pass "dry-run"

run_install "$target" --profile baseline >/dev/null
[[ -f "$target/docs/guardrails/agents/core.md" ]] || fail "missing agents/core.md"
[[ -f "$target/docs/guardrails/checklists/definition-of-done.md" ]] || fail "missing checklist path"
[[ -f "$target/docs/guardrails/INSTALL_MANIFEST.txt" ]] || fail "missing manifest"
grep -q 'profile: baseline' "$target/docs/guardrails/INSTALL_MANIFEST.txt" || fail "manifest profile"
[[ ! -f "$target/docs/guardrails/core.md" ]] || fail "unexpected flat core.md"
pass "baseline install nested"

target2="$TMP/ops"
mkdir -p "$target2"
run_install "$target2" --profile ops >/dev/null
[[ -f "$target2/docs/guardrails/agents/cost.md" ]] || fail "ops missing agents/cost.md"
[[ -f "$target2/docs/guardrails/checklists/cost.md" ]] || fail "ops missing checklists/cost.md"
head -1 "$target2/docs/guardrails/agents/cost.md" | grep -qi cost || fail "agent cost header"
head -1 "$target2/docs/guardrails/checklists/cost.md" | grep -qi cost || fail "checklist cost header"
pass "ops cost no collision"

# --- flat leftover warning ---
target3="$TMP/flatmix"
mkdir -p "$target3/docs/guardrails"
# simulate 0.2.x flat leftover
echo "# old flat core" > "$target3/docs/guardrails/core.md"
warn="$(run_install "$target3" --profile baseline 2>&1)"
echo "$warn" | grep -q "flat leftover docs/guardrails/core.md" || fail "missing flat leftover warning"
[[ -f "$target3/docs/guardrails/agents/core.md" ]] || fail "nested core missing after mix install"
[[ -f "$target3/docs/guardrails/core.md" ]] || fail "flat leftover should remain (no delete)"
pass "flat leftover warning"

# --- dry-run reports flat leftovers before nested write ---
target4="$TMP/flatdry"
mkdir -p "$target4/docs/guardrails"
echo "# old flat core" > "$target4/docs/guardrails/core.md"
dryw="$(run_install "$target4" --profile baseline --dry-run 2>&1)"
echo "$dryw" | grep -q "flat leftover docs/guardrails/core.md" || fail "dry-run missing flat leftover warning"
[[ ! -f "$target4/docs/guardrails/agents/core.md" ]] || fail "dry-run should not write nested"
pass "dry-run flat leftover warning"

echo "All install-packs shell tests passed."

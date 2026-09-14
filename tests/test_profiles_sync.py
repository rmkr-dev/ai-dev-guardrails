"""Ensure ai_guardrails.profiles stays aligned with scripts/install-packs.sh."""

from __future__ import annotations

import re
from pathlib import Path

from ai_guardrails.profiles import EXTRAS, BASELINE, PROFILE_NAMES, packs_for

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "install-packs.sh"


def _bash_array(name: str, text: str) -> list[str]:
    # Match name=( ... ) block with one path per line
    m = re.search(rf"^{name}=\(\n(.*?)^\)", text, flags=re.M | re.S)
    assert m, f"array {name} not found in install-packs.sh"
    items = []
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        items.append(line)
    return items


def test_baseline_matches_script() -> None:
    text = SCRIPT.read_text()
    assert list(BASELINE) == _bash_array("baseline_packs", text)


def test_extras_match_script() -> None:
    text = SCRIPT.read_text()
    mapping = {
        "api": "api_extra",
        "ops": "ops_extra",
        "data": "data_extra",
        "security": "security_extra",
        "web": "web_extra",
    }
    for profile, arr in mapping.items():
        assert tuple(_bash_array(arr, text)) == EXTRAS[profile]


def test_profile_names_documented_in_script_usage() -> None:
    text = SCRIPT.read_text()
    for name in PROFILE_NAMES:
        if name == "full":
            continue
        assert name in text


def test_packs_for_composed() -> None:
    api = packs_for("api")
    assert api is not None
    assert api[: len(BASELINE)] == list(BASELINE)

"""Ensure --list-profiles text mentions every pack from install-packs.sh arrays."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "install-packs.sh"


def _bash_array(name: str, text: str) -> list[str]:
    m = re.search(rf"^{name}=\(\n(.*?)^\)", text, flags=re.M | re.S)
    assert m, f"array {name} not found"
    items = []
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        items.append(line)
    return items


def test_list_profiles_mentions_all_extra_packs() -> None:
    text = SCRIPT.read_text()
    out = subprocess.check_output(["bash", str(SCRIPT), "--list-profiles"], text=True)
    mapping = {
        "api": "api_extra",
        "ops": "ops_extra",
        "data": "data_extra",
        "security": "security_extra",
        "web": "web_extra",
    }
    for profile, arr in mapping.items():
        for pack in _bash_array(arr, text):
            assert pack in out, f"{profile}: list-profiles missing {pack}"
    for pack in _bash_array("baseline_packs", text):
        assert pack in out, f"baseline: list-profiles missing {pack}"

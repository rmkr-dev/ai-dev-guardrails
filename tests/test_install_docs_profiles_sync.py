"""Keep install.md profile table aligned with PROFILE_NAMES."""

from __future__ import annotations

import re
from pathlib import Path

from ai_guardrails.profiles import PROFILE_NAMES

ROOT = Path(__file__).resolve().parents[1]
INSTALL = ROOT / "docs" / "references" / "install.md"


def test_install_md_profiles_table_lists_all_profile_names() -> None:
    text = INSTALL.read_text()
    # Rows like: | `baseline` | ...
    listed = re.findall(r"^\| `([a-z]+)` \|", text, flags=re.M)
    # Restrict to the Profiles (script) section table — first occurrence block after heading
    m = re.search(
        r"## Profiles \(script\)\n\n\| Profile \| Intent \|\n\| --- \| --- \|\n((?:\|.+\n)+)",
        text,
    )
    assert m, "install.md missing Profiles (script) table"
    rows = re.findall(r"^\| `([a-z]+)` \|", m.group(1), flags=re.M)
    assert tuple(rows) == PROFILE_NAMES, f"install.md profiles {rows} != {PROFILE_NAMES}"

"""Keep profiles.md documenting every PROFILE_NAMES entry."""

from __future__ import annotations

import re
from pathlib import Path

from ai_guardrails.profiles import PROFILE_NAMES

ROOT = Path(__file__).resolve().parents[1]
PROFILES_MD = ROOT / "docs" / "references" / "profiles.md"


def test_profiles_md_documents_every_profile_name() -> None:
    text = PROFILES_MD.read_text()
    # Heading style ### `web` or table row | `web` |
    for name in PROFILE_NAMES:
        assert (
            f"### `{name}`" in text
            or f"| `{name}` |" in text
            or f"`{name}`" in text
        ), f"profiles.md missing profile {name}"
    # Prefer ordered table or headings covering non-full names
    for name in PROFILE_NAMES:
        if name == "full":
            continue
        assert f"`{name}`" in text

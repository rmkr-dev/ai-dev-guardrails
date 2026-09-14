"""Keep published version strings aligned across metadata files."""

from __future__ import annotations

import re
from pathlib import Path

from ai_guardrails import __version__

ROOT = Path(__file__).resolve().parents[1]


def _pyproject_version() -> str:
    text = (ROOT / "pyproject.toml").read_text()
    m = re.search(r'^version\s*=\s*"([^"]+)"', text, flags=re.M)
    assert m, "pyproject.toml missing version"
    return m.group(1)


def _citation_version() -> str:
    text = (ROOT / "CITATION.cff").read_text()
    m = re.search(r"^version:\s*(\S+)", text, flags=re.M)
    assert m, "CITATION.cff missing version"
    return m.group(1)


def _readme_status_version() -> str:
    text = (ROOT / "README.md").read_text()
    m = re.search(r"\*\*v(\d+\.\d+\.\d+)\*\*", text)
    assert m, "README.md missing **vX.Y.Z** status line"
    return m.group(1)


def _changelog_latest() -> str:
    text = (ROOT / "CHANGELOG.md").read_text()
    m = re.search(r"^## \[(\d+\.\d+\.\d+)\]", text, flags=re.M)
    assert m, "CHANGELOG.md missing latest ## [X.Y.Z] heading"
    return m.group(1)


def test_version_metadata_aligned() -> None:
    expected = _pyproject_version()
    assert __version__ == expected
    assert _citation_version() == expected
    assert _readme_status_version() == expected
    assert _changelog_latest() == expected

"""Keep docs check catalogs aligned with DEFAULT_CHECKS."""

from __future__ import annotations

import re
from pathlib import Path

from ai_guardrails.checks import DEFAULT_CHECKS

ROOT = Path(__file__).resolve().parents[1]


def _check_names() -> list[str]:
    # Each check_* returns CheckResult with name=...; call with nonexistent root
    # is heavy — derive from function names: check_foo -> foo (special cases none)
    names = []
    for fn in DEFAULT_CHECKS:
        assert fn.__name__.startswith("check_")
        names.append(fn.__name__[len("check_") :])
    return names


def test_architecture_lists_all_default_checks() -> None:
    text = (ROOT / "docs/architecture/architecture.md").read_text()
    m = re.search(r"Default checks \((\d+)\): ([^\n]+)", text)
    assert m, "architecture.md missing Default checks line"
    count = int(m.group(1))
    names = _check_names()
    assert count == len(names)
    listed = [p.strip(" `.") for p in m.group(2).split(",")]
    assert listed == names


def test_validator_checks_table_lists_all_default_checks() -> None:
    text = (ROOT / "docs/references/validator-checks.md").read_text()
    names = _check_names()
    for name in names:
        assert f"`{name}`" in text, f"validator-checks.md missing {name}"
    # table row count for check names
    rows = re.findall(r"^\| `([a-z_]+)` \|", text, flags=re.M)
    assert rows == names

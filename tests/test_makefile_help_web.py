"""Makefile help mentions web profile and nested leftovers."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_makefile_help_mentions_web_and_nested() -> None:
    text = (ROOT / "Makefile").read_text()
    assert "PROFILE=baseline|api|ops|data|security|web|full" in text
    assert "Nested install" in text
    assert "--no-strict" in text
    assert "docs/references/install.md" in text

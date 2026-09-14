"""CLI --no-strict exits zero even when checks fail."""

from __future__ import annotations

from pathlib import Path

from click.testing import CliRunner

from ai_guardrails.cli import main


def test_check_no_strict_allows_failures(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("# only readme\n")
    runner = CliRunner()
    result = runner.invoke(main, ["check", str(tmp_path), "--no-strict"])
    assert result.exit_code == 0
    assert "FAIL" in result.output

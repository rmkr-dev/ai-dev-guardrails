from __future__ import annotations

from pathlib import Path

from click.testing import CliRunner

from ai_guardrails.cli import main


def _seed_minimal(root: Path) -> None:
    (root / "README.md").write_text("# r\n")
    (root / "AGENTS.md").write_text("# a\n")


def test_check_only(tmp_path: Path) -> None:
    _seed_minimal(tmp_path)
    runner = CliRunner()
    result = runner.invoke(main, ["check", str(tmp_path), "--only", "readme,agents_md"])
    assert result.exit_code == 0
    assert "readme" in result.output
    assert "agents_md" in result.output
    assert "license" not in result.output
    assert "2/2 checks passed" in result.output


def test_check_skip(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("# r\n")
    runner = CliRunner()
    result = runner.invoke(
        main, ["check", str(tmp_path), "--only", "readme,agents_md", "--skip", "agents_md"]
    )
    assert result.exit_code == 0
    assert "1/1 checks passed" in result.output
    assert "agents_md" not in result.output


def test_check_only_unknown(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("# r\n")
    runner = CliRunner()
    result = runner.invoke(main, ["check", str(tmp_path), "--only", "not_a_check"])
    assert result.exit_code != 0
    assert "unknown check name" in result.output


def test_check_only_unknown_suggests(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("# r\n")
    runner = CliRunner()
    result = runner.invoke(main, ["check", str(tmp_path), "--only", "readm"])
    assert result.exit_code != 0
    assert "did you mean" in result.output
    assert "readme" in result.output

from __future__ import annotations

from pathlib import Path

import pytest

from ai_guardrails.checks import (
    check_agents_md,
    check_architecture_docs,
    check_readme,
    check_tests_or_ci,
    run_checks,
)


def _touch(path: Path, content: str = "# x\n") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def test_check_agents_md_pass_fail(tmp_path: Path) -> None:
    assert check_agents_md(tmp_path).ok is False
    _touch(tmp_path / "AGENTS.md")
    assert check_agents_md(tmp_path).ok is True


def test_check_readme_pass_fail(tmp_path: Path) -> None:
    assert check_readme(tmp_path).ok is False
    _touch(tmp_path / "README.md")
    assert check_readme(tmp_path).ok is True


def test_architecture_dir_with_markdown(tmp_path: Path) -> None:
    assert check_architecture_docs(tmp_path).ok is False
    _touch(tmp_path / "docs" / "architecture" / "architecture.md")
    result = check_architecture_docs(tmp_path)
    assert result.ok is True
    assert "docs/architecture" in result.detail


def test_architecture_flat_file(tmp_path: Path) -> None:
    _touch(tmp_path / "docs" / "architecture.md")
    assert check_architecture_docs(tmp_path).ok is True


def test_tests_directory_indicator(tmp_path: Path) -> None:
    assert check_tests_or_ci(tmp_path).ok is False
    _touch(tmp_path / "tests" / "test_sample.py", "def test_ok():\n    assert True\n")
    result = check_tests_or_ci(tmp_path)
    assert result.ok is True
    assert "tests" in result.detail


def test_ci_workflow_indicator(tmp_path: Path) -> None:
    _touch(tmp_path / ".github" / "workflows" / "ci.yml", "name: CI\n")
    result = check_tests_or_ci(tmp_path)
    assert result.ok is True
    assert "ci:" in result.detail


def test_run_checks_all_pass(tmp_path: Path) -> None:
    _touch(tmp_path / "AGENTS.md")
    _touch(tmp_path / "README.md")
    _touch(tmp_path / "docs" / "architecture" / "overview.md")
    _touch(tmp_path / "tests" / "test_x.py", "def test_x():\n    assert 1\n")
    results = run_checks(tmp_path)
    assert all(r.ok for r in results)
    assert {r.name for r in results} == {
        "agents_md",
        "readme",
        "architecture_docs",
        "tests_or_ci",
    }


def test_run_checks_rejects_file(tmp_path: Path) -> None:
    f = tmp_path / "notadir.txt"
    f.write_text("x")
    with pytest.raises(FileNotFoundError):
        run_checks(f)

from __future__ import annotations

from pathlib import Path

import pytest

from ai_guardrails.checks import check_gitignore, run_checks


def _touch(path: Path, content: str = "# x\n") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def _seed_all(tmp_path: Path) -> None:
    for name in ("AGENTS.md", "README.md", "CONTRIBUTING.md", "SECURITY.md"):
        _touch(tmp_path / name)
    _touch(tmp_path / "LICENSE", "MIT\n")
    _touch(tmp_path / ".gitignore", "*.pyc\n")
    _touch(tmp_path / "docs" / "architecture" / "overview.md")
    _touch(tmp_path / "tests" / "test_x.py", "def test_x():\n    assert 1\n")
    _touch(tmp_path / ".github" / "CODEOWNERS", "* @rmkr-dev\n")


def test_gitignore(tmp_path: Path) -> None:
    assert check_gitignore(tmp_path).ok is False
    _touch(tmp_path / ".gitignore")
    assert check_gitignore(tmp_path).ok is True


def test_run_checks_all_pass(tmp_path: Path) -> None:
    _seed_all(tmp_path)
    results = run_checks(tmp_path)
    assert all(r.ok for r in results)
    assert "gitignore" in {r.name for r in results}
    assert len(results) == 9


def test_run_checks_rejects_file(tmp_path: Path) -> None:
    f = tmp_path / "notadir.txt"
    f.write_text("x")
    with pytest.raises(FileNotFoundError):
        run_checks(f)

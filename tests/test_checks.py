from __future__ import annotations

from pathlib import Path

import pytest

from ai_guardrails.checks import (
    check_changelog,
    check_dependabot,
    check_editorconfig,
    check_gitignore,
    check_makefile,
    check_pr_template,
    run_checks,
)


def _touch(path: Path, content: str = "# x\n") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def _seed_all(tmp_path: Path) -> None:
    for name in ("AGENTS.md", "README.md", "CONTRIBUTING.md", "SECURITY.md", "CHANGELOG.md"):
        _touch(tmp_path / name)
    _touch(tmp_path / "LICENSE", "MIT\n")
    _touch(tmp_path / ".gitignore", "*.pyc\n")
    _touch(tmp_path / "docs" / "architecture" / "overview.md")
    _touch(tmp_path / "tests" / "test_x.py", "def test_x():\n    assert 1\n")
    _touch(tmp_path / ".github" / "CODEOWNERS", "* @rmkr-dev\n")
    _touch(tmp_path / ".github" / "PULL_REQUEST_TEMPLATE.md", "## Summary\n")
    _touch(tmp_path / ".github" / "dependabot.yml", "version: 2\n")
    _touch(tmp_path / ".editorconfig", "root = true\n")
    _touch(tmp_path / "Makefile", "test:\n\tpytest -q\n")


def test_gitignore(tmp_path: Path) -> None:
    assert check_gitignore(tmp_path).ok is False
    _touch(tmp_path / ".gitignore")
    assert check_gitignore(tmp_path).ok is True


def test_changelog(tmp_path: Path) -> None:
    assert check_changelog(tmp_path).ok is False
    _touch(tmp_path / "CHANGELOG.md")
    assert check_changelog(tmp_path).ok is True


def test_pr_template(tmp_path: Path) -> None:
    assert check_pr_template(tmp_path).ok is False
    _touch(tmp_path / ".github" / "PULL_REQUEST_TEMPLATE.md")
    assert check_pr_template(tmp_path).ok is True


def test_pr_template_dir(tmp_path: Path) -> None:
    _touch(tmp_path / ".github" / "PULL_REQUEST_TEMPLATE" / "default.md")
    assert check_pr_template(tmp_path).ok is True


def test_dependabot(tmp_path: Path) -> None:
    assert check_dependabot(tmp_path).ok is False
    _touch(tmp_path / ".github" / "dependabot.yml", "version: 2\n")
    _touch(tmp_path / ".editorconfig", "root = true\n")
    _touch(tmp_path / "Makefile", "test:\n\tpytest -q\n")
    assert check_dependabot(tmp_path).ok is True


def test_editorconfig(tmp_path: Path) -> None:
    assert check_editorconfig(tmp_path).ok is False
    _touch(tmp_path / ".editorconfig", "root = true\n")
    _touch(tmp_path / "Makefile", "test:\n\tpytest -q\n")
    assert check_editorconfig(tmp_path).ok is True


def test_makefile(tmp_path: Path) -> None:
    assert check_makefile(tmp_path).ok is False
    _touch(tmp_path / "Makefile", "test:\n\tpytest -q\n")
    assert check_makefile(tmp_path).ok is True


def test_run_checks_all_pass(tmp_path: Path) -> None:
    _seed_all(tmp_path)
    results = run_checks(tmp_path)
    assert all(r.ok for r in results)
    names = {r.name for r in results}
    assert "gitignore" in names
    assert "changelog" in names
    assert "pr_template" in names
    assert "dependabot" in names
    assert "editorconfig" in names
    assert "makefile" in names
    assert len(results) == 14


def test_run_checks_rejects_file(tmp_path: Path) -> None:
    f = tmp_path / "notadir.txt"
    f.write_text("x")
    with pytest.raises(FileNotFoundError):
        run_checks(f)

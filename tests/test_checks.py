from __future__ import annotations

from pathlib import Path

import pytest

from ai_guardrails.checks import (
    check_agents_md,
    check_architecture_docs,
    check_codeowners,
    check_contributing,
    check_license,
    check_readme,
    check_security_md,
    check_tests_or_ci,
    run_checks,
)


def _touch(path: Path, content: str = "# x\n") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def test_basics(tmp_path: Path) -> None:
    assert check_agents_md(tmp_path).ok is False
    assert check_readme(tmp_path).ok is False
    _touch(tmp_path / "AGENTS.md")
    _touch(tmp_path / "README.md")
    assert check_agents_md(tmp_path).ok is True
    assert check_readme(tmp_path).ok is True


def test_architecture_and_tests_ci(tmp_path: Path) -> None:
    assert check_architecture_docs(tmp_path).ok is False
    _touch(tmp_path / "docs" / "architecture" / "architecture.md")
    assert check_architecture_docs(tmp_path).ok is True
    assert check_tests_or_ci(tmp_path).ok is False
    _touch(tmp_path / ".github" / "workflows" / "ci.yml", "name: CI\n")
    assert check_tests_or_ci(tmp_path).ok is True


def test_license_security_codeowners_contributing(tmp_path: Path) -> None:
    assert check_license(tmp_path).ok is False
    assert check_security_md(tmp_path).ok is False
    assert check_codeowners(tmp_path).ok is False
    assert check_contributing(tmp_path).ok is False
    _touch(tmp_path / "LICENSE", "MIT\n")
    _touch(tmp_path / "SECURITY.md")
    _touch(tmp_path / ".github" / "CODEOWNERS", "* @owner\n")
    _touch(tmp_path / "CONTRIBUTING.md")
    assert check_license(tmp_path).ok is True
    assert check_security_md(tmp_path).ok is True
    assert check_codeowners(tmp_path).ok is True
    assert check_contributing(tmp_path).ok is True


def _seed_all(tmp_path: Path) -> None:
    _touch(tmp_path / "AGENTS.md")
    _touch(tmp_path / "README.md")
    _touch(tmp_path / "CONTRIBUTING.md")
    _touch(tmp_path / "docs" / "architecture" / "overview.md")
    _touch(tmp_path / "tests" / "test_x.py", "def test_x():\n    assert 1\n")
    _touch(tmp_path / "LICENSE", "MIT\n")
    _touch(tmp_path / "SECURITY.md")
    _touch(tmp_path / ".github" / "CODEOWNERS", "* @rmkr-dev\n")


def test_run_checks_all_pass(tmp_path: Path) -> None:
    _seed_all(tmp_path)
    results = run_checks(tmp_path)
    assert all(r.ok for r in results)
    assert {r.name for r in results} == {
        "agents_md",
        "readme",
        "architecture_docs",
        "tests_or_ci",
        "license",
        "security_md",
        "codeowners",
        "contributing",
    }


def test_run_checks_rejects_file(tmp_path: Path) -> None:
    f = tmp_path / "notadir.txt"
    f.write_text("x")
    with pytest.raises(FileNotFoundError):
        run_checks(f)

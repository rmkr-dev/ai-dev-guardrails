from __future__ import annotations

from pathlib import Path

from click.testing import CliRunner

from ai_guardrails.cli import main


def _seed_good(root: Path) -> None:
    for name, content in {
        "AGENTS.md": "# agents\n",
        "README.md": "# readme\n",
        "LICENSE": "MIT\n",
        "SECURITY.md": "# security\n",
        "CONTRIBUTING.md": "# contrib\n",
        "CHANGELOG.md": "# changelog\n",
        ".gitignore": "*.pyc\n",
    }.items():
        (root / name).write_text(content)
    github = root / ".github"
    github.mkdir()
    (github / "CODEOWNERS").write_text("* @rmkr-dev\n")
    (github / "PULL_REQUEST_TEMPLATE.md").write_text("## Summary\n")
    arch = root / "docs" / "architecture"
    arch.mkdir(parents=True)
    (arch / "architecture.md").write_text("# arch\n")
    tests = root / "tests"
    tests.mkdir()
    (tests / "test_ok.py").write_text("def test_ok():\n    assert True\n")


def test_cli_check_pass(tmp_path: Path) -> None:
    _seed_good(tmp_path)
    runner = CliRunner()
    result = runner.invoke(main, ["check", str(tmp_path)])
    assert result.exit_code == 0
    assert "11/11 checks passed" in result.output


def test_cli_check_fail_strict(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("# only readme\n")
    runner = CliRunner()
    result = runner.invoke(main, ["check", str(tmp_path)])
    assert result.exit_code == 1


def test_cli_list_checks() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["list-checks"])
    assert result.exit_code == 0
    lines = [ln.strip() for ln in result.output.splitlines() if ln.strip()]
    assert lines == [
        "agents_md",
        "readme",
        "architecture_docs",
        "tests_or_ci",
        "license",
        "security_md",
        "codeowners",
        "contributing",
        "gitignore",
        "changelog",
        "pr_template",
    ]

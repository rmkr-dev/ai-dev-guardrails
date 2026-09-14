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
    (github / "dependabot.yml").write_text("version: 2\n")
    (root / ".editorconfig").write_text("root = true\n")
    (root / "Makefile").write_text("test:\n\tpytest -q\n")
    issue = github / "ISSUE_TEMPLATE"
    issue.mkdir()
    (issue / "bug_report.md").write_text("## Bug\n")
    (root / ".pre-commit-config.yaml").write_text("repos: []\n")
    (root / "CODE_OF_CONDUCT.md").write_text("# CoC\n")
    (github / "FUNDING.yml").write_text("github: [rmkr-dev]\n")
    (root / "CITATION.cff").write_text("cff-version: 1.2.0\n")
    (root / "SUPPORT.md").write_text("# Support\n")
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
    assert "20/20 checks passed" in result.output


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
        "dependabot",
        "editorconfig",
        "makefile",
        "issue_templates",
        "pre_commit",
        "code_of_conduct",
        "funding",
        "citation",
        "support",
    ]


def test_cli_check_json(tmp_path: Path) -> None:
    _seed_good(tmp_path)
    runner = CliRunner()
    result = runner.invoke(main, ["check", str(tmp_path), "--format", "json"])
    assert result.exit_code == 0
    import json

    data = json.loads(result.output)
    assert data["failed"] == 0
    assert data["total"] == data["passed"]
    assert any(c["name"] == "readme" for c in data["checks"])


def test_cli_list_checks_json() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["list-checks", "--format", "json"])
    assert result.exit_code == 0
    import json

    data = json.loads(result.output)
    assert data["total"] == len(data["checks"])
    assert "readme" in data["checks"]
    assert "citation" in data["checks"]


def test_check_no_strict_allows_failures(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("# only readme\n")
    runner = CliRunner()
    result = runner.invoke(main, ["check", str(tmp_path), "--no-strict"])
    assert result.exit_code == 0
    assert "FAIL" in result.output


def test_check_fail_only(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("# only readme\n")
    runner = CliRunner()
    result = runner.invoke(main, ["check", str(tmp_path), "--no-strict", "--fail-only"])
    assert result.exit_code == 0
    assert "[FAIL]" in result.output
    assert "[PASS]" not in result.output
    assert "checks passed" in result.output


def test_list_checks_describe() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["list-checks", "--describe"])
    assert result.exit_code == 0
    assert "readme —" in result.output
    assert "Root README.md present" in result.output


def test_list_checks_describe_json() -> None:
    import json

    runner = CliRunner()
    result = runner.invoke(main, ["list-checks", "--describe", "--format", "json"])
    assert result.exit_code == 0
    data = json.loads(result.output)
    assert data["total"] == len(data["checks"])
    assert isinstance(data["checks"][0], dict)
    assert data["checks"][0]["name"] == "agents_md"
    assert "summary" in data["checks"][0]

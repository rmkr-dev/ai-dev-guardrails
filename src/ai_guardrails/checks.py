"""Hygiene checks against a target repository root."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class CheckResult:
    name: str
    ok: bool
    detail: str


def _exists(root: Path, rel: str) -> bool:
    return (root / rel).is_file()


def check_agents_md(root: Path) -> CheckResult:
    ok = _exists(root, "AGENTS.md")
    return CheckResult(
        "agents_md",
        ok,
        "AGENTS.md present" if ok else "missing AGENTS.md at repository root",
    )


def check_readme(root: Path) -> CheckResult:
    ok = _exists(root, "README.md")
    return CheckResult(
        "readme",
        ok,
        "README.md present" if ok else "missing README.md at repository root",
    )


def check_architecture_docs(root: Path) -> CheckResult:
    candidates = [
        "docs/architecture",
        "docs/architecture.md",
        "architecture.md",
    ]
    ok = False
    detail = "missing docs/architecture/ (or architecture.md)"
    for rel in candidates:
        path = root / rel
        if path.is_dir() and any(path.rglob("*.md")):
            ok = True
            detail = f"architecture docs found under {rel}/"
            break
        if path.is_file():
            ok = True
            detail = f"architecture doc found at {rel}"
            break
    return CheckResult("architecture_docs", ok, detail)


def check_tests_or_ci(root: Path) -> CheckResult:
    """Pass if tests/ or test indicators OR CI workflow indicators exist."""
    test_hits: list[str] = []
    if (root / "tests").is_dir() and any((root / "tests").rglob("test_*.py")):
        test_hits.append("tests/test_*.py")
    if (root / "tests").is_dir() and any((root / "tests").rglob("*_test.py")):
        test_hits.append("tests/*_test.py")
    if (root / "test").is_dir():
        test_hits.append("test/")
    if list(root.glob("test_*.py")) or list(root.glob("*_test.py")):
        test_hits.append("root test_*.py")

    ci_hits: list[str] = []
    workflows = root / ".github" / "workflows"
    if workflows.is_dir() and (
        any(workflows.glob("*.yml")) or any(workflows.glob("*.yaml"))
    ):
        ci_hits.append(".github/workflows/*")
    if (root / ".gitlab-ci.yml").is_file():
        ci_hits.append(".gitlab-ci.yml")
    if (root / "Jenkinsfile").is_file():
        ci_hits.append("Jenkinsfile")
    if (root / "azure-pipelines.yml").is_file():
        ci_hits.append("azure-pipelines.yml")

    ok = bool(test_hits or ci_hits)
    if ok:
        parts = []
        if test_hits:
            parts.append("tests: " + ", ".join(test_hits))
        if ci_hits:
            parts.append("ci: " + ", ".join(ci_hits))
        detail = "; ".join(parts)
    else:
        detail = "missing tests/ (or test_*.py) and CI workflow indicators"
    return CheckResult("tests_or_ci", ok, detail)


def check_license(root: Path) -> CheckResult:
    for name in ("LICENSE", "LICENSE.md", "COPYING"):
        if _exists(root, name):
            return CheckResult("license", True, f"{name} present")
    return CheckResult("license", False, "missing LICENSE (or LICENSE.md / COPYING)")


def check_security_md(root: Path) -> CheckResult:
    ok = _exists(root, "SECURITY.md")
    return CheckResult(
        "security_md",
        ok,
        "SECURITY.md present" if ok else "missing SECURITY.md at repository root",
    )


def check_codeowners(root: Path) -> CheckResult:
    for rel in (".github/CODEOWNERS", "CODEOWNERS", "docs/CODEOWNERS"):
        if _exists(root, rel):
            return CheckResult("codeowners", True, f"{rel} present")
    return CheckResult(
        "codeowners",
        False,
        "missing CODEOWNERS (.github/CODEOWNERS preferred)",
    )


def check_contributing(root: Path) -> CheckResult:
    for name in ("CONTRIBUTING.md", "CONTRIBUTING"):
        if _exists(root, name):
            return CheckResult("contributing", True, f"{name} present")
    return CheckResult(
        "contributing",
        False,
        "missing CONTRIBUTING.md at repository root",
    )


def check_gitignore(root: Path) -> CheckResult:
    ok = _exists(root, ".gitignore")
    return CheckResult(
        "gitignore",
        ok,
        ".gitignore present" if ok else "missing .gitignore at repository root",
    )


def check_changelog(root: Path) -> CheckResult:
    for name in ("CHANGELOG.md", "CHANGELOG", "HISTORY.md"):
        if _exists(root, name):
            return CheckResult("changelog", True, f"{name} present")
    return CheckResult(
        "changelog",
        False,
        "missing CHANGELOG.md (or CHANGELOG / HISTORY.md)",
    )


def check_pr_template(root: Path) -> CheckResult:
    candidates = [
        ".github/PULL_REQUEST_TEMPLATE.md",
        ".github/pull_request_template.md",
        "PULL_REQUEST_TEMPLATE.md",
        "docs/pull_request_template.md",
    ]
    for rel in candidates:
        if _exists(root, rel):
            return CheckResult("pr_template", True, f"{rel} present")
    # Directory form: .github/PULL_REQUEST_TEMPLATE/*.md
    pr_dir = root / ".github" / "PULL_REQUEST_TEMPLATE"
    if pr_dir.is_dir() and any(pr_dir.glob("*.md")):
        return CheckResult(
            "pr_template",
            True,
            ".github/PULL_REQUEST_TEMPLATE/*.md present",
        )
    return CheckResult(
        "pr_template",
        False,
        "missing PR template (.github/PULL_REQUEST_TEMPLATE.md preferred)",
    )



def check_dependabot(root: Path) -> CheckResult:
    candidates = [
        ".github/dependabot.yml",
        ".github/dependabot.yaml",
        ".dependabot/config.yml",
    ]
    for rel in candidates:
        if _exists(root, rel):
            return CheckResult("dependabot", True, f"{rel} present")
    return CheckResult(
        "dependabot",
        False,
        "missing Dependabot config (.github/dependabot.yml preferred)",
    )



def check_editorconfig(root: Path) -> CheckResult:
    ok = _exists(root, ".editorconfig")
    return CheckResult(
        "editorconfig",
        ok,
        ".editorconfig present" if ok else "missing .editorconfig at repository root",
    )


DEFAULT_CHECKS = (
    check_agents_md,
    check_readme,
    check_architecture_docs,
    check_tests_or_ci,
    check_license,
    check_security_md,
    check_codeowners,
    check_contributing,
    check_gitignore,
    check_changelog,
    check_pr_template,
    check_dependabot,
    check_editorconfig,
)


def run_checks(root: Path) -> list[CheckResult]:
    root = root.resolve()
    if not root.is_dir():
        raise FileNotFoundError(f"not a directory: {root}")
    return [fn(root) for fn in DEFAULT_CHECKS]

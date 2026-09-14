"""Catalog coherence guards (profiles, docs, versions, Makefile help).

One module instead of many tiny sync-test files — reduces maintainer churn when
catalogs change. Behavior is unchanged; only layout consolidated.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

from ai_guardrails import __version__
from ai_guardrails.checks import DEFAULT_CHECKS
from ai_guardrails.profiles import BASELINE, EXTRAS, PROFILE_NAMES, packs_for

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "install-packs.sh"
PACK_CATS = ("agents", "checklists", "prompts")


def _check_names() -> list[str]:
    names: list[str] = []
    for fn in DEFAULT_CHECKS:
        assert fn.__name__.startswith("check_")
        names.append(fn.__name__[len("check_") :])
    return names


def _bash_array(name: str, text: str) -> list[str]:
    m = re.search(rf"^{name}=\(\n(.*?)^\)", text, flags=re.M | re.S)
    assert m, f"array {name} not found"
    items: list[str] = []
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        items.append(line)
    return items


def _pack_rels() -> list[str]:
    rels: list[str] = []
    for cat in PACK_CATS:
        for path in sorted((ROOT / "packs" / cat).glob("*.md")):
            rels.append(f"{cat}/{path.name}")
    return rels


# --- profiles ↔ install-packs.sh ---------------------------------------------


def test_baseline_matches_script() -> None:
    text = SCRIPT.read_text()
    assert list(BASELINE) == _bash_array("baseline_packs", text)


def test_extras_match_script() -> None:
    text = SCRIPT.read_text()
    mapping = {
        "api": "api_extra",
        "ops": "ops_extra",
        "data": "data_extra",
        "security": "security_extra",
        "web": "web_extra",
    }
    for profile, arr in mapping.items():
        assert tuple(_bash_array(arr, text)) == EXTRAS[profile]


def test_profile_names_documented_in_script_usage() -> None:
    text = SCRIPT.read_text()
    for name in PROFILE_NAMES:
        if name == "full":
            continue
        assert name in text


def test_packs_for_composed() -> None:
    api = packs_for("api")
    assert api is not None
    assert api[: len(BASELINE)] == list(BASELINE)


def test_list_profiles_mentions_all_extra_packs() -> None:
    text = SCRIPT.read_text()
    out = subprocess.check_output(["bash", str(SCRIPT), "--list-profiles"], text=True)
    mapping = {
        "api": "api_extra",
        "ops": "ops_extra",
        "data": "data_extra",
        "security": "security_extra",
        "web": "web_extra",
    }
    for profile, arr in mapping.items():
        for pack in _bash_array(arr, text):
            assert pack in out, f"{profile}: list-profiles missing {pack}"
    for pack in _bash_array("baseline_packs", text):
        assert pack in out, f"baseline: list-profiles missing {pack}"


# --- docs catalogs -----------------------------------------------------------


def test_architecture_lists_all_default_checks() -> None:
    text = (ROOT / "docs/architecture/architecture.md").read_text()
    m = re.search(r"Default checks \((\d+)\): ([^\n]+)", text)
    assert m, "architecture.md missing Default checks line"
    names = _check_names()
    assert int(m.group(1)) == len(names)
    listed = [p.strip(" `.") for p in m.group(2).split(",")]
    assert listed == names


def test_validator_checks_table_lists_all_default_checks() -> None:
    text = (ROOT / "docs/references/validator-checks.md").read_text()
    names = _check_names()
    for name in names:
        assert f"`{name}`" in text, f"validator-checks.md missing {name}"
    rows = re.findall(r"^\| `([a-z_]+)` \|", text, flags=re.M)
    assert rows == names


def test_readme_lists_all_default_checks() -> None:
    text = (ROOT / "README.md").read_text()
    m = re.search(r"Default checks \((\d+)\): ([^\n]+)", text)
    assert m, "README.md missing Default checks line"
    names = _check_names()
    assert int(m.group(1)) == len(names)
    listed = [p.strip(" `.") for p in m.group(2).split(",")]
    assert listed == names


def test_install_md_profiles_table_lists_all_profile_names() -> None:
    text = (ROOT / "docs" / "references" / "install.md").read_text()
    m = re.search(
        r"## Profiles \(script\)\n\n\| Profile \| Intent \|\n\| --- \| --- \|\n((?:\|.+\n)+)",
        text,
    )
    assert m, "install.md missing Profiles (script) table"
    rows = re.findall(r"^\| `([a-z]+)` \|", m.group(1), flags=re.M)
    assert tuple(rows) == PROFILE_NAMES, f"install.md profiles {rows} != {PROFILE_NAMES}"


def test_profiles_md_documents_every_profile_name() -> None:
    text = (ROOT / "docs" / "references" / "profiles.md").read_text()
    for name in PROFILE_NAMES:
        assert (
            f"### `{name}`" in text
            or f"| `{name}` |" in text
            or f"`{name}`" in text
        ), f"profiles.md missing profile {name}"


def test_migrate_doc_lists_every_nested_pack_path() -> None:
    text = (ROOT / "docs" / "references" / "migrate-nested-install.md").read_text()
    missing = [rel for rel in _pack_rels() if rel not in text]
    assert not missing, (
        "migrate-nested-install.md missing nested pack path(s): " + ", ".join(missing)
    )


def test_migrate_doc_mentions_a11y_accessibility_pair() -> None:
    text = (ROOT / "docs" / "references" / "migrate-nested-install.md").read_text()
    assert "agents/a11y.md" in text
    assert "checklists/accessibility.md" in text
    assert "a11y" in text and "accessibility" in text


# --- version + Makefile help -------------------------------------------------


def test_version_metadata_aligned() -> None:
    pyproject = (ROOT / "pyproject.toml").read_text()
    m = re.search(r'^version\s*=\s*"([^"]+)"', pyproject, flags=re.M)
    assert m, "pyproject.toml missing version"
    expected = m.group(1)
    assert __version__ == expected

    citation = (ROOT / "CITATION.cff").read_text()
    cm = re.search(r"^version:\s*(\S+)", citation, flags=re.M)
    assert cm and cm.group(1) == expected

    readme = (ROOT / "README.md").read_text()
    rm = re.search(r"\*\*v(\d+\.\d+\.\d+)\*\*", readme)
    assert rm and rm.group(1) == expected

    changelog = (ROOT / "CHANGELOG.md").read_text()
    # Allow Unreleased section above the latest tagged heading
    lm = re.search(r"^## \[(\d+\.\d+\.\d+)\]", changelog, flags=re.M)
    assert lm and lm.group(1) == expected


def test_makefile_help_mentions_web_and_nested() -> None:
    text = (ROOT / "Makefile").read_text()
    assert "PROFILE=baseline|api|ops|data|security|web|full" in text
    assert "Nested install" in text
    assert "--no-strict" in text
    assert "docs/references/install.md" in text

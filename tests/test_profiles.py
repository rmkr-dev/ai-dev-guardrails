from __future__ import annotations

import json

from click.testing import CliRunner

from ai_guardrails.cli import main
from ai_guardrails.profiles import packs_for


def test_packs_for_baseline() -> None:
    packs = packs_for("baseline")
    assert packs is not None
    assert "agents/core.md" in packs
    assert packs[0] == "agents/core.md"


def test_packs_for_ops_includes_cost() -> None:
    packs = packs_for("ops")
    assert packs is not None
    assert "agents/cost.md" in packs
    assert "checklists/cost.md" in packs


def test_cli_profiles_text() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["profiles"])
    assert result.exit_code == 0
    assert "baseline:" in result.output
    assert "packs)" in result.output
    assert "agents/core.md" in result.output
    assert "ops:" in result.output


def test_cli_profiles_json_one() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["profiles", "--profile", "api", "--format", "json"])
    assert result.exit_code == 0
    data = json.loads(result.output)
    assert data["profile"] == "api"
    assert "agents/api.md" in data["packs"]


def test_cli_profiles_unknown() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["profiles", "--profile", "nope"])
    assert result.exit_code != 0


def test_cli_profiles_json_catalog() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["profiles", "--format", "json"])
    assert result.exit_code == 0
    data = json.loads(result.output)
    assert "profiles" in data
    for name in ("baseline", "api", "ops", "data", "security", "web", "full"):
        assert name in data["profiles"]
    assert "agents/core.md" in data["profiles"]["baseline"]
    assert "agents/frontend.md" in data["profiles"]["web"]
    assert isinstance(data["profiles"]["full"], str)
    assert data["counts"]["baseline"] == len(data["profiles"]["baseline"])
    assert data["counts"]["web"] == len(data["profiles"]["web"])
    assert data["counts"]["full"] is None


def test_cli_profiles_web_text() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["profiles", "--profile", "web"])
    assert result.exit_code == 0
    assert "agents/frontend.md" in result.output
    assert "agents/a11y.md" in result.output
    assert "checklists/accessibility.md" in result.output


def test_web_profile_includes_frontend() -> None:
    from ai_guardrails.profiles import PROFILE_NAMES

    assert "web" in PROFILE_NAMES
    packs = packs_for("web")
    assert packs is not None
    assert "agents/frontend.md" in packs
    assert "checklists/frontend.md" in packs

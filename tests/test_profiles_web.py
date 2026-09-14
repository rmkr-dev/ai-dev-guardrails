
from ai_guardrails.profiles import PROFILE_NAMES, packs_for

def test_web_profile_includes_frontend():
    assert "web" in PROFILE_NAMES
    packs = packs_for("web")
    assert packs is not None
    assert "agents/frontend.md" in packs
    assert "checklists/frontend.md" in packs

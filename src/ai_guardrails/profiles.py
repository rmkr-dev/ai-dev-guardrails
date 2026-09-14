"""Install profile catalog (mirrors scripts/install-packs.sh)."""

from __future__ import annotations

BASELINE = (
    "agents/core.md",
    "agents/security.md",
    "agents/secrets.md",
    "agents/testing.md",
    "agents/docs.md",
    "agents/commits.md",
    "checklists/definition-of-done.md",
    "checklists/pr-self-review.md",
)

EXTRAS: dict[str, tuple[str, ...]] = {
    "api": (
        "agents/api.md",
        "agents/deps.md",
        "agents/supply-chain.md",
        "prompts/test-plan.md",
        "prompts/change-impact.md",
        "checklists/supply-chain.md",
    ),
    "ops": (
        "agents/observability.md",
        "agents/ci.md",
        "agents/incidents.md",
        "agents/performance.md",
        "agents/a11y.md",
        "agents/privacy.md",
        "agents/resilience.md",
        "agents/cost.md",
        "prompts/incident-response.md",
        "prompts/runbook-draft.md",
        "prompts/privacy-review.md",
        "checklists/observability.md",
        "checklists/accessibility.md",
        "checklists/resilience.md",
        "checklists/cost.md",
    ),
    "data": (
        "agents/data.md",
        "agents/api.md",
        "prompts/migration-review.md",
        "prompts/change-impact.md",
    ),
    "security": (
        "agents/security.md",
        "agents/secrets.md",
        "agents/privacy.md",
        "agents/threat-model.md",
        "prompts/security-review.md",
        "prompts/privacy-review.md",
        "prompts/threat-model.md",
    ),
    "web": (
        "agents/frontend.md",
        "agents/a11y.md",
        "agents/i18n.md",
        "checklists/frontend.md",
        "checklists/accessibility.md",
        "checklists/i18n.md",
    ),
}

PROFILE_NAMES = ("baseline", "api", "ops", "data", "security", "web", "full")


def packs_for(profile: str) -> list[str] | None:
    """Return pack paths for a named profile, or None if unknown.

    ``full`` returns None to signal ``install-packs.sh --profile full`` should
    expand from the packs/ tree rather than a fixed list.
    """
    if profile == "baseline":
        return list(BASELINE)
    if profile == "full":
        return None
    extra = EXTRAS.get(profile)
    if extra is None:
        raise KeyError(profile)
    # de-dupe while preserving order
    seen: set[str] = set()
    out: list[str] = []
    for p in list(BASELINE) + list(extra):
        if p not in seen:
            seen.add(p)
            out.append(p)
    return out


def describe_profiles() -> dict[str, list[str] | str]:
    """Human/machine catalog for ``ai-guardrails profiles``."""
    catalog: dict[str, list[str] | str] = {"baseline": list(BASELINE)}
    for name in ("api", "ops", "data", "security", "web"):
        catalog[name] = packs_for(name) or []
    catalog["full"] = "all packs/agents, packs/checklists, packs/prompts *.md"
    return catalog

"""Keep migrate-nested-install.md nested targets aligned with packs/ tree."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK_CATS = ("agents", "checklists", "prompts")
MIGRATE = ROOT / "docs" / "references" / "migrate-nested-install.md"


def _pack_rels() -> list[str]:
    rels: list[str] = []
    for cat in PACK_CATS:
        for path in sorted((ROOT / "packs" / cat).glob("*.md")):
            rels.append(f"{cat}/{path.name}")
    return rels


def test_migrate_doc_lists_every_nested_pack_path() -> None:
    text = MIGRATE.read_text()
    missing = [rel for rel in _pack_rels() if rel not in text]
    assert not missing, (
        "migrate-nested-install.md missing nested pack path(s): "
        + ", ".join(missing)
    )


def test_migrate_doc_mentions_a11y_accessibility_pair() -> None:
    text = MIGRATE.read_text()
    assert "agents/a11y.md" in text
    assert "checklists/accessibility.md" in text
    assert "a11y" in text and "accessibility" in text

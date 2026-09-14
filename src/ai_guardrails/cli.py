"""CLI entrypoint: ai-guardrails check <path>."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import click

from ai_guardrails import __version__
from ai_guardrails.checks import CHECK_SUMMARIES, DEFAULT_CHECKS, run_checks
from ai_guardrails.profiles import PROFILE_NAMES, describe_profiles, packs_for


def _parse_name_list(value: str | None) -> set[str] | None:
    if value is None or value.strip() == "":
        return None
    names = {part.strip() for part in value.split(",") if part.strip()}
    return names or None



def _suggest_names(unknown: set[str], known: set[str]) -> str:
    """Best-effort close matches for unknown check names."""
    hints: list[str] = []
    for name in sorted(unknown):
        # Prefer prefix / containment matches; fall back to shared prefix length
        cands = sorted(
            known,
            key=lambda k: (
                0 if k.startswith(name) or name.startswith(k) else 1,
                0 if name in k or k in name else 1,
                -sum(1 for a, b in zip(name, k) if a == b),
                k,
            ),
        )
        top = [c for c in cands[:3] if c]
        if top:
            hints.append(f"{name} (did you mean {', '.join(top)}?)")
        else:
            hints.append(name)
    return ", ".join(hints)


def _filter_results(results, only: set[str] | None, skip: set[str] | None):
    known = {r.name for r in results}
    if only is not None:
        unknown = only - known
        if unknown:
            raise click.ClickException(
                "unknown check name(s) for --only: " + _suggest_names(unknown, known)
            )
        results = [r for r in results if r.name in only]
    if skip is not None:
        unknown = skip - known
        if unknown:
            raise click.ClickException(
                "unknown check name(s) for --skip: " + _suggest_names(unknown, known)
            )
        results = [r for r in results if r.name not in skip]
    return results


@click.group()
@click.version_option(__version__, prog_name="ai-guardrails")
def main() -> None:
    """Repo hygiene checks for ai-dev-guardrails consumers."""


@main.command("check")
@click.argument("target", type=click.Path(exists=True, file_okay=False, path_type=Path))
@click.option(
    "--strict/--no-strict",
    default=True,
    show_default=True,
    help="Exit non-zero when any check fails.",
)
@click.option(
    "--format",
    "fmt",
    type=click.Choice(["text", "json"], case_sensitive=False),
    default="text",
    show_default=True,
    help="Output format.",
)
@click.option(
    "--only",
    "only_names",
    default=None,
    help="Comma-separated check names to run (default: all).",
)
@click.option(
    "--skip",
    "skip_names",
    default=None,
    help="Comma-separated check names to omit.",
)
@click.option(
    "--fail-only",
    is_flag=True,
    default=False,
    help="In text mode, print only failing checks (summary still shown).",
)
def check_cmd(
    target: Path,
    strict: bool,
    fmt: str,
    only_names: str | None,
    skip_names: str | None,
    fail_only: bool,
) -> None:
    """Check TARGET repo for required hygiene files and indicators."""
    results = run_checks(target)
    only = _parse_name_list(only_names)
    skip = _parse_name_list(skip_names)
    results = _filter_results(results, only, skip)
    failed = sum(1 for r in results if not r.ok)
    if fmt == "json":
        payload = {
            "version": __version__,
            "root": str(target.resolve()),
            "passed": len(results) - failed,
            "failed": failed,
            "total": len(results),
            "checks": [
                {"name": r.name, "ok": r.ok, "detail": r.detail} for r in results
            ],
        }
        click.echo(json.dumps(payload, indent=2, sort_keys=True))
    else:
        for r in results:
            if fail_only and r.ok:
                continue
            mark = "PASS" if r.ok else "FAIL"
            click.echo(f"[{mark}] {r.name}: {r.detail}")
        click.echo(f"{len(results) - failed}/{len(results)} checks passed")
    if strict and failed:
        sys.exit(1)


@main.command("list-checks")
@click.option(
    "--format",
    "fmt",
    type=click.Choice(["text", "json"], case_sensitive=False),
    default="text",
    show_default=True,
    help="Output format.",
)
@click.option(
    "--describe/--no-describe",
    default=False,
    show_default=True,
    help="Include short summaries (text: name — summary; json: checks as objects).",
)
def list_checks_cmd(fmt: str, describe: bool) -> None:
    """Print the default check names in run order."""
    names = [fn.__name__.removeprefix("check_") for fn in DEFAULT_CHECKS]
    if fmt == "json":
        if describe:
            payload = {
                "checks": [
                    {"name": n, "summary": CHECK_SUMMARIES.get(n, "")} for n in names
                ],
                "total": len(names),
            }
        else:
            payload = {"checks": names, "total": len(names)}
        click.echo(json.dumps(payload, indent=2))
    else:
        for name in names:
            if describe:
                summary = CHECK_SUMMARIES.get(name, "")
                click.echo(f"{name} — {summary}" if summary else name)
            else:
                click.echo(name)



@main.command("profiles")
@click.option(
    "--format",
    "fmt",
    type=click.Choice(["text", "json"], case_sensitive=False),
    default="text",
    show_default=True,
    help="Output format.",
)
@click.option(
    "--profile",
    "profile_name",
    default=None,
    help="Show packs for one profile (baseline|api|ops|data|security|web|full).",
)
def profiles_cmd(fmt: str, profile_name: str | None) -> None:
    """Print install profile catalog (mirrors scripts/install-packs.sh)."""
    if profile_name is not None:
        if profile_name not in PROFILE_NAMES:
            raise click.ClickException(
                f"unknown profile: {profile_name}; choose from {', '.join(PROFILE_NAMES)}"
            )
        if profile_name == "full":
            packs: list[str] | str = "all packs/agents, packs/checklists, packs/prompts *.md"
        else:
            packs = packs_for(profile_name) or []
        if fmt == "json":
            click.echo(
                json.dumps({"profile": profile_name, "packs": packs}, indent=2, sort_keys=True)
            )
        else:
            if isinstance(packs, str):
                click.echo(f"{profile_name}: {packs}")
            else:
                click.echo(f"{profile_name}: ({len(packs)} packs)")
                for p in packs:
                    click.echo(f"  {p}")
        return

    catalog = describe_profiles()
    if fmt == "json":
        counts = {
            name: (len(packs) if isinstance(packs, list) else None)
            for name, packs in catalog.items()
        }
        click.echo(
            json.dumps(
                {"profiles": catalog, "counts": counts},
                indent=2,
                sort_keys=True,
            )
        )
    else:
        for name in PROFILE_NAMES:
            packs = catalog[name]
            if isinstance(packs, str):
                click.echo(f"{name}: {packs}")
            else:
                click.echo(f"{name}: ({len(packs)} packs)")
                for p in packs:
                    click.echo(f"  {p}")
            click.echo("")


if __name__ == "__main__":
    main()

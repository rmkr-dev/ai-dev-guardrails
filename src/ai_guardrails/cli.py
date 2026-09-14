"""CLI entrypoint: ai-guardrails check <path>."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import click

from ai_guardrails import __version__
from ai_guardrails.checks import DEFAULT_CHECKS, run_checks


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
def check_cmd(target: Path, strict: bool, fmt: str) -> None:
    """Check TARGET repo for required hygiene files and indicators."""
    results = run_checks(target)
    failed = sum(1 for r in results if not r.ok)
    if fmt == "json":
        payload = {
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
def list_checks_cmd(fmt: str) -> None:
    """Print the default check names in run order."""
    names = [fn.__name__.removeprefix("check_") for fn in DEFAULT_CHECKS]
    if fmt == "json":
        click.echo(json.dumps({"checks": names, "total": len(names)}, indent=2))
    else:
        for name in names:
            click.echo(name)


if __name__ == "__main__":
    main()

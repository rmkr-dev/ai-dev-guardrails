"""CLI entrypoint: ai-guardrails check <path>."""

from __future__ import annotations

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
def check_cmd(target: Path, strict: bool) -> None:
    """Check TARGET repo for required hygiene files and indicators."""
    results = run_checks(target)
    failed = 0
    for r in results:
        mark = "PASS" if r.ok else "FAIL"
        click.echo(f"[{mark}] {r.name}: {r.detail}")
        if not r.ok:
            failed += 1
    click.echo(f"{len(results) - failed}/{len(results)} checks passed")
    if strict and failed:
        sys.exit(1)


@main.command("list-checks")
def list_checks_cmd() -> None:
    """Print the default check names in run order."""
    for fn in DEFAULT_CHECKS:
        # Derive stable names from CheckResult by invoking against a throwaway? 
        # Prefer explicit order matching DEFAULT_CHECKS implementation names.
        raw = fn.__name__.removeprefix("check_")
        click.echo(raw)




if __name__ == "__main__":
    main()

"""Run bash tests/test_install_packs.sh via pytest so CI covers install UX."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_install_packs_shell_suite() -> None:
    script = ROOT / "tests" / "test_install_packs.sh"
    assert script.is_file()
    proc = subprocess.run(
        ["bash", str(script)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        sys.stderr.write(proc.stdout + "\n" + proc.stderr)
    assert proc.returncode == 0, proc.stderr or proc.stdout
    assert "All install-packs shell tests passed." in proc.stdout

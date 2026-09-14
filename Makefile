.PHONY: test check list-checks install install-packs lint fmt help

install:
	python -m pip install -e ".[dev]"

test:
	pytest -q

check:
	ai-guardrails check .

list-checks:
	ai-guardrails list-checks

# Example: make install-packs TARGET=/path/to/repo PROFILE=baseline
install-packs:
	@test -n "$(TARGET)" || (echo "Set TARGET=/path/to/consumer-repo" >&2; exit 2)
	bash scripts/install-packs.sh "$(TARGET)" --profile "$(or $(PROFILE),baseline)"

# Optional local hygiene (no extra deps required beyond stdlib/pytest)
lint:
	python -m compileall -q src tests
	pytest -q --collect-only >/dev/null

fmt:
	@echo "No autoformatter configured yet; run your editor format-on-save or add ruff/black later."

help:
	@echo "Targets: install test check list-checks lint fmt install-packs"
	@echo "install-packs requires TARGET=/path/to/repo [PROFILE=baseline|api|ops|data|security|full]"
	@echo "Script extras: --dry-run, --list-profiles (see docs/references/install.md)"

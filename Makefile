.PHONY: test check list-checks profiles install install-packs install-packs-test lint fmt help

install:
	python -m pip install -e ".[dev]"

test:
	pytest -q

check:
	ai-guardrails check .

list-checks:
	ai-guardrails list-checks

profiles:
	ai-guardrails profiles

# Example: make install-packs TARGET=/path/to/repo PROFILE=baseline
# Optional: DEST=docs/guardrails DRY_RUN=1 QUIET=1
install-packs:
	@test -n "$(TARGET)" || (echo "Set TARGET=/path/to/consumer-repo" >&2; exit 2)
	@args="--profile $(or $(PROFILE),baseline)"; \
	 if [ -n "$(DEST)" ]; then args="$$args --dest $(DEST)"; fi; \
	 if [ "$(DRY_RUN)" = "1" ]; then args="$$args --dry-run"; fi; \
	 if [ "$(QUIET)" = "1" ]; then args="$$args --quiet"; fi; \
	 bash scripts/install-packs.sh "$(TARGET)" $$args

install-packs-test:
	bash tests/test_install_packs.sh

# Optional local hygiene (no extra deps required beyond stdlib/pytest)
lint:
	python -m compileall -q src tests
	pytest -q --collect-only >/dev/null

fmt:
	@echo "No autoformatter configured yet; run your editor format-on-save or add ruff/black later."

help:
	@echo "Targets: install test check list-checks profiles lint fmt install-packs install-packs-test"
	@echo "install-packs requires TARGET=/path/to/repo [PROFILE=baseline|api|ops|data|security|web|full]"
	@echo "  optional: DEST=rel/path DRY_RUN=1 QUIET=1"
	@echo "Script extras: --dry-run, --quiet, --list-profiles, --version (see docs/references/install.md)"
	@echo "  Nested install; flat 0.2.x leftovers are warned (not deleted) on install/--dry-run"
	@echo "  Profiles include web (frontend/a11y/i18n); see docs/references/install.md"
	@echo "CLI: ai-guardrails profiles | check --only/--skip/--fail-only/--no-strict | list-checks --describe"

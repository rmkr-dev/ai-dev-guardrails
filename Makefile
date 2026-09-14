.PHONY: test check list-checks install install-packs

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

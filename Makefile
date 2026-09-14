.PHONY: test check list-checks install

install:
	python -m pip install -e ".[dev]"

test:
	pytest -q

check:
	ai-guardrails check .

list-checks:
	ai-guardrails list-checks

# Testing guardrails (Copilot / Claude / Codex)

Use with [core.md](core.md). For agents writing or reviewing tests.

## Defaults

- Ship tests in the **same PR** as the behavior they cover.
- Prefer the repo’s existing test framework; do not introduce a second one without an ADR.
- Name tests after behavior (`test_check_fails_without_readme`), not implementation trivia.
- Avoid flaky time/network dependencies; use fakes or temp directories.
- Keep fixtures small and local to the test module unless shared helpers already exist.

## What “enough” means for a slice

- Happy path for the new behavior
- At least one meaningful failure / edge path
- CLI or public API exit codes/messages when those are user-visible
- Regression coverage when fixing a bug (reproduce failing case first when practical)

## Layout and naming

- Mirror the package layout under `tests/` when the repo already does.
- Prefer `test_*.py` / `*_test.py` conventions the repo uses; do not invent a third style.
- One logical behavior per test function; share setup via fixtures, not copy-paste blobs.

## Isolation

- Tests must not require network, cloud credentials, or live third-party services by default.
- Prefer temp dirs and in-memory fakes over mutating the developer’s real home/repo state.
- Do not depend on test ordering; each test should stand alone.

## Do not

- Delete or skip failing tests to “get green” without fixing the cause
- Commit recorded secrets inside fixtures
- Add heavyweight end-to-end harnesses when unit tests suffice for the slice
- Assert on wall-clock timestamps or exact log formatting unless that is the contract
- Leave `pytest.mark.skip` / `xfail` without a linked issue or PR note

## Review prompt (optional)

When asking Copilot / Claude / Codex to review tests, include: “List missing edge cases, flaky patterns, and any fixtures that could leak secrets.”

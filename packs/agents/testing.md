# Testing guardrails (Copilot / Claude / Codex)

Use with [core.md](core.md). For agents writing or reviewing tests.

## Defaults

- Ship tests in the **same PR** as the behavior they cover.
- Prefer the repo’s existing test framework; do not introduce a second one without an ADR.
- Name tests after behavior (`test_check_fails_without_readme`), not implementation trivia.
- Avoid flaky time/network dependencies; use fakes or temp directories.

## What “enough” means for a slice

- Happy path for the new behavior
- At least one meaningful failure / edge path
- CLI or public API exit codes/messages when those are user-visible

## Do not

- Delete or skip failing tests to “get green” without fixing the cause
- Commit recorded secrets inside fixtures
- Add heavyweight end-to-end harnesses when unit tests suffice for the slice

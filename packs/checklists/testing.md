# Testing readiness checklist

For humans and agents before merging behavior changes. Pair with [agents/testing.md](../agents/testing.md).

- [ ] Tests ship in the **same PR** as the behavior
- [ ] Happy path covered
- [ ] At least one meaningful failure / edge path covered
- [ ] Bug fixes include a regression test when practical
- [ ] No network/cloud credentials required for default unit tests
- [ ] No skipped/xfailed tests without a linked issue or PR note
- [ ] Fixtures contain no real secrets
- [ ] CLI/public API messages and exit codes asserted when user-visible
- [ ] Local `pytest` (or repo equivalent) passes

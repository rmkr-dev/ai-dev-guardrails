# Frontend / UI checklist (pre-merge)

Use with `agents/frontend.md` when a PR changes web UI, docs chrome, or rich human-facing surfaces.

- [ ] Existing components / styles reused (no drive-by framework)
- [ ] Keyboard and accessible name for new controls
- [ ] Loading / empty / error states included
- [ ] Performance: no unbounded client fan-out
- [ ] Copy reviewed (i18n if the repo localizes)
- [ ] a11y checks/tests updated when the repo has them

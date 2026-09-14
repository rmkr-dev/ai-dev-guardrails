# Frontend / UI surface guardrails (Copilot / Claude / Codex)

Use with [core.md](core.md), [a11y.md](a11y.md), [performance.md](performance.md), and [i18n.md](i18n.md). For agents touching web UI, docs sites, or rich CLI help that users read.

## Defaults

- Prefer patterns and components **already in the consumer repo**; do not introduce a new UI framework for a one-line fix.
- Accessibility is not optional for interactive UI (see [a11y.md](a11y.md)).
- Do not invent design-system tokens or theme files the product does not use.
- Keep user-visible strings reviewable (and i18n-ready when the repo already localizes).

## Before coding

1. Name the surface (page, component, CLI help, docs site).
2. List existing components / CSS approach / test harness to reuse.
3. Note keyboard and screen-reader expectations for new controls.

## While coding

- Ship loading / empty / error states with the feature, not as a follow-up.
- Avoid layout thrash and unbounded client fetches (see [performance.md](performance.md) and [cost.md](cost.md)).
- Prefer semantic HTML / native controls before ARIA folklore.
- Update a11y and visual regression tests the repo already runs.

## Slice checklist

- [ ] Reused existing UI primitives where possible
- [ ] Keyboard path works for new interactive controls
- [ ] Loading / empty / error states present
- [ ] No new framework without human approval
- [ ] User-visible copy is intentional (and localized if required)

## Do not

- Add a CSS-in-JS or bundler toolchain “while here”
- Ship icon-only controls without accessible names
- Block paste / zoom / text resize without a documented exception
- Hide errors behind spinners forever

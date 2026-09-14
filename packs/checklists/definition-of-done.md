# Definition of Done checklist

For humans and agents (Copilot / Claude / Codex). Copy into PR templates or keep under `docs/` / `packs/` in the consumer repo.

A slice is **done** when every applicable item is true:

## Scope

- [ ] The change matches the agreed slice; nothing extra landed “for later convenience”
- [ ] Unrelated refactors were deferred or split into another PR

## Completeness

- [ ] Behavior (code) for the slice is present
- [ ] Tests for new or changed behavior ship in the same PR
- [ ] CI / automation updates required by the slice are included
- [ ] User- or contributor-facing docs that describe the behavior are updated

## Honesty

- [ ] Docs match reality (planned work is labeled planned)
- [ ] No stub implementations that pretend to work
- [ ] No badges or required checks for CI that is not configured
- [ ] No orphan files (everything added has a reader and a link)

## Safety

- [ ] No secrets, credentials, or personal contact details in the tree or history of this PR
- [ ] High-impact items (auth, license, security defaults, public API) are flagged for a human

## Review readiness

- [ ] Commit messages are conventional and stand alone
- [ ] PR description explains intent, risk, and how to validate
- [ ] Local documented checks pass
- [ ] The repo would remain coherent if no further PR ever shipped

# Core agent guardrails (Copilot / Claude / Codex)

Use this module when an agent (or a human pairing with one) changes a software repository. Paste into or link from the target repo’s `AGENTS.md`.

## Mission

Ship the **smallest correct complete slice**. Prefer clarity for the next human reviewer over cleverness.

## Before coding

1. Read the target repo’s `README.md`, `AGENTS.md` (if present), and docs that touch the change.
2. Restate the slice in one short paragraph. If it is larger than one reviewable PR, split it.
3. List files you expect to touch. Stop if the list spans unrelated concerns.

## While coding

- Prefer existing patterns in the repo over new frameworks.
- Update behavior, tests, and docs that the slice requires **in the same change**.
- Do not leave stubs that pretend to work, TODOs that block production paths, or docs that describe missing files.
- Do not add Node/npm unless the repo already uses it and the slice requires it.
- Do not commit secrets, tokens, private keys, or `.env` files.

## After coding

1. Run the repo’s documented checks (tests, linters, validators).
2. Diff as a stranger: are commit messages and the PR body enough without chat history?
3. Confirm no orphan files and no speculative “for later” scaffolding.

## Out of scope for this module

Eval harnesses, cloud agent runtimes, and full org templates belong in other repositories. Keep this module focused on day-to-day engineering guardrails.

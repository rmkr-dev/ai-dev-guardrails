# Test plan prompt (Copilot / Claude / Codex)

Paste when drafting the Test plan section of a PR.

```text
Given this PR diff and title/body, write a concrete Test plan checklist.

Include:
- [ ] commands to run locally (pytest, linters, ai-guardrails check, etc.)
- [ ] docs or links a reviewer should open
- [ ] edge cases worth manual probing
- [ ] any high-impact items needing human approval

Prefer the repo’s existing scripts. Do not invent CI jobs that are not in the tree.
No secrets. No company names.
```

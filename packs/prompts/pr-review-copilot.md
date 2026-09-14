# PR review prompt — GitHub Copilot

Use in Copilot Chat on a PR page or with the diff attached. Complements [pr-review.md](pr-review.md).

```text
You are reviewing a GitHub pull request with Copilot. Focus on merge readiness.

Priorities for this tool:
- Call out CI-relevant gaps (missing tests, broken scripts, workflow permission creep)
- Prefer inline-style findings: file path + what to change
- Flag AGENTS.md / pack contradictions if the repo uses ai-dev-guardrails modules

Structure the answer as:
## Blockers
## Suggestions
## Test plan gaps

Do not invent files that are not in the diff. Do not suggest Node/npm unless the repo already uses it.
```

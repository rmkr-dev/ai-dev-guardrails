# Release checklist

For humans tagging a version of a pack or library repo (and agents drafting the release).

- [ ] CHANGELOG entry matches files that actually shipped
- [ ] Version in packaging metadata matches the tag (`pyproject.toml` / equivalent)
- [ ] README status line and docs still match reality
- [ ] CI green on the commit to tag
- [ ] Annotated tag message explains the release in one line
- [ ] GitHub Release notes summarize consumer-visible changes
- [ ] No secrets in tag message, release notes, or artifacts

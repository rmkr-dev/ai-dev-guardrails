# Supply-chain checklist

For humans and agents before merging dependency, CI permission, or release-publish changes.

- [ ] Lockfile / pins updated with the dependency change
- [ ] Major upgrades justified in the PR body
- [ ] No new long-lived secrets in workflows or docs
- [ ] Actions `permissions` remain least-privilege
- [ ] Install scripts do not pipe unpinned remote scripts to a shell
- [ ] Publish / signing / registry steps call out human approval when needed
- [ ] Dependabot/renovate changes are intentional and scoped

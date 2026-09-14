# Cost / capacity checklist (pre-merge)

Use with `agents/cost.md` when a PR adds cloud resources, always-on jobs, large artifacts, or high-cardinality telemetry.

- [ ] Cost drivers named in the PR (compute, storage, egress, vendor units)
- [ ] Retention and metric/log cardinality are bounded
- [ ] Always-on resources have an owner / scale note
- [ ] No multi-GB fixtures committed to git
- [ ] Retries / polling budgets are finite
- [ ] Human approval recorded for new paid vendors or regions

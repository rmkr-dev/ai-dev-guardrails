# Resilience checklist

For humans and agents before merging retry/timeout/degradation changes.

- [ ] Timeouts are finite and match consumer norms
- [ ] Retries are bounded; backoff/jitter considered
- [ ] Idempotency assumptions documented for retried operations
- [ ] Dependency-down / timeout tests updated
- [ ] Logs/metrics cover failures without secrets or raw PII
- [ ] User-visible degradation behavior is intentional
- [ ] New cross-service policies call out human approval

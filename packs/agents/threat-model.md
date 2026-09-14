# Threat modeling guardrails (Copilot / Claude / Codex)

Use with [security.md](security.md), [secrets.md](secrets.md), and [privacy.md](privacy.md). For agents drafting or updating lightweight threat notes for a slice.

## Defaults

- Prefer **asset / adversary / control** language over theater. Stay proportional to the change.
- Do not invent compliance frameworks (SOC2, ISO) claims the consumer did not ask for.
- Never include real secrets, customer names, or internal-only hostnames in examples.
- Link to existing SECURITY.md and AuthZ patterns in the repo.

## Before drafting

1. Name the assets touched (data, credentials, admin surfaces, CI).
2. List trust boundaries that move with this PR.
3. Note existing controls (authn, authz, encryption, logging) the code already uses.

## While drafting

- Enumerate realistic threats for *this* slice, not a full STRIDE encyclopedia.
- Map each threat to a mitigation that lands in the same PR or a tracked follow-up.
- Call out residual risk needing human approval.

## Slice checklist

- [ ] Assets and trust boundaries stated
- [ ] Threats are specific to the diff
- [ ] Mitigations are concrete (code, config, or process)
- [ ] Residual risks labeled for humans
- [ ] No secrets or real customer data in the note

## Do not

- Rubber-stamp “no security impact” on auth/crypto/CI permission changes
- Copy a generic STRIDE table without tying it to the change
- Promise certifications or audits

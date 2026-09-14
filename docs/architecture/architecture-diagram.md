# Architecture diagram

```mermaid
flowchart LR
  subgraph packRepo["ai-dev-guardrails"]
    AG["AGENTS.md"]
    DOC["docs/architecture"]
    PACKS["packs/ agents|checklists|prompts"]
    CLI["ai-guardrails check"]
    INST["install-packs.sh"]
  end

  subgraph consumer["Consumer repository"]
    CAG["AGENTS.md nested links"]
    CMOD["docs/guardrails/ agents|checklists|prompts"]
    CCI["Optional CI invoking CLI"]
  end

  AG --> CAG
  PACKS --> INST
  INST --> CMOD
  CLI --> CCI
  DOC -. describes .-> packRepo
```

All solid edges reflect files that exist in this repository today. Consumer CI wiring is optional and owned by the consumer.

Install preserves nested `agents/` / `checklists/` / `prompts/` paths (ADR-007 / ADR-008). Flat 0.2.x leftovers are warned, not deleted — see [migrate-nested-install.md](../references/migrate-nested-install.md).

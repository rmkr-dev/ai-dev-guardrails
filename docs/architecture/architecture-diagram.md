# Architecture diagram

Mermaid view of **this** repository’s surfaces and how a consumer repo relates to them.

```mermaid
flowchart LR
  subgraph packRepo["ai-dev-guardrails"]
    AG["AGENTS.md"]
    DOC["docs/architecture"]
    PACKS["packs/ agents checklists prompts"]
    CLI["ai-guardrails CLI planned"]
  end

  subgraph consumer["Consumer repository"]
    CAG["AGENTS.md copy"]
    CMOD["Selected pack modules"]
    CCI["Optional CI check"]
  end

  AG --> CAG
  PACKS --> CMOD
  CLI -.-> CCI
  DOC -. describes .-> packRepo
```

Solid edges are current. The CLI edge remains planned until the Python package ships.

# Architecture diagram

Mermaid view of **this** repository’s surfaces and how a consumer repo relates to them. Docs match reality: packs and the CLI are shown as *planned* until they exist in the tree.

```mermaid
flowchart LR
  subgraph packRepo["ai-dev-guardrails"]
    AG["AGENTS.md"]
    DOC["docs/architecture"]
    PACKS["packs/ planned"]
    CLI["ai-guardrails CLI planned"]
  end

  subgraph consumer["Consumer repository"]
    CAG["AGENTS.md copy"]
    CMOD["Selected pack modules"]
    CCI["Optional CI check"]
  end

  AG --> CAG
  PACKS -.-> CMOD
  CLI -.-> CCI
  DOC -. describes .-> packRepo
```

Solid edges are current. Dashed edges are planned follow-up PRs.

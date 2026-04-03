# AIOS Genesis Research Archive

This directory preserves the foundational research reports that informed the AIOS architecture and governance framework. These are the deep research outputs from the original planning agent sessions that produced the architectural decisions encoded in the governing documents.

**These files are read-only historical artifacts.** They are never modified, but they serve as intellectual provenance for the governing documents.

---

## Research Reports

### Original Planning Agent Outputs

| Report | What It Informed |
|--------|-----------------|
| `ai_os_market_analysis.md` | MPOA economics, pricing model ($99-198/mo subscriptions), competitive landscape (Twilio, Genesys, Salesforce), moat analysis, TAM/SAM/SOM |
| `migration_plan.md` | Technical Manifesto containerization strategy, Docker extraction, Strangler Fig migration from monolith to AI OS |
| `node_architecture.md` | Direct ancestor of NodeContract specification, intent loop design, 4 UI planes, MCP integration, the formal AIOS specification (877 lines) |
| `ui_control_plane.md` | DCP design with OPA policy-as-code, GitOps patterns, SLSA/Sigstore supply chain integrity, OpenTelemetry observability |
| `internal_dev_control_plane.md` | Constitution's legislative process, DCP governance gates (intake -> resolution -> evidence -> approval -> promotion), evidence management |
| `coding_intent_loop_plan.md` | AIP and agents.md, internal coding swarm model, governed agent execution within the OS's own intent loop |

### Strategic & Business Analysis

| Report | What It Informed |
|--------|-----------------|
| `ai_os_doctrine.md` | The 10 Operating Doctrines — foundational design philosophy defining intent-first architecture, model-proposes/OS-decides, DISC+ARCH behavioral profiles, proficiency gating, skill indirection, fallback routes, node contracts, voice-first constraints, coding swarm governance, single authority per class |
| `redhat_comparison.md` | Strategic positioning of Gateway Global AI as "Red Hat for AI+CX" — distribution model analogy, unit economics ($198/mo vs $8-15K/mo DIY), self-extending coding swarm as multiplier, appliance deployment strategy |
| `business_plan.md` | Full business plan with meta prompt, market sizing (TAM/SAM/SOM), revenue projections ($90M-$5.4B ARR scenarios), valuation framework (6-20x ARR multiples), go-to-market strategy, Red Hat acquisition comparable |
| `ai_os_market_analysis_full.md` | Detailed market & business analysis with sourced data — CRM ($113B), contact center ($47.7B), voice AI ($15.5B) market sizes, competitor revenue benchmarks (Twilio $1.3B, Genesys $3B, Salesforce $38B), deployment model analysis, moat assessment |

---

## How These Relate to the Governing Documents

```
Research                          Governing Documents
────────────────────────          ──────────────────────────────
ai_os_market_analysis.md    ──>   MPOA (economics, pricing)
ai_os_market_analysis_full.md     Marketplace Terms (vendor model)

migration_plan.md           ──>   Technical Manifesto (containerization)
                                  Docker Extraction (deployment)

node_architecture.md        ──>   NodeContract Specification
                                  PolicyRecord Specification
                                  Technical Manifesto (intent loop, UI planes)

ui_control_plane.md         ──>   Governance Constitution (legislative process)
                                  Technical Manifesto (DCP, supply chain)

internal_dev_control_plane.md ──> Governance Constitution (DCP gates)
                                  CLI Developer Guide (validation pipeline)

coding_intent_loop_plan.md  ──>   Agent Integration Protocol (AIP)
                                  agents.md (agent mandate)

ai_os_doctrine.md           ──>   Technical Manifesto (10 doctrines)
                                  All governing documents (design philosophy)

redhat_comparison.md        ──>   MPOA (distribution model, unit economics)
                                  Business strategy (appliance, subscription)

business_plan.md            ──>   MPOA (revenue model, market positioning)
                                  Marketplace Terms (go-to-market strategy)
```

---

## Usage in Meta-Prompts

These reports can be optionally injected into document creation and source analysis meta-prompts when you want the AI to understand the full historical reasoning behind a decision, not just the current governing text. Pass the `--include-research` flag to the relevant script (when supported).

# AIOS Document Registry

*Auto-generated on 2026-04-02 by `scripts/registry_generator.py`. Do not edit manually.*

---

## All Documents

| Document ID | Title | Version | Status | Category | Path |
|-------------|-------|---------|--------|----------|------|
| AIOS-CORE-002 | The Gateway Global AIOS Governance Constitution | 1.0.0 | ratified | core | `core\governance_constitution.md` |
| AIOS-CORE-003 | Gateway Global AIOS Master Platform Operating Agreement | 3.0.0 | ratified | core | `core\master_platform_operating_agreement.md` |
| AIOS-CORE-001 | AIOS Technical Manifesto & Platform Economics | 1.0.0 | ratified | core | `core\technical_manifesto.md` |
| AIOS-SPEC-003 | AIOS Agent Integration Protocol (AIP) | 1.2.0 | ratified | specification | `specifications\AgentIntegrationProtocol.md` |
| AIOS-SPEC-005 | AIOS Agent Integration Guide (AGENTS.md) | 1.0.0 | ratified | specification | `specifications\agents.md` |
| AIOS-SPEC-004 | AIOS CLI Developer Experience Guide | 1.0.0 | ratified | specification | `specifications\CLIDeveloperGuide.md` |
| AIOS-SPEC-007 | Google Workspace Integration Governance | 0.1.0 | draft | specification | `specifications\GoogleWorkspaceIntegrationGovernance.md` |
| AIOS-SPEC-001 | AIOS NodeContract Specification | 1.0.0 | ratified | specification | `specifications\NodeContract.md` |
| AIOS-SPEC-002 | AIOS PolicyRecord Specification | 1.0.0 | ratified | specification | `specifications\PolicyRecord.md` |
| AIOS-SPEC-009 | Security & Sandboxing Model | 1.0.0 | draft | specification | `specifications\SecuritySandboxingModel.md` |
| AIOS-SPEC-006 | UI Component Registry Standard | 1.2.0 | draft | specification | `specifications\UIComponentRegistryStandard.md` |
| AIOS-COMM-002 | Data Privacy & Compliance Addendum | 1.0.0 | draft | commercial | `commercial\DataPrivacyComplianceAddendum.md` |
| AIOS-COMM-001 | AIOS Marketplace Terms & Vendor Onboarding | 1.0.0 | draft | commercial | `commercial\MarketplaceTermsOnboarding.md` |
| AMD-2026-005 | Workspace Model & Governed Interface Surfaces | 1.0.0 | ratified | amendment | `amendments\AMD-2026-005.md` |
| AMD-2026-006 | Google Workspace Governed Integration Plane | 0.1.0 | draft | amendment | `amendments\AMD-2026-006.md` |
| — | Agent-Native CLI Design Patterns (Google CLI Article Analysis) | — | ratified | — | `amendments\ammendment_google.md` |
| AIOS-REF-012 | Ecosystem Roadmap & Versioning Policy | 1.0.0 | draft | reference | `reference\EcosystemRoadmapVersioningPolicy.md` |
| — | gateway_plan | — | unregistered | reference | `reference\gateway_plan.md` |
| — | gateway_plan_review | — | unregistered | reference | `reference\gateway_plan_review.md` |
| AIOS-REF-011 | Governance Council Operating Manual | 1.0.0 | draft | reference | `reference\GovernanceCouncilOperatingManual.md` |
| — | intent_driven_skill | — | unregistered | reference | `reference\intent_driven_skill.md` |
| — | ptt_interface | — | unregistered | reference | `reference\ptt_interface.md` |
| — | shell_overhaul | — | unregistered | reference | `reference\shell_overhaul.md` |
| — | UI_PHILOSOPHY | — | unregistered | reference | `reference\UI_PHILOSOPHY.md` |
| — | uifix_ptt | — | unregistered | reference | `reference\uifix_ptt.md` |

---

## Cross-Reference Map

### The Gateway Global AIOS Governance Constitution (AIOS-CORE-002)

| Referenced Document | Relationship |
|---------------------|--------------|
| AIOS-CORE-001 | constrains |
| AIOS-CORE-003 | constrains |

### Gateway Global AIOS Master Platform Operating Agreement (AIOS-CORE-003)

| Referenced Document | Relationship |
|---------------------|--------------|
| AIOS-CORE-001 | incorporates |
| AIOS-CORE-002 | constrained_by |

### AIOS Technical Manifesto & Platform Economics (AIOS-CORE-001)

| Referenced Document | Relationship |
|---------------------|--------------|
| AIOS-CORE-002 | constrained_by |
| AIOS-CORE-003 | incorporated_by |

### AIOS Agent Integration Protocol (AIP) (AIOS-SPEC-003)

| Referenced Document | Relationship |
|---------------------|--------------|
| AIOS-CORE-002 | constrained_by |
| AIOS-SPEC-004 | complements |
| AIOS-SPEC-005 | complements |
| AMD-2026-005 | constrained_by |
| AIOS-SPEC-007 | constrained_by |

### AIOS Agent Integration Guide (AGENTS.md) (AIOS-SPEC-005)

| Referenced Document | Relationship |
|---------------------|--------------|
| AIOS-SPEC-003 | implements |
| AIOS-SPEC-004 | complements |

### AIOS CLI Developer Experience Guide (AIOS-SPEC-004)

| Referenced Document | Relationship |
|---------------------|--------------|
| AIOS-CORE-001 | implements |
| AIOS-CORE-002 | constrained_by |
| AIOS-CORE-003 | implements |
| AIOS-SPEC-003 | complements |

### Google Workspace Integration Governance (AIOS-SPEC-007)

| Referenced Document | Relationship |
|---------------------|--------------|
| AIOS-CORE-001 | implements |
| AIOS-CORE-002 | constrained_by |
| AMD-2026-005 | constrained_by |
| AIOS-SPEC-003 | complements |
| AIOS-SPEC-006 | complements |

### AIOS NodeContract Specification (AIOS-SPEC-001)

| Referenced Document | Relationship |
|---------------------|--------------|
| AIOS-CORE-001 | implements |
| AIOS-CORE-002 | constrained_by |
| AIOS-SPEC-002 | extends |

### AIOS PolicyRecord Specification (AIOS-SPEC-002)

| Referenced Document | Relationship |
|---------------------|--------------|
| AIOS-CORE-001 | implements |
| AIOS-CORE-002 | constrained_by |
| AIOS-CORE-003 | implements |
| AIOS-SPEC-001 | complements |

### Security & Sandboxing Model (AIOS-SPEC-009)

| Referenced Document | Relationship |
|---------------------|--------------|
| AIOS-CORE-001 | implements |
| AIOS-CORE-002 | constrained_by |
| AIOS-COMM-001 | enforced_by |
| AIOS-SPEC-006 | extends |
| AIOS-SPEC-005 | complements |

### UI Component Registry Standard (AIOS-SPEC-006)

| Referenced Document | Relationship |
|---------------------|--------------|
| AIOS-CORE-001 | implements |
| AIOS-CORE-002 | constrained_by |
| AIOS-COMM-001 | extended_by |
| AIOS-CORE-003 | enforced_by |
| AMD-2026-005 | constrained_by |
| AIOS-SPEC-007 | constrained_by |

### Data Privacy & Compliance Addendum (AIOS-COMM-002)

| Referenced Document | Relationship |
|---------------------|--------------|
| AIOS-CORE-001 | implements |
| AIOS-CORE-003 | amends |
| AIOS-CORE-002 | constrained_by |
| AIOS-SPEC-009 | complements |

### AIOS Marketplace Terms & Vendor Onboarding (AIOS-COMM-001)

| Referenced Document | Relationship |
|---------------------|--------------|
| AIOS-CORE-003 | extends |
| AIOS-CORE-002 | constrained_by |

### Workspace Model & Governed Interface Surfaces (AMD-2026-005)

| Referenced Document | Relationship |
|---------------------|--------------|
| AIOS-CORE-001 | amends |
| AIOS-SPEC-003 | amends |
| AIOS-SPEC-006 | amends |

### Google Workspace Governed Integration Plane (AMD-2026-006)

| Referenced Document | Relationship |
|---------------------|--------------|
| AMD-2026-005 | amends |
| AIOS-SPEC-003 | amends |
| AIOS-SPEC-006 | amends |

### Ecosystem Roadmap & Versioning Policy (AIOS-REF-012)

| Referenced Document | Relationship |
|---------------------|--------------|
| AIOS-CORE-001 | implements |
| AIOS-CORE-002 | governed_by |
| AIOS-CORE-003 | complements |
| AIOS-COMM-001 | extends |

### Governance Council Operating Manual (AIOS-REF-011)

| Referenced Document | Relationship |
|---------------------|--------------|
| AIOS-CORE-002 | operationalizes |
| AIOS-SPEC-009 | complements |
| AIOS-COMM-002 | complements |

---

## Document Statistics

- **Total documents:** 25
- **Ratified:** 10
- **Draft:** 8
- **Under review:** 0
- **Unregistered (no front matter):** 7

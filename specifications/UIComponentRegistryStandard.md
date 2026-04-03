---
document_id: AIOS-SPEC-006
title: UI Component Registry Standard
version: 1.2.0
status: draft
category: specification
author: Gateway Global
created: 2026-04-02
last_updated: 2026-04-02
reviewers: []
supersedes: null
cross_references:
  - { doc_id: "AIOS-CORE-001", relationship: "implements" }
  - { doc_id: "AIOS-CORE-002", relationship: "constrained_by" }
  - { doc_id: "AIOS-COMM-001", relationship: "extended_by" }
  - { doc_id: "AIOS-CORE-003", relationship: "enforced_by" }
  - { doc_id: "AMD-2026-005", relationship: "constrained_by" }
  - { doc_id: "AIOS-SPEC-007", relationship: "constrained_by" }
amendment_history:
  - amendment_id: AMD-2026-005
    ratified: 2026-04-02
    summary: Governed interface surfaces, workspace vs workflow, footer contract, load states, registration requirements
  - amendment_id: AMD-2026-006
    ratified: null
    summary: Google Workspace governed canvas surfaces
---
# AIOS UI Component Registry Standard v1.2.0

## 1. Architectural Purpose

The AIOS UI Component Registry is the **canonical, governed collection** of UI primitives that the Stateful Shell is permitted to render. Every component in the registry corresponds to a concrete implementation in the global `shadcn/ui` library (or a custom, approved extension). This standard ensures that **UI sovereignty** (Technical Manifesto Article II) is enforced at the level of each individual visual element.

By requiring all components to be explicitly registered, versioned, and accessibility‑certified, the Platform prevents the "vibe‑coded" UI fragmentation that plagues ungoverned AI systems. No agent, Kit, or NodeContract may reference a component that is not present in the registry – the DCP compiler will reject any such reference.

---

## 2. Relationship to Governing Documents

| Principle | Enforced Via |
|-----------|--------------|
| **UI Sovereignty** (Technical Manifesto Art II) | The registry is the exclusive source of truth for renderable components. The Canvas agent emits only `component_id`s that exist in the registry. |
| **Legislative Process** (Constitution Art II) | Adding or modifying a component is a legislative act. Proposals go through the DCP; high‑risk or core‑UI changes may trigger Tier 3 ratification. |
| **Economic & SLA Terms** (MPOA Art VI) | The UI Component SLA (72 business hours for approval) is directly enforced by this standard. |
| **Marketplace Certification** (Marketplace Terms Phase 2) | Vendors submitting Kits that require custom components must follow this standard's submission process. |

---

## 3. Registry Structure & Metadata

The registry is stored as a versioned JSON file (e.g., `{{GATEWAY_COMPONENT_REGISTRY_URL}}`) and is mirrored locally by the `aios registry list --components` command. Each component entry contains the following required fields:

| Field | Type | Description |
|-------|------|-------------|
| `component_id` | string | Globally unique identifier (kebab‑case, e.g., `aios-check-in-form`). |
| `version` | string | Semantic version (e.g., `1.2.0`). |
| `source` | enum | `shadcn/ui` (core) or `custom` (vendor‑submitted). |
| `variants` | array of strings | Allowed variants (e.g., `["default", "destructive"]`). |
| `wcag_level` | string | Must be `AA` (WCAG 2.1 Level AA). |
| `accessibility_attestation` | object | Signed attestation from the submitter (for custom components). |
| `owner` | string | Entity that controls the component (e.g., `gateway-global` or a vendor ID). |
| `deprecated` | boolean | If `true`, the component is scheduled for removal. |
| `replaces` | string (optional) | For deprecations: the `component_id` that supersedes this one. |

### Example Entry

```json
{
  "component_id": "aios-confirmation-dialog",
  "version": "2.0.0",
  "source": "custom",
  "variants": ["default", "destructive", "warning"],
  "wcag_level": "AA",
  "accessibility_attestation": {
    "signed_by": "vendor:cloudbeds",
    "date": "2026-04-01",
    "signature": "base64-rsa-sha256..."
  },
  "owner": "cloudbeds",
  "deprecated": false
}
```

---

## 4. Component Submission & Approval Workflow

### 4.1 Core (`shadcn/ui`) Components
- Automatically available – no submission required.
- Version updates follow the `shadcn/ui` release cycle; the Platform mirrors them weekly.

### 4.2 Custom Components (Vendor‑Submitted)

**Step 1 – Drafting**  
Vendor develops the component in isolation, ensuring it complies with:
- `shadcn/ui` styling conventions (Tailwind CSS, Radix UI primitives).
- WCAG 2.1 Level AA (automated + manual testing).
- The component must be stateless (no local session storage) – all state is managed by the Stateful Shell.

**Step 2 – Submission via DCP**  
Vendor creates a Pull Request that adds the component to the staging registry. The PR must include:
- The component's source code (or a reference to a public repository).
- A filled‑out `component_manifest.json` (metadata as defined in Section 3).
- Accessibility test report (e.g., axe‑core, Lighthouse).
- Signed attestation (using the vendor's private key, consistent with BYOK).

**Step 3 – Automated Validation**  
The DCP compiler runs:
- Schema validation against the registry schema.
- WCAG compliance linter (checks for missing ARIA labels, keyboard navigation, etc.).
- Build test (ensures the component renders correctly in the Shell's sandbox).

**Step 4 – Governance Board Review**  
The UI/UX Governance Board (defined in Constitution Article I, composed of OS Kernel Team and Digital Governance Officers) performs a final human review within **three (3) consecutive business days** (MPOA Article I). The review checks:
- Visual consistency with the AIOS design language.
- Absence of security or privacy leaks (e.g., no accidental telemetry).
- Adherence to the "deterministic fallback" principle (the component must degrade gracefully).

**Step 5 – Approval & Publication**  
If approved, the component is added to the production registry with version `1.0.0`. The vendor is notified via the Marketplace portal. The new component becomes immediately available for use in NodeContracts.

**Step 6 – Rejection & Remediation**  
If rejected, the Board provides a written explanation and specific remediation steps. The vendor may resubmit after addressing the issues; the 72‑hour SLA restarts.

---

## 5. Versioning & Deprecation

- **Semantic versioning** is mandatory (`MAJOR.MINOR.PATCH`).
  - `MAJOR`: Breaking changes (e.g., removed variant, different default behavior).
  - `MINOR`: New variant or non‑breaking enhancement.
  - `PATCH`: Bug fixes, accessibility improvements, no API change.
- **Deprecation**: A component may be marked `deprecated: true` after a **90‑day notice** posted in the `Ecosystem Roadmap` and communicated to all active vendors. The `replaces` field must point to the recommended alternative.
- **Removal**: After the deprecation period, the component is removed from the registry. Any Kit that still references it will fail DCP validation and must be updated.

---

## 6. Compliance & Enforcement

- **Compile‑time enforcement**: The DCP compiler (`aios validate`) checks every `permitted_ui_components` entry against the current registry. Unlisted or deprecated components cause a build failure.
- **Runtime enforcement**: The Stateful Shell ignores any `RenderDirective` that refers to an unregistered component and logs a `UI_VIOLATION` event to the immutable audit log (Technical Manifesto Art VI).
- **Vendor accountability**: Submitting a component that is later found to violate accessibility or security rules may result in the component's immediate suspension and trigger the due‑process provisions of the Marketplace Terms (Phase 5).

---

## 7. Relation to the CLI and Agent Workflow

- Developers and agents discover components via:
  ```bash
  aios registry list --components
  ```
  which returns the full registry as a JSON array.
- The `aios create contract` command pre‑populates the `permitted_ui_components` array with a comment encouraging the developer to replace the placeholder with a real component ID.
- The Agent Integration Protocol (AIP) mandates that agents **never hallucinate component IDs**; they must call `mcp:aios:registry_list` before referencing a component.

---

## 8. Governed Interface Surfaces

This specification recognizes a distinction between:

- **Shell** — the governing orchestration surface
- **View** — a mounted governed interface surface for a specific workspace, workflow, or system mode

### Shell Responsibilities

The shell MUST own:

- canvas open/close behavior,
- transition orchestration,
- policy denial presentation,
- audit event dispatch,
- active state disclosure,
- global mode switching where applicable.

### View Responsibilities

A governed view MUST own:

- presentation of a single surface,
- view-local controls,
- content layout,
- explicit disclosure of its purpose and state,
- compliance with footer and exit contracts.

A view MUST NOT silently mutate global canvas state outside the shell/controller contract.

---

## 9. Workspace and Workflow Surface Types

The registry MUST distinguish between:

### Workspace Surface

A governed selection surface that exposes available work, statuses, templates, and entry actions.

Example:

- `amendment_hub`

### Workflow Surface

A governed execution surface for a single run or concrete operation.

Example:

- `amendment_workflow`

### Rules

1. Workspace surfaces MUST NOT auto-create execution runs on entry.
2. Workflow surfaces MUST require the identifiers needed to load a concrete run.
3. If a workflow surface is requested without required identifiers, the system MUST return an explicit error or disambiguation state.

---

## 10. Footer Injection Contract

Governed views MAY inject footer controls, but all footer behavior MUST respect shell governance.

### Footer Zones

| Zone | Ownership | Typical Use |
|------|-----------|-------------|
| Left | shell or view | close, back, exit |
| Center | mode-aware | PTT, input, primary action |
| Right | shell or view | menu, status, save, share |

### Minimum Requirements

Every governed subsurface MUST provide:

- an exit path that preserves system integrity,
- clear disclosure of active mode where relevant,
- no ambiguity about whether controls are shell-global or view-owned.

### FooterConfig

```ts
interface FooterConfig {
  leftActions?: FooterAction[];
  centerType?: "PTT" | "INPUT" | "PRIMARY_ACTION" | null;
  rightActions?: FooterAction[];
  allowClose: boolean;
}
```

### Governance Rule

A view MUST document which controls are shell-global and which are view-owned.

---

## 11. Truthful Load States

Governed views that load remote or persisted resources MUST distinguish:

- `ok`
- `empty`
- `error`

A governed view MUST NOT represent `error` as `empty`.

When `loadState === "error"`, the UI MUST present an explicit error outcome and SHOULD offer retry behavior.

This rule is binding for Amendment Program workspace surfaces and any future governed workspace using the same model.

---

## 12. Registration Requirements for Governed Views

Every governed view registered under this specification MUST define:

- `view_id`
- `surface_type` (`workspace` | `workflow` | `system`)
- required params
- footer contract
- exit contract
- supported load states
- audit/event requirements

### Example

```json
{
  "view_id": "amendment_hub",
  "surface_type": "workspace",
  "required_params": [],
  "load_states": ["ok", "empty", "error"],
  "footer_contract": {
    "allowClose": true
  }
}
```

---

## 13. Google Workspace Governed Canvas Surfaces

Governed Workspace UI is defined by **AIOS-SPEC-007** and amendment **AMD-2026-006**. Surfaces MUST use the same **workspace vs workflow** rules as Amendment Program hubs: hub surfaces do not auto-create execution runs; editor/workflow surfaces require resource identifiers.

### 13.1 Registered surface IDs (non-exhaustive)

| `view_id` | `surface_type` | Notes |
|-----------|----------------|-------|
| `workspace_hub` | workspace | Entry hub for Workspace integration (Phase 1) |
| `workspace_mail_hub` | workspace | Mail-focused hub |
| `workspace_calendar_hub` | workspace | Calendar-focused hub |
| `workspace_drive_hub` | workspace | Drive-focused hub |
| `workspace_docs_hub` | workspace | Docs library hub |
| `workspace_doc_editor` | workflow | Single document; requires doc ref |
| `workspace_sheet_editor` | workflow | Single sheet; requires sheet ref |
| `workspace_mail_draft` | workflow | Draft composition; requires draft id when applicable |
| `workspace_event_editor` | workflow | Calendar event; requires event ref |
| `workspace_search_results` | workspace | Cross-resource search results |
| `workspace_automation_console` | workflow | Automation — restricted by POL-WORKSPACE-004 |

### 13.2 Requirements

Each surface MUST declare: required params, read/write class (via SPEC-007 scope class), footer contract, exit contract, load states (`ok` | `empty` | `error`), and audit hooks.

---

## 14. Appendices

### A. Example Component Manifest

```json
{
  "component_id": "aios-weather-card",
  "version": "1.0.0",
  "source": "custom",
  "variants": ["default", "compact"],
  "wcag_level": "AA",
  "accessibility_attestation": {
    "signed_by": "vendor:weather-api",
    "date": "2026-04-02",
    "signature": "base64-signature"
  },
  "owner": "weather-api",
  "deprecated": false
}
```

### B. WCAG 2.1 Level AA Checklist (Summary)

- **1.3.1 Info and Relationships** – semantic HTML, ARIA landmarks.
- **1.4.3 Contrast (Minimum)** – 4.5:1 for normal text.
- **2.1.1 Keyboard** – all functionality available via keyboard.
- **2.4.7 Focus Visible** – visible focus indicator.
- **3.3.2 Labels or Instructions** – labels for all form controls.
- **4.1.2 Name, Role, Value** – ARIA attributes where needed.

Full WCAG 2.1 Level AA criteria apply. The Governance Board may reject components that fail any criterion.

---

**This standard is governed by the AIOS Governance Constitution (v1.0).**  
Amendments to the registry schema, submission workflow, or deprecation policy must follow the Constitution's legislative process (RFC, simulation, supermajority ratification).

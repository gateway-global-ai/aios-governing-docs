# AIOS UI Component Registry Standard v1.0.0

## 1. Architectural Purpose

The AIOS UI Component Registry is the **canonical, governed collection** of UI primitives that the Stateful Shell is permitted to render. Every component in the registry corresponds to a concrete implementation in the global `shadcn/ui` library (or a custom, approved extension). This standard ensures that **UI sovereignty** (Technical Manifesto Article II) is enforced at the level of each individual visual element.

By requiring all components to be explicitly registered, versioned, and accessibility‑certified, the Platform prevents the “vibe‑coded” UI fragmentation that plagues ungoverned AI systems. No agent, Kit, or NodeContract may reference a component that is not present in the registry – the DCP compiler will reject any such reference.

---

## 2. Relationship to Governing Documents

| Principle | Enforced Via |
|-----------|--------------|
| **UI Sovereignty** (Technical Manifesto Art II) | The registry is the exclusive source of truth for renderable components. The Canvas agent emits only `component_id`s that exist in the registry. |
| **Legislative Process** (Constitution Art II) | Adding or modifying a component is a legislative act. Proposals go through the DCP; high‑risk or core‑UI changes may trigger Tier 3 ratification. |
| **Economic & SLA Terms** (MPOA Art VI) | The UI Component SLA (72 business hours for approval) is directly enforced by this standard. |
| **Marketplace Certification** (Marketplace Terms Phase 2) | Vendors submitting Kits that require custom components must follow this standard’s submission process. |

---

## 3. Registry Structure & Metadata

The registry is stored as a versioned JSON file (e.g., `https://registry.aios.dev/components.json`) and is mirrored locally by the `aios registry list --components` command. Each component entry contains the following required fields:

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

### 4.1. Core (`shadcn/ui`) Components
- Automatically available – no submission required.
- Version updates follow the `shadcn/ui` release cycle; the Platform mirrors them weekly.

### 4.2. Custom Components (Vendor‑Submitted)

**Step 1 – Drafting**  
Vendor develops the component in isolation, ensuring it complies with:
- `shadcn/ui` styling conventions (Tailwind CSS, Radix UI primitives).
- WCAG 2.1 Level AA (automated + manual testing).
- The component must be stateless (no local session storage) – all state is managed by the Stateful Shell.

**Step 2 – Submission via DCP**  
Vendor creates a Pull Request that adds the component to the staging registry. The PR must include:
- The component’s source code (or a reference to a public repository).
- A filled‑out `component_manifest.json` (metadata as defined in Section 3).
- Accessibility test report (e.g., axe‑core, Lighthouse).
- Signed attestation (using the vendor’s private key, consistent with BYOK).

**Step 3 – Automated Validation**  
The DCP compiler runs:
- Schema validation against the registry schema.
- WCAG compliance linter (checks for missing ARIA labels, keyboard navigation, etc.).
- Build test (ensures the component renders correctly in the Shell’s sandbox).

**Step 4 – Governance Board Review**  
The UI/UX Governance Board (defined in Constitution Article I, composed of OS Kernel Team and Digital Governance Officers) performs a final human review within **three (3) consecutive business days** (MPOA Article I). The review checks:
- Visual consistency with the AIOS design language.
- Absence of security or privacy leaks (e.g., no accidental telemetry).
- Adherence to the “deterministic fallback” principle (the component must degrade gracefully).

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
- **Vendor accountability**: Submitting a component that is later found to violate accessibility or security rules may result in the component’s immediate suspension and trigger the due‑process provisions of the Marketplace Terms (Phase 5).

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

## 8. Appendices

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
Amendments to the registry schema, submission workflow, or deprecation policy must follow the Constitution’s legislative process (RFC, simulation, supermajority ratification).

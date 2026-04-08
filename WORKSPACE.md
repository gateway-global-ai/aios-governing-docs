# WORKSPACE.md

Status: Informative stub.

This file exists to satisfy repository cross-references from governance documents.

Normative authority for Workspace integration, intent, and related governance remains in:

- AIOS-SPEC-007
- AIOS-SPEC-009
- other ratified or draft governance artifacts in this repository as applicable

This file should not be treated as a standalone source of normative law unless a future governance action explicitly elevates it.

## Operator notes (informative)

These notes align with **[AMD-2026-009](amendments/AMD-2026-009.md)** (ratified) and **[AMD-2026-009-ADD-001](amendments/AMD-2026-009-ADD-001-retrieval-backend-neutrality.md)** (ratified); they do **not** add normative requirements beyond **[AIOS-SPEC-007](specifications/GoogleWorkspaceIntegrationGovernance.md)** and related specs.

- **PSE / web retrieval credentials:** Values such as **`GOOGLE_PSE_*`**, engine identifiers, and API keys **SHALL** remain **server-side** on the MCP host. They **MUST NOT** ship in browser bundles (for example via **`VITE_*`** client env).
- **Policy-registered backends:** Alternative retrieval backends **MAY** be configured when registered in policy per ADD-001; keep routing consistent with **AIOS-SPEC-007** §3 and **POL-WEB-*** policy rows in **[AIOS_POLICY_INDEX](reference/AIOS_POLICY_INDEX.md)**.

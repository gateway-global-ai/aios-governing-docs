# Building an Internal Development Control Plane for a Voice‑First, Intent‑Driven AI OS

## Executive summary

A Development Control Plane (DCP) is a **governance-first orchestration layer** that converts work requests (features, fixes, policies, vertical expansions) into **phased execution lanes** with explicit gates, artifacts, approvals, and evidence-based completion. It functions as an internal “Lead System Architect” that operationalizes what you are currently doing manually: decomposing work, enforcing sequencing, binding work to contracts/registries/tests, routing peer review, and fail‑closing when authority is unclear. Your existing internal doctrine already describes this role: classify work, enforce merge gates, preserve server authority, fail closed, and require evidence before marking work “done.” fileciteturn0file0

For your voice-first AI OS, the DCP should be designed as a **control-plane service (not customer runtime)** and should integrate tightly with (a) your intent-loop pipeline Phases A–D and its traces; (b) your registries and validators; (c) your existing CI governance gates (Sovereign Guard); (d) plane boundaries for MCP usage; and (e) hospitality vertical governance for Cloudbeds integration. The internal repo audit you provided already reflects a two-plane model (customer runtime vs internal worker plane), registry-driven validation, and CI enforcement—this is the foundation the DCP should build on rather than replace. fileciteturn0file1

Key industry lessons that map well to a DCP:

- **Policy-as-code with a centralized Policy Decision Point (PDP)** decouples policy from application logic and works across “diff inputs” like JSON/YAML/PR metadata. citeturn0search4turn0search0turn6search1  
- **GitOps** treats declarative state in Git as a single source of truth and enforces drift correction and approval workflows. citeturn0search3turn4search3turn4search7  
- **Workflow engines** (durable execution) make gates reliable, retryable, and auditable. citeturn4search20turn4search4turn9search4  
- **Supply-chain integrity** (SLSA, Sigstore, in‑toto attestations) turns “trust” into verifiable provenance and gateable evidence in CI. citeturn2search0turn2search1turn12search6turn12search3  
- **Observability standards** (OpenTelemetry + W3C Trace Context) let the DCP correlate policy decisions, approvals, CI runs, and runtime traces across services. citeturn1search1turn1search2turn1search9  
- **AI security standards** (NIST AI RMF + GenAI Profile, OWASP LLM Top 10, MITRE ATLAS) provide structured risk controls for agentic systems, prompt injection, and tool misuse—core concerns for a voice-first AI OS and for internal agent orchestration. citeturn3search0turn8search2turn8search0turn8search1

Recommended architecture: implement DCP as a **service boundary** with (1) an Intake API, (2) a Policy Engine (OPA-style) for deterministic gating decisions, (3) a Workflow Orchestrator (Temporal-style) to reliably run multi-step gates, (4) an Evidence Store (CI artifacts, test proofs, contract hashes), (5) an Approval UI/Queue (Backstage plugin or dedicated UI), and (6) adapters to GitHub (status checks), your registries, Sovereign Guard CI scripts, and hospitality/Cloudbeds constraints. GitHub branch protection plus required status checks should enforce that DCP gates pass before merge. citeturn1search4turn1search0turn1search8

A phased delivery plan is the lowest-risk route: start with a “thin” DCP that **publishes required status checks** and **blocks merges** unless gates pass; then add reviewer UX and richer audit/tracing; then add agent execution lanes, supply-chain attestations, and vertical-specific governance for Cloudbeds.

---

## Scope and requirements for a DCP in a voice‑first AI OS

A DCP for your system must reflect two hard truths:

1) **Runtime authority is server-side and contract-bound.** Your intent-loop Phases A–D (observation → resolver → merge → derivation) exist to keep the OS deterministic and fail-closed, and your internal doctrine demands that clients render rather than decide authority. fileciteturn0file0

2) **Most failures are governance failures, not coding failures.** The DCP’s job is to make governance executable: enforce sequencing, prevent drift, require registries and validators, and keep plane boundaries intact. fileciteturn0file0turn0file1

### What the DCP owns

- **Work intake & classification:** translate a freeform request into a typed work item (runtime spine / platform governance / vertical domain / repairs). fileciteturn0file0  
- **Phase planning & gate generation:** produce phases, merge gates, required artifacts (schemas/tests/registry delta statements), and explicit “done means.” fileciteturn0file0  
- **Policy evaluation & fail-closed decisions:** deterministic evaluation of “can this change ship?” (e.g., are registry updates present? are validators updated? are forbidden files touched?). Policy-as-code is the industry standard approach for this class of guardrail. citeturn0search4turn6search1  
- **Evidence management:** store/verifiable pointers to test runs, CI logs, governance scripts, provenance attestations, and approvals. SLSA/in‑toto attestations are the strongest industry pattern for “verifiable evidence.” citeturn2search0turn12search6turn12search3  
- **Approvals & review routing:** who must approve what, when; record decisions and rationale; enforce two-party review for high-risk domains. GitHub rulesets/branch protection and required status checks are the native enforcement surface. citeturn1search8turn1search4turn1search0  
- **Audit & trace correlation:** unify traces across DCP → CI → runtime, using OpenTelemetry semantics and W3C trace context propagation. citeturn1search1turn1search2turn1search13

### What the DCP must not own

- **Customer runtime decisions.** It should not live in the hot voice path, nor invent runtime UI; it should enforce that runtime uses registered views, typed payloads, syscalls, and validators. fileciteturn0file0  
- **Domain execution logic.** Like Kubernetes admission control, the DCP should decide “allow/deny/require proof” rather than execute business workflows. Admission control exists precisely to intercept and validate requests before persistence or deployment. citeturn0search8turn6search0  
- **Plane boundary violations.** Tooling MCPs (e.g., workspace data access) must stay in the internal operator plane unless a governed proxy is created; the DCP should enforce this boundary as policy. fileciteturn0file0turn0file1

### Security and risk drivers specific to agentic systems

- **Prompt injection and insecure output handling** are widely recognized risks for LLM applications and especially for tool-using agents. citeturn8search0turn8search4  
- **AI risk governance and documentation** are central themes of NIST’s AI RMF and its GenAI profile, emphasizing structured risk management across lifecycle and context. citeturn3search0turn8search2turn8search6  
- **Adversarial threat modeling for ML/AI** has a structured knowledge base in MITRE ATLAS, which can inform the DCP’s security gates for agent tooling and data flows. citeturn8search1turn8search5

---

## Industry patterns and product comparisons

The DCP is not a single off-the-shelf product; it is an internal control-plane composition. The table below compares 10 widely used patterns/products that map to DCP functions.

| Pattern / product | Purpose | Fit for a voice‑first AI OS DCP | Typical integration points | Pros | Cons | Maturity signals | Licensing / cost posture |
|---|---|---|---|---|---|---|---|
| entity["organization","Open Policy Agent","cncf policy engine"] | Policy-as-code PDP for JSON/YAML inputs, decisions via Rego. citeturn0search4turn0search0 | Excellent for deterministic gate decisions, plane boundaries, and “deny by default.” citeturn6search1 | DCP policy evaluation, CI checks, registry validation, PR metadata gating. citeturn6search1turn10search36 | Decouples policy from code; reusable policies; supports CI/CD use cases. citeturn6search1turn0search13 | Requires policy discipline and testing; policy drift risk if unmanaged. citeturn6search1 | CNCF graduated project; extensive docs. citeturn0search13turn10search35 | Apache‑2.0. citeturn10search0 |
| entity["organization","Gatekeeper","kubernetes admission policy"] | OPA-based admission control for Kubernetes; validating/mutating webhooks. citeturn0search5turn0search1 | Strong analogy for “intercept requests and fail closed”; use as design reference even outside K8s. citeturn0search5turn0search11 | If DCP deploys into K8s, enforce infra policy; mirror patterns for repo/runtime admission. citeturn0search5turn0search8 | Mature admission patterns, constraint libraries. citeturn10search5turn0search11 | Kubernetes-centric; not a general workflow orchestrator. citeturn0search5 | Production adoption; CNCF ecosystem. citeturn0search5turn10search13 | Apache‑2.0. citeturn10search1 |
| entity["organization","Kyverno","kubernetes policy engine"] | Kubernetes-native policy engine with validate/mutate/generate and policy reports. citeturn0search2turn0search35 | Useful if DCP governs K8s resources; strong “policy reports” model for reviewer UX. citeturn0search35turn0search9 | Cluster policy, CI validation of manifests, policy reporting dashboards. citeturn0search35turn3search33 | YAML-native; policy reports; integrates with policy working group formats. citeturn0search35turn0search2 | Kubernetes boundary; less direct for PR/workflow gating outside K8s. citeturn0search2 | CNCF maturity listed as graduated (recent). citeturn11search2 | Apache‑2.0. citeturn11search4turn11search0 |
| entity["organization","Argo CD","gitops cd for k8s"] | GitOps CD: reconcile desired state in Git to live state and report drift. citeturn0search3turn0search24 | Great fit for “registry = desired state” and drift management; informs DCP’s “single source of truth” stance. citeturn0search3turn0search37 | Deploy governance services, manage config repos, enforce “Git as truth.” citeturn0search3 | Drift detection, reconciliation UI, Git-centric approvals. citeturn0search3turn0search24 | Requires K8s; not a generalized policy engine. citeturn0search3 | Widely adopted, CNCF ecosystem. citeturn0search16 | Apache‑2.0. citeturn10search2 |
| entity["organization","Flux","gitops toolkit"] | GitOps toolkit: keep clusters in sync with config sources and automate updates. citeturn4search3turn4search7 | Similar benefits as Argo CD; good for env promotion and multi-tenant patterns in infra governance. citeturn4search3turn10search15 | Deploy DCP services/config; multi-tenant patterns and GitOps promotion. citeturn4search11turn10search15 | Modular controllers; strong GitOps integration. citeturn4search7turn4search3 | K8s-centric; doesn’t replace approval workflow UI. citeturn4search3 | Mature ecosystem + docs. citeturn4search3turn4search7 | Apache‑2.0 (project). citeturn10search7 |
| entity["organization","Temporal","durable execution engine"] | Durable execution workflows with replay/determinism primitives. citeturn4search20turn4search36 | Excellent for DCP gating because gates are multi-step, retryable, and need strong audit history. citeturn4search28turn4search12 | Orchestrate gate pipelines, evidence collection, reviewer routing, retries/timeouts. citeturn4search4turn4search36 | Strong reliability for long-running approvals; explicit workflow history. citeturn4search36turn4search12 | Adds infra complexity; requires determinism constraints in workflows. citeturn4search12turn4search4 | Mature docs + broad adoption. citeturn4search20turn9search4 | MIT for server; optional paid cloud. citeturn9search0turn9search24 |
| entity["organization","Backstage","developer portal framework"] | Internal developer portal: software catalog + tooling integration. citeturn4search5turn9search9 | Strong fit for DCP reviewer UX: work queues, gate status, evidence panels as portal views. citeturn4search5turn4search1 | Reviewer dashboards, catalog of services/registries, PR/CI integrations. citeturn4search5 | Unifies tooling and docs in one UI; supports governance-as-UX. citeturn4search5 | Needs productization for your specific gates; portal ≠ policy engine. citeturn4search5 | CNCF incubating (project page). citeturn4search1 | Apache‑2.0. citeturn9search1turn9search9 |
| entity["organization","GitHub Actions","ci workflow system"] | CI execution and integration point for required status checks and branch rules. citeturn1search8turn1search0 | Core enforcement surface: DCP publishes checks; branch rules require them. citeturn1search4turn1search0 | Run Sovereign Guard, policy tests, provenance attestations, DCP gate calls. citeturn1search0turn12search6 | Ubiquitous; integrates with PR UX. citeturn1search0turn1search8 | CI sprawl unless centralized; secrets management must be disciplined. citeturn1search8 | Very mature ecosystem. citeturn1search8 | Included with GitHub tiers; variable enterprise cost. citeturn1search8 |
| entity["organization","Tekton","k8s native cicd engine"] | Kubernetes-native CI/CD primitives (Tasks/Pipelines) for standardized execution. citeturn6search2 | Good if you want DCP gates to run inside K8s with standardized CRDs; can complement GitHub Actions. citeturn6search2turn6search3 | Gate execution in cluster; standardized pipeline definitions. citeturn6search2 | Portable K8s-native pipelines. citeturn6search2 | Operational overhead; less directly tied to PR approvals than GitHub-native checks. citeturn6search2 | CNCF incubating (recent). citeturn11search3turn11search11 | Apache‑2.0. citeturn11search1 |
| entity["organization","MLflow","model lifecycle registry"] | Model registry + lineage + lifecycle governance for ML artifacts. citeturn5search0 | Useful if your OS includes model experiments or agent evaluation artifacts; informs DCP evidence/lineage model. citeturn5search0turn5search18 | Store eval runs, model/agent versions, provenance of policy/test artifacts. citeturn5search0 | Strong lineage/versioning model; UI + APIs. citeturn5search0turn5search4 | Not a general policy/approval system; model-centric. citeturn5search0 | Mature open-source project. citeturn5search8turn9search35 | Apache‑2.0. citeturn9search3turn9search19 |

image_group{"layout":"carousel","aspect_ratio":"16:9","query":["Open Policy Agent architecture diagram policy decision point","Argo CD GitOps architecture diagram out of sync desired state","Backstage developer portal software catalog diagram","Temporal workflow engine architecture diagram durable execution"],"num_per_query":1}

---

## Recommended DCP architecture and integration mapping

A DCP for your monorepo Node/TypeScript stack should be built as a **control-plane service mesh** with explicit authority lines. The architecture below assumes (a) an existing intent-loop A–D implementation for runtime surfaces; (b) an existing CI “Sovereign Guard” style workflow; and (c) an internal operator plane for agent work. fileciteturn0file1turn0file2

### Architecture diagram

```mermaid
flowchart LR
  %% Actors
  Dev[Developer / PM / Operator] -->|voice or web intake| DCP_API[DCP Intake API]

  %% Core DCP services
  DCP_API --> DCP_DB[(DCP DB: work items, phases, approvals)]
  DCP_API --> POLICY[PDP Policy Engine\n(OPA/Rego or equivalent)]
  DCP_API --> WF[Workflow Orchestrator\n(Temporal-style durable execution)]
  WF --> EVID[(Evidence Store:\nCI artifacts, test proofs, contract hashes)]
  WF --> AUDIT[(Append-only Audit Log)]
  WF --> OBS[Observability\n(OpenTelemetry traces/logs/metrics)]

  %% Repo/CI integration
  Dev -->|PR| GH[Git Hosting + PR UX]
  GH -->|webhook| DCP_API
  DCP_API -->|publish required checks| GH
  GH -->|run workflows| CI[CI Runner\n(GitHub Actions)]
  CI -->|run governance scripts| SG[Sovereign Guard + Validators]
  CI -->|policy tests| POLICY
  CI -->|attest provenance| PROV[SLSA/in-toto Attestations]
  PROV --> EVID

  %% Registry & contracts
  DCP_API --> REG[Registry Service\n(view/action/integration registries)]
  SG --> REG
  POLICY --> REG

  %% Runtime spine linkage (not hot path)
  REG --> RT[Runtime Control Plane\n(intent-loop A–D, canvas validators)]
  RT --> OBS

  %% MCP plane boundary
  DCP_API --> MCPB[Plane Boundary Controller\n(MCP allowed only in internal plane)]
  MCPB --> LOCAL[Local Agent Plane\n(admin-only, orchestrated)]
  LOCAL --> EVID

  %% Hospitality vertical
  DCP_API --> HOSP[Hospitality Governance Module\n(Cloudbeds constraints)]
  HOSP --> POLICY
  HOSP --> REG
  HOSP --> EVID

  %% Authority lines
  classDef authority fill:#eef,stroke:#33f,stroke-width:1px;
  class DCP_API,POLICY,WF,REG,SG,RT,MCPB authority;
```

### Authority model and fail‑closed posture

The architecture borrows proven patterns from Kubernetes admission control: intercept requests **after authentication and authorization but before persistence/enforcement**, and fail closed when policy rejects. Kubernetes documentation explicitly frames admission control as intercepting requests prior to persistence. citeturn0search8turn6search0

For a DCP, “requests” are PRs, merges, releases, registry updates, deployment promotions, and privileged agent tasks. The DCP enforces fail-closed by:

- Default-deny on unknown work classifications or missing artifacts (policy-as-code PDP). citeturn0search13turn6search1  
- Requiring branch protection status checks to pass before merge (GitHub enforcement). citeturn1search4turn1search0turn1search8  
- Requiring provenance attestations for build outputs at higher assurance levels (SLSA/in‑toto). citeturn2search0turn12search6turn12search3

### Explicit mapping to your intent-loop Phases A–D

Your runtime spine (observation → resolver → merge → derivation) is a runtime control-plane pattern; the DCP should **govern changes** to that spine and also reuse its governance primitives (typed contracts, fail-closed behavior, trace vocabulary). fileciteturn0file2turn0file0

A concrete mapping:

- **Phase A (Observation)**: DCP collects “change observation” for a work item: files touched, registries impacted, risk classification, affected tenants, and required tests. This mirrors the runtime Phase A goal: get structured state before decisions. Admission systems do the same by capturing request objects as inputs. citeturn0search8turn6search0  
- **Phase B (Resolver)**: DCP resolves an authoritative “Work Resolution” (allowed actions, required gates, required approvers, forbidden paths, required evidence). This is the dev analog of runtime IntentLoopResolver. Policy-as-code PDPs are built for this role. citeturn0search4turn6search1  
- **Phase C (Merge)**: DCP merges policy resolution with CI reality—e.g., if CI reports a failing governance script or missing registry delta statement, the DCP updates the “final allowed merge decision” and publishes it as a required status check. GitHub required checks are designed for exactly this merge gating. citeturn1search0turn1search4  
- **Phase D (Derivation)**: DCP derives reviewer UX surfaces: the approval queue, missing artifact checklist, evidence links, and “next permitted action.” Backstage-style portals are purpose-built to unify such developer workflows and catalog governance state. citeturn4search5turn4search1

This mapping makes the DCP conceptually aligned with your OS: voice-first intent loop as the runtime spine, and “intent loop for development” as the governance spine.

### Integration with registries, Sovereign Guard, and MCP plane boundaries

- **Registries**: DCP must treat registry artifacts as authoritative desired state, consistent with GitOps principles where Git defines desired configuration. citeturn0search3turn4search3turn0search37  
- **Sovereign Guard**: DCP should not replace CI governance scripts; it should orchestrate them, interpret their results, and publish gating decisions. Your internal audit already highlights registry validators and CI gates as existing “machine truth”; the DCP becomes the routing/decision layer above them. fileciteturn0file1  
- **MCP plane boundaries**: DCP policy should explicitly prevent tooling MCPs from becoming runtime UI generators. Your governance prompt already calls out “do not collapse design-time and runtime planes” and “do not confuse tooling MCPs with runtime UI generation,” which should become enforceable policy rules. fileciteturn0file0

### Integration with Cloudbeds hospitality vertical

Cloudbeds integration introduces high-value, high-risk data and operational constraints. Cloudbeds documentation emphasizes API keys and OAuth options, permission scopes, and webhooks/event lifecycles. citeturn7search0turn7search1turn7search5turn7search21

A hospitality governance module inside DCP should:

- Enforce **tenant/property isolation**: bind Cloudbeds credentials and scopes to a siteConfigId/tenant identity record, and prevent cross-tenant execution. Cloudbeds supports scoped credentials and highlights permission scopes tied to endpoints. citeturn7search14turn7search12  
- Encode Cloudbeds auth rules: API keys are described as preferred and long-lived but operationally constrained (e.g., inactivity windows), and OAuth requires client_id/client_secret/redirect_uri and scopes. citeturn7search1turn7search5turn7search12  
- Model webhook ingestion as events, ideally using a common event envelope such as CloudEvents, which is intended to standardize event metadata across producers/consumers. citeturn1search3turn1search7turn7search21

---

## Data models, APIs, and reviewer UX

A DCP must make governance **machine-checkable** and **reviewer-friendly**. This requires a small set of typed contracts and APIs.

### Core data model concepts

The following objects should be first-class in the DCP database:

- **WorkItem**: intake record, classification, scope, tenants, risk posture.
- **PhasePlan**: ordered phases, each with gate requirements.
- **WorkResolution**: authoritative computed decision record (policy outputs), versioned and immutable once finalized.
- **ApprovalRecord**: approver identity, decision, rationale, timestamp, binding scope.
- **EvidenceArtifact**: links to CI runs, test outputs, contract hashes, provenance attestations.
- **AuditEvent**: append-only log record, correlated with trace IDs.

This mirrors patterns from secure SDLC frameworks, which emphasize integrating security practices into lifecycle and maintaining evidence that practices occurred. citeturn2search3turn3search1

### API and contract sketches

Below are concrete sketches aligned to your Node/TypeScript monorepo assumption.

```ts
// shared/dcpContracts.ts
export const DCP_CONTRACT_VERSION = "dcp.v1" as const;

export type WorkClassification =
  | "control_plane_governance"
  | "runtime_feature"
  | "vertical_feature"
  | "repair_hardening"
  | "design_time_sdk_registry"
  | "legacy_cleanup";

export type GateStatus = "pending" | "pass" | "fail" | "waived";

export interface WorkIntakeRequest {
  contractVersion: typeof DCP_CONTRACT_VERSION;
  title: string;
  problemStatement: string;
  classificationHint?: WorkClassification;
  tenants?: { siteConfigId: string; vertical?: "hospitality" | "generic" }[];
  repoContext?: { baseRef: string; headRef?: string; prNumber?: number };
  requestedBy: { actorId: string; actorType: "human" | "system" };
  constraints?: {
    forbiddenPaths?: string[];
    allowedDomains?: string[]; // maps to your jurisdiction concept
  };
}

export interface WorkItem {
  contractVersion: typeof DCP_CONTRACT_VERSION;
  workItemId: string;
  createdAt: string;
  classification: WorkClassification;
  riskTier: "low" | "medium" | "high";
  state: "intake" | "planned" | "in_progress" | "awaiting_approval" | "completed" | "rejected";
  tenants: { siteConfigId: string; vertical?: "hospitality" | "generic" }[];
}

export interface PhaseGate {
  gateId: string;
  name: string;
  requiredArtifacts: string[];   // e.g. "zod_schema_locked", "registry_delta_declared"
  requiredChecks: string[];      // CI checks / scripts
  requiredApprovals: string[];   // roles, e.g. "lead_architect", "security"
  status: GateStatus;
  failureReason?: string;
}

export interface WorkResolution {
  contractVersion: typeof DCP_CONTRACT_VERSION;
  resolutionId: string;
  workItemId: string;
  computedAt: string;
  policyVersion: string;         // e.g., "rego.bundle.sha256:..."
  allowedActions: string[];      // e.g. "open_pr", "merge", "release"
  forbiddenPaths: string[];
  requiredGates: PhaseGate[];
  auditNotes: string[];          // prefixed strings (deny:, fallback:, etc)
}

export interface ApprovalRecord {
  contractVersion: typeof DCP_CONTRACT_VERSION;
  approvalId: string;
  workItemId: string;
  gateId?: string;
  decision: "approve" | "reject" | "waive";
  rationale: string;
  approvedBy: { actorId: string; actorType: "human" | "system" };
  approvedAt: string;
}

export interface AuditEvent {
  contractVersion: typeof DCP_CONTRACT_VERSION;
  eventId: string;
  occurredAt: string;
  actor: { actorId: string; actorType: "human" | "system" };
  workItemId?: string;
  kind:
    | "work.intake"
    | "work.classified"
    | "policy.evaluated"
    | "gate.updated"
    | "approval.recorded"
    | "ci.check.reported"
    | "evidence.attached";
  trace: { traceId?: string; spanId?: string }; // W3C trace context compatible
  payload: Record<string, unknown>;
}
```

These objects should be **strictly validated** at boundaries (Zod/JSON schema), reflecting the same “contract-first, strict parsing” stance used in robust policy systems. OPA itself is designed to evaluate policies over structured document data like JSON. citeturn0search0turn0search4

### Minimal REST API surface

A minimal DCP service can be implemented with these endpoints:

- `POST /api/dcp/work-items` → create intake record; return `WorkItem`.
- `POST /api/dcp/work-items/:id/plan` → generate PhasePlan + initial WorkResolution.
- `POST /api/dcp/work-items/:id/evaluate` → recompute WorkResolution for a PR/commit.
- `POST /api/dcp/work-items/:id/approvals` → record approval/waiver.
- `GET /api/dcp/work-items/:id` → full state view.
- `POST /api/dcp/webhooks/github` → ingest PR events, re-evaluate, publish check run status.

GitHub’s model of required status checks and protected branches expects checks to be posted and to pass before merge. citeturn1search0turn1search4turn1search8

### Reviewer and approver UX

A DCP reviewer UX should reduce cognitive load and align with deterministic governance:

- **Work Queue View**: list of work items awaiting approval, grouped by risk tier and tenant impact.
- **Gate Timeline View**: gates with pass/fail/waived status; each gate expands to required artifacts and missing evidence.
- **Evidence Panel**: links to CI runs, test logs, contract/schema diffs, provenance attestations.
- **Policy Explanation Panel**: a compact “why denied” view derived from structured audit notes (prefixes), not a freeform model narrative.
- **Diff-Aware Registry Panel**: highlights whether registries were updated; forces “registry delta” or “no registry delta” statements.

Backstage is explicitly framed as a developer portal with a centralized catalog and integrations, making it a strong host for these UX surfaces. citeturn4search5turn4search1

---

## Audit, tracing, security, tenant isolation, and compliance posture

### Audit and tracing requirements

A DCP must correlate:

- A work item intake → policy evaluation(s) → CI checks → approvals → merge → release → runtime deployment.

OpenTelemetry defines standard models for traces/logs/metrics and supports correlating signals; W3C Trace Context defines portable headers (`traceparent`, `tracestate`) for propagation across service boundaries. citeturn1search1turn1search2turn1search25

Recommended practice:

- Every DCP decision emits an `AuditEvent` with trace IDs.
- CI workflows propagate a trace ID into DCP calls (or DCP generates and returns one).
- Runtime control-plane logs include the same trace IDs when changes correspond to shipped artifacts (e.g., contract hashes).

### Security and identity controls

Use established standards as a checklist baseline:

- **Digital identity**: NIST SP 800-63 provides structured guidance for identity proofing/authentication/federation assurance levels. citeturn3search9turn3search5  
- **Control catalog**: NIST SP 800-53 provides a comprehensive catalog of security and privacy controls and emphasizes flexible, customizable controls within risk management. citeturn3search1turn3search8  
- **Secure SDLC**: NIST SSDF recommends integrating secure development practices into SDLCs and treating them as outcomes that can be evidenced. citeturn2search3turn2search11  
- **AI-specific secure development profile**: NIST has an SSDF community profile for AI development (AI model development throughout SDLC), relevant if DCP governs models/agents beyond typical code. citeturn2search23  
- **AI risk governance**: NIST AI RMF and the GenAI profile provide lifecycle risk guidance for AI systems. citeturn3search0turn8search2turn8search6

### Agent and LLM safety gates for DCP

Because a DCP may orchestrate internal agents or accept model-generated artifacts, threat models must include:

- Prompt injection (LLM01) and insecure output handling (LLM02/LLM-related risks) as recognized by OWASP’s Top 10 for LLM Applications project. citeturn8search0turn8search4  
- Adversarial AI tactics and techniques cataloged in MITRE ATLAS as a structured threat reference. citeturn8search1turn8search5

Practical DCP gates:

- Treat any LLM-produced content as **untrusted until validated** by schema checks, deterministic tests, and policy checks.
- Require explicit human approval for:
  - changes that expand tool permissions or entitlements,
  - changes that touch identity/auth boundaries,
  - changes that alter runtime view registries or syscall validators.

### Tenant isolation and Cloudbeds credentials

Cloudbeds documentation differentiates auth approaches (API keys vs OAuth) and emphasizes permission scopes. citeturn7search8turn7search12turn7search5

DCP should enforce:

- **Credential binding**: every Cloudbeds credential is stored as `(siteConfigId, environment, scope set, issuer)` and never reused across tenants.
- **Least privilege**: only allow endpoint scopes required for the work item (Cloudbeds docs emphasize selecting permission scopes). citeturn7search14turn7search12  
- **Event handling discipline**: Cloudbeds webhooks can drive automation; treat webhook events as untrusted inputs requiring validation and idempotency. citeturn7search21  
- **Deprecation awareness**: Cloudbeds notes API version deprecations (e.g., v1.1 deprecation notice). DCP should allow only supported versions in production integrations. citeturn7search0

### Security and compliance checklist

A practical checklist for DCP readiness:

- Identity and access
  - OIDC/JWT auth for DCP API; no anonymous mutation endpoints. citeturn3search9turn3search5
  - Role-based access control for approvals and waivers, with separation of duties (policy + approver roles). citeturn3search1
- Data protection
  - Encrypt secrets at rest; rotate; never place Cloudbeds keys in CI logs.
  - Tenant isolation invariants in policy (deny cross-tenant evidence reuse).
- Audit integrity
  - Append-only audit log (write-once semantics); correlate with trace IDs. citeturn1search2turn1search1
- Supply chain security
  - Require SLSA provenance (or equivalent provenance attestations) for release builds. citeturn2search0turn12search2turn12search6
  - Use Sigstore signing/verification where feasible (keyless OIDC flows exist). citeturn2search1turn2search9turn2search21
- AI/agent safety
  - OWASP LLM Top 10 threat mitigations for internal agents and tool outputs. citeturn8search0turn8search4
  - MITRE ATLAS threat modeling for agent tooling routes. citeturn8search1turn8search5

---

## CI integration, testing strategy, observability, and automation rules

### CI/CD gate design patterns

GitHub’s required status checks and protected branch rules provide a native enforcement surface: if checks are required, they must pass before merge. citeturn1search0turn1search4turn1search8

Recommended rule set:

- A single “DCP Gate” check aggregates:
  - Sovereign Guard scripts,
  - policy-as-code evaluation results,
  - registry validator outputs,
  - provenance attestation presence on release branches.

OPA documents CI/CD usage explicitly as enforcing organizational policies before code reaches production, including repository governance checks and dependency policy enforcement. citeturn6search1turn10search36

### Suggested GitHub Actions workflow snippets

Sample: DCP gate check (conceptual)

```yaml
name: dcp-gate
on:
  pull_request:
    types: [opened, synchronize, reopened, ready_for_review]
jobs:
  gate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run sovereign guard
        run: |
          npm ci
          npm run governance:sovereign-gate
      - name: Evaluate DCP policy
        run: |
          curl -sS -X POST "$DCP_URL/api/dcp/work-items/${{ github.event.pull_request.number }}/evaluate" \
            -H "Authorization: Bearer $DCP_TOKEN" \
            -H "Content-Type: application/json" \
            -d '{"repo":{"owner":"${{ github.repository_owner }}","repo":"${{ github.event.repository.name }}","sha":"${{ github.sha }}"}}'
      - name: Fail if DCP denied
        run: |
          # fetch decision; exit 1 if denied
          echo "enforce fail-closed"
```

Sample: provenance attestation for release artifacts

GitHub now supports build provenance attestations that bind a subject artifact/digest to a SLSA provenance predicate using in‑toto format. citeturn12search6turn12search3

### Testing strategy

A DCP requires a layered test approach:

- **Policy unit tests**: test policy bundles (Rego/CEL equivalents) with deterministic inputs; treat as critical code. OPA emphasizes policy checks in CI/CD and supports policy-based validation of structured inputs. citeturn6search1turn0search0  
- **Contract tests**: Zod/JSON schema validation tests for `WorkResolution`, `ApprovalRecord`, `AuditEvent`.
- **Integration tests**: simulate PR webhook ingestion → policy evaluation → published status check.
- **End-to-end tests**: staging repo path: create PR → ensure DCP gates block merge until evidence exists.

Additionally, MLOps systems highlight the importance of metadata and lineage for debugging and governance; TFX ML Metadata explicitly frames pipeline metadata as a logging/lineage equivalent for ML systems. citeturn5search2turn5search21  
Even if you do not run ML pipelines, the **lineage discipline** applies directly to governance evidence.

### Observability requirements

Adopt OpenTelemetry for standardized telemetry signals and W3C Trace Context propagation for cross-service correlation. citeturn1search1turn1search2turn1search25  
Use CloudEvents as an event envelope standard for webhook/event flows (including Cloudbeds webhooks) to normalize event metadata and facilitate auditability. citeturn1search3turn1search11turn7search21

---

## Implementation plan, rollout strategy, and prioritized backlog

### Step-by-step implementation plan with phases, artifacts, gates, and effort

Assumptions: unknown budget/team size; Node/TypeScript monorepo; existing runtime intent-loop A–D implemented; existing CI governance workflows exist. fileciteturn0file1turn0file2

**Phase foundation and contracts (effort: low/med)**  
Milestones:
- Define `dcpContracts.ts` with strict schema validation.
- Implement append-only `AuditEvent` store and trace ID propagation fields (W3C-compatible).
Required artifacts:
- Zod schemas + contract version constants.
- Unit tests for parsing and fail-closed invariants (deny on unknown keys, missing required audit fields).
CI gates:
- Typecheck + contract tests must pass.

**Phase minimal gate enforcement (effort: med)**  
Milestones:
- Build DCP API endpoints: intake, evaluate, publish decision.
- GitHub App/webhook handler that posts required check results.
Required artifacts:
- Policy bundle structure and versioning (policyVersion hash).
- “DCP Gate” check registered as required status check.
CI gates:
- Protected branch requires DCP Gate. citeturn1search4turn1search0

**Phase policy-as-code PDP integration (effort: med)**  
Milestones:
- Integrate a PDP (OPA-style) for deterministic “allow/deny/require evidence” decisions. citeturn0search4turn6search1  
- Encode plane boundary policies and forbidden path rules from doctrine. fileciteturn0file0  
Required artifacts:
- Rego policy tests (or equivalent) treated as first-class.
CI gates:
- Policy tests required.

**Phase reviewer UX and approval workflow (effort: med/high)**  
Milestones:
- Backstage plugin or dedicated UI: Work Queue + Gate Timeline + Evidence Panel. citeturn4search5turn4search1  
- Approval records stored immutably and reflected in gate status.
Required artifacts:
- UX acceptance tests (smoke tests), role-based access enforcement.
CI gates:
- UI build/test and basic security checks.

**Phase supply-chain evidence and attestations (effort: med/high)**  
Milestones:
- SLSA provenance attestations for release builds; in‑toto statement storage. citeturn2search0turn12search6turn12search3  
- Optional Sigstore signing for artifacts/containers. citeturn2search1turn2search9  
Required artifacts:
- Evidence link schema: attestation digest + subject digest.
CI gates:
- Release branch requires provenance present.

**Phase hospitality governance module (Cloudbeds) (effort: med/high)**  
Milestones:
- Encode Cloudbeds credential binding rules, scopes, and webhook validation gates in DCP. citeturn7search12turn7search21turn7search5  
- Add tenant isolation tests and “no cross-tenant credential use” policies.
Required artifacts:
- Integration tests using Cloudbeds sandbox/dummy data guidance (Cloudbeds indicates dev accounts and dummy data). citeturn7search14  
CI gates:
- Vertical governance gate required for hospitality-tagged work items.

### Rollout strategy and change management

A DCP changes culture; roll out in controlled increments:

- Start in **observe-only mode**: DCP posts advisory checks but does not block merges. This builds trust and reveals false positives.
- Move to **block-on-high-risk**: only high-risk classes (auth, entitlements, registry/schema changes) are hard-gated.
- Expand to **default required**: DCP Gate becomes required status check for protected branches. citeturn1search4turn1search8  
- Add **waiver discipline**: waivers require explicit approver identity and expiry triggers, consistent with secure SDLC controls. citeturn2search3turn3search1

### Prioritized backlog of follow-up work

1. Implement DCP policy bundle versioning and distribution (hash-addressed policy sets). citeturn6search1turn0search4  
2. Add “registry delta required” gate for view/action/integration registry modified files; fail closed. citeturn0search3turn4search3  
3. Add supply-chain provenance gate for releases using GitHub build provenance attestations (in‑toto/SLSA). citeturn12search6turn12search2  
4. Add Sigstore verification gate for container images in deployment environments. citeturn2search21turn2search9  
5. Implement Backstage plugin for DCP queue + DCP evidence view. citeturn4search5turn4search1  
6. Add OpenTelemetry instrumentation to DCP and propagate W3C trace context across CI calls. citeturn1search1turn1search2  
7. Add CloudEvents envelope for webhook/event ingestion pipelines, including Cloudbeds webhooks. citeturn1search3turn7search21  
8. Encode OWASP LLM Top 10 gates for internal agents (prompt injection, insecure output handling) for any agent-driven codegen or tooling execution. citeturn8search0turn8search4  
9. MITRE ATLAS-based threat modeling checklist for agent/tooling routes as a “high-risk work item” gate. citeturn8search1turn8search5  
10. Hospitality vertical module: Cloudbeds auth/scope/tenant isolation invariants with e2e tests and webhook idempotency requirements. citeturn7search12turn7search21turn7search5

### Recommended first three sprints with deliverables

**Sprint one (deliverables: contracts + advisory gate)**  
- `dcpContracts.ts` + Zod schemas + unit tests.  
- DCP Intake API + AuditEvent append-only logging.  
- GitHub webhook ingestion that posts an **advisory** DCP Gate check.

**Sprint two (deliverables: enforceable gates + policy PDP)**  
- Policy-as-code PDP integration (OPA-style evaluation). citeturn0search4turn6search1  
- DCP Gate becomes **required** for high-risk paths (auth/registry/schema/entitlements). citeturn1search4turn1search8  
- Evidence attachment model (CI run links, test results) in DCP DB.

**Sprint three (deliverables: reviewer UX + provenance pilot)**  
- Backstage (or dedicated UI) queue and gate timeline view. citeturn4search5turn9search9  
- Provenance pilot for release builds using GitHub attest-build-provenance → stored as evidence. citeturn12search6turn12search3  
- Initial hospitality governance policy scaffolding for Cloudbeds: enforce scope binding rules and tenant isolation invariants. citeturn7search12turn7search14
# AI OS Coding Intent Loop Plan

## Purpose
Convert the existing coding-agent direction into an AI OS-native plan that preserves the required hierarchy:

**intent loop -> scope/permissions -> agent/swarm selection -> tools/actions -> outcomes/views**

This plan does **not** create a parallel architecture. It turns the existing repo direction into a concrete implementation program for an internal coding swarm that can build and maintain the AI OS itself.

---

## 1. Executive decision

### What this system is
An **internal coding swarm** operating on the same governed OS pattern already used elsewhere in the repo.

### What this system is not
- not a generic PM bot
- not a tool-first orchestrator
- not a path-blocked no-code mutation layer
- not Cursor as the control surface

### Governing principle
The primary safety boundary is:
- **isolated feature branch / worktree**
- **intent-derived scope**
- **required checks**
- **evidence packet**
- **peer review / PR gating before merge**

---

## 2. Repo-truth summary

### Already present and reusable
The repo already contains the critical substrate for this plan:

- governance canon and control-plane docs
- intent-loop and canvas-control runtime concepts
- local internal worker lane(s)
- workspace-provisioning patterns
- ui-agent / shadcn design-time worker patterns
- readiness / governance / verification scripts
- mutation-gate / execution-contract concepts
- swarm/orchestration mindset for governed role provisioning

### Missing as first-class artifacts
The repo does **not yet** appear to have the internal coding swarm fully formalized as its own plane.

Missing or incomplete artifacts likely include:
- coding swarm schematic
- coding-specific role capability registry
- intent-execution contracts for coding work
- scope/action/skill registry for coding work
- project / queue / review command-center surfaces
- internal coding-swarm provisioning flow
- branch/worktree execution service
- evidence-packet to PR integration layer

---

## 3. Core architecture

## 3.1 Runtime hierarchy

```text
Jason request
  -> Intent Loop
      -> IntentExecution
          -> ScopeExecution(s)
              -> SkillBinding(s)
                  -> ActionRun(s)
                      -> OutcomePacket
                          -> Review gates
                              -> PR / merge readiness
```

This is the required OS spine.

## 3.2 Plane separation

### A. Intent / Control Plane
Owns:
- classification
- scope derivation
- permission derivation
- specialist selection
- review requirements
- visible state / command-center view

### B. Execution Plane
Owns:
- branch/worktree preparation
- tool invocation
- file mutation
- test execution
- MCP calls
- artifact generation

### C. Review Plane
Owns:
- diff/evidence inspection
- readiness state
- policy satisfaction
- PR creation/update
- merge gate state

---

## 4. Intent loop for coding agents

```text
[User / Jason]
    |
    v
[Intent Loop Resolver]
    |
    +--> classify intent_key
    +--> derive scope graph
    +--> derive permission context
    +--> choose agent/swarm roles
    |
    v
[IntentExecution]
    |
    +--> [ScopeExecution: workspace]
    +--> [ScopeExecution: ui]
    +--> [ScopeExecution: voice]
    +--> [ScopeExecution: canvas]
    +--> [ScopeExecution: routing]
    +--> [ScopeExecution: governance]
    +--> [ScopeExecution: verification]
    |
    v
[SkillBinding per scope]
    |
    +--> repo_analysis
    +--> workspace_integration
    +--> ui_generation
    +--> canvas_surface_derivation
    +--> voice_verification
    +--> registry_alignment
    +--> route_contract_design
    +--> test_verification
    +--> review_packaging
    |
    v
[ActionRun]
    |
    +--> create_branch
    +--> create_worktree
    +--> inspect_files
    +--> modify_files
    +--> call_workspace_mcp
    +--> call_shadcn_mcp
    +--> run_checks
    +--> package_review_artifacts
    |
    v
[OutcomePacket]
    |
    +--> files_touched
    +--> checks_run
    +--> blockers
    +--> risks
    +--> review_ready
    |
    v
[PR + Required Review]
```

---

## 5. Agent roster

## 5.1 First-wave agents

### coding_intent_orchestrator
Purpose:
- accepts internal engineering intent
- creates IntentExecution
- derives scopes and permissions
- assigns specialists
- tracks evidence and review state

### workspace_integration_agent
Purpose:
- owns OS Core App integration powered by Google Workspace
- extends the current workspace-provisioning lane into broader OS Core integration work

### ui_agent
Purpose:
- generates governed layouts and UI implementation plans
- uses shadcn MCP as design-time discovery only
- ships through approved UI-core patterns

### canvas_orchestration_agent
Purpose:
- owns canvas syscall composition
- owns view derivation and typed payload composition
- owns resolver-adjacent surface behavior

### registry_governance_agent
Purpose:
- owns registry alignment
- owns views/actions/routes/schema-anchor updates
- owns governance-side artifact normalization

### routing_agent
Purpose:
- owns route contracts
- owns route/view/action wiring
- owns handler and service boundaries

### verification_agent
Purpose:
- owns lint/typecheck/tests/readiness reports
- owns evidence packet validation
- owns review readiness state

## 5.2 Second-wave specialist

### voice_architect_agent
Purpose:
- owns voice PTT layer work
- explicit-task and elevated-review specialist
- not a casual free-mutation executor

Reason to phase second:
- voice is the most sensitive execution surface
- it needs the review/evidence plane in place first

---

## 6. Scope model

## 6.1 Initial scope keys

- `workspace_scope`
- `ui_scope`
- `voice_scope`
- `canvas_scope`
- `routing_scope`
- `governance_scope`
- `verification_scope`
- `migration_scope`

## 6.2 Scope behavior

Scopes are not file lists.
Scopes are intent-derived execution slices.

Each scope determines:
- which specialist lane can execute
- which skills can be bound
- which actions are legal
- which checks are required
- which review gates apply

---

## 7. Permissions model

## 7.1 Replace file-path blocking
Do **not** use broad permanent deny/allow lists as the main governance model.

### Old model
- forbidden domains
- hard-coded mutation denial
- governance by prevention

### New model
Permissions derive from:
- `intent_key`
- `scope_key`
- `approval_tier`
- `branch / worktree`
- `required_checks`
- `required_review_gates`

## 7.2 Permission resolution

```text
intent -> scopes -> policy context -> agent selection -> allowed skills -> allowed actions
```

## 7.3 Permission tiers

### Tier 0
Low-risk analysis / docs / passive inspection

### Tier 1
Normal UI / routes / standard client/server work

### Tier 2
Shared contracts / canvas control / registries / routing / control-plane work

### Tier 3
Voice runtime / credential-sensitive / critical control-plane mutation

### Important rule
Tier 3 means **elevated**, not **forbidden**.

The system allows the work on the branch, but requires:
- stronger checks
- stronger evidence
- stronger review

---

## 8. Skills and actions

## 8.1 Initial skill set

- `repo_analysis`
- `branch_preparation`
- `workspace_integration`
- `ui_generation`
- `canvas_surface_derivation`
- `voice_verification`
- `registry_alignment`
- `route_contract_design`
- `test_verification`
- `review_packaging`

## 8.2 Initial action set

- `create_branch`
- `create_worktree`
- `inspect_files`
- `modify_files`
- `call_workspace_mcp`
- `call_shadcn_mcp`
- `run_checks`
- `summarize_diff`
- `package_review_artifacts`
- `open_or_update_pr`

## 8.3 Rule
Skills are capability bundles.
Actions are concrete executable operations.

Tools are implementation details beneath actions.

---

## 9. GitHub policy model

## 9.1 Branch lifecycle

```text
base: main
  -> create feature branch from intent execution
  -> optional worktree per scope
  -> execute actions on feature branch only
  -> collect evidence
  -> open/update PR
  -> required checks + reviewers
  -> merge only when review gates satisfied
```

## 9.2 Safety boundary
The feature branch/worktree is the sandbox.

## 9.3 Merge gating
Required before merge:
- checks pass
- evidence packet attached/valid
- required reviewers approve
- outcome packet marked review-ready

## 9.4 Domain-sensitive review
If OutcomePacket touches elevated domains like voice/control-plane:
- more checks required
- stronger reviewer requirements
- no automatic merge

---

## 10. Command-center / views

## Required internal views

### A. Project Intake View
Shows:
- intent request
- derived intent key
- planned scopes
- approval tier

### B. Scope Board View
Shows:
- active scopes
- assigned agents
- status per scope
- blockers

### C. Execution Packet View
Shows:
- branch
- worktree
- skills bound
- actions planned
- required checks

### D. Evidence / Review View
Shows:
- diff summary
- files touched
- checks run
- risks
- review-ready state
- PR link / gate status

### E. Outcome View
Shows:
- completed scopes
- remaining blockers
- follow-up tasks
- merge readiness

---

## 11. Schemas

## 11.1 IntentExecution
```ts
export interface IntentExecution {
  id: string;
  workItemId: string;
  intentKey: string;
  intentInput: Record<string, unknown>;
  state: 'planning' | 'executing' | 'review' | 'completed' | 'failed';
  approvalTier: 'tier0' | 'tier1' | 'tier2' | 'tier3';
  startedAt: string;
  completedAt?: string;
}
```

## 11.2 ScopeExecution
```ts
export interface ScopeExecution {
  id: string;
  intentExecutionId: string;
  scopeKey:
    | 'workspace_scope'
    | 'ui_scope'
    | 'voice_scope'
    | 'canvas_scope'
    | 'routing_scope'
    | 'governance_scope'
    | 'verification_scope'
    | 'migration_scope';
  assignedAgentRole?: string;
  state: 'queued' | 'active' | 'blocked' | 'done';
  scopePlan: Record<string, unknown>;
}
```

## 11.3 SkillBinding
```ts
export interface SkillBinding {
  id: string;
  scopeExecutionId: string;
  skillKey:
    | 'repo_analysis'
    | 'branch_preparation'
    | 'workspace_integration'
    | 'ui_generation'
    | 'canvas_surface_derivation'
    | 'voice_verification'
    | 'registry_alignment'
    | 'route_contract_design'
    | 'test_verification'
    | 'review_packaging';
  config: Record<string, unknown>;
}
```

## 11.4 ActionRun
```ts
export interface ActionRun {
  id: string;
  skillBindingId: string;
  actionKey:
    | 'create_branch'
    | 'create_worktree'
    | 'inspect_files'
    | 'modify_files'
    | 'call_workspace_mcp'
    | 'call_shadcn_mcp'
    | 'run_checks'
    | 'summarize_diff'
    | 'package_review_artifacts'
    | 'open_or_update_pr';
  state: 'queued' | 'running' | 'blocked' | 'succeeded' | 'failed';
  input: Record<string, unknown>;
  output?: Record<string, unknown>;
  startedAt?: string;
  completedAt?: string;
}
```

## 11.5 OutcomePacket
```ts
export interface OutcomePacket {
  id: string;
  intentExecutionId: string;
  filesTouched: Array<{
    path: string;
    changeType: 'added' | 'modified' | 'deleted';
  }>;
  checksRun: Array<{
    cmd: string;
    status: 'passed' | 'failed' | 'skipped';
    artifactUri?: string;
  }>;
  blockers: string[];
  risks: string[];
  reviewReady: boolean;
  requiredGates: string[];
  summary: Record<string, unknown>;
}
```

---

## 12. Route map

## 12.1 Intent/control plane routes

### POST `/api/coding-intents`
Create WorkItem + IntentExecution from internal engineering request.

### GET `/api/coding-intents/:intentExecutionId`
Read current execution state.

### POST `/api/coding-intents/:intentExecutionId/derive-scopes`
Resolve scopes from intent.

### POST `/api/coding-intents/:intentExecutionId/bind-skills`
Bind skill set to resolved scopes.

### POST `/api/coding-intents/:intentExecutionId/create-execution-packet`
Generate branch/worktree/policy packet.

## 12.2 Execution plane routes

### POST `/api/coding-actions/dispatch`
Dispatch ActionRun to a specialist agent.

### POST `/api/local-agent/task`
Existing local worker entry upgraded to accept ExecutionPacket + ActionRequest.

### GET `/api/local-agent/health`
Check Ollama/local worker readiness.

### POST `/api/git/branches`
Create feature branch.

### POST `/api/git/worktrees`
Create worktree.

## 12.3 Review plane routes

### POST `/api/coding-intents/:intentExecutionId/outcome`
Publish/update OutcomePacket.

### POST `/api/coding-intents/:intentExecutionId/review-gates/evaluate`
Evaluate readiness + required gates.

### POST `/api/github/prs`
Open or update PR for execution.

### GET `/api/github/prs/:intentExecutionId`
Fetch PR/gate state.

---

## 13. Cursor agent plan

Cursor should be treated as a **design-time implementation assistant**, not the source of truth.

Its job is to:
- operate against the repo plan
- follow intent-loop-first hierarchy
- generate implementation diffs and artifact updates
- not invent a parallel architecture

## Cursor implementation slices

### Slice 1 — contracts and tables
- add IntentExecution / ScopeExecution / SkillBinding / ActionRun / OutcomePacket schemas
- add migration for storage

### Slice 2 — intent-control service
- implement intent classification to scope graph
- permission derivation from scope + approval tier

### Slice 3 — execution packet + branch/worktree service
- create branch/worktree utilities
- generate execution packets

### Slice 4 — local-agent upgrade
- upgrade `/api/local-agent/task` to accept structured execution packets
- persist ActionRun and evidence

### Slice 5 — GitHub review plane
- PR open/update service
- evidence packet publishing
- review readiness + merge gate state

### Slice 6 — command center view
- intake view
- scope board
- evidence/review panel

---

## 14. Cursor system prompt

```text
You are the AI OS implementation agent working inside the Gateway Global repo.

You must follow this hierarchy exactly:
intent loop -> scope/permissions -> agent/swarm selection -> tools/actions -> outcomes/views

Rules:
1. Do not invent a parallel architecture.
2. Treat the coding-agent plan and repo governance docs as the governing proposal.
3. Preserve the intent loop as the grounding layer.
4. Tool orchestration is execution, not governance.
5. Model coding work as intent-driven scopes supported by skills and realized through actions.
6. Governance is enforced by branch isolation, required checks, evidence packets, and review readiness — not broad hard-coded file deny lists.
7. If a surface is sensitive (voice, credential broker, core control-plane), elevate review requirements instead of hard-blocking implementation.
8. Prefer repo-native patterns, routes, registries, and schemas over introducing external abstractions.
9. Every implementation response must include:
   - what intent/scope this change supports
   - files to create/modify
   - schemas/routes/services affected
   - checks to run
   - risks/blockers
10. Do not claim completion without evidence.

Your output style:
- concrete
- repo-specific
- implementation-first
- no generic PM language
- no replacement architecture unless explicitly requested

When producing code plans, always structure them as:
A. intent supported
B. scopes affected
C. skills/actions required
D. files/routes/schemas to change
E. checks/evidence required
F. review gate implications
```

---

## 15. First implementation milestone

## Milestone name
**Intent-Driven Coding Swarm Foundation**

## Deliverables
- contracts for IntentExecution / ScopeExecution / SkillBinding / ActionRun / OutcomePacket
- migration for persistence
- branch/worktree service
- structured execution packet generation
- upgraded local-agent task route
- minimal command-center intake + scope board view

## Acceptance criteria
- internal engineering request becomes an IntentExecution
- scopes are derived and visible
- specialist lane can be assigned
- execution packet includes branch/worktree/checks/review requirements
- ActionRun result is stored as evidence
- OutcomePacket can mark review-ready before PR merge

---

## 16. Immediate decision

Proceed with first-wave swarm:
- coding_intent_orchestrator
- workspace_integration_agent
- ui_agent
- canvas_orchestration_agent
- registry_governance_agent
- routing_agent
- verification_agent

Phase voice as second-wave specialist after the review/evidence plane is live.

That gives the AI OS a real internal coding swarm built on the same governed intent-loop spine as the rest of the system.


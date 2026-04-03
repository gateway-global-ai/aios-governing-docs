Gateway Global AI — Internal Command OS v1

1. Design Principle

Gateway Global AI manages itself through its own intent-driven OS. No separate admin dashboard product. Internal actors authenticate via OTP, resolve to a governed role, enter an operating cycle, and see only the views and actions their role-cycle pair permits. Everything flows through the same PolicyDecision, IntentLoopStateVector, view/action registries, and audit chain used for customer-facing execution.



2. Actor Model (Roles)

Map internal roles to the existing IntentLoopActorClass from [shared/intentLoopContract.ts](shared/intentLoopContract.ts) and policy-gates.yaml allowed_actor_classes.

2.1. Role Definitions







Role



actorClass



DB Column (admin_users.role)



Policy Gate Classes





Founder / Architect



management



superadmin



management





Operator / Manager



management



manager



management





Engineer / Builder



employee



engineer



employee





Customer Success



employee



customer_success



employee





Read-only Auditor



employee



auditor



employee (read-only gates only)

Implementation:





Extend admin_users.role from free text (admin / superadmin) to a governed enum: superadmin, manager, engineer, customer_success, auditor. Add a CHECK constraint.



Create a mapping function resolveActorClass(role: string): IntentLoopActorClass in a new shared/internalActorContract.ts:





superadmin / manager -> management



engineer / customer_success / auditor -> employee



Wire into auth: After OTP verify in [server/auth.ts](server/auth.ts), the session payload already returns role. The client and server policy layer use resolveActorClass(role) to derive actorClass for intent loop and policy gate checks.

2.2. Permission Matrix

graph LR
    subgraph roles [Internal Roles]
        SA[superadmin]
        MG[manager]
        EN[engineer]
        CS[customer_success]
        AU[auditor]
    end
    subgraph actorClass [Actor Classes]
        MGMT[management]
        EMP[employee]
    end
    SA --> MGMT
    MG --> MGMT
    EN --> EMP
    CS --> EMP
    AU --> EMP

2.3. Per-Role Capability Summary





superadmin: Full read/write across all internal domains. Sensitive mutations (publish, delete, telephony activation, vault). Only role that can override knowledge certification or approve design studio publish.



manager: Read/write for agents, projects, tasks, approvals. Can review and approve coding review gates. Cannot perform sensitive mutations (telephony paid activation, vault, design studio publish).



engineer: Read/write on assigned work items, intent executions, coding swarm. Can inspect agents (read-only). Cannot modify agent behavior, approve review gates, or access billing/telephony.



customer_success: Read/write on customer accounts, onboarding sessions, site configs (controlled). Cannot access coding swarm, agent behavior mutations, or platform settings.



auditor: Read-only everywhere. No write actions. Cannot approve, reject, or mutate anything.



3. Operating Cycles (Journey States)

These are the internal lifecycle state machines that govern what phase of work an entity is in.

3.1. Cycle Definitions

A. Build Cycle (engineering / coding swarm)

States: intake -> planning -> executing -> review -> promoted | blocked

Maps directly to existing intent_executions.state progression and work_items.status. No new table needed — extend work_items.status values.

B. Customer Cycle (client operations)

States: lead -> onboarding -> active -> support -> expansion -> retained | churn_risk

Maps to customer_accounts + onboarding_sessions.status + site_configs lifecycle. Extend customer_accounts with a lifecycle_stage column.

C. Platform Cycle (OS operations)

States: configuration -> validation -> ready -> deployed -> monitored -> incident | recovery

Maps to site_configs + readiness gates + deployment status. Track via site_configs metadata or a thin platform_deployment_states table if needed.

D. Knowledge Cycle (docs / knowledge assets)

States: ingested -> classified -> certified -> active -> stale -> rejected

Already exists conceptually in the knowledge certification layer. Can be derived from knowledge_dimensions + knowledge_certification_overrides state.

E. Approval Cycle (gated decisions)

States: requested -> under_review -> approved | denied | escalated

Maps to existing review_gates.state + intake_change_requests.status. Already has DB backing.

3.2. Cycle-to-Table Mapping

graph TD
    BuildCycle["Build Cycle"] --> workItems["work_items.status"]
    BuildCycle --> intentExec["intent_executions.state"]
    CustomerCycle["Customer Cycle"] --> custAcct["customer_accounts.lifecycle_stage (NEW)"]
    CustomerCycle --> onboarding["onboarding_sessions.status"]
    PlatformCycle["Platform Cycle"] --> siteConfigs["site_configs + readiness"]
    KnowledgeCycle["Knowledge Cycle"] --> knowledgeDims["knowledge_dimensions + cert overrides"]
    ApprovalCycle["Approval Cycle"] --> reviewGates["review_gates.state"]
    ApprovalCycle --> intakeChanges["intake_change_requests.status"]



4. Internal Intents

Map to the intent loop model. Each intent has a key, required actor class, required context keys, and target view.







Intent Key



Actor Classes



Required Context Keys



Target View



Mutation Level





internal.view_agents



management, employee



siteConfigId?



cmd_agents_list



read_only





internal.inspect_agent



management, employee



agentId



cmd_agent_detail



read_only





internal.update_agent_behavior



management



agentId, siteConfigId



cmd_agent_detail



controlled





internal.view_work_items



management, employee



siteConfigId?



cmd_work_items_list



read_only





internal.inspect_work_item



management, employee



workItemId



cmd_work_item_detail



read_only





internal.view_tasks



management, employee



-



cmd_tasks_list



read_only





internal.inspect_task



management, employee



intentExecutionId



cmd_task_detail



read_only





internal.assign_task



management



intentExecutionId, agentId



cmd_task_detail



controlled





internal.view_approvals



management



-



cmd_approvals_list



read_only





internal.approve_review_gate



management



reviewGateId



cmd_approval_detail



controlled





internal.view_customers



management, employee



-



cmd_customers_list



read_only





internal.inspect_customer



management, employee



customerAccountId



cmd_customer_detail



read_only





internal.view_violations



management, employee



-



cmd_violations_list



read_only





internal.check_system_status



management, employee



-



cmd_system_status



read_only





internal.create_work_item



management



siteConfigId?



cmd_work_item_create



controlled





internal.review_knowledge_status



management, employee



siteConfigId?



cmd_knowledge_status



read_only



5. Views

New viewId entries to add to the VIEW_REGISTRY ([docs-governance/canonical/VIEW_REGISTRY.md](docs-governance/canonical/VIEW_REGISTRY.md)) and typed view models in [shared/canvasViewContract.ts](shared/canvasViewContract.ts).

5.1. Command Home





viewId: cmd_home



category: menu



requiredContextKeys: none (derives from auth session)



allowedActions: navigate to any cmd_* view the role permits



policyGate: admin_access



description: Role-aware starting surface showing priorities, blocked items, pending approvals, recent agent activity. Content varies by role.

5.2. Agents List / Detail





viewId: cmd_agents_list / cmd_agent_detail



category: inspector



requiredContextKeys: siteConfigId? / agentId



allowedActions: agent.updateBehavior (management only), agent.inspect, navigate



policyGate: agent_config_access

5.3. Work Items List / Detail / Create





viewId: cmd_work_items_list / cmd_work_item_detail / cmd_work_item_create



category: inspector / inspector / form



requiredContextKeys: - / workItemId / siteConfigId?



allowedActions: workItem.create, workItem.inspect, workItem.execute (trigger orchestrator)



policyGate: workspace_access

5.4. Tasks List / Detail





viewId: cmd_tasks_list / cmd_task_detail



category: inspector



requiredContextKeys: - / intentExecutionId



allowedActions: task.assign, task.inspect, task.execute



policyGate: workspace_access

5.5. Approvals List / Detail





viewId: cmd_approvals_list / cmd_approval_detail



category: controller



requiredContextKeys: - / reviewGateId



allowedActions: approval.approve, approval.deny, approval.escalate



policyGate: admin_access + mutation requires management

5.6. System Status





viewId: cmd_system_status



category: inspector



requiredContextKeys: none



allowedActions: read-only inspection



policyGate: admin_access



6. Actions

New actionId entries to add to the ACTION_REGISTRY ([docs-governance/canonical/ACTION_REGISTRY.md](docs-governance/canonical/ACTION_REGISTRY.md)).







actionId



Entity



Required Keys



Mutation Level



Domain Handler





cmd.navigate



-



targetViewId



none



client router





cmd.agent.inspect



agents



agentId



read_only



GET /api/agents/:id





cmd.agent.updateBehavior



agents



agentId, siteConfigId



controlled



existing agent.updateBehavior handler





cmd.workItem.create



workItems



title, siteConfigId?



controlled



POST /api/coding-intents





cmd.workItem.inspect



workItems



workItemId



read_only



GET /api/coding-intents/:id





cmd.workItem.execute



workItems



intentExecutionId



controlled



POST /api/coding-intents/:id/execute





cmd.task.inspect



intentExecutions



intentExecutionId



read_only



GET /api/coding-intents/:id





cmd.task.assign



scopeExecutions



scopeId, agentRoleType



controlled



new handler





cmd.approval.approve



reviewGates



reviewGateId



controlled



PATCH /api/review-gates/:id





cmd.approval.deny



reviewGates



reviewGateId



controlled



PATCH /api/review-gates/:id





cmd.approval.escalate



reviewGates



reviewGateId



controlled



PATCH /api/review-gates/:id





cmd.customer.inspect



customerAccounts



customerAccountId



read_only



GET /api/customers/:id





cmd.violation.inspect



orchestrationViolations



violationId



read_only



new handler





cmd.knowledge.reviewStatus



knowledgeDimensions



siteConfigId?



read_only



existing knowledge routes



7. Policy Gates (New entries for registry-yaml/policy-gates.yaml)







gate_id



allowed_actor_classes



mutation_level



description





cmd.home



employee, management



none



Command OS home





cmd.work_items.read



employee, management



read_only



View work items





cmd.work_items.write



management



controlled



Create/modify work items





cmd.work_items.execute



management



controlled



Trigger autonomous execution





cmd.tasks.read



employee, management



read_only



View tasks





cmd.tasks.assign



management



controlled



Assign agent to task





cmd.approvals.read



employee, management



read_only



View pending approvals





cmd.approvals.decide



management



controlled



Approve/deny/escalate





cmd.violations.read



employee, management



read_only



View violation log





cmd.system_status.read



employee, management



read_only



Platform health

Existing gates (admin_access, agent_config_access, workspace_access) are reused where they already cover the need.



8. Logical Routes (New entries for LOGICAL_ROUTE_REGISTRY.md)







routeId



domain



requiredContextKeys



requiredRoleScope



linkedViewId



browserPath





cmd.home



internal



-



employee, management



cmd_home



/command





cmd.agents.list



internal



siteConfigId?



employee, management



cmd_agents_list



/command/agents





cmd.agents.detail



internal



agentId



employee, management



cmd_agent_detail



/command/agents/:id





cmd.work_items.list



internal



-



employee, management



cmd_work_items_list



/command/work-items





cmd.work_items.detail



internal



workItemId



employee, management



cmd_work_item_detail



/command/work-items/:id





cmd.tasks.list



internal



-



employee, management



cmd_tasks_list



/command/tasks





cmd.tasks.detail



internal



intentExecutionId



employee, management



cmd_task_detail



/command/tasks/:id





cmd.approvals.list



internal



-



management



cmd_approvals_list



/command/approvals





cmd.approvals.detail



internal



reviewGateId



management



cmd_approval_detail



/command/approvals/:id





cmd.system_status



internal



-



employee, management



cmd_system_status



/command/status





cmd.customers.list



internal



-



employee, management



cmd_customers_list



/command/customers





cmd.violations.list



internal



-



employee, management



cmd_violations_list



/command/violations





cmd.knowledge.status



internal



siteConfigId?



employee, management



cmd_knowledge_status



/command/knowledge



9. Context Keys (New entries for CONTEXT_KEYS.md)





workItemId — scopes to a specific work_items row



intentExecutionId — already conceptually used; formalize



reviewGateId — scopes to a specific review_gates row



violationId — scopes to an orchestration_violations row



targetViewId — navigation target for cmd.navigate action



10. Schema Changes

10.1. admin_users.role enum enforcement

Migration to add a CHECK constraint:

ALTER TABLE admin_users ADD CONSTRAINT admin_users_role_check
  CHECK (role IN ('superadmin', 'manager', 'engineer', 'customer_success', 'auditor'));

Ensure existing admin rows are migrated to superadmin or appropriate role first.

10.2. customer_accounts.lifecycle_stage (new column)

ALTER TABLE customer_accounts ADD COLUMN IF NOT EXISTS lifecycle_stage TEXT
  NOT NULL DEFAULT 'lead'
  CHECK (lifecycle_stage IN ('lead', 'onboarding', 'active', 'support', 'expansion', 'retained', 'churn_risk'));

10.3. work_items.status values

Verify/extend CHECK constraint to include: queued, planning, executing, review, promoted, blocked, cancelled.



11. New Shared Contract

Create shared/internalCommandContract.ts:





INTERNAL_ROLES const array



InternalRole type



resolveActorClass(role: InternalRole): IntentLoopActorClass



INTERNAL_CYCLE_STATES per cycle



CMD_VIEW_IDS const array



CMD_ACTION_IDS const array



CmdHomeViewModel, CmdAgentsListViewModel, CmdWorkItemsListViewModel, CmdTasksListViewModel, CmdApprovalsListViewModel, CmdSystemStatusViewModel typed interfaces



12. Server Routes

Create [server/routes/commandRoutes.ts](server/routes/commandRoutes.ts) — modular router mounted at /api/command:





GET /api/command/home — returns role-derived home data (counts, priorities, recent activity)



GET /api/command/agents — list agents (reuses existing queries)



GET /api/command/work-items — list work items



GET /api/command/tasks — list intent executions



GET /api/command/approvals — list review gates in pending state



GET /api/command/violations — list orchestration violations



GET /api/command/system-status — aggregated platform health

All routes use requireAuth middleware and check resolveActorClass(req.session.user.role) against the gate's allowed_actor_classes.



13. Client Shell

Create client/src/pages/command/CommandShell.tsx as the internal OS shell:





Sidebar navigation derived from role (only shows views the role can access)



Routes under /command/*



Uses existing auth context from [client/src/lib/auth.tsx](client/src/lib/auth.tsx)



Renders cmd_* views based on route



14. Auth Flow Enhancement

sequenceDiagram
    participant Actor
    participant Client
    participant Server
    participant DB

    Actor->>Client: Enter phone/email
    Client->>Server: POST /api/auth/send-otp
    Server->>DB: Verify admin_users row exists
    Server-->>Actor: OTP via Twilio Verify
    Actor->>Client: Enter OTP
    Client->>Server: POST /api/auth/verify-otp
    Server->>DB: Create auth_session, update last_login_at
    Server-->>Client: token + user (id, phone, name, role)
    Client->>Client: resolveActorClass(role)
    Client->>Client: Derive allowed views from role
    Client->>Client: Render CommandShell with role-scoped nav

No changes to the OTP mechanism itself. The enhancement is post-auth: the client uses the role to derive what the actor sees.



15. Phased Implementation

Phase 1 — Foundation (this slice)





shared/internalCommandContract.ts — roles, actor class mapping, view/action IDs



Migration: admin_users.role CHECK constraint



server/routes/commandRoutes.ts — API surface



Registry updates: VIEW_REGISTRY, ACTION_REGISTRY, LOGICAL_ROUTE_REGISTRY, CONTEXT_KEYS, policy-gates.yaml



Basic CommandShell.tsx + cmd_home view



Agents list/detail views (reuse existing data)



Work items list/detail views

Phase 2 — Operations





Tasks list/detail with assignment



Approvals list with approve/deny/escalate



Violations list



Customer list/detail



customer_accounts.lifecycle_stage migration

Phase 3 — Intelligence





System status (aggregated health)



Knowledge status view



Voice-first internal operation (future)



Coding swarm dispatch from command surface
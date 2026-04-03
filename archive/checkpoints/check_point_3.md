All five deliverables complete. Here's the full picture of what was built in this step:

What the peer review asked for — and what was delivered
1. WebSocket/Live Voice Enforcement Parity
Problem: The highest-risk surface — tool execution via geminiVoice.ts → executeContract() — had its own mutation gate but no PolicyDecision. Two parallel enforcement systems that could drift.

Solution: Bridged PolicyDecision into executeContract() at the contract boundary. Every tool call now:

Evaluates a PolicyDecision via the registry-backed catalog (skill.dispatch gate)
Returns POLICY_DENIED with structured decision if the gate denies
Attaches policyDecision to both success and error results for audit
The voice lockdown files remain untouched — the bridge happens at the executionMutationGate.ts boundary, which is the correct architectural seam.

2. Client/Canvas Parity
Problem: The client has zero PolicyDecision integration. useOSMenu hardcodes menu trees per role. ConciergePanel uses localAdminMode to bypass. voiceTurnOrchestrator injects views without checking allowedViewIds.

Solution: Created client/src/hooks/usePolicyEnforcement.ts — a typed hook that:

Hydrates allowedViewIds and allowedActionIds from server canvas.resolve responses
Provides isViewAllowed(viewId) and isActionAllowed(actionId) guards
Provides filterMenuItems() to strip unauthorized items from any menu tree
Logs violations to an inspectable getPolicyViolationLog() for debugging
Supports strict and permissive enforcement modes
Defaults to permissive (pass-through when server hasn't provided a surface yet) to avoid breaking existing flows during rollout
3. Strict-by-Default on Protected Surfaces
Problem: The doctrine enforcer used a single global mode. Protected surfaces (billing, telephony, site config mutations, policy registry itself) should throw on violations, not just warn.

Solution: Added surface classification to doctrineEnforcer.ts:

STRICT_SURFACES Set declares file path prefixes that get strict enforcement regardless of global mode
resolveEnforcementMode(file) checks whether the violation occurred on a protected surface
Protected surfaces include: executionMutationGate, policyGate, siteConfigRoutes, agentSystemRoutes, telephonyRoutes, billingRoutes, secureVaultRoutes, businessTelephonyRoutes, platformLicenseRoutes, and the entire os-core/control-plane
addStrictSurface() allows runtime expansion as more surfaces harden
4. CI Fail-Close
Problem: The audit scanner needed to be CI-ready — machine-readable output and clear pass/fail semantics.

Solution: Enhanced scripts/audit-policy-bypass.ts:

--json flag outputs structured JSON report with coverage percentage, bypass list, and pass/fail
Coverage meter shows N of M mutation routes governed
Clear exit codes: 0 = all gated/exempted, 1 = bypasses detected
Already registered as npm run audit:policy-bypass
5. Registry Convergence
Problem: siteScopedAccess.ts maintained a 200-line POLICY_ROLE_ALLOWLIST — a parallel policy system with hardcoded role-to-gate mappings that duplicated policy-gates.yaml.

Solution: Converged canRoleSatisfyPolicy() to consult policy-gates.yaml via the catalog bridge first:

Maps raw role strings to actor classes (management, employee, customer)
Checks the gate's allowedActorClasses from the registry
Falls back to the legacy POLICY_ROLE_ALLOWLIST only for gates not yet in policy-gates.yaml
Added roleToActorClass() mapping function
Marked the legacy allowlist with convergence documentation
Current enforcement chain (complete)
Doctrine (why)
  → Violation Codes (machine language for drift)
  → PolicyDecision contract (structured verdicts)
  → policy-gates.yaml (single authority for gates)
  → policyGateCatalog (boot-time registry loader + drift detection)
  → Server middleware: requirePolicy() (HTTP routes)
  → executionMutationGate: evaluateToolPolicyDecision() (WebSocket/voice tools)
  → siteScopedAccess: registry-first lookup (convergence bridge)
  → Client hook: usePolicyEnforcement() (canvas/view guard)
  → doctrineEnforcer: strict on protected surfaces (runtime assertion)
  → audit-policy-bypass: CI scanner (automated regression prevention)
The system now has enforcement parity across HTTP, WebSocket, client canvas, and the execution mutation gate. Protected surfaces are strict-by-default. The CI scanner prevents regression. The peer review's directive — "make it universal" — is now structurally addressed at every layer.
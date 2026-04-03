What was delivered — all five improvements shipped
1. Certification Lifecycle
The KnowledgeItemSchema now carries lastValidatedAt and refreshIntervalHours. The filter enforces a staleness check:


knowledgeCertificationContract.ts
Lines 256-265
    let effectiveLevel = item.certificationLevel;
    if (
      item.lastValidatedAt &&
      item.refreshIntervalHours &&
      item.refreshIntervalHours > 0
    ) {
      const staleAfterMs = item.refreshIntervalHours * 3_600_000;
      const validatedAt = new Date(item.lastValidatedAt);
      if (now.getTime() - validatedAt.getTime() > staleAfterMs) {
        effectiveLevel = "unverified";
      }
Stale knowledge does not get rejected — it gets downgraded to unverified, which means it's excluded from approved+trusted gates (billing, voice) but still available with disclaimers on general chat. The DB columns expires_at, last_validated_at, and refresh_interval_hours are all live on knowledge_artifacts.

2. Conflict Resolution
Source priority is encoded as data:


knowledgeCertificationContract.ts
Lines 108-115
export const SOURCE_CONFLICT_PRIORITY: Record<KnowledgeSourceType, number> = {
  system: 100,
  owner: 75,
  web: 50,
  external: 50,
  inference: 25,
};
When resolveConflicts: true is set on the filter context, resolveKnowledgeConflicts() keeps the highest-priority item per dimensionId. Items without a dimension are always kept — conflict resolution only applies when two items explicitly claim the same knowledge space.

The DB column conflict_priority stores this per-artifact, and the migration backfilled it from existing trust_weight values.

3. Knowledge Scope Binding
Three levels of scope binding are now enforced:

siteConfigId — always enforced (existing behavior)
agentId — new column on knowledge_artifacts; when set, the item is only visible to that specific agent
swarmRole — new column; restricts to a specific role type (e.g., billing_analyst cannot see marketing docs)
The filter checks both:


knowledgeCertificationContract.ts
Lines 271-281
    if (context.agentId && item.agentId && item.agentId !== context.agentId) {
      rejected.push(item);
      rejections.push({ knowledgeId: item.knowledgeId, reason: "agent_scope_mismatch" });
      continue;
    }
    if (context.swarmRole && item.swarmRole && item.swarmRole !== context.swarmRole) {
      rejected.push(item);
      rejections.push({ knowledgeId: item.knowledgeId, reason: "swarm_role_scope_mismatch" });
      continue;
    }
The assembleGovernedKnowledge call accepts opts.agentId and opts.swarmRole to activate scope filtering.

4. Knowledge Audit Trail
New knowledge_audit_log table records every prompt assembly:

Column	What it captures
total_candidates	How many items were considered
admitted_count / rejected_count	Filter outcome counts
allowed_levels / allowed_source_types	Policy constraints applied
admitted_ids / rejected_ids	Exact item IDs
rejection_reasons	Structured [{id, reason}] — why each item was filtered
knowledge_block_chars	Size of what reached the model
filter_duration_ms	Performance tracking
session_id / channel / policy_gate	Context correlation
This is fire-and-forget — failures log a warning but never block the prompt path.

5. Knowledge DDL
Migration 0078_knowledge_certification_governance.sql — applied successfully:

13 new columns on knowledge_artifacts (source_type, certification_level, certification_source, confidence_score, certified_at, certified_by, expires_at, last_validated_at, refresh_interval_hours, agent_id, swarm_role, conflict_priority, source_id)
4 CHECK constraints including chk_inference_not_approved — the DB itself prevents inference from being approved or trusted
6 new indexes for governance queries (certification_level, source_type, expires_at, agent_scope, swarm_role_scope, conflict_priority)
knowledge_audit_log table with 2 indexes
Backfill of existing artifacts from trust_weight to the new certification model
The DB-level doctrine enforcement
This is the strongest line in the migration:

ALTER TABLE knowledge_artifacts
  ADD CONSTRAINT chk_inference_not_approved
  CHECK (NOT (source_type = 'inference' AND certification_level IN ('approved', 'trusted')));
This means Doctrine 11 is enforced at the database level. Even if a bug in application code tries to store LLM output as approved, PostgreSQL rejects the row. That's physics, not policy.

Enforcement chain (complete)
Knowledge Source Registry (knowledge-sources.yaml)
  → Ingest with source_type + certification_level (DB columns)
  → DB constraint: inference ≠ approved|trusted
  → PolicyDecision.allowedKnowledgeLevels (per gate)
  → filterKnowledgeByCertification():
       rejected level → excluded
       expired → excluded  
       stale (refresh interval exceeded) → downgrade to unverified
       level not allowed → excluded
       source type not allowed → excluded
       agent scope mismatch → excluded
       swarm role mismatch → excluded
       conflict resolution → highest priority per dimension wins
       cap to maxItems → overflow excluded
  → Model receives ONLY admitted knowledge
  → knowledge_audit_log records everyt
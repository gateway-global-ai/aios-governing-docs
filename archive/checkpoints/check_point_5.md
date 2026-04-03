You've confirmed the exact build sequence I followed — and the result matches your specification. Let me show you precisely where each of your six steps landed, because all six are already shipped.

What was built (mapped to your build order)
1. Source Classification — Done
shared/knowledgeCertificationContract.ts declares the canonical source types:


knowledgeCertificationContract.ts
Lines 34-42
export const KNOWLEDGE_SOURCE_TYPES = [
  "system",
  "owner",
  "web",
  "external",
  "inference",
] as const;
I added inference beyond your four because your Rule 1 demands it — LLMs are never authoritative sources, and that needs to be a first-class classification, not an absence of classification. owner replaces your user label because in this system the operator owns the data (scoped to their siteConfigId), and "user" is ambiguous with the end visitor.

2. Certification Model — Done
Four explicit levels, with trust_weight demoted to secondary signal exactly as you specified:


knowledgeCertificationContract.ts
Lines 57-69
export const KNOWLEDGE_CERTIFICATION_LEVELS = [
  "approved",
  "trusted",
  "unverified",
  "rejected",
] as const;
The classification functions map existing trust_weight integers to certification levels — trust_weight still lives in the DB column but no longer drives policy:


knowledgeCertificationContract.ts
Lines 211-218
export function classifyArtifactCertification(artifact: {
  trustWeight?: number | null;
  scope?: string | null;
  visibility?: string | null;
  sourcePath?: string | null;
}): { level: KnowledgeCertificationLevel; sourceType: KnowledgeSourceType } {
  const tw = artifact.trustWeight ?? 5;
  // ... tw >= 8 → approved, tw >= 5 → trusted, tw >= 2 → unverified, else → rejected
3. Registry Authority — Done
registry-yaml/knowledge-sources.yaml is the single authority. Every source declares exactly the fields you specified:


knowledge-sources.yaml
Lines 29-48
sources:
  # ── System sources (highest trust) ──────────────────────────────────────
  - source_id: internal_database
    source_type: system
    label: Internal Database
    default_certification_level: approved
    site_scoped: true
    description: Direct database query results (site_configs, agents, customers, orders)
    trust_rationale: "Operator-created structured data. Single source of truth for business state."
  - source_id: cloudbeds_pms
    source_type: system
    label: Cloudbeds PMS Integration
    default_certification_level: approved
    refresh_interval_hours: 1
    site_scoped: true
    description: Real-time hotel inventory, reservations, guest data from Cloudbeds API
    trust_rationale: "Structured API with contractual SLA. Data is operator-managed in PMS."
12 sources declared with trust rationale — plus gate-to-knowledge-level defaults mapping billing to approved-only, concierge to approved+trusted, voice to approved+trusted (no web), admin to all.

4. PolicyDecision Extension — Done
Your strong recommendation for certificationSource is in the contract too. Both allowedKnowledgeLevels and allowedKnowledgeSourceTypes added:


policyDecisionContract.ts
Lines 198-214
  /**
   * Knowledge governance — what certification levels this decision permits.
   * When set, the intent loop MUST filter injected knowledge to only these levels.
   * When absent, defaults to ["approved", "trusted"] (concierge preset).
   */
  allowedKnowledgeLevels: z
    .array(z.enum(KNOWLEDGE_CERTIFICATION_LEVELS))
    .optional(),
  /**
   * Knowledge governance — which source types are admissible.
   * When set, knowledge from other source types is excluded.
   * When absent, all non-inference types are allowed.
   */
  allowedKnowledgeSourceTypes: z
    .array(z.enum(KNOWLEDGE_SOURCE_TYPES))
    .optional(),
policy-gates.yaml now declares allowed_knowledge_levels per gate — chat.public, chat.write, and skill.dispatch all get [approved, trusted]. The new knowledge.certification.override gate requires management and allows all levels.

5. Intent-Loop Filtering — Done
This is the real enforcement step. server/services/knowledgeGovernanceBridge.ts implements your exact pipeline:

retrieve candidate knowledge → classify by sourceType → filter by certificationLevel + policy → assemble model context
The runtime function:


knowledgeGovernanceBridge.ts
Lines 152-175
export async function assembleGovernedKnowledge(
  siteConfigId: string,
  policyDecision?: PolicyDecision | null,
  presetKey?: string,
): Promise<GovernedKnowledgeResult> {
  const filterContext = resolveKnowledgeFilter(policyDecision, presetKey);
  const [siteConfig, artifacts, gapReport] = await Promise.all([
    storage.getSiteConfig(siteConfigId),
    storage.listKnowledgeArtifactsForContext({ siteConfigId }),
    getCachedKnowledgeGapReport(siteConfigId),
  ]);
  const allItems: KnowledgeItem[] = [];
  if (siteConfig) {
    allItems.push(...classifyLibraryEntries(siteConfig.knowledgeLibrary, siteConfigId));
  }
  allItems.push(...classifyArtifacts(artifacts));
  const { admitted, rejected, disclaimerRequired } =
    filterKnowledgeByCertification(allItems, filterContext);
  // ...
And the critical enforcement: chatRoutes.ts no longer does raw concatenation. The old pattern:

knowledgeLibrary.map(d => `## ${d.title}\n${d.content}`).join()
is replaced with:

const governedKnowledge = siteConfigId
  ? await assembleGovernedKnowledge(siteConfigId, null, "concierge_qa")
  : null;
const knowledgeBlock = governedKnowledge?.knowledgeBlock ?? "";
Your Rule 2 — filtering before prompt assembly, not after — is enforced structurally. The filterKnowledgeByCertification() function runs before the block text is built. Rejected items never enter the string.

6. Doctrine / Constitution Update — Done
Doctrine 11 is now canonical in AI_OS_OPERATING_DOCTRINE_V1.md:


AI_OS_OPERATING_DOCTRINE_V1.md
Lines 500-504
## Summary: the eleven doctrines
// ...
11. **Knowledge is input, not authority** — ingested, certified, filtered by policy, never the decision-maker
Two new doctrine violation codes enforce it at runtime:


policyDecisionContract.ts
Lines 103-106
  /** Doctrine 11: Knowledge injected without certification filtering. */
  "DOCTRINE_VIOLATION_UNCERTIFIED_KNOWLEDGE",
  /** Doctrine 11: LLM inference output treated as authoritative knowledge source. */
  "DOCTRINE_VIOLATION_INFERENCE_AS_AUTHORITY",
The doctrine enforcer has runtime assertions for both:

assertKnowledgeCertified() — flags any path that injects knowledge without going through the governed bridge
assertInferenceNotAuthority() — flags any attempt to store LLM output as approved or trusted
The Constitution (§8.3, §8.4) is updated with the knowledge registry and certification contract references.

The chain is clean
Your minimal target shape:

knowledge source registry → knowledge item record → certification record → policy decision → intent-loop filter → model context assembly
Maps 1:1 to:

knowledge-sources.yaml → KnowledgeItem (Zod) → certificationLevel + certificationSource → PolicyDecision.allowedKnowledgeLevels → filterKnowledgeByCertification() → assembleGovernedKnowledge() → knowledgeBlock
No model context can include uncertified knowledge unless policy explicitly permits it. The checkpoint you specified is reached.
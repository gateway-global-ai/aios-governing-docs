System State — March 31, 2026
What exists (proven, enforced, deployed)
Three governed planes:

Plane	Status	Key enforcement
Execution	Enforced	PolicyDecision gates every mutation (HTTP, WS, tools)
Control	Registry-backed	policy-gates.yaml, doctrine violation codes, CI scanner
Knowledge	Certified	Source classification, certification levels, DB constraints, audit trail
Eleven doctrines — all machine-enforceable, not just documented.

Database-level invariants:

chk_inference_not_approved — LLM output cannot be stored as authoritative
chk_source_type, chk_certification_level, chk_certification_source — enum enforcement at the DB layer
Knowledge filter pipeline (correct order, proven):

level → expiration → staleness → policy → source type → scope → conflict → cap → audit
External intelligence pattern (repeatable):

External signal → classify → certify → policy-filter → context assembly → audit
Proven with SerpAPI reviews. Ready for: Yelp, social media, support tickets, call transcripts, survey data — same pipeline.

What this session built (complete inventory)
Artifact	Path	Purpose
Knowledge Certification Contract	shared/knowledgeCertificationContract.ts	Zod schemas, filter function, review classifier, conflict resolution
PolicyDecision extension	shared/policyDecisionContract.ts	allowedKnowledgeLevels, allowedKnowledgeSourceTypes, 2 new doctrine codes
Knowledge Sources Registry	registry-yaml/knowledge-sources.yaml	Single authority for 12 knowledge sources + gate defaults
Knowledge Governance Bridge	server/services/knowledgeGovernanceBridge.ts	Runtime filter + audit logger between knowledge store and model context
Policy Gates (knowledge)	registry-yaml/policy-gates.yaml	allowed_knowledge_levels per gate, 2 new knowledge gates
Doctrine 11	docs-governance/canonical/AI_OS_OPERATING_DOCTRINE_V1.md	Knowledge is input, not authority
Doctrine Enforcer extensions	os-core/.../doctrineEnforcer.ts	assertKnowledgeCertified(), assertInferenceNotAuthority()
DDL migration	migrations/0078_knowledge_certification_governance.sql	13 columns, 4 constraints, 6 indexes, audit log table, backfill
Schema update	shared/schema.ts	knowledgeArtifacts certification columns + knowledgeAuditLog table
Chat route wiring	server/routes/chatRoutes.ts	Raw concatenation → assembleGovernedKnowledge()
Voice knowledge bridge	server/services/voiceKnowledgeBridge.ts	assembleGovernedVoiceKnowledge() with voice_live preset
Review classifier	shared/knowledgeCertificationContract.ts	Star-based experience/lesson classification
Review integration	server/tools/dataIngestionHandler.ts	Intelligence brief with classified experience/lesson sections
Pricing update	Schema + tool declarations	$1.00/review, authorization required
Constitution update	LEAN_AI_OS_CORE_CONSTITUTION_V1.md	§8.3 + §8.4 knowledge governance
The four options you offered
All four are now genuinely safe to pursue. Before this session, none of them were — because uncontrolled knowledge would have undermined any production deployment, any customer onboarding, and any monetizable layer.

Now:

Docker image — the extraction manifest already exists, and the system is structurally complete
First production deployment — the deployment checklist is written, enforcement is proven
Agent/swarm creation pipeline — skills + knowledge + policy are wired; the pattern is proven
Customer onboarding flow — reviews + knowledge + voice can onboard safely
The system cannot lie to itself. That's the foundation everything else stands on.

Where do you want to go?
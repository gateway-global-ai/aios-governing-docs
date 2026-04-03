IntentNextStepPacket — Execution Complete
Files Created
shared/canvasViewContract.ts (edited) — Added 6 new types:

IntentActionMode — 5-mode enum: direct_execute, open_canvas, need_grounding, need_auth, need_confirmation
IntentNextStepFilter — reflects real API params / DB columns as filterable capabilities
IntentNextStepReduction — executable sort+limit operations ("pick 5 cheapest")
IntentNextStepViewOption — available canvas rendering modes (list, map, compare)
IntentNextStepPacket — the full skill response with resultCount, resultSummary, filters, reductions, viewOptions, promptToUser, queryContext
server/services/intentNextStepDeriver.ts (new) — The reflection function:

QueryResultMeta interface for passing real query results
deriveActionMode() — determines action from security gates, result counts, filter availability
buildPromptToUser() — assembles grounded speech from real numbers and real capability labels
deriveNextStepPacket() — main export, builds the full packet from resolve result + resolution + query metadata
server/routes/canvasControlRoutes.ts (edited) — Wired into canvas.resolve:

Calls deriveNextStepPacket(mergedResolve, loopResolution) after surface derivation
Includes nextStep in HTTP response alongside existing intentLoopResolution, intentLoopTrace, surfaceDerivation
client/src/services/voiceTurnOrchestrator.ts (edited) — Consumes the packet:

Parses nextStep from canvas.resolve response
Stores as lastNextStepPacket on the orchestrator
buildSpeechGroundingContext prioritizes nextStep.resultSummary for screen summary and nextStep.promptToUser for speaking instructions
Exposes getLastNextStepPacket() for ConciergePanel canvas rendering decisions
docs-governance/canonical/INTENT_NEXT_STEP_PACKET_SPEC_V1.md (new) — Full governance spec covering the core principle, architecture, design rules, action modes, re-query loop, prohibited patterns, and integration points

What This Enables
Any agent in the system now receives a structured skill response that tells it:

What it found — real count, real summary
What it can do — real filters, real sorts, real reductions (all executable)
How it can show it — real view options the canvas can render
What to say — data-grounded prompt built from real numbers
The lost agent is now a super agent. No hallucination possible — every path in the packet maps to something the system can actually execute.
# VALIDATION_RESULTS

**Generated:** 20260408-051157Z (UTC) by `run_isolated_execution_demo.py` 0.3.1

## install

**cwd:** `C:\Apps\aios-exec-demos\demo_exec_ui_review-20260408-051157Z`

**command:** `npm ci`

**exit 0**

```
added 316 packages, and audited 317 packages in 4s

46 packages are looking for funding
  run `npm fund` for details

1 high severity vulnerability

To address all issues, run:
  npm audit fix

Run `npm audit` for details.
npm warn deprecated node-domexception@1.0.0: Use your platform's native DOMException instead
```

## build

**cwd:** `C:\Apps\aios-exec-demos\demo_exec_ui_review-20260408-051157Z`

**command:** `npm run build`

**exit 0**

```
> react-example@0.0.0 build
> vite build

vite v6.4.1 building for production...
transforming...
âœ“ 2151 modules transformed.
rendering chunks...
computing gzip size...
dist/index.html                   1.02 kB â”‚ gzip:   0.54 kB
dist/assets/index-DzShswzP.css   69.75 kB â”‚ gzip:  11.73 kB
dist/assets/index-BlM5wY3H.js   821.82 kB â”‚ gzip: 212.02 kB
âœ“ built in 4.93s

(!) Some chunks are larger than 500 kB after minification. Consider:
- Using dynamic import() to code-split the application
- Use build.rollupOptions.output.manualChunks to improve chunking: https://rollupjs.org/configuration-options/#output-manualchunks
- Adjust chunk size limit for this warning via build.chunkSizeWarningLimit.
```

## test

**cwd:** `C:\Apps\aios-exec-demos\demo_exec_ui_review-20260408-051157Z`

**command:** `npm test`

**exit 0**

```
> react-example@0.0.0 test
> tsx --test scripts/uiReviewRag.test.ts src/workspace/mailSearchRows.test.ts src/workspace/contactsMcpParse.test.ts src/workspace/workspaceIntentRouter.test.ts src/workspace/workspacePostConnect.test.ts src/workspace/driveListEmpty.test.ts src/workspace/callWorkspaceMcpAdapterCallsite.test.ts src/local-llm/threadSummaryV1.test.ts src/scope/scopeEngine.test.ts src/shell/shellStateCommands.test.ts src/shell/shellIntentRouter.test.ts src/shell/shellBootstrap.test.ts src/shell/shellAuthority.test.ts src/shell/shellNavigationApply.test.ts src/shell/workspaceState.test.ts src/core/shell/sessionEntryClassification.test.ts src/core/shell/shellPrimaryOutcome.test.ts src/core/compliance/spec009DisclosurePredicates.test.ts src/core/policy/localInterpretationRequired.test.ts src/core/coreImportBoundary.test.ts src/shellCanvas/deriveWorkspaceIntentForDisclosure.test.ts src/compliance/spec009PrimaryDisclosure.presentation.test.ts

â–¶ uiReviewRag
  âœ” tokenizeQuery drops stopwords (1.2211ms)
  âœ” scoreChunk ranks relevant chunk higher (0.3619ms)
  âœ” retrieveTopK returns ordered chunks (0.3851ms)
âœ” uiReviewRag (2.9727ms)
âœ” secondary line includes workspace and voice notes (3.7979ms)
âœ” secondary line adds capability when local required and degraded (1.2129ms)
âœ” disclosure needed: voice mode without voice input (0.8606ms)
âœ” disclosure not needed: chat mode without voice (0.1489ms)
âœ” disclosure needed: workspace error (0.0994ms)
âœ” disclosure needed: workspace auth_required (execution token missing) (0.0887ms)
âœ” disclosure needed: local required but not ready (0.1309ms)
â–¶ src/core import boundary
  âœ” no core source file imports React or UI packages (8.3091ms)
âœ” src/core import boundary (12.4246ms)
â–¶ resolvedIntentRequiresLocalModel
  âœ” is false for null/undefined (1.3137ms)
  âœ” is false for typical read intents (1.0096ms)
  âœ” is true for thread summarize (0.1683ms)
âœ” resolvedIntentRequiresLocalModel (4.4593ms)
â–¶ sessionEntryClassification (AMD-2026-012 Â§5)
  âœ” classifies as new when no prior engagement (1.5142ms)
  âœ” classifies as returning after markSessionEntryEngaged (0.491ms)
âœ” sessionEntryClassification (AMD-2026-012 Â§5) (3.9749ms)
â–¶ deriveShellPrimaryOutcome (AMD-2026-012 Â§7)
  âœ” idle shell without canvas â†’ ready_for_intent (0.8027ms)
  âœ” workspace onboarding â†’ needs_auth (0.1343ms)
  âœ” agent processing with no canvas â†’ ready_to_execute (0.2164ms)
  âœ” hub visible, agent idle â†’ executed_with_result (0.1325ms)
  âœ” agent error â†’ execution_failed (0.0946ms)
âœ” deriveShellPrimaryOutcome (AMD-2026-012 Â§7) (2.454ms)
â–¶ threadSummaryV1
  âœ” parses plain JSON (2.2507ms)
  âœ” extracts JSON from fenced block (3.8228ms)
  âœ” extractJsonObjectText finds object in prose (1.4991ms)
  âœ” fails on invalid JSON (1.1856ms)
  âœ” fails when root is array (0.4612ms)
  âœ” coerces types safely (0.2358ms)
âœ” threadSummaryV1 (13.2078ms)
â–¶ validateScopeOperation
  âœ” allows read when key is in review_files (1.5724ms)
  âœ” allows read when key is only in modify_files (0.2274ms)
  âœ” denies read when key is outside envelope (0.2925ms)
  âœ” denies when key is in protected_files (0.2141ms)
  âœ” allows write when key is in modify_files (0.1832ms)
  âœ” denies write when key is review-only (0.1897ms)
âœ” validateScopeOperation (5.5181ms)
â–¶ routingEnvelopeToScopeTarget
  âœ” maps thread.read to read + gmail:thread key (1.1988ms)
  âœ” fails thread.read without resource id (1.2549ms)
  âœ” maps draft_reply to write + gmail:message key (0.7471ms)
  âœ” maps calendar.list to read + fixed list key (0.5539ms)
  âœ” maps calendar.get to read + gcal:event key (0.6215ms)
  âœ” maps calendar.events.list to read + gcal:events window key (0.7591ms)
  âœ” fails calendar.events.list without time range (0.6609ms)
  âœ” fails for unmapped intent when envelope would need routing (0.3287ms)
âœ” routingEnvelopeToScopeTarget (7.3445ms)
â–¶ buildExecutionScope outputs
  âœ” thread read: review contains thread key, empty modify (1.858ms)
  âœ” summarize: same review surface as thread read for same id (0.231ms)
  âœ” draft reply: message in modify_files; optional thread in review (0.1938ms)
  âœ” draft reply without thread: message only in review (0.2614ms)
  âœ” calendar list: fixed logical key in review (0.1956ms)
  âœ” calendar get: event id in review (0.1906ms)
  âœ” calendar events list: window key in review (1.0301ms)
âœ” buildExecutionScope outputs (4.4743ms)
â–¶ scopeMetrics
  âœ” increments scope check counters (1.3699ms)
  âœ” records summarize bounded context and averages (0.4463ms)
âœ” scopeMetrics (2.181ms)
â–¶ deriveWorkspaceIntentForDisclosure
  âœ” returns null without canvas (1.2624ms)
  âœ” maps calendar hub (0.8292ms)
  âœ” maps mail hub to search when no successful read (0.1841ms)
  âœ” maps mail hub to read when mailRead ok (0.1636ms)
âœ” deriveWorkspaceIntentForDisclosure (5.1803ms)
â–¶ allowShellSurfaceTransition
  âœ” allows primary always (1.9097ms)
  âœ” denies operator without eligibility (0.2872ms)
  âœ” allows operator when eligible (0.1392ms)
  âœ” denies developer without eligibility (0.3021ms)
  âœ” allows developer when developerEligible (0.1817ms)
âœ” allowShellSurfaceTransition (5.3306ms)
â–¶ clampSurfaceModeToInterimAuthority
  âœ” maps denied elevated to primary (0.1559ms)
âœ” clampSurfaceModeToInterimAuthority (0.2847ms)
â–¶ readInterimShellAuthority
  âœ” treats URL aios_operator as operator elevation (2.3443ms)
  âœ” treats URL aios_dev as developer elevation (0.9353ms)
  âœ” treats legacy operator storage as operator elevation (1.3389ms)
  âœ” treats interim operator unlock as operator elevation (0.4372ms)
  âœ” treats legacy diagnostics only as developer elevation (and operator via legacy hint) (0.3158ms)
âœ” readInterimShellAuthority (5.934ms)
â–¶ resolveInitialSurfaceMode (precedence)
  âœ” prefers persisted session surface mode when interim authority allows it (2.2342ms)
  âœ” uses URL aios_operator when no persisted mode (1.6798ms)
  âœ” defaults to primary (0.6046ms)
  âœ” clamps persisted elevated mode without interim authority to primary (0.9217ms)
âœ” resolveInitialSurfaceMode (precedence) (8.7737ms)
â–¶ routeShellAgentText app.shell.*
  âœ” applies enter_operator without delegating canvas routing (6.8251ms)
  âœ” applies surface_mode with surface field (0.8298ms)
  âœ” applies switch_to_chat (0.8006ms)
  âœ” does not delegate canvas for unknown app.shell.* (0.5349ms)
  âœ” does not delegate canvas for unrecognized app.open.* (0.7418ms)
  âœ” delegates workspace intents to canvas router (0.2039ms)
âœ” routeShellAgentText app.shell.* (13.3898ms)
â–¶ shellStateCommandToNavigationAction
  âœ” maps surface and app_mode commands (1.1013ms)
âœ” shellStateCommandToNavigationAction (2.1228ms)
â–¶ getShellNavigationDenialMessage
  âœ” returns null for voice/chat shell action (0.255ms)
  âœ” denies operator surface without eligibility (0.1951ms)
âœ” getShellNavigationDenialMessage (0.6352ms)
â–¶ tryApplyShellNavigationAction
  âœ” applies set_voice_chat_mode (0.2479ms)
  âœ” does not apply surface when denied (0.1255ms)
âœ” tryApplyShellNavigationAction (0.5126ms)
â–¶ applyShellNavigationAction
  âœ” routes set_mode to setAppTargetMode (0.132ms)
âœ” applyShellNavigationAction (0.2661ms)
â–¶ tryParseShellStateCommand
  âœ” parses surface modes (3.4323ms)
  âœ” parses voice/chat (0.2446ms)
  âœ” returns null for normal sentences (0.3867ms)
âœ” tryParseShellStateCommand (6.1238ms)
â–¶ shouldShowWorkspaceHub (#14)
  âœ” allows hub for connected and auth_required only (0.5485ms)
âœ” shouldShowWorkspaceHub (#14) (1.4344ms)
â–¶ callWorkspaceMcpAdapter callsite guard
  âœ” only allowlisted src files reference callWorkspaceMcpAdapter (bypass blocked or absent) (32.6721ms)
âœ” callWorkspaceMcpAdapter callsite guard (34.1216ms)
â–¶ parseContactsListMcpText
  âœ” parses blocks, summary, and next page token (1.7366ms)
  âœ” handles contact without Name line (0.3382ms)
âœ” parseContactsListMcpText (3.5358ms)
â–¶ workspaceDriveListDataIsEmpty
  âœ” treats null as empty (1.6798ms)
  âœ” detects empty files array (Drive API shape) (0.3199ms)
  âœ” detects non-empty files (0.1716ms)
  âœ” unwraps nested data.files (1.9276ms)
  âœ” returns false for unknown object without list keys (show raw ok) (0.6341ms)
âœ” workspaceDriveListDataIsEmpty (8.163ms)
â–¶ unwrapMailSearchPayload
  âœ” unwraps JSON-RPC result envelope (0.9095ms)
  âœ” chains result.data when present (0.3717ms)
  âœ” leaves bare API shape unchanged (0.5062ms)
âœ” unwrapMailSearchPayload (2.7122ms)
â–¶ normalizeMailSearchRows
  âœ” extracts minimal Gmail list ids (id + threadId) (0.8246ms)
  âœ” unwraps MCP result wrapper before extraction (0.2938ms)
  âœ” flattens thread â†’ messages with metadata (15.3381ms)
  âœ” does not treat bare thread stubs as message ids (0.3596ms)
  âœ” maps subject and nested sender (0.7638ms)
  âœ” returns empty for non-object payloads (0.6655ms)
  âœ” dedupes by message id (0.3665ms)
âœ” normalizeMailSearchRows (19.0405ms)
â–¶ workspaceMailReadMessageIdFromIntent
  âœ” returns message id only for workspace.mail.read (0.711ms)
  âœ” returns undefined for workspace.mail.search even if resource_id is set (0.1629ms)
  âœ” returns undefined for workspace.mail.thread.read (thread id, not message id) (0.1115ms)
âœ” workspaceMailReadMessageIdFromIntent (1.8754ms)
â–¶ workspaceIntentToCanvasView
  âœ” maps workspace.drive.list to workspace_drive_hub (0.8461ms)
âœ” workspaceIntentToCanvasView (1.039ms)
â–¶ workspaceViewAfterConnect
  âœ” resumes calendar hub (1.0494ms)
  âœ” resumes mail hub with message id (0.1139ms)
  âœ” defaults generic workspace_hub to calendar list (0.0791ms)
  âœ” defaults undefined view to calendar list (0.0719ms)
âœ” workspaceViewAfterConnect (2.0874ms)
â„¹ tests 111
â„¹ suites 30
â„¹ pass 111
â„¹ fail 0
â„¹ cancelled 0
â„¹ skipped 0
â„¹ todo 0
â„¹ duration_ms 751.0631
```


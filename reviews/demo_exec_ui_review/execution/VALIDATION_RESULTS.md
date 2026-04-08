# VALIDATION_RESULTS

**Generated:** 20260408-050629Z (UTC) by `run_isolated_execution_demo.py` 0.3.1

## install

**cwd:** `C:\Apps\aios-exec-demo_exec_ui_review-20260408-050629Z`

**command:** `npm ci`

**exit 0**

```
added 316 packages, and audited 317 packages in 3s

46 packages are looking for funding
  run `npm fund` for details

1 high severity vulnerability

To address all issues, run:
  npm audit fix

Run `npm audit` for details.
npm warn deprecated node-domexception@1.0.0: Use your platform's native DOMException instead
```

## build

**cwd:** `C:\Apps\aios-exec-demo_exec_ui_review-20260408-050629Z`

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
âœ“ built in 5.63s

(!) Some chunks are larger than 500 kB after minification. Consider:
- Using dynamic import() to code-split the application
- Use build.rollupOptions.output.manualChunks to improve chunking: https://rollupjs.org/configuration-options/#output-manualchunks
- Adjust chunk size limit for this warning via build.chunkSizeWarningLimit.
```

## test

**cwd:** `C:\Apps\aios-exec-demo_exec_ui_review-20260408-050629Z`

**command:** `npm test`

**exit 0**

```
> react-example@0.0.0 test
> tsx --test scripts/uiReviewRag.test.ts src/workspace/mailSearchRows.test.ts src/workspace/contactsMcpParse.test.ts src/workspace/workspaceIntentRouter.test.ts src/workspace/workspacePostConnect.test.ts src/workspace/driveListEmpty.test.ts src/workspace/callWorkspaceMcpAdapterCallsite.test.ts src/local-llm/threadSummaryV1.test.ts src/scope/scopeEngine.test.ts src/shell/shellStateCommands.test.ts src/shell/shellIntentRouter.test.ts src/shell/shellBootstrap.test.ts src/shell/shellAuthority.test.ts src/shell/shellNavigationApply.test.ts src/shell/workspaceState.test.ts src/core/shell/sessionEntryClassification.test.ts src/core/shell/shellPrimaryOutcome.test.ts src/core/compliance/spec009DisclosurePredicates.test.ts src/core/policy/localInterpretationRequired.test.ts src/core/coreImportBoundary.test.ts src/shellCanvas/deriveWorkspaceIntentForDisclosure.test.ts src/compliance/spec009PrimaryDisclosure.presentation.test.ts

â–¶ uiReviewRag
  âœ” tokenizeQuery drops stopwords (1.8889ms)
  âœ” scoreChunk ranks relevant chunk higher (0.5166ms)
  âœ” retrieveTopK returns ordered chunks (3.9253ms)
âœ” uiReviewRag (7.8802ms)
âœ” secondary line includes workspace and voice notes (3.1912ms)
âœ” secondary line adds capability when local required and degraded (0.4134ms)
âœ” disclosure needed: voice mode without voice input (1.3445ms)
âœ” disclosure not needed: chat mode without voice (0.2236ms)
âœ” disclosure needed: workspace error (0.1613ms)
âœ” disclosure needed: workspace auth_required (execution token missing) (0.1841ms)
âœ” disclosure needed: local required but not ready (0.2401ms)
â–¶ src/core import boundary
  âœ” no core source file imports React or UI packages (5.0903ms)
âœ” src/core import boundary (6.2522ms)
â–¶ resolvedIntentRequiresLocalModel
  âœ” is false for null/undefined (1.0501ms)
  âœ” is false for typical read intents (0.2262ms)
  âœ” is true for thread summarize (0.1592ms)
âœ” resolvedIntentRequiresLocalModel (2.9052ms)
â–¶ sessionEntryClassification (AMD-2026-012 Â§5)
  âœ” classifies as new when no prior engagement (1.7099ms)
  âœ” classifies as returning after markSessionEntryEngaged (0.5267ms)
âœ” sessionEntryClassification (AMD-2026-012 Â§5) (4.2615ms)
â–¶ deriveShellPrimaryOutcome (AMD-2026-012 Â§7)
  âœ” idle shell without canvas â†’ ready_for_intent (1.7623ms)
  âœ” workspace onboarding â†’ needs_auth (0.2584ms)
  âœ” agent processing with no canvas â†’ ready_to_execute (0.1603ms)
  âœ” hub visible, agent idle â†’ executed_with_result (0.9189ms)
  âœ” agent error â†’ execution_failed (0.3254ms)
âœ” deriveShellPrimaryOutcome (AMD-2026-012 Â§7) (5.6111ms)
â–¶ threadSummaryV1
  âœ” parses plain JSON (1.1757ms)
  âœ” extracts JSON from fenced block (1.0539ms)
  âœ” extractJsonObjectText finds object in prose (0.2573ms)
  âœ” fails on invalid JSON (0.1813ms)
  âœ” fails when root is array (0.1597ms)
  âœ” coerces types safely (0.2307ms)
âœ” threadSummaryV1 (4.4812ms)
â–¶ validateScopeOperation
  âœ” allows read when key is in review_files (1.2011ms)
  âœ” allows read when key is only in modify_files (0.2394ms)
  âœ” denies read when key is outside envelope (0.274ms)
  âœ” denies when key is in protected_files (0.2027ms)
  âœ” allows write when key is in modify_files (0.1905ms)
  âœ” denies write when key is review-only (0.1642ms)
âœ” validateScopeOperation (3.9553ms)
â–¶ routingEnvelopeToScopeTarget
  âœ” maps thread.read to read + gmail:thread key (0.5265ms)
  âœ” fails thread.read without resource id (0.2045ms)
  âœ” maps draft_reply to write + gmail:message key (0.2804ms)
  âœ” maps calendar.list to read + fixed list key (0.2168ms)
  âœ” maps calendar.get to read + gcal:event key (0.2459ms)
  âœ” maps calendar.events.list to read + gcal:events window key (0.3055ms)
  âœ” fails calendar.events.list without time range (0.1705ms)
  âœ” fails for unmapped intent when envelope would need routing (0.2191ms)
âœ” routingEnvelopeToScopeTarget (2.7774ms)
â–¶ buildExecutionScope outputs
  âœ” thread read: review contains thread key, empty modify (2.3255ms)
  âœ” summarize: same review surface as thread read for same id (0.3523ms)
  âœ” draft reply: message in modify_files; optional thread in review (0.2964ms)
  âœ” draft reply without thread: message only in review (0.2327ms)
  âœ” calendar list: fixed logical key in review (1.1783ms)
  âœ” calendar get: event id in review (0.2399ms)
  âœ” calendar events list: window key in review (0.1663ms)
âœ” buildExecutionScope outputs (5.2079ms)
â–¶ scopeMetrics
  âœ” increments scope check counters (0.4163ms)
  âœ” records summarize bounded context and averages (0.1697ms)
âœ” scopeMetrics (0.6937ms)
â–¶ deriveWorkspaceIntentForDisclosure
  âœ” returns null without canvas (1.6918ms)
  âœ” maps calendar hub (0.2086ms)
  âœ” maps mail hub to search when no successful read (0.2569ms)
  âœ” maps mail hub to read when mailRead ok (0.2463ms)
âœ” deriveWorkspaceIntentForDisclosure (3.9909ms)
â–¶ allowShellSurfaceTransition
  âœ” allows primary always (1.2677ms)
  âœ” denies operator without eligibility (0.1988ms)
  âœ” allows operator when eligible (0.1339ms)
  âœ” denies developer without eligibility (0.1177ms)
  âœ” allows developer when developerEligible (0.1278ms)
âœ” allowShellSurfaceTransition (3.4146ms)
â–¶ clampSurfaceModeToInterimAuthority
  âœ” maps denied elevated to primary (0.1493ms)
âœ” clampSurfaceModeToInterimAuthority (0.2577ms)
â–¶ readInterimShellAuthority
  âœ” treats URL aios_operator as operator elevation (1.1404ms)
  âœ” treats URL aios_dev as developer elevation (0.5019ms)
  âœ” treats legacy operator storage as operator elevation (0.4174ms)
  âœ” treats interim operator unlock as operator elevation (0.4ms)
  âœ” treats legacy diagnostics only as developer elevation (and operator via legacy hint) (0.3468ms)
âœ” readInterimShellAuthority (3.2307ms)
â–¶ resolveInitialSurfaceMode (precedence)
  âœ” prefers persisted session surface mode when interim authority allows it (1.797ms)
  âœ” uses URL aios_operator when no persisted mode (0.5313ms)
  âœ” defaults to primary (0.5215ms)
  âœ” clamps persisted elevated mode without interim authority to primary (0.4047ms)
âœ” resolveInitialSurfaceMode (precedence) (4.6553ms)
â–¶ routeShellAgentText app.shell.*
  âœ” applies enter_operator without delegating canvas routing (2.4508ms)
  âœ” applies surface_mode with surface field (0.3662ms)
  âœ” applies switch_to_chat (0.2207ms)
  âœ” does not delegate canvas for unknown app.shell.* (0.2007ms)
  âœ” does not delegate canvas for unrecognized app.open.* (0.2572ms)
  âœ” delegates workspace intents to canvas router (0.2178ms)
âœ” routeShellAgentText app.shell.* (5.4591ms)
â–¶ shellStateCommandToNavigationAction
  âœ” maps surface and app_mode commands (1.7854ms)
âœ” shellStateCommandToNavigationAction (3.0827ms)
â–¶ getShellNavigationDenialMessage
  âœ” returns null for voice/chat shell action (0.3362ms)
  âœ” denies operator surface without eligibility (0.3336ms)
âœ” getShellNavigationDenialMessage (0.9357ms)
â–¶ tryApplyShellNavigationAction
  âœ” applies set_voice_chat_mode (0.4243ms)
  âœ” does not apply surface when denied (0.2031ms)
âœ” tryApplyShellNavigationAction (0.8467ms)
â–¶ applyShellNavigationAction
  âœ” routes set_mode to setAppTargetMode (0.2992ms)
âœ” applyShellNavigationAction (0.5415ms)
â–¶ tryParseShellStateCommand
  âœ” parses surface modes (2.7649ms)
  âœ” parses voice/chat (0.2427ms)
  âœ” returns null for normal sentences (0.4431ms)
âœ” tryParseShellStateCommand (4.8182ms)
â–¶ shouldShowWorkspaceHub (#14)
  âœ” allows hub for connected and auth_required only (0.6319ms)
âœ” shouldShowWorkspaceHub (#14) (1.5026ms)
â–¶ callWorkspaceMcpAdapter callsite guard
  âœ” only allowlisted src files reference callWorkspaceMcpAdapter (bypass blocked or absent) (22.7461ms)
âœ” callWorkspaceMcpAdapter callsite guard (23.9927ms)
â–¶ parseContactsListMcpText
  âœ” parses blocks, summary, and next page token (1.9913ms)
  âœ” handles contact without Name line (0.4554ms)
âœ” parseContactsListMcpText (4.3332ms)
â–¶ workspaceDriveListDataIsEmpty
  âœ” treats null as empty (0.9925ms)
  âœ” detects empty files array (Drive API shape) (0.1843ms)
  âœ” detects non-empty files (0.1395ms)
  âœ” unwraps nested data.files (0.1469ms)
  âœ” returns false for unknown object without list keys (show raw ok) (0.1314ms)
âœ” workspaceDriveListDataIsEmpty (2.9637ms)
â–¶ unwrapMailSearchPayload
  âœ” unwraps JSON-RPC result envelope (1.2955ms)
  âœ” chains result.data when present (0.4175ms)
  âœ” leaves bare API shape unchanged (0.636ms)
âœ” unwrapMailSearchPayload (3.5924ms)
â–¶ normalizeMailSearchRows
  âœ” extracts minimal Gmail list ids (id + threadId) (0.925ms)
  âœ” unwraps MCP result wrapper before extraction (0.4098ms)
  âœ” flattens thread â†’ messages with metadata (19.5403ms)
  âœ” does not treat bare thread stubs as message ids (0.3593ms)
  âœ” maps subject and nested sender (0.4913ms)
  âœ” returns empty for non-object payloads (0.4317ms)
  âœ” dedupes by message id (0.1941ms)
âœ” normalizeMailSearchRows (22.7646ms)
â–¶ workspaceMailReadMessageIdFromIntent
  âœ” returns message id only for workspace.mail.read (1.2878ms)
  âœ” returns undefined for workspace.mail.search even if resource_id is set (0.2018ms)
  âœ” returns undefined for workspace.mail.thread.read (thread id, not message id) (0.2038ms)
âœ” workspaceMailReadMessageIdFromIntent (3.1329ms)
â–¶ workspaceIntentToCanvasView
  âœ” maps workspace.drive.list to workspace_drive_hub (1.7756ms)
âœ” workspaceIntentToCanvasView (1.9686ms)
â–¶ workspaceViewAfterConnect
  âœ” resumes calendar hub (1.8311ms)
  âœ” resumes mail hub with message id (0.214ms)
  âœ” defaults generic workspace_hub to calendar list (0.1326ms)
  âœ” defaults undefined view to calendar list (0.1303ms)
âœ” workspaceViewAfterConnect (3.5678ms)
â„¹ tests 111
â„¹ suites 30
â„¹ pass 111
â„¹ fail 0
â„¹ cancelled 0
â„¹ skipped 0
â„¹ todo 0
â„¹ duration_ms 969.9117
```


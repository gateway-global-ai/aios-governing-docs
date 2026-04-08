# VALIDATION_RESULTS

**Generated:** 20260408-051145Z (UTC) by `run_isolated_execution_demo.py` 0.3.1

## install

**cwd:** `C:\Apps\aios-exec-demos\demo_exec_packet_wt_full-20260408-051145Z`

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

**cwd:** `C:\Apps\aios-exec-demos\demo_exec_packet_wt_full-20260408-051145Z`

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
âœ“ built in 5.66s

(!) Some chunks are larger than 500 kB after minification. Consider:
- Using dynamic import() to code-split the application
- Use build.rollupOptions.output.manualChunks to improve chunking: https://rollupjs.org/configuration-options/#output-manualchunks
- Adjust chunk size limit for this warning via build.chunkSizeWarningLimit.
```

## test

**cwd:** `C:\Apps\aios-exec-demos\demo_exec_packet_wt_full-20260408-051145Z`

**command:** `npm test`

**exit 0**

```
> react-example@0.0.0 test
> tsx --test scripts/uiReviewRag.test.ts src/workspace/mailSearchRows.test.ts src/workspace/contactsMcpParse.test.ts src/workspace/workspaceIntentRouter.test.ts src/workspace/workspacePostConnect.test.ts src/workspace/driveListEmpty.test.ts src/workspace/callWorkspaceMcpAdapterCallsite.test.ts src/local-llm/threadSummaryV1.test.ts src/scope/scopeEngine.test.ts src/shell/shellStateCommands.test.ts src/shell/shellIntentRouter.test.ts src/shell/shellBootstrap.test.ts src/shell/shellAuthority.test.ts src/shell/shellNavigationApply.test.ts src/shell/workspaceState.test.ts src/core/shell/sessionEntryClassification.test.ts src/core/shell/shellPrimaryOutcome.test.ts src/core/compliance/spec009DisclosurePredicates.test.ts src/core/policy/localInterpretationRequired.test.ts src/core/coreImportBoundary.test.ts src/shellCanvas/deriveWorkspaceIntentForDisclosure.test.ts src/compliance/spec009PrimaryDisclosure.presentation.test.ts

â–¶ uiReviewRag
  âœ” tokenizeQuery drops stopwords (1.3462ms)
  âœ” scoreChunk ranks relevant chunk higher (0.4261ms)
  âœ” retrieveTopK returns ordered chunks (0.4399ms)
âœ” uiReviewRag (3.5436ms)
âœ” secondary line includes workspace and voice notes (1.4039ms)
âœ” secondary line adds capability when local required and degraded (0.3038ms)
âœ” disclosure needed: voice mode without voice input (1.2487ms)
âœ” disclosure not needed: chat mode without voice (0.234ms)
âœ” disclosure needed: workspace error (0.1537ms)
âœ” disclosure needed: workspace auth_required (execution token missing) (0.1485ms)
âœ” disclosure needed: local required but not ready (0.2138ms)
â–¶ src/core import boundary
  âœ” no core source file imports React or UI packages (4.0822ms)
âœ” src/core import boundary (5.2175ms)
â–¶ resolvedIntentRequiresLocalModel
  âœ” is false for null/undefined (0.9773ms)
  âœ” is false for typical read intents (0.1842ms)
  âœ” is true for thread summarize (0.1183ms)
âœ” resolvedIntentRequiresLocalModel (2.5398ms)
â–¶ sessionEntryClassification (AMD-2026-012 Â§5)
  âœ” classifies as new when no prior engagement (1.4769ms)
  âœ” classifies as returning after markSessionEntryEngaged (0.4363ms)
âœ” sessionEntryClassification (AMD-2026-012 Â§5) (3.2644ms)
â–¶ deriveShellPrimaryOutcome (AMD-2026-012 Â§7)
  âœ” idle shell without canvas â†’ ready_for_intent (1.0443ms)
  âœ” workspace onboarding â†’ needs_auth (0.186ms)
  âœ” agent processing with no canvas â†’ ready_to_execute (0.1206ms)
  âœ” hub visible, agent idle â†’ executed_with_result (0.1367ms)
  âœ” agent error â†’ execution_failed (0.1162ms)
âœ” deriveShellPrimaryOutcome (AMD-2026-012 Â§7) (3.1417ms)
â–¶ threadSummaryV1
  âœ” parses plain JSON (1.2205ms)
  âœ” extracts JSON from fenced block (2.1197ms)
  âœ” extractJsonObjectText finds object in prose (0.2932ms)
  âœ” fails on invalid JSON (0.2029ms)
  âœ” fails when root is array (0.1605ms)
  âœ” coerces types safely (0.2334ms)
âœ” threadSummaryV1 (5.768ms)
â–¶ validateScopeOperation
  âœ” allows read when key is in review_files (1.1225ms)
  âœ” allows read when key is only in modify_files (0.2054ms)
  âœ” denies read when key is outside envelope (0.1888ms)
  âœ” denies when key is in protected_files (0.1959ms)
  âœ” allows write when key is in modify_files (0.1714ms)
  âœ” denies write when key is review-only (0.1443ms)
âœ” validateScopeOperation (3.4083ms)
â–¶ routingEnvelopeToScopeTarget
  âœ” maps thread.read to read + gmail:thread key (0.4689ms)
  âœ” fails thread.read without resource id (0.1732ms)
  âœ” maps draft_reply to write + gmail:message key (0.2244ms)
  âœ” maps calendar.list to read + fixed list key (0.2077ms)
  âœ” maps calendar.get to read + gcal:event key (0.2147ms)
  âœ” maps calendar.events.list to read + gcal:events window key (0.2145ms)
  âœ” fails calendar.events.list without time range (0.1143ms)
  âœ” fails for unmapped intent when envelope would need routing (0.169ms)
âœ” routingEnvelopeToScopeTarget (2.2235ms)
â–¶ buildExecutionScope outputs
  âœ” thread read: review contains thread key, empty modify (1.4979ms)
  âœ” summarize: same review surface as thread read for same id (0.2345ms)
  âœ” draft reply: message in modify_files; optional thread in review (0.2098ms)
  âœ” draft reply without thread: message only in review (0.1554ms)
  âœ” calendar list: fixed logical key in review (0.1658ms)
  âœ” calendar get: event id in review (0.1768ms)
  âœ” calendar events list: window key in review (0.1768ms)
âœ” buildExecutionScope outputs (2.8913ms)
â–¶ scopeMetrics
  âœ” increments scope check counters (0.4717ms)
  âœ” records summarize bounded context and averages (0.1901ms)
âœ” scopeMetrics (0.7948ms)
â–¶ deriveWorkspaceIntentForDisclosure
  âœ” returns null without canvas (1.2154ms)
  âœ” maps calendar hub (0.2371ms)
  âœ” maps mail hub to search when no successful read (0.177ms)
  âœ” maps mail hub to read when mailRead ok (0.3389ms)
âœ” deriveWorkspaceIntentForDisclosure (3.7674ms)
â–¶ allowShellSurfaceTransition
  âœ” allows primary always (0.9954ms)
  âœ” denies operator without eligibility (0.2098ms)
  âœ” allows operator when eligible (0.1616ms)
  âœ” denies developer without eligibility (0.1352ms)
  âœ” allows developer when developerEligible (0.1834ms)
âœ” allowShellSurfaceTransition (3.0119ms)
â–¶ clampSurfaceModeToInterimAuthority
  âœ” maps denied elevated to primary (0.1633ms)
âœ” clampSurfaceModeToInterimAuthority (0.285ms)
â–¶ readInterimShellAuthority
  âœ” treats URL aios_operator as operator elevation (0.9588ms)
  âœ” treats URL aios_dev as developer elevation (0.3921ms)
  âœ” treats legacy operator storage as operator elevation (0.3796ms)
  âœ” treats interim operator unlock as operator elevation (0.2961ms)
  âœ” treats legacy diagnostics only as developer elevation (and operator via legacy hint) (0.238ms)
âœ” readInterimShellAuthority (2.6007ms)
â–¶ resolveInitialSurfaceMode (precedence)
  âœ” prefers persisted session surface mode when interim authority allows it (2.148ms)
  âœ” uses URL aios_operator when no persisted mode (0.5197ms)
  âœ” defaults to primary (0.6506ms)
  âœ” clamps persisted elevated mode without interim authority to primary (0.755ms)
âœ” resolveInitialSurfaceMode (precedence) (5.6481ms)
â–¶ routeShellAgentText app.shell.*
  âœ” applies enter_operator without delegating canvas routing (1.8741ms)
  âœ” applies surface_mode with surface field (0.232ms)
  âœ” applies switch_to_chat (0.1586ms)
  âœ” does not delegate canvas for unknown app.shell.* (0.1421ms)
  âœ” does not delegate canvas for unrecognized app.open.* (0.4655ms)
  âœ” delegates workspace intents to canvas router (0.178ms)
âœ” routeShellAgentText app.shell.* (4.4791ms)
â–¶ shellStateCommandToNavigationAction
  âœ” maps surface and app_mode commands (2.0102ms)
âœ” shellStateCommandToNavigationAction (3.3191ms)
â–¶ getShellNavigationDenialMessage
  âœ” returns null for voice/chat shell action (0.2718ms)
  âœ” denies operator surface without eligibility (0.2541ms)
âœ” getShellNavigationDenialMessage (0.7476ms)
â–¶ tryApplyShellNavigationAction
  âœ” applies set_voice_chat_mode (0.3738ms)
  âœ” does not apply surface when denied (0.1799ms)
âœ” tryApplyShellNavigationAction (0.7466ms)
â–¶ applyShellNavigationAction
  âœ” routes set_mode to setAppTargetMode (0.2125ms)
âœ” applyShellNavigationAction (0.41ms)
â–¶ tryParseShellStateCommand
  âœ” parses surface modes (2.8966ms)
  âœ” parses voice/chat (0.2451ms)
  âœ” returns null for normal sentences (0.459ms)
âœ” tryParseShellStateCommand (4.8653ms)
â–¶ shouldShowWorkspaceHub (#14)
  âœ” allows hub for connected and auth_required only (0.8663ms)
âœ” shouldShowWorkspaceHub (#14) (2.0189ms)
â–¶ callWorkspaceMcpAdapter callsite guard
  âœ” only allowlisted src files reference callWorkspaceMcpAdapter (bypass blocked or absent) (25.7948ms)
âœ” callWorkspaceMcpAdapter callsite guard (26.8958ms)
â–¶ parseContactsListMcpText
  âœ” parses blocks, summary, and next page token (1.2393ms)
  âœ” handles contact without Name line (0.212ms)
âœ” parseContactsListMcpText (2.3603ms)
â–¶ workspaceDriveListDataIsEmpty
  âœ” treats null as empty (1.2417ms)
  âœ” detects empty files array (Drive API shape) (0.2259ms)
  âœ” detects non-empty files (0.2184ms)
  âœ” unwraps nested data.files (0.1368ms)
  âœ” returns false for unknown object without list keys (show raw ok) (0.0878ms)
âœ” workspaceDriveListDataIsEmpty (3.3607ms)
â–¶ unwrapMailSearchPayload
  âœ” unwraps JSON-RPC result envelope (0.9523ms)
  âœ” chains result.data when present (0.437ms)
  âœ” leaves bare API shape unchanged (0.6468ms)
âœ” unwrapMailSearchPayload (3.0527ms)
â–¶ normalizeMailSearchRows
  âœ” extracts minimal Gmail list ids (id + threadId) (0.9668ms)
  âœ” unwraps MCP result wrapper before extraction (0.3092ms)
  âœ” flattens thread â†’ messages with metadata (19.2243ms)
  âœ” does not treat bare thread stubs as message ids (0.3335ms)
  âœ” maps subject and nested sender (0.4685ms)
  âœ” returns empty for non-object payloads (0.4108ms)
  âœ” dedupes by message id (0.1931ms)
âœ” normalizeMailSearchRows (22.2945ms)
â–¶ workspaceMailReadMessageIdFromIntent
  âœ” returns message id only for workspace.mail.read (0.5629ms)
  âœ” returns undefined for workspace.mail.search even if resource_id is set (0.1065ms)
  âœ” returns undefined for workspace.mail.thread.read (thread id, not message id) (0.0806ms)
âœ” workspaceMailReadMessageIdFromIntent (1.5331ms)
â–¶ workspaceIntentToCanvasView
  âœ” maps workspace.drive.list to workspace_drive_hub (0.6326ms)
âœ” workspaceIntentToCanvasView (0.7227ms)
â–¶ workspaceViewAfterConnect
  âœ” resumes calendar hub (1.5524ms)
  âœ” resumes mail hub with message id (0.1565ms)
  âœ” defaults generic workspace_hub to calendar list (0.1081ms)
  âœ” defaults undefined view to calendar list (0.108ms)
âœ” workspaceViewAfterConnect (3.0772ms)
â„¹ tests 111
â„¹ suites 30
â„¹ pass 111
â„¹ fail 0
â„¹ cancelled 0
â„¹ skipped 0
â„¹ todo 0
â„¹ duration_ms 618.3914
```


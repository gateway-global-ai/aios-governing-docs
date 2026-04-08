# VALIDATION_RESULTS

**Generated:** 20260408-044900Z (UTC) by `run_isolated_execution_demo.py` 0.3.0

## install

**cwd:** `C:\Apps\aios-exec-demo_exec_packet_wt_full-20260408-044900Z`

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

**cwd:** `C:\Apps\aios-exec-demo_exec_packet_wt_full-20260408-044900Z`

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
âœ“ built in 5.23s

(!) Some chunks are larger than 500 kB after minification. Consider:
- Using dynamic import() to code-split the application
- Use build.rollupOptions.output.manualChunks to improve chunking: https://rollupjs.org/configuration-options/#output-manualchunks
- Adjust chunk size limit for this warning via build.chunkSizeWarningLimit.
```

## test

**cwd:** `C:\Apps\aios-exec-demo_exec_packet_wt_full-20260408-044900Z`

**command:** `npm test`

**exit 0**

```
> react-example@0.0.0 test
> tsx --test scripts/uiReviewRag.test.ts src/workspace/mailSearchRows.test.ts src/workspace/contactsMcpParse.test.ts src/workspace/workspaceIntentRouter.test.ts src/workspace/workspacePostConnect.test.ts src/workspace/driveListEmpty.test.ts src/workspace/callWorkspaceMcpAdapterCallsite.test.ts src/local-llm/threadSummaryV1.test.ts src/scope/scopeEngine.test.ts src/shell/shellStateCommands.test.ts src/shell/shellIntentRouter.test.ts src/shell/shellBootstrap.test.ts src/shell/shellAuthority.test.ts src/shell/shellNavigationApply.test.ts src/shell/workspaceState.test.ts src/core/shell/sessionEntryClassification.test.ts src/core/shell/shellPrimaryOutcome.test.ts src/core/compliance/spec009DisclosurePredicates.test.ts src/core/policy/localInterpretationRequired.test.ts src/core/coreImportBoundary.test.ts src/shellCanvas/deriveWorkspaceIntentForDisclosure.test.ts src/compliance/spec009PrimaryDisclosure.presentation.test.ts

â–¶ uiReviewRag
  âœ” tokenizeQuery drops stopwords (1.287ms)
  âœ” scoreChunk ranks relevant chunk higher (0.4236ms)
  âœ” retrieveTopK returns ordered chunks (0.6503ms)
âœ” uiReviewRag (3.7574ms)
âœ” secondary line includes workspace and voice notes (1.6646ms)
âœ” secondary line adds capability when local required and degraded (0.3967ms)
âœ” disclosure needed: voice mode without voice input (0.9966ms)
âœ” disclosure not needed: chat mode without voice (0.1812ms)
âœ” disclosure needed: workspace error (0.1179ms)
âœ” disclosure needed: workspace auth_required (execution token missing) (0.1021ms)
âœ” disclosure needed: local required but not ready (0.153ms)
â–¶ src/core import boundary
  âœ” no core source file imports React or UI packages (6.0136ms)
âœ” src/core import boundary (7.2807ms)
â–¶ resolvedIntentRequiresLocalModel
  âœ” is false for null/undefined (1.3613ms)
  âœ” is false for typical read intents (0.3859ms)
  âœ” is true for thread summarize (0.1596ms)
âœ” resolvedIntentRequiresLocalModel (4.3595ms)
â–¶ sessionEntryClassification (AMD-2026-012 Â§5)
  âœ” classifies as new when no prior engagement (1.483ms)
  âœ” classifies as returning after markSessionEntryEngaged (0.4073ms)
âœ” sessionEntryClassification (AMD-2026-012 Â§5) (3.0795ms)
â–¶ deriveShellPrimaryOutcome (AMD-2026-012 Â§7)
  âœ” idle shell without canvas â†’ ready_for_intent (1.0211ms)
  âœ” workspace onboarding â†’ needs_auth (0.1604ms)
  âœ” agent processing with no canvas â†’ ready_to_execute (0.1184ms)
  âœ” hub visible, agent idle â†’ executed_with_result (0.0978ms)
  âœ” agent error â†’ execution_failed (0.0867ms)
âœ” deriveShellPrimaryOutcome (AMD-2026-012 Â§7) (2.7317ms)
â–¶ threadSummaryV1
  âœ” parses plain JSON (1.628ms)
  âœ” extracts JSON from fenced block (1.1308ms)
  âœ” extractJsonObjectText finds object in prose (0.2875ms)
  âœ” fails on invalid JSON (0.2247ms)
  âœ” fails when root is array (0.2106ms)
  âœ” coerces types safely (0.2748ms)
âœ” threadSummaryV1 (5.5206ms)
â–¶ validateScopeOperation
  âœ” allows read when key is in review_files (1.3157ms)
  âœ” allows read when key is only in modify_files (0.3319ms)
  âœ” denies read when key is outside envelope (0.2889ms)
  âœ” denies when key is in protected_files (0.2395ms)
  âœ” allows write when key is in modify_files (0.1981ms)
  âœ” denies write when key is review-only (0.1905ms)
âœ” validateScopeOperation (4.3351ms)
â–¶ routingEnvelopeToScopeTarget
  âœ” maps thread.read to read + gmail:thread key (0.526ms)
  âœ” fails thread.read without resource id (0.2189ms)
  âœ” maps draft_reply to write + gmail:message key (0.3359ms)
  âœ” maps calendar.list to read + fixed list key (0.3858ms)
  âœ” maps calendar.get to read + gcal:event key (0.2976ms)
  âœ” maps calendar.events.list to read + gcal:events window key (0.222ms)
  âœ” fails calendar.events.list without time range (0.2391ms)
  âœ” fails for unmapped intent when envelope would need routing (0.2306ms)
âœ” routingEnvelopeToScopeTarget (3.2756ms)
â–¶ buildExecutionScope outputs
  âœ” thread read: review contains thread key, empty modify (2.0536ms)
  âœ” summarize: same review surface as thread read for same id (0.2551ms)
  âœ” draft reply: message in modify_files; optional thread in review (0.2036ms)
  âœ” draft reply without thread: message only in review (0.1933ms)
  âœ” calendar list: fixed logical key in review (0.1475ms)
  âœ” calendar get: event id in review (0.1621ms)
  âœ” calendar events list: window key in review (0.1544ms)
âœ” buildExecutionScope outputs (3.56ms)
â–¶ scopeMetrics
  âœ” increments scope check counters (0.4862ms)
  âœ” records summarize bounded context and averages (0.1955ms)
âœ” scopeMetrics (0.8111ms)
â–¶ deriveWorkspaceIntentForDisclosure
  âœ” returns null without canvas (0.8233ms)
  âœ” maps calendar hub (0.1742ms)
  âœ” maps mail hub to search when no successful read (0.1505ms)
  âœ” maps mail hub to read when mailRead ok (0.151ms)
âœ” deriveWorkspaceIntentForDisclosure (2.4671ms)
â–¶ allowShellSurfaceTransition
  âœ” allows primary always (0.9961ms)
  âœ” denies operator without eligibility (0.1944ms)
  âœ” allows operator when eligible (0.127ms)
  âœ” denies developer without eligibility (0.1148ms)
  âœ” allows developer when developerEligible (0.1228ms)
âœ” allowShellSurfaceTransition (2.8394ms)
â–¶ clampSurfaceModeToInterimAuthority
  âœ” maps denied elevated to primary (0.1665ms)
âœ” clampSurfaceModeToInterimAuthority (0.2835ms)
â–¶ readInterimShellAuthority
  âœ” treats URL aios_operator as operator elevation (0.9891ms)
  âœ” treats URL aios_dev as developer elevation (0.4229ms)
  âœ” treats legacy operator storage as operator elevation (0.4144ms)
  âœ” treats interim operator unlock as operator elevation (0.3097ms)
  âœ” treats legacy diagnostics only as developer elevation (and operator via legacy hint) (0.2283ms)
âœ” readInterimShellAuthority (2.7291ms)
â–¶ resolveInitialSurfaceMode (precedence)
  âœ” prefers persisted session surface mode when interim authority allows it (2.6804ms)
  âœ” uses URL aios_operator when no persisted mode (0.4775ms)
  âœ” defaults to primary (0.6641ms)
  âœ” clamps persisted elevated mode without interim authority to primary (4.2364ms)
âœ” resolveInitialSurfaceMode (precedence) (10.4885ms)
â–¶ routeShellAgentText app.shell.*
  âœ” applies enter_operator without delegating canvas routing (2.9256ms)
  âœ” applies surface_mode with surface field (0.6276ms)
  âœ” applies switch_to_chat (0.3911ms)
  âœ” does not delegate canvas for unknown app.shell.* (0.2156ms)
  âœ” does not delegate canvas for unrecognized app.open.* (0.4299ms)
  âœ” delegates workspace intents to canvas router (0.4576ms)
âœ” routeShellAgentText app.shell.* (7.2263ms)
â–¶ shellStateCommandToNavigationAction
  âœ” maps surface and app_mode commands (1.5702ms)
âœ” shellStateCommandToNavigationAction (2.6059ms)
â–¶ getShellNavigationDenialMessage
  âœ” returns null for voice/chat shell action (0.2843ms)
  âœ” denies operator surface without eligibility (0.2354ms)
âœ” getShellNavigationDenialMessage (0.7427ms)
â–¶ tryApplyShellNavigationAction
  âœ” applies set_voice_chat_mode (0.3396ms)
  âœ” does not apply surface when denied (0.1699ms)
âœ” tryApplyShellNavigationAction (0.6706ms)
â–¶ applyShellNavigationAction
  âœ” routes set_mode to setAppTargetMode (0.213ms)
âœ” applyShellNavigationAction (0.3931ms)
â–¶ tryParseShellStateCommand
  âœ” parses surface modes (2.7127ms)
  âœ” parses voice/chat (0.2842ms)
  âœ” returns null for normal sentences (0.4578ms)
âœ” tryParseShellStateCommand (4.866ms)
â–¶ shouldShowWorkspaceHub (#14)
  âœ” allows hub for connected and auth_required only (0.8332ms)
âœ” shouldShowWorkspaceHub (#14) (1.9256ms)
â–¶ callWorkspaceMcpAdapter callsite guard
  âœ” only allowlisted src files reference callWorkspaceMcpAdapter (bypass blocked or absent) (24.426ms)
âœ” callWorkspaceMcpAdapter callsite guard (25.7396ms)
â–¶ parseContactsListMcpText
  âœ” parses blocks, summary, and next page token (1.0911ms)
  âœ” handles contact without Name line (0.2513ms)
âœ” parseContactsListMcpText (2.1647ms)
â–¶ workspaceDriveListDataIsEmpty
  âœ” treats null as empty (0.968ms)
  âœ” detects empty files array (Drive API shape) (0.1263ms)
  âœ” detects non-empty files (0.0869ms)
  âœ” unwraps nested data.files (0.0996ms)
  âœ” returns false for unknown object without list keys (show raw ok) (0.1136ms)
âœ” workspaceDriveListDataIsEmpty (2.5915ms)
â–¶ unwrapMailSearchPayload
  âœ” unwraps JSON-RPC result envelope (1.0285ms)
  âœ” chains result.data when present (0.3398ms)
  âœ” leaves bare API shape unchanged (0.5169ms)
âœ” unwrapMailSearchPayload (2.9751ms)
â–¶ normalizeMailSearchRows
  âœ” extracts minimal Gmail list ids (id + threadId) (1.7327ms)
  âœ” unwraps MCP result wrapper before extraction (0.5019ms)
  âœ” flattens thread â†’ messages with metadata (17.1608ms)
  âœ” does not treat bare thread stubs as message ids (0.4208ms)
  âœ” maps subject and nested sender (0.5479ms)
  âœ” returns empty for non-object payloads (0.4498ms)
  âœ” dedupes by message id (0.2159ms)
âœ” normalizeMailSearchRows (21.4803ms)
â–¶ workspaceMailReadMessageIdFromIntent
  âœ” returns message id only for workspace.mail.read (1.0483ms)
  âœ” returns undefined for workspace.mail.search even if resource_id is set (0.2078ms)
  âœ” returns undefined for workspace.mail.thread.read (thread id, not message id) (0.1578ms)
âœ” workspaceMailReadMessageIdFromIntent (3.3754ms)
â–¶ workspaceIntentToCanvasView
  âœ” maps workspace.drive.list to workspace_drive_hub (1.0273ms)
âœ” workspaceIntentToCanvasView (1.1936ms)
â–¶ workspaceViewAfterConnect
  âœ” resumes calendar hub (1.9325ms)
  âœ” resumes mail hub with message id (0.2397ms)
  âœ” defaults generic workspace_hub to calendar list (0.1699ms)
  âœ” defaults undefined view to calendar list (0.1775ms)
âœ” workspaceViewAfterConnect (4.0892ms)
â„¹ tests 111
â„¹ suites 30
â„¹ pass 111
â„¹ fail 0
â„¹ cancelled 0
â„¹ skipped 0
â„¹ todo 0
â„¹ duration_ms 829.1581
```


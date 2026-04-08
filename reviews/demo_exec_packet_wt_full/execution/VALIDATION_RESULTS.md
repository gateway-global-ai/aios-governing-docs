# VALIDATION_RESULTS

**Generated:** 20260408-050617Z (UTC) by `run_isolated_execution_demo.py` 0.3.1

## install

**cwd:** `C:\Apps\aios-exec-demo_exec_packet_wt_full-20260408-050617Z`

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

**cwd:** `C:\Apps\aios-exec-demo_exec_packet_wt_full-20260408-050617Z`

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
âœ“ built in 5.56s

(!) Some chunks are larger than 500 kB after minification. Consider:
- Using dynamic import() to code-split the application
- Use build.rollupOptions.output.manualChunks to improve chunking: https://rollupjs.org/configuration-options/#output-manualchunks
- Adjust chunk size limit for this warning via build.chunkSizeWarningLimit.
```

## test

**cwd:** `C:\Apps\aios-exec-demo_exec_packet_wt_full-20260408-050617Z`

**command:** `npm test`

**exit 0**

```
> react-example@0.0.0 test
> tsx --test scripts/uiReviewRag.test.ts src/workspace/mailSearchRows.test.ts src/workspace/contactsMcpParse.test.ts src/workspace/workspaceIntentRouter.test.ts src/workspace/workspacePostConnect.test.ts src/workspace/driveListEmpty.test.ts src/workspace/callWorkspaceMcpAdapterCallsite.test.ts src/local-llm/threadSummaryV1.test.ts src/scope/scopeEngine.test.ts src/shell/shellStateCommands.test.ts src/shell/shellIntentRouter.test.ts src/shell/shellBootstrap.test.ts src/shell/shellAuthority.test.ts src/shell/shellNavigationApply.test.ts src/shell/workspaceState.test.ts src/core/shell/sessionEntryClassification.test.ts src/core/shell/shellPrimaryOutcome.test.ts src/core/compliance/spec009DisclosurePredicates.test.ts src/core/policy/localInterpretationRequired.test.ts src/core/coreImportBoundary.test.ts src/shellCanvas/deriveWorkspaceIntentForDisclosure.test.ts src/compliance/spec009PrimaryDisclosure.presentation.test.ts

â–¶ uiReviewRag
  âœ” tokenizeQuery drops stopwords (1.9429ms)
  âœ” scoreChunk ranks relevant chunk higher (0.4479ms)
  âœ” retrieveTopK returns ordered chunks (0.5246ms)
âœ” uiReviewRag (4.2755ms)
âœ” secondary line includes workspace and voice notes (7.0476ms)
âœ” secondary line adds capability when local required and degraded (0.2493ms)
âœ” disclosure needed: voice mode without voice input (1.5415ms)
âœ” disclosure not needed: chat mode without voice (0.2214ms)
âœ” disclosure needed: workspace error (0.1468ms)
âœ” disclosure needed: workspace auth_required (execution token missing) (0.1555ms)
âœ” disclosure needed: local required but not ready (0.2201ms)
â–¶ src/core import boundary
  âœ” no core source file imports React or UI packages (5.1176ms)
âœ” src/core import boundary (6.3144ms)
â–¶ resolvedIntentRequiresLocalModel
  âœ” is false for null/undefined (1.2498ms)
  âœ” is false for typical read intents (0.1826ms)
  âœ” is true for thread summarize (0.1007ms)
âœ” resolvedIntentRequiresLocalModel (3.0416ms)
â–¶ sessionEntryClassification (AMD-2026-012 Â§5)
  âœ” classifies as new when no prior engagement (2.743ms)
  âœ” classifies as returning after markSessionEntryEngaged (0.6494ms)
âœ” sessionEntryClassification (AMD-2026-012 Â§5) (5.1845ms)
â–¶ deriveShellPrimaryOutcome (AMD-2026-012 Â§7)
  âœ” idle shell without canvas â†’ ready_for_intent (0.9721ms)
  âœ” workspace onboarding â†’ needs_auth (0.1888ms)
  âœ” agent processing with no canvas â†’ ready_to_execute (0.2639ms)
  âœ” hub visible, agent idle â†’ executed_with_result (0.1679ms)
  âœ” agent error â†’ execution_failed (0.1409ms)
âœ” deriveShellPrimaryOutcome (AMD-2026-012 Â§7) (3.5068ms)
â–¶ threadSummaryV1
  âœ” parses plain JSON (1.4596ms)
  âœ” extracts JSON from fenced block (1.1879ms)
  âœ” extractJsonObjectText finds object in prose (0.2958ms)
  âœ” fails on invalid JSON (0.2344ms)
  âœ” fails when root is array (0.1776ms)
  âœ” coerces types safely (0.3004ms)
âœ” threadSummaryV1 (5.3488ms)
â–¶ validateScopeOperation
  âœ” allows read when key is in review_files (1.0884ms)
  âœ” allows read when key is only in modify_files (0.2084ms)
  âœ” denies read when key is outside envelope (0.1896ms)
  âœ” denies when key is in protected_files (0.1609ms)
  âœ” allows write when key is in modify_files (0.1343ms)
  âœ” denies write when key is review-only (0.1222ms)
âœ” validateScopeOperation (3.1814ms)
â–¶ routingEnvelopeToScopeTarget
  âœ” maps thread.read to read + gmail:thread key (0.4894ms)
  âœ” fails thread.read without resource id (0.1843ms)
  âœ” maps draft_reply to write + gmail:message key (0.2202ms)
  âœ” maps calendar.list to read + fixed list key (0.1811ms)
  âœ” maps calendar.get to read + gcal:event key (0.1787ms)
  âœ” maps calendar.events.list to read + gcal:events window key (0.2297ms)
  âœ” fails calendar.events.list without time range (0.1187ms)
  âœ” fails for unmapped intent when envelope would need routing (0.1711ms)
âœ” routingEnvelopeToScopeTarget (2.191ms)
â–¶ buildExecutionScope outputs
  âœ” thread read: review contains thread key, empty modify (1.549ms)
  âœ” summarize: same review surface as thread read for same id (0.2197ms)
  âœ” draft reply: message in modify_files; optional thread in review (0.1441ms)
  âœ” draft reply without thread: message only in review (0.1091ms)
  âœ” calendar list: fixed logical key in review (0.1274ms)
  âœ” calendar get: event id in review (0.1424ms)
  âœ” calendar events list: window key in review (0.1364ms)
âœ” buildExecutionScope outputs (2.6585ms)
â–¶ scopeMetrics
  âœ” increments scope check counters (0.5003ms)
  âœ” records summarize bounded context and averages (0.2105ms)
âœ” scopeMetrics (0.8478ms)
â–¶ deriveWorkspaceIntentForDisclosure
  âœ” returns null without canvas (1.2867ms)
  âœ” maps calendar hub (0.247ms)
  âœ” maps mail hub to search when no successful read (0.1946ms)
  âœ” maps mail hub to read when mailRead ok (0.209ms)
âœ” deriveWorkspaceIntentForDisclosure (3.7711ms)
â–¶ allowShellSurfaceTransition
  âœ” allows primary always (0.9818ms)
  âœ” denies operator without eligibility (0.2029ms)
  âœ” allows operator when eligible (0.1664ms)
  âœ” denies developer without eligibility (0.1561ms)
  âœ” allows developer when developerEligible (0.1913ms)
âœ” allowShellSurfaceTransition (3.0125ms)
â–¶ clampSurfaceModeToInterimAuthority
  âœ” maps denied elevated to primary (0.1691ms)
âœ” clampSurfaceModeToInterimAuthority (0.2991ms)
â–¶ readInterimShellAuthority
  âœ” treats URL aios_operator as operator elevation (1.0528ms)
  âœ” treats URL aios_dev as developer elevation (0.4714ms)
  âœ” treats legacy operator storage as operator elevation (0.3814ms)
  âœ” treats interim operator unlock as operator elevation (0.3493ms)
  âœ” treats legacy diagnostics only as developer elevation (and operator via legacy hint) (0.2407ms)
âœ” readInterimShellAuthority (2.8898ms)
â–¶ resolveInitialSurfaceMode (precedence)
  âœ” prefers persisted session surface mode when interim authority allows it (2.2536ms)
  âœ” uses URL aios_operator when no persisted mode (0.4238ms)
  âœ” defaults to primary (0.4339ms)
  âœ” clamps persisted elevated mode without interim authority to primary (0.3635ms)
âœ” resolveInitialSurfaceMode (precedence) (5.1884ms)
â–¶ routeShellAgentText app.shell.*
  âœ” applies enter_operator without delegating canvas routing (3.6949ms)
  âœ” applies surface_mode with surface field (0.331ms)
  âœ” applies switch_to_chat (0.4508ms)
  âœ” does not delegate canvas for unknown app.shell.* (0.1995ms)
  âœ” does not delegate canvas for unrecognized app.open.* (0.3436ms)
  âœ” delegates workspace intents to canvas router (0.2489ms)
âœ” routeShellAgentText app.shell.* (6.9842ms)
â–¶ shellStateCommandToNavigationAction
  âœ” maps surface and app_mode commands (3.9594ms)
âœ” shellStateCommandToNavigationAction (5.6455ms)
â–¶ getShellNavigationDenialMessage
  âœ” returns null for voice/chat shell action (0.3869ms)
  âœ” denies operator surface without eligibility (0.3321ms)
âœ” getShellNavigationDenialMessage (1.0269ms)
â–¶ tryApplyShellNavigationAction
  âœ” applies set_voice_chat_mode (1.1455ms)
  âœ” does not apply surface when denied (0.251ms)
âœ” tryApplyShellNavigationAction (1.6653ms)
â–¶ applyShellNavigationAction
  âœ” routes set_mode to setAppTargetMode (0.7325ms)
âœ” applyShellNavigationAction (1.5005ms)
â–¶ tryParseShellStateCommand
  âœ” parses surface modes (2.7863ms)
  âœ” parses voice/chat (0.2261ms)
  âœ” returns null for normal sentences (0.4082ms)
âœ” tryParseShellStateCommand (4.7561ms)
â–¶ shouldShowWorkspaceHub (#14)
  âœ” allows hub for connected and auth_required only (0.866ms)
âœ” shouldShowWorkspaceHub (#14) (1.9757ms)
â–¶ callWorkspaceMcpAdapter callsite guard
  âœ” only allowlisted src files reference callWorkspaceMcpAdapter (bypass blocked or absent) (13.8157ms)
âœ” callWorkspaceMcpAdapter callsite guard (15.1582ms)
â–¶ parseContactsListMcpText
  âœ” parses blocks, summary, and next page token (1.356ms)
  âœ” handles contact without Name line (0.4228ms)
âœ” parseContactsListMcpText (3.0432ms)
â–¶ workspaceDriveListDataIsEmpty
  âœ” treats null as empty (1.1887ms)
  âœ” detects empty files array (Drive API shape) (0.2589ms)
  âœ” detects non-empty files (0.1879ms)
  âœ” unwraps nested data.files (0.194ms)
  âœ” returns false for unknown object without list keys (show raw ok) (0.202ms)
âœ” workspaceDriveListDataIsEmpty (3.648ms)
â–¶ unwrapMailSearchPayload
  âœ” unwraps JSON-RPC result envelope (0.9281ms)
  âœ” chains result.data when present (0.3139ms)
  âœ” leaves bare API shape unchanged (0.5261ms)
âœ” unwrapMailSearchPayload (2.7334ms)
â–¶ normalizeMailSearchRows
  âœ” extracts minimal Gmail list ids (id + threadId) (0.8002ms)
  âœ” unwraps MCP result wrapper before extraction (0.2969ms)
  âœ” flattens thread â†’ messages with metadata (17.3999ms)
  âœ” does not treat bare thread stubs as message ids (0.3485ms)
  âœ” maps subject and nested sender (0.493ms)
  âœ” returns empty for non-object payloads (0.4316ms)
  âœ” dedupes by message id (0.2121ms)
âœ” normalizeMailSearchRows (20.3398ms)
â–¶ workspaceMailReadMessageIdFromIntent
  âœ” returns message id only for workspace.mail.read (0.6036ms)
  âœ” returns undefined for workspace.mail.search even if resource_id is set (0.1145ms)
  âœ” returns undefined for workspace.mail.thread.read (thread id, not message id) (0.0917ms)
âœ” workspaceMailReadMessageIdFromIntent (1.6786ms)
â–¶ workspaceIntentToCanvasView
  âœ” maps workspace.drive.list to workspace_drive_hub (0.6843ms)
âœ” workspaceIntentToCanvasView (0.7868ms)
â–¶ workspaceViewAfterConnect
  âœ” resumes calendar hub (1.6385ms)
  âœ” resumes mail hub with message id (0.2028ms)
  âœ” defaults generic workspace_hub to calendar list (0.1266ms)
  âœ” defaults undefined view to calendar list (0.1296ms)
âœ” workspaceViewAfterConnect (3.3337ms)
â„¹ tests 111
â„¹ suites 30
â„¹ pass 111
â„¹ fail 0
â„¹ cancelled 0
â„¹ skipped 0
â„¹ todo 0
â„¹ duration_ms 696.5082
```


# Visual evidence — manual capture (MVP)

**Automation:** Screenshots are **not** produced by the runner (`visual_capture_automated` is false in `EXECUTION_TRANSACTION.json`). What is missing until you add files here is **visible proof**, not a secret success.

**Required captures (from `EXECUTION_TRANSACTION.json` → `required_visual_proofs`):**

- [ ] screenshot: full app shell with identity bar + command rail visible (baseline)
- [ ] screenshot: workspace hub open showing connection or auth state (signed-in, auth_required, or error — whichever matches run)
- [ ] screenshot: same session with voice idle panel visible OR note N/A if voice chrome hidden by design for this branch
- [ ] short note: which route or overlay state each image corresponds to (one line each)

Complete this checklist after `npm run dev` or your preferred preview.

- [ ] Route / surface: …
- [ ] Screenshot saved as `screenshots/01-<surface>.png`
- [ ] Notes on expected vs observed behavior

Add files under this folder; the **`artifacts`** object in the transaction points here.

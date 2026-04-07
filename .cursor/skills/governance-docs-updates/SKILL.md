---
name: governance-docs-updates
description: >-
  Updates AIOS governing documents in this repo (specs, amendments, registry,
  peer review, CHANGELOG). Use when editing AMD/SPEC drafts, DOCUMENT_REGISTRY,
  triangulated review, or pushing to GitHub gateway-global-ai/aios-governing-docs.
---

# Governance docs updates (AIOS)

## This repository

Remote: **https://github.com/gateway-global-ai/aios-governing-docs**

Use repo root as working directory for git and for `scripts/` commands.

---

## Binding rules (do not skip)

1. **Ratification path (AMD-2026-005):** Author validation → triangulated peer review → thresholds (composite ≥ 3.5, no dimension below 3) → ratification. No extra post–peer-review human audit as a workflow gate unless constitutional law already requires it.
2. **Workspace / Google (SPEC-007):** Layer 2 `workspace.*` intents map to **exactly one** Layer 1 `workspace.google.*` scope class; product integrations use control plane + adapter, not raw tool exposure.
3. **Registry:** After changing governed markdown with front matter under `core/`, `specifications/`, `commercial/`, `amendments/`, or `reference/`, run **`scripts/registry_generator.py`**.
4. **Cross-references:** Keep YAML `document_id` / `cross_references` consistent; follow `templates/amendment_template.md` for amendments.

---

## Checklist (substantive changes)

- [ ] Correct files; match `STYLE_GUIDE.md` and front matter conventions.
- [ ] New documents: required front matter fields.
- [ ] `py -3 scripts/registry_generator.py`
- [ ] `CHANGELOG.md` when user-visible.
- [ ] Specs/amendments: bump `version` / `last_updated` when appropriate.

---

## Peer review

```bash
cd scripts
py -3 peer_review.py specifications/<Doc>.md --round 1 --rubric light --smart-context
```

Requires `.env` keys — see `DEVELOPER.md`.

---

## Git / GitHub

Prefer a **PR** to `main` with **CI green**; see **README.md** (GitHub vs AIOS governance), **DEVELOPER.md** (Git and GitHub), and **`.github/pull_request_template.md`**. **Solo maintainer:** GitHub **required approving reviews** should be off or zero—governance review stays **in-repo** (peer review, ratification), not on the GitHub Approve button.

```bash
git add -A
git commit -m "docs: <message>"
git push origin <branch>
```

---

## Do not

- Hand-edit `DOCUMENT_REGISTRY.md` / `.json` (regenerate).
- Change AMD-2026-005 / SPEC-007 norms without amendment or ratified SPEC update.

---

## Related product repo

Voice UI and Workspace runtime: **ai-os-voice-interface** (separate repo). Doc changes here do not automatically change app code.

## Summary

<!-- What this PR does (short). -->

## Governance

- **GitHub** = merge mechanics and **required status checks** (CI). A GitHub **Approve** is **not** AIOS triangulated peer review, thresholds, or ratification in-repo (**AMD-2026-005**).
- **Required status checks** still gate merge when enabled on `main`.
- If this PR changes **governed** documents or material governance text, reference **in-repo** artifacts when applicable (e.g. `reviews/…`, ratification output, amendment paths).

## Checklist

- [ ] **Status checks** expected to pass (e.g. Governance integrity / `pytest`).
- [ ] **Review / ratification artifacts** linked or noted if this PR changes governed docs or governance substance.
- [ ] **`registry_generator.py`** run if governed doc paths or front matter changed (see **DEVELOPER.md**).
- [ ] **CHANGELOG.md** updated if the change is user-visible.

<!-- Normative context: **README.md** § GitHub vs AIOS governance; **DEVELOPER.md** § Git and GitHub. -->

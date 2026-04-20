# Audit and change history — AMD-2026-008-ADD-004

**Purpose:** Give an **external peer reviewer** a single narrative: **what was requested**, **how decisions were reasoned**, **which files carry those decisions**, and **how that ties to `CHANGELOG.md`**.  
**Audience:** Someone who did **not** participate in the Cursor session(s) that produced these edits.  
**Date of package:** 2026-04-08.

---

## 1. Problem statement (user requirements)

The ADD-004 workstream had reached a delicate state after **Phase E** and **Round 1** **`peer_review.py`** on assessed **`draft` `0.2.0`**:

1. **Committee packet** still read like **open / pending** even though **Round 1** had **completed** and **[AMD-2026-005](../../../amendments/AMD-2026-005.md)** **ratification gate** had **FAILED** (not “still waiting on committee”).
2. **`draft` `0.3.0`** needed to be framed as a **deliberate author response** to **Round 1 synthesis themes** (implementation seam, SPEC/MPOA/parent pointers, addendum precedence / incorporation clarity, policy-equivalent surfaces), not an ad hoc bump.
3. A **status split** had to stay **consistent everywhere**: **artifact health** (planning, knowledge, packet structure) **good**; **review gate** **FAIL**; **next state** **revise, not ratify** — without conflating packet integrity with ratification eligibility.

**Explicit closure label chosen for the committee layer:** **`superseded_by_round_1_findings`** (as opposed to “deferred to 0.3.0” or “answered” alone), because the pre–Round 1 committee questions were **overtaken** by executed Phase E + triangulated peer review evidence.

---

## 2. Reasoning chain (logic history)

### 2.1 Why separate “artifact health” from “review gate”

**AMD-2026-005** evaluates the **draft amendment text** and evidence bundle for **ratification readiness**. Supporting artifacts (architect/UI plans, knowledge notes, folder hygiene) can be **coherent** while the **normative draft** still scores **below** composite / dimension thresholds. Mixing those signals confuses **“is the folder messy?”** with **“does this draft pass the peer-review law?”** The amendment’s **§0** table and downstream packet READMEs now **state both** layers explicitly.

### 2.2 Why close the committee packet without “pending”

The committee packet was written as a **Phase D** advisory step. After **Phase E** (`0.2.0`) and **Round 1** (**FAIL**), leaving **“Pending”** on committee questions would **misrepresent process state**: the governing evidence is now **Round 1 synthesis + ratification gate report**, not an unanswered committee queue. Closure as **`superseded_by_round_1_findings`** records that the **committee layer** is **procedurally complete**; **doctrine revision** continues via **`0.3.0`** and **Round 2**.

### 2.3 Why `0.3.0` is labeled “Round 2 preparation”

Round 1 failed primarily on **DeepSeek** lane (composite **2.8**, dimensions **&lt; 3** per gate report). **`0.3.0`** maps synthesis themes into **specific sections** (see amendment **§0.2** and **addendum_history**) so Round 2 assesses a **document that responds to known gaps**, not a silent version tick.

### 2.4 Why reorder §0.1 before §0.2

Definitions are **foundational**; revision posture is **meta** about the draft version. Reading **definitions first**, then **revision posture**, matches how a human reviewer parses the document.

### 2.5 Why change `peer_review.py` to preserve YAML keys

`PACKET_IDENTITY.yaml` is **regenerated** each run. Without a merge step, optional fields documenting **which draft Round 1 assessed** (`round_1_reviewed_draft`) and a compact **status_split** token could **disappear** on Round 2, confusing auditors. The script now **preserves** those keys if present in the existing file.

### 2.6 Registry and tracker

**`registry_generator.py`** was run so **DOCUMENT_REGISTRY** reflects current amendment front matter. **`AMD-AMENDMENT-REVIEW-TRACKER-001`** was bumped to **v1.2.8** with an **`amendment_history`** summary row so the **governed tracker** matches packet and queue state.

---

## 3. Map: user ask → primary artifacts

| User ask | Where it landed |
|----------|------------------|
| Committee not “Pending” | [`planning/COMMITTEE_PACKET.md`](../planning/COMMITTEE_PACKET.md) — **Closed** + **`superseded_by_round_1_findings`** + disposition table |
| `0.3.0` as synthesis response | [`amendments/AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md`](../../../amendments/AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md) — **§0.2**, **addendum_history** |
| Status split everywhere | Packet [`README.md`](../README.md); [`round_1/RATIFICATION_GATE_REPORT.md`](../round_1/RATIFICATION_GATE_REPORT.md); [`round_1/REVIEW_SYNTHESIS.md`](../round_1/REVIEW_SYNTHESIS.md); [`round_1/README.md`](../round_1/README.md); [`reviews/amd_2026_008/README.md`](../../amd_2026_008/README.md); tracker; `review_queue.json` |
| Procedural vs integrity | Repeated language: **closure is procedural**; **gate failure is doctrinal / AMD-2026-005** |
| Tooling | [`scripts/peer_review.py`](../../../scripts/peer_review.py) — preserve identity keys |

---

## 4. CHANGELOG alignment

The authoritative record is **[`CHANGELOG.md`](../../../CHANGELOG.md)** under **`[Unreleased]` → `Changed`**.

Chronological bullets for this amendment (newest first in file):

1. **`0.3.0` + committee closure + status split** — matches **§2–3** of this audit.
2. **`peer_review.py` / `context_assembler`** — disambiguating review filenames + `PACKET_IDENTITY`.
3. **`0.2.0` + Round 1 re-run** — Phase E content + **FAIL** gate + triad.
4. **`0.1.0` + pipeline intake** — initial filing + partial Round 1 superseded by later triad.

A **verbatim excerpt** of the ADD-004–related bullets is in **`CHANGELOG_EXCERPT_ADD004.md`** in this folder.

---

## 5. What an external reviewer should verify

1. **Internal consistency:** Every surface that names ADD-004’s version should agree: **current draft head `0.3.0`**, **Round 1 assessed `0.2.0`**, **Round 2 next** on `0.3.0`.
2. **Gate report integrity:** [`round_1/RATIFICATION_GATE_REPORT.md`](../round_1/RATIFICATION_GATE_REPORT.md) still describes **FAIL** on **`0.2.0`**; banners must not imply Round 1 **PASS**.
3. **Committee closure:** [`COMMITTEE_PACKET.md`](../planning/COMMITTEE_PACKET.md) does not invite new **Phase D** work without a **Council / coordinator** decision to reopen.
4. **CHANGELOG:** The top ADD-004 bullet in **`CHANGELOG.md`** matches the **file list** in **`FILE_MANIFEST.md`** for this closure pass.
5. **Script behavior:** Re-running **`peer_review.py`** for Round 2 should **not** drop **`round_1_reviewed_draft`** / **`status_split`** from [`PACKET_IDENTITY.yaml`](../round_1/PACKET_IDENTITY.yaml) if those keys remain in the file before the run.

---

## 6. Known limitations of this audit

- This document reflects **authoring-session intent** and **repository paths**; it does **not** replace **git history** after commits land. Reviewers should **`git diff`** against their baseline branch.
- **API keys / `.env`** for **`peer_review.py`** are **not** included; Round 2 is a **future operational step**.

---

*Audit narrative — AMD-2026-008-ADD-004 — external peer review package — 2026-04-08.*

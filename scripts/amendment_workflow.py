"""
Amendment program runs: template-backed proposals, simulated peer review, synthesis, console steps.
Does not modify governing document files — demo / founder workflow only.
"""

from __future__ import annotations

import json
import re
import uuid
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path

from brand_config import expand_gateway_placeholders

# governing_docs/
WORKFLOW_ROOT = Path(__file__).resolve().parent.parent / "amendment_workflow"
TEMPLATES_DIR = WORKFLOW_ROOT / "templates"
RUNS_DIR = WORKFLOW_ROOT / "runs"


def _now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _ensure_dirs() -> None:
    TEMPLATES_DIR.mkdir(parents=True, exist_ok=True)
    RUNS_DIR.mkdir(parents=True, exist_ok=True)


def list_templates() -> list[dict]:
    _ensure_dirs()
    out = []
    for meta in sorted(TEMPLATES_DIR.glob("*-meta.json")):
        data = json.loads(meta.read_text(encoding="utf-8"))
        out.append(
            {
                "template_id": data.get("template_id", meta.stem.replace("-meta", "")),
                "title": data.get("title", ""),
                "amendment_id": data.get("amendment_id", ""),
                "affected_documents": data.get("affected_documents", []),
            }
        )
    return out


def _load_template_markdown(template_id: str) -> tuple[dict, str]:
    meta_path = TEMPLATES_DIR / f"{template_id}-meta.json"
    md_path = TEMPLATES_DIR / f"{template_id}.md"
    if not meta_path.exists() or not md_path.exists():
        raise ValueError(f"Unknown template: {template_id}")
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    body = expand_gateway_placeholders(md_path.read_text(encoding="utf-8"))
    return meta, body


def _simulated_peer_reviews(template_title: str) -> list[dict]:
    return [
        {
            "reviewer": "Peer A (architecture)",
            "model": "simulated",
            "dimensions": {"clarity": 4, "feasibility": 5, "alignment": 5},
            "summary": (
                f"Architecture review of “{template_title}”: Article X placement after Art IX is sound. "
                "Recommend explicit linkage to audit log schema in Technical Manifesto Art VI."
            ),
        },
        {
            "reviewer": "Peer B (governance)",
            "model": "simulated",
            "dimensions": {"clarity": 5, "feasibility": 4, "alignment": 5},
            "summary": (
                "Constitution updates should reference the existing transparency log cadence. "
                "Judicial disclosure requirement is clear; add cross-reference to Council Operating Manual for escalations."
            ),
        },
        {
            "reviewer": "Peer C (UX/registry)",
            "model": "simulated",
            "dimensions": {"clarity": 4, "feasibility": 4, "alignment": 4},
            "summary": (
                "Mandatory `aios-intent-identity-card` should specify z-index and conflict rules with vendor UI. "
                "Registry bump to 1.1.0 MINOR is consistent with non-breaking platform addition."
            ),
        },
    ]


def _synthesized_plan(meta: dict, reviews: list[dict]) -> str:
    lines = [
        "## Recommended plan (synthesized)",
        "",
        f"**Amendment:** {meta.get('amendment_id', '')} — {meta.get('title', '')}",
        "",
        "### Consensus",
        "- Proceed with **Technical Manifesto** new Article X and **Constitution** transparency hooks as drafted.",
        "- **UI Component Registry**: register `aios-intent-identity-card` as a system-managed mandatory component with WCAG AA.",
        "- **Roadmap**: schedule Intent Identity Disclosure under the stated quarter; treat as MINOR platform addition.",
        "",
        "### Actions before merge (human)",
        "1. Open RFC thread and attach this proposal + simulated reviews.",
        "2. Run staging simulation: Stateful Shell renders identity card on IntentKey transitions.",
        "3. Council supermajority vote per Constitution Art VI.",
        "4. After ratification, apply patches to affected files and bump versions (1.0.0 → 1.1.0 where noted).",
        "",
        "### Peer review highlights",
    ]
    for r in reviews:
        lines.append(f"- **{r['reviewer']}:** {r['summary'][:200]}{'…' if len(r['summary']) > 200 else ''}")
    lines.append("")
    lines.append("*This synthesis is generated for the amendment workflow demo; it does not modify the repository.*")
    return "\n".join(lines)


@dataclass
class WorkflowStep:
    id: str
    label: str
    status: str  # pending | active | completed
    detail: str
    at: str | None


def create_run(template_id: str) -> dict:
    _ensure_dirs()
    meta, proposal_md = _load_template_markdown(template_id)
    run_id = f"awr-{uuid.uuid4().hex[:12]}"
    run_dir = RUNS_DIR / run_id
    run_dir.mkdir(parents=True, exist_ok=False)

    steps = [
        WorkflowStep(
            "load",
            "Load proposal & metadata",
            "completed",
            f"Template `{template_id}` loaded ({len(proposal_md)} chars).",
            _now_iso(),
        ),
        WorkflowStep(
            "peer",
            "Peer review (simulated)",
            "active",
            "Waiting for advance — will generate three peer reviews.",
            None,
        ),
        WorkflowStep(
            "synthesize",
            "Synthesize plan",
            "pending",
            "Merge reviews into a recommended plan with action steps.",
            None,
        ),
        WorkflowStep(
            "preview",
            "Merge preview (no repo writes)",
            "pending",
            "Confirm patch intent without applying changes to core/spec files.",
            None,
        ),
        WorkflowStep(
            "done",
            "Workflow complete",
            "pending",
            "Mark run finished; optional export of artifacts.",
            None,
        ),
    ]

    peer_reviews: list[dict] = []
    consolidated = ""

    state = {
        "run_id": run_id,
        "template_id": template_id,
        "created_at": _now_iso(),
        "updated_at": _now_iso(),
        "status": "in_progress",
        "meta": meta,
        "proposal_markdown": proposal_md,
        "peer_reviews": peer_reviews,
        "consolidated_plan_markdown": consolidated,
        "steps": [asdict(s) for s in steps],
        "console": [
            {"ts": _now_iso(), "level": "info", "message": f"Run {run_id} created from template {template_id}."},
            {"ts": _now_iso(), "level": "ok", "message": "Proposal loaded into workspace."},
        ],
    }

    (run_dir / "state.json").write_text(json.dumps(state, indent=2), encoding="utf-8")
    return state


def _load_state(run_id: str) -> dict:
    path = RUNS_DIR / run_id / "state.json"
    if not path.exists():
        raise ValueError(f"Run not found: {run_id}")
    return json.loads(path.read_text(encoding="utf-8"))


def get_run(run_id: str) -> dict:
    return _load_state(run_id)


def advance_run(run_id: str) -> dict:
    state = _load_state(run_id)
    steps = state["steps"]
    meta = state["meta"]

    def idx_active() -> int:
        for i, s in enumerate(steps):
            if s["status"] == "active":
                return i
        return -1

    i = idx_active()
    if i < 0:
        state["status"] = "completed"
        state["updated_at"] = _now_iso()
        _persist(state)
        return state

    # complete current active step
    if steps[i]["status"] == "active":
        steps[i]["status"] = "completed"
        steps[i]["at"] = _now_iso()
        if steps[i]["id"] == "peer":
            state["peer_reviews"] = _simulated_peer_reviews(meta.get("title", "Amendment"))
            steps[i]["detail"] = f"Collected {len(state['peer_reviews'])} peer reviews (simulated)."
            state["console"].append(
                {"ts": _now_iso(), "level": "ok", "message": "Peer reviews generated (simulated triangulation)."}
            )
        elif steps[i]["id"] == "synthesize":
            state["consolidated_plan_markdown"] = _synthesized_plan(meta, state["peer_reviews"])
            steps[i]["detail"] = "Consolidated plan drafted from peer feedback."
            state["console"].append(
                {"ts": _now_iso(), "level": "ok", "message": "Recommended plan and action steps written."}
            )
        elif steps[i]["id"] == "preview":
            steps[i]["detail"] = "Merge preview acknowledged — no files modified in this demo."
            state["console"].append(
                {"ts": _now_iso(), "level": "warn", "message": "Demo mode: repository left unchanged."}
            )
        elif steps[i]["id"] == "done":
            steps[i]["detail"] = "Amendment program run closed."
            state["console"].append({"ts": _now_iso(), "level": "ok", "message": "Workflow finished."})
            state["status"] = "completed"

    # activate next pending
    for j in range(len(steps)):
        if steps[j]["status"] == "pending":
            steps[j]["status"] = "active"
            if steps[j]["id"] == "peer":
                steps[j]["detail"] = "Advance to generate simulated peer reviews."
            elif steps[j]["id"] == "synthesize":
                steps[j]["detail"] = "Advance to synthesize recommended plan."
            elif steps[j]["id"] == "preview":
                steps[j]["detail"] = "Advance to acknowledge merge preview (no writes)."
            elif steps[j]["id"] == "done":
                steps[j]["detail"] = "Advance to complete workflow."
            state["console"].append(
                {"ts": _now_iso(), "level": "info", "message": f"Step active: {steps[j]['label']}"}
            )
            break
    else:
        # no pending — mark complete
        state["status"] = "completed"
        state["console"].append({"ts": _now_iso(), "level": "ok", "message": "All steps completed."})

    state["updated_at"] = _now_iso()
    state["steps"] = steps
    _persist(state)
    return state


def _persist(state: dict) -> None:
    run_id = state["run_id"]
    path = RUNS_DIR / run_id / "state.json"
    path.write_text(json.dumps(state, indent=2), encoding="utf-8")

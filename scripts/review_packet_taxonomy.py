"""
Shared helpers for AIOS review packet taxonomy (identity / status / events).
Used by peer_review.py and validate_review_packet.py.
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

# Identity v2: stable facts only (see AIOS-REVIEW-PACKET-TAXONOMY-001)
PACKET_IDENTITY_ALLOWED_KEYS = frozenset({
    "document_id",
    "document_path",
    "packet_slug",
    "current_head_version",
    "review_round",
    "packet_path",
    "manifest_path",
    "packet_schema_version",
    "generated_by",
    "generated_at",
})

PACKET_STATUS_REQUIRED_KEYS = frozenset({
    "document_id",
    "packet_slug",
    "current_head_version",
    "last_reviewed_version",
    "artifact_health",
    "review_gate_status",
    "committee_status",
    "next_action",
    "lifecycle_phase",
    "status_updated_at",
    "status_updated_by",
})

PACKET_EVENTS_TOP_LEVEL_KEYS = frozenset({
    "packet_schema_version",
    "document_id",
    "packet_slug",
    "events",
})

PACKET_EVENT_REQUIRED_KEYS = frozenset({
    "event_id",
    "timestamp",
    "actor",
    "event_type",
    "from_version",
    "to_version",
    "round",
    "summary",
    "evidence_paths",
})

ARTIFACT_HEALTH = frozenset({"healthy", "stale_supporting_artifacts", "identity_mismatch", "incomplete_packet"})
REVIEW_GATE = frozenset({"not_run", "incomplete", "pass", "fail"})
COMMITTEE = frozenset({"open", "answered", "closed_superseded_by_review", "reopened_by_council"})
NEXT_ACTION = frozenset({
    "revise",
    "peer_review_round_1",
    "peer_review_round_2",
    "ratification_motion",
    "archive",
    "manual_resolution",
})
LIFECYCLE = frozenset({
    "planning",
    "phase_e_revision",
    "round_1_complete",
    "round_2_ready",
    "ratification_ready",
    "archived",
})
EVENT_TYPES = frozenset({
    "packet_initialized",
    "draft_revised",
    "review_round_completed",
    "review_gate_failed",
    "review_gate_passed",
    "committee_closed_superseded",
    "packet_status_corrected",
    "handoff_hardening_applied",
    "external_review_package_created",
})

PACKET_SCHEMA_VERSION_CURRENT = "2"
HANDOFF_AUTHORITY_LINE = "**If this note contradicts `PACKET_STATUS.yaml` or `PACKET_EVENTS.yaml`, the YAML artifacts win.**"

# --- AMD-2026-005 gate (automated inference from saved review files) ---


def _parse_front_matter(text: str) -> dict[str, Any]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    block = text[3:end]
    try:
        return yaml.safe_load(block) or {}
    except Exception:
        return {}


def _dimension_scores_from_markdown(body: str) -> list[int]:
    """Extract numeric dimension scores (1-5) from rubric scorecard tables."""
    scores: list[int] = []
    for line in body.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        if re.match(r"^\|[\s\-:]+\|", line):
            continue
        if "Composite" in line:
            continue
        parts = [p.strip() for p in line.split("|")]
        parts = [p for p in parts if p]
        if len(parts) < 3:
            continue
        if not parts[0].isdigit():
            continue
        score_cell = parts[-1].replace("*", "").strip()
        m = re.match(r"^(\d+)$", score_cell)
        if m:
            v = int(m.group(1))
            if 1 <= v <= 5:
                scores.append(v)
    return scores


def infer_amd_2026_005_gate_from_round_dir(round_dir: Path) -> tuple[str, str]:
    """
    Returns (review_gate_status, one_line_summary).
    review_gate_status: pass | fail | incomplete
    """
    reviews = sorted(round_dir.glob("review_*__*.md"))
    if len(reviews) < 3:
        return (
            "incomplete",
            f"Triangulation incomplete: expected 3 review files, found {len(reviews)}.",
        )

    composites: list[float] = []
    min_dim_global = 5
    for rp in reviews:
        text = rp.read_text(encoding="utf-8", errors="replace")
        fm = _parse_front_matter(text)
        cs = fm.get("composite_score")
        if cs is None:
            return (
                "incomplete",
                f"Missing composite_score in front matter: {rp.name}.",
            )
        try:
            composites.append(float(cs))
        except (TypeError, ValueError):
            return ("incomplete", f"Invalid composite_score in {rp.name}.")

        body = text.split("---", 2)[-1] if text.startswith("---") else text
        dims = _dimension_scores_from_markdown(body)
        if dims:
            min_dim_global = min(min_dim_global, min(dims))

    # If we never got dimension rows, do not fail on dimension rule
    worst_composite = min(composites)
    if worst_composite < 3.5:
        return (
            "fail",
            f"AMD-2026-005 composite threshold not met (min composite {worst_composite}; require ≥ 3.5).",
        )
    # Dimension rule: no dimension < 3
    if min_dim_global < 3:
        return (
            "fail",
            f"AMD-2026-005 dimension threshold not met (minimum dimension score {min_dim_global}; require ≥ 3).",
        )
    return (
        "pass",
        f"AMD-2026-005 thresholds satisfied (min composite {worst_composite}; min dimension {min_dim_global}).",
    )


def next_event_id(events: list[dict[str, Any]]) -> str:
    n = len(events) + 1
    return f"evt-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}-{n:03d}"


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _assert_exact_keys(label: str, actual: set[str], required: frozenset[str]) -> None:
    extra = actual - required
    missing = required - actual
    if extra or missing:
        raise ValueError(f"{label} key mismatch: extra={sorted(extra)} missing={sorted(missing)}")


DEFAULT_HANDOFF_NOTE = """# Handoff note (non-authoritative)

**If this note contradicts `PACKET_STATUS.yaml` or `PACKET_EVENTS.yaml`, the YAML artifacts win.**

- Confirm each review filename includes `__<DOCUMENT_ID>.md` before attaching outside the repo.
- Run `py -3 scripts/validate_review_packet.py --round-dir <this_round_dir>` before export.

See **AIOS-REVIEW-PACKET-TAXONOMY-001**.
"""


def write_packet_identity_v2(
    round_dir: Path,
    base_dir: Path,
    *,
    document_id: str,
    document_path: str,
    packet_slug: str,
    current_head_version: str,
    review_round: int,
    manifest_rel: str,
    generated_by: str = "peer_review.py",
) -> None:
    packet_rel = round_dir.relative_to(base_dir).as_posix()
    body: dict[str, Any] = {
        "document_id": document_id,
        "document_path": document_path.replace("\\", "/"),
        "packet_slug": packet_slug,
        "current_head_version": current_head_version,
        "review_round": review_round,
        "packet_path": packet_rel,
        "manifest_path": manifest_rel.replace("\\", "/"),
        "packet_schema_version": PACKET_SCHEMA_VERSION_CURRENT,
        "generated_by": generated_by,
        "generated_at": utc_now_iso(),
    }
    _assert_exact_keys("PACKET_IDENTITY", set(body.keys()), PACKET_IDENTITY_ALLOWED_KEYS)
    (round_dir / "PACKET_IDENTITY.yaml").write_text(
        yaml.dump(body, default_flow_style=False, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )


def _load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except Exception:
        return {}


def _version_tuple(v: str) -> tuple[int, ...]:
    if not v or not str(v).strip():
        return ()
    parts: list[int] = []
    for p in str(v).strip().split("."):
        if p.isdigit():
            parts.append(int(p))
        else:
            m = re.match(r"^(\d+)", p)
            if m:
                parts.append(int(m.group(1)))
    return tuple(parts)


def merge_and_write_packet_status(
    round_dir: Path,
    *,
    document_id: str,
    packet_slug: str,
    current_head_version: str,
    last_reviewed_version: str,
    review_round: int,
    gate: str,
    gate_summary: str,
) -> None:
    path = round_dir / "PACKET_STATUS.yaml"
    prev = _load_yaml(path)

    artifact_health = prev.get("artifact_health") or "healthy"
    # Peer review does not mutate committee_status; preserve prior coordinator / author edits.
    committee = prev.get("committee_status", "open")

    if gate == "pass":
        review_gate_status = "pass"
        if review_round == 1:
            next_action = "peer_review_round_2"
            lifecycle_phase = "round_1_complete"
        else:
            next_action = "ratification_motion"
            lifecycle_phase = "ratification_ready"
    elif gate == "fail":
        review_gate_status = "fail"
        next_action = "revise"
        lifecycle_phase = "round_1_complete" if review_round == 1 else "round_2_ready"
        ch = _version_tuple(str(current_head_version))
        lr = _version_tuple(str(last_reviewed_version))
        if review_round == 1 and ch and lr and ch > lr:
            next_action = "peer_review_round_2"
            lifecycle_phase = "round_2_ready"
    else:
        review_gate_status = "incomplete"
        next_action = "manual_resolution"
        lifecycle_phase = "round_1_complete" if review_round == 1 else "round_2_ready"

    body = {
        "document_id": document_id,
        "packet_slug": packet_slug,
        "current_head_version": current_head_version,
        "last_reviewed_version": last_reviewed_version,
        "artifact_health": artifact_health,
        "review_gate_status": review_gate_status,
        "committee_status": committee,
        "next_action": next_action,
        "lifecycle_phase": lifecycle_phase,
        "status_updated_at": utc_now_iso(),
        "status_updated_by": "peer_review.py",
    }
    _assert_exact_keys("PACKET_STATUS", set(body.keys()), PACKET_STATUS_REQUIRED_KEYS)
    path.write_text(
        yaml.dump(body, default_flow_style=False, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )


def append_packet_events_peer_review(
    round_dir: Path,
    base_dir: Path,
    *,
    document_id: str,
    packet_slug: str,
    from_version: str,
    reviewed_version: str,
    review_round: int,
    gate: str,
    gate_summary: str,
) -> None:
    path = round_dir / "PACKET_EVENTS.yaml"
    prev = _load_yaml(path)
    events: list[dict[str, Any]] = list(prev.get("events") or [])

    def rel(p: Path) -> str:
        return p.relative_to(base_dir).as_posix()

    evidence_paths: list[str] = []
    manifests = sorted(round_dir.glob("peer_review_manifest_*.json"))
    if manifests:
        evidence_paths.append(rel(manifests[-1]))
    for rf in sorted(round_dir.glob("review_*__*.md")):
        evidence_paths.append(rel(rf))

    ts = utc_now_iso()
    e1 = {
        "event_id": next_event_id(events),
        "timestamp": ts,
        "actor": "peer_review.py",
        "event_type": "review_round_completed",
        "from_version": from_version,
        "to_version": reviewed_version,
        "round": review_round,
        "summary": f"Peer review round {review_round} completed for assessed draft {reviewed_version}.",
        "evidence_paths": evidence_paths[:12],
    }
    events.append(e1)

    if gate == "pass":
        events.append({
            "event_id": next_event_id(events),
            "timestamp": utc_now_iso(),
            "actor": "peer_review.py",
            "event_type": "review_gate_passed",
            "from_version": reviewed_version,
            "to_version": reviewed_version,
            "round": review_round,
            "summary": gate_summary[:500],
            "evidence_paths": evidence_paths[:12],
        })
    elif gate == "fail":
        events.append({
            "event_id": next_event_id(events),
            "timestamp": utc_now_iso(),
            "actor": "peer_review.py",
            "event_type": "review_gate_failed",
            "from_version": reviewed_version,
            "to_version": reviewed_version,
            "round": review_round,
            "summary": gate_summary[:500],
            "evidence_paths": evidence_paths[:12],
        })
    # incomplete: no second gate event

    for ev in events:
        _assert_exact_keys("PACKET_EVENTS.event", set(ev.keys()), PACKET_EVENT_REQUIRED_KEYS)

    out = {
        "packet_schema_version": PACKET_SCHEMA_VERSION_CURRENT,
        "document_id": document_id,
        "packet_slug": packet_slug,
        "events": events,
    }
    _assert_exact_keys("PACKET_EVENTS", set(out.keys()), PACKET_EVENTS_TOP_LEVEL_KEYS)
    path.write_text(
        yaml.dump(out, default_flow_style=False, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )


def ensure_default_handoff_note(round_dir: Path) -> None:
    p = round_dir / "HANDOFF_NOTE.md"
    if not p.exists():
        p.write_text(DEFAULT_HANDOFF_NOTE, encoding="utf-8")

#!/usr/bin/env python3
"""
Validate review packet taxonomy artifacts under reviews/<slug>/round_N/.

Exit 0 = PASS, exit 1 = FAIL (prints findings to stderr).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

from review_packet_taxonomy import (
    ARTIFACT_HEALTH,
    COMMITTEE,
    EVENT_TYPES,
    HANDOFF_AUTHORITY_LINE,
    LIFECYCLE,
    NEXT_ACTION,
    PACKET_EVENT_REQUIRED_KEYS,
    PACKET_EVENTS_TOP_LEVEL_KEYS,
    PACKET_IDENTITY_ALLOWED_KEYS,
    PACKET_SCHEMA_VERSION_CURRENT,
    PACKET_STATUS_REQUIRED_KEYS,
    REVIEW_GATE,
)

BASE_DIR = Path(__file__).resolve().parent.parent


def _err(msg: str) -> None:
    print(msg, file=sys.stderr)


def _parse_front_matter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    try:
        return yaml.safe_load(text[3:end]) or {}
    except Exception:
        return {}


def _parse_version_tuple(v: str) -> tuple[int, ...]:
    if not v or not str(v).strip():
        return ()
    parts = []
    for p in str(v).strip().split("."):
        if p.isdigit():
            parts.append(int(p))
        else:
            m = re.match(r"^(\d+)", p)
            if m:
                parts.append(int(m.group(1)))
    return tuple(parts)


def validate_round_dir(round_dir: Path, base_dir: Path) -> tuple[str, list[str]]:
    """
    Returns (overall, messages) where overall is PASS|FAIL|legacy_packet_schema|schema_version_missing
    """
    msgs: list[str] = []
    overall = "PASS"

    identity_path = round_dir / "PACKET_IDENTITY.yaml"
    status_path = round_dir / "PACKET_STATUS.yaml"
    events_path = round_dir / "PACKET_EVENTS.yaml"
    handoff_path = round_dir / "HANDOFF_NOTE.md"

    if not identity_path.exists():
        msgs.append("FAIL: PACKET_IDENTITY.yaml missing")
        return "FAIL", msgs

    try:
        identity = yaml.safe_load(identity_path.read_text(encoding="utf-8")) or {}
    except Exception as e:
        msgs.append(f"FAIL: PACKET_IDENTITY.yaml unreadable: {e}")
        return "FAIL", msgs

    legacy_keys = identity.keys() & {
        "schema",
        "handoff_note",
        "document_relative_path",
        "document_slug",
        "version",
        "title",
        "status",
        "generated_utc",
        "round_1_reviewed_draft",
        "status_split",
        "peer_review_manifest",
    }
    if legacy_keys:
        msgs.append(f"legacy_packet_schema: identity contains legacy keys {sorted(legacy_keys)}")
        overall = "legacy_packet_schema"

    extra = set(identity.keys()) - PACKET_IDENTITY_ALLOWED_KEYS
    if extra:
        msgs.append(f"FAIL: PACKET_IDENTITY.yaml has disallowed keys: {sorted(extra)}")
        overall = "FAIL"

    missing = PACKET_IDENTITY_ALLOWED_KEYS - set(identity.keys())
    if missing:
        msgs.append(f"FAIL: PACKET_IDENTITY.yaml missing keys: {sorted(missing)}")
        overall = "FAIL"

    psv = identity.get("packet_schema_version")
    if psv is None or str(psv).strip() == "":
        msgs.append("schema_version_missing: packet_schema_version not set in PACKET_IDENTITY.yaml")
        if overall == "PASS":
            overall = "schema_version_missing"

    if psv is not None and str(psv) != PACKET_SCHEMA_VERSION_CURRENT:
        msgs.append(f"NOTE: packet_schema_version is {psv!r}; current taxonomy is {PACKET_SCHEMA_VERSION_CURRENT!r}")

    # Slug: .../reviews/<slug>/round_N
    parts = round_dir.parts
    try:
        ri = parts.index("reviews")
        slug_from_path = parts[ri + 1]
    except (ValueError, IndexError):
        slug_from_path = ""
    if identity.get("packet_slug") and slug_from_path and identity["packet_slug"] != slug_from_path:
        msgs.append(
            f"FAIL: packet_slug {identity.get('packet_slug')!r} != path slug {slug_from_path!r}",
        )
        overall = "FAIL"

    manifest_rel = identity.get("manifest_path")
    if manifest_rel:
        mp = (base_dir / manifest_rel).resolve()
        if not mp.exists():
            msgs.append(f"FAIL: manifest_path not found: {manifest_rel}")
            overall = "FAIL"

    if not status_path.exists():
        msgs.append("FAIL: PACKET_STATUS.yaml missing")
        overall = "FAIL"
    else:
        try:
            status = yaml.safe_load(status_path.read_text(encoding="utf-8")) or {}
        except Exception as e:
            msgs.append(f"FAIL: PACKET_STATUS.yaml unreadable: {e}")
            overall = "FAIL"
            status = {}
        extra = set(status.keys()) - PACKET_STATUS_REQUIRED_KEYS
        if extra:
            msgs.append(f"FAIL: PACKET_STATUS.yaml has disallowed keys: {sorted(extra)}")
            overall = "FAIL"
        sm = PACKET_STATUS_REQUIRED_KEYS - set(status.keys())
        if sm:
            msgs.append(f"FAIL: PACKET_STATUS.yaml missing keys: {sorted(sm)}")
            overall = "FAIL"
        if status.get("artifact_health") not in ARTIFACT_HEALTH:
            msgs.append(f"FAIL: artifact_health invalid: {status.get('artifact_health')!r}")
            overall = "FAIL"
        if status.get("review_gate_status") not in REVIEW_GATE:
            msgs.append(f"FAIL: review_gate_status invalid: {status.get('review_gate_status')!r}")
            overall = "FAIL"
        if status.get("committee_status") not in COMMITTEE:
            msgs.append(f"FAIL: committee_status invalid: {status.get('committee_status')!r}")
            overall = "FAIL"
        if status.get("next_action") not in NEXT_ACTION:
            msgs.append(f"FAIL: next_action invalid: {status.get('next_action')!r}")
            overall = "FAIL"
        if status.get("lifecycle_phase") not in LIFECYCLE:
            msgs.append(f"FAIL: lifecycle_phase invalid: {status.get('lifecycle_phase')!r}")
            overall = "FAIL"

        if identity.get("document_id") and status.get("document_id"):
            if identity["document_id"] != status["document_id"]:
                msgs.append("FAIL: document_id mismatch identity vs status")
                overall = "FAIL"
        if identity.get("packet_slug") and status.get("packet_slug"):
            if identity["packet_slug"] != status["packet_slug"]:
                msgs.append("FAIL: packet_slug mismatch identity vs status")
                overall = "FAIL"
        if identity.get("current_head_version") and status.get("current_head_version"):
            if str(identity["current_head_version"]) != str(status["current_head_version"]):
                msgs.append("FAIL: current_head_version mismatch identity vs status")
                overall = "FAIL"

        ch = _parse_version_tuple(str(status.get("current_head_version") or ""))
        lr = _parse_version_tuple(str(status.get("last_reviewed_version") or ""))
        if ch and lr and lr > ch:
            msgs.append("FAIL: last_reviewed_version is ahead of current_head_version (impossible)")
            overall = "FAIL"

    if not events_path.exists():
        msgs.append("FAIL: PACKET_EVENTS.yaml missing")
        overall = "FAIL"
    else:
        try:
            pe = yaml.safe_load(events_path.read_text(encoding="utf-8")) or {}
        except Exception as e:
            msgs.append(f"FAIL: PACKET_EVENTS.yaml unreadable: {e}")
            overall = "FAIL"
            pe = {}
        top_extra = set(pe.keys()) - PACKET_EVENTS_TOP_LEVEL_KEYS
        if top_extra:
            msgs.append(f"FAIL: PACKET_EVENTS.yaml has disallowed keys: {sorted(top_extra)}")
            overall = "FAIL"
        top_missing = PACKET_EVENTS_TOP_LEVEL_KEYS - set(pe.keys())
        if top_missing:
            msgs.append(f"FAIL: PACKET_EVENTS.yaml missing keys: {sorted(top_missing)}")
            overall = "FAIL"
        if pe.get("document_id") and identity.get("document_id"):
            if pe["document_id"] != identity["document_id"]:
                msgs.append("FAIL: document_id mismatch identity vs events header")
                overall = "FAIL"
        if pe.get("packet_slug") and identity.get("packet_slug"):
            if pe["packet_slug"] != identity["packet_slug"]:
                msgs.append("FAIL: packet_slug mismatch identity vs events header")
                overall = "FAIL"
        if pe.get("packet_schema_version") is None:
            msgs.append("FAIL: PACKET_EVENTS.yaml missing packet_schema_version")
            overall = "FAIL"
        elif str(pe.get("packet_schema_version")) != PACKET_SCHEMA_VERSION_CURRENT:
            msgs.append(
                f"FAIL: PACKET_EVENTS.yaml packet_schema_version {pe.get('packet_schema_version')!r} != {PACKET_SCHEMA_VERSION_CURRENT!r}"
            )
            overall = "FAIL"
        evs = pe.get("events")
        if not isinstance(evs, list):
            msgs.append("FAIL: PACKET_EVENTS.yaml events must be a list")
            overall = "FAIL"
        else:
            for i, ev in enumerate(evs):
                if not isinstance(ev, dict):
                    msgs.append(f"FAIL: events[{i}] not an object")
                    overall = "FAIL"
                    continue
                extra = set(ev.keys()) - PACKET_EVENT_REQUIRED_KEYS
                if extra:
                    msgs.append(f"FAIL: events[{i}] has disallowed keys: {sorted(extra)}")
                    overall = "FAIL"
                em = PACKET_EVENT_REQUIRED_KEYS - set(ev.keys())
                if em:
                    msgs.append(f"FAIL: events[{i}] missing keys: {sorted(em)}")
                    overall = "FAIL"
                et = ev.get("event_type")
                if et not in EVENT_TYPES:
                    msgs.append(f"FAIL: events[{i}] invalid event_type: {et!r}")
                    overall = "FAIL"
                summ = ev.get("summary") or ""
                if isinstance(summ, str) and summ.count("\n\n") > 0:
                    msgs.append(f"FAIL: events[{i}] summary must be one paragraph max")
                    overall = "FAIL"
                paths = ev.get("evidence_paths")
                if not isinstance(paths, list):
                    msgs.append(f"FAIL: events[{i}] evidence_paths must be a list")
                    overall = "FAIL"
                else:
                    for ep in paths:
                        if not isinstance(ep, str) or not ep.strip():
                            continue
                        ep_path = (base_dir / ep).resolve()
                        if not ep_path.exists():
                            msgs.append(f"FAIL: evidence path missing: {ep}")
                            overall = "FAIL"

    if not handoff_path.exists():
        msgs.append("FAIL: HANDOFF_NOTE.md missing")
        overall = "FAIL"
    else:
        try:
            handoff = handoff_path.read_text(encoding="utf-8")
        except Exception as e:
            msgs.append(f"FAIL: HANDOFF_NOTE.md unreadable: {e}")
            overall = "FAIL"
            handoff = ""
        if HANDOFF_AUTHORITY_LINE not in handoff:
            msgs.append("FAIL: HANDOFF_NOTE.md missing YAML precedence warning")
            overall = "FAIL"

    # Review files front matter
    for rf in sorted(round_dir.glob("review_*__*.md")):
        text = rf.read_text(encoding="utf-8", errors="replace")
        fm = _parse_front_matter(text)
        did = fm.get("document_id")
        if did and identity.get("document_id") and did != identity["document_id"]:
            msgs.append(f"FAIL: review {rf.name} document_id {did!r} != PACKET_IDENTITY document_id")
            overall = "FAIL"
        dr = fm.get("document_reviewed")
        dp = identity.get("document_path")
        if dr and dp and str(dr).replace("\\", "/") != str(dp).replace("\\", "/"):
            msgs.append(f"FAIL: review {rf.name} document_reviewed does not match identity document_path")
            overall = "FAIL"

    if overall == "legacy_packet_schema" and not any(m.startswith("FAIL:") for m in msgs):
        pass
    elif overall == "schema_version_missing" and not any(m.startswith("FAIL:") for m in msgs):
        pass

    return overall, msgs


def main() -> int:
    p = argparse.ArgumentParser(description="Validate review packet YAML taxonomy")
    p.add_argument(
        "--round-dir",
        required=True,
        help="Path to reviews/<slug>/round_N (folder containing PACKET_*.yaml)",
    )
    args = p.parse_args()
    round_dir = Path(args.round_dir).resolve()
    if not round_dir.is_dir():
        _err(f"Not a directory: {round_dir}")
        return 1

    overall, msgs = validate_round_dir(round_dir, BASE_DIR)
    for m in msgs:
        _err(m)
    _err(f"Result: {overall}")
    if any(m.startswith("FAIL:") for m in msgs):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

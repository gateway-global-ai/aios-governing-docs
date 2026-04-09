#!/usr/bin/env python3
"""
Thin CLI for the CANI writer / persistence service bridge.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import yaml

from cani_writer import (
    CaniWriterError,
    append_observation_event,
    append_recommendation_event,
    materialize_observation_set,
    materialize_recommendation_packet,
    update_recommendation_status,
)


def _load_structured(path: str) -> dict[str, Any]:
    file_path = Path(path)
    text = file_path.read_text(encoding="utf-8")
    if file_path.suffix.lower() == ".json":
        return json.loads(text)
    return yaml.safe_load(text) or {}


def _load_text(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Write governed CANI persisted artifacts")
    sub = parser.add_subparsers(dest="command", required=True)

    obs = sub.add_parser("materialize-observation", help="Create a new observation set")
    obs.add_argument("--target-dir", required=True)
    obs.add_argument("--identity", required=True, help="YAML/JSON file with observation identity")
    obs.add_argument("--event", required=True, help="YAML/JSON file with the first observation event")
    obs.add_argument("--handoff")

    obs_append = sub.add_parser("append-observation-event", help="Append an observation event")
    obs_append.add_argument("--target-dir", required=True)
    obs_append.add_argument("--event", required=True, help="YAML/JSON file with the event to append")

    rec = sub.add_parser("materialize-recommendation", help="Create a new recommendation packet")
    rec.add_argument("--target-dir", required=True)
    rec.add_argument("--identity", required=True)
    rec.add_argument("--status", required=True)
    rec.add_argument("--event", required=True)
    rec.add_argument("--handoff", required=True)

    rec_append = sub.add_parser("append-recommendation-event", help="Append a recommendation event")
    rec_append.add_argument("--target-dir", required=True)
    rec_append.add_argument("--event", required=True)

    rec_status = sub.add_parser("update-recommendation-status", help="Update recommendation current status")
    rec_status.add_argument("--target-dir", required=True)
    rec_status.add_argument("--status", required=True)

    args = parser.parse_args()
    try:
        if args.command == "materialize-observation":
            materialize_observation_set(
                args.target_dir,
                identity=_load_structured(args.identity),
                first_event=_load_structured(args.event),
                handoff_note=_load_text(args.handoff) if args.handoff else None,
            )
        elif args.command == "append-observation-event":
            append_observation_event(
                args.target_dir,
                event=_load_structured(args.event),
            )
        elif args.command == "materialize-recommendation":
            materialize_recommendation_packet(
                args.target_dir,
                identity=_load_structured(args.identity),
                status=_load_structured(args.status),
                first_event=_load_structured(args.event),
                handoff_note=_load_text(args.handoff),
            )
        elif args.command == "append-recommendation-event":
            append_recommendation_event(
                args.target_dir,
                event=_load_structured(args.event),
            )
        elif args.command == "update-recommendation-status":
            update_recommendation_status(
                args.target_dir,
                status=_load_structured(args.status),
            )
    except CaniWriterError as exc:
        print(f"WRITE REFUSED: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

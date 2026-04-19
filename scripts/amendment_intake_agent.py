#!/usr/bin/env python3
"""
CLI scaffold for governed amendment intake orchestration.

Stage 2 implementation:
  - read-only with respect to doctrine
  - explicit manual gate recording only
  - no substitute peer review
  - no silent ratification
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Callable

from intake_paths import resolve_intake_paths
from intake_phases import (
    PhaseResult,
    flag_author_revision,
    init_intake,
    mark_author_revision_complete,
    prepare_committee,
    prepare_kernel_review,
    prepare_ratification_handoff,
    record_committee_state,
    record_kernel_review,
    refresh_evidence,
    run_architect,
    run_peer_review,
    run_ui,
    validate_peer_review_packet,
    verify_architect,
    verify_ui,
)
from intake_runtime import IntakeRuntimeError, current_actor
from intake_state import load_events, load_handoff, load_identity, load_status

PHASE_ORDER = [
    "evidence",
    "architect",
    "ui",
    "committee",
    "author_revision",
    "peer_review",
    "validate_packet",
    "kernel",
    "ratification_handoff",
]


def _default_round(status: dict) -> int:
    if str(status.get("next_action") or "") == "run_peer_review_round_2":
        return 2
    return 1


def _result_to_json(result: PhaseResult) -> str:
    return json.dumps(
        {
            "phase": result.phase,
            "dry_run": result.dry_run,
            "changed_paths": result.changed_paths,
            "message": result.message,
            "status": result.status,
        },
        indent=2,
    )


def _print_status(paths) -> int:
    identity = load_identity(paths)
    status = load_status(paths)
    events = load_events(paths)
    handoff = load_handoff(paths)
    print(
        json.dumps(
            {
                "document_id": paths.document_id,
                "document_path": paths.document_path,
                "amendment_slug": paths.amendment_slug,
                "paths": {
                    "intake": paths.intake_dir.relative_to(paths.base_dir).as_posix(),
                    "planning": paths.planning_dir.relative_to(paths.base_dir).as_posix(),
                    "kernel": paths.kernel_dir.relative_to(paths.base_dir).as_posix(),
                    "ratification": paths.ratification_dir.relative_to(paths.base_dir).as_posix(),
                },
                "initialized": bool(identity and status and events and handoff),
                "identity": identity,
                "status": status,
                "events_count": len(events.get("events", [])) if events else 0,
            },
            indent=2,
        )
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Governed amendment intake scaffold")
    parser.add_argument("document", help="Path to amendment file relative to repo root")
    parser.add_argument("--status", action="store_true", help="Show intake status and paths")
    parser.add_argument("--init", action="store_true", help="Initialize intake artifacts")
    parser.add_argument("--phase", choices=PHASE_ORDER, help="Run one orchestration phase")
    parser.add_argument("--through", choices=PHASE_ORDER, help="Run phases in order through the named phase")
    parser.add_argument("--dry-run", action="store_true", help="Plan commands and writes without executing them")
    parser.add_argument("--architect-verified", action="store_true", help="Record architect verification")
    parser.add_argument("--ui-verified", action="store_true", help="Record UI verification")
    parser.add_argument("--committee-approved", action="store_true", help="Record committee approved")
    parser.add_argument(
        "--committee-approved-with-changes",
        action="store_true",
        help="Record committee approved with changes",
    )
    parser.add_argument(
        "--committee-superseded-by-review",
        action="store_true",
        help="Record committee closed as superseded by review",
    )
    parser.add_argument("--author-revision-complete", action="store_true", help="Record author revision completion")
    parser.add_argument("--kernel-skipped", action="store_true", help="Record advisory kernel review skipped")
    parser.add_argument("--kernel-complete", action="store_true", help="Record advisory kernel review complete")
    parser.add_argument(
        "--prepare-ratification-handoff",
        action="store_true",
        help="Prepare non-doctrine ratification handoff artifacts",
    )
    parser.add_argument("--actor", help="Human/operator identity for recorded actions")
    parser.add_argument("--architect-bundle", help="Override architect KB bundle path; audited in intake events")
    parser.add_argument("--architect-manifest", help="Override architect KB manifest path; audited in intake events")
    parser.add_argument("--committee-note", default="", help="Required note for committee state changes")
    parser.add_argument("--kernel-skip-reason", default="", help="Required reason when kernel review is skipped")
    parser.add_argument("--round", type=int, choices=[1, 2], help="Peer review round override")
    args = parser.parse_args()

    try:
        paths = resolve_intake_paths(args.document)
        if args.status:
            return _print_status(paths)

        actor = current_actor(args.actor)
        if args.architect_bundle or args.architect_manifest:
            if not (args.phase == "architect" or args.through == "architect"):
                raise IntakeRuntimeError(
                    "--architect-bundle and --architect-manifest are only allowed with --phase architect or --through architect."
                )

        results: list[PhaseResult] = []
        if args.init:
            results.append(init_intake(paths, actor=actor, dry_run=args.dry_run))

        manual_flags = [
            args.architect_verified,
            args.ui_verified,
            args.committee_approved,
            args.committee_approved_with_changes,
            args.committee_superseded_by_review,
            args.author_revision_complete,
            args.kernel_skipped,
            args.kernel_complete,
            args.prepare_ratification_handoff,
        ]
        if sum(1 for x in manual_flags if x) > 1:
            raise IntakeRuntimeError("Use only one manual gate flag at a time.")

        if args.architect_verified:
            results.append(verify_architect(paths, actor=actor, dry_run=args.dry_run))
        elif args.ui_verified:
            results.append(verify_ui(paths, actor=actor, dry_run=args.dry_run))
        elif args.committee_approved:
            if not args.committee_note.strip():
                raise IntakeRuntimeError("--committee-note is required when recording committee state.")
            results.append(
                record_committee_state(
                    paths,
                    actor=actor,
                    committee_status="approved",
                    note=args.committee_note,
                    dry_run=args.dry_run,
                )
            )
        elif args.committee_approved_with_changes:
            if not args.committee_note.strip():
                raise IntakeRuntimeError("--committee-note is required when recording committee state.")
            results.append(
                record_committee_state(
                    paths,
                    actor=actor,
                    committee_status="approved_with_changes",
                    note=args.committee_note,
                    dry_run=args.dry_run,
                )
            )
        elif args.committee_superseded_by_review:
            if not args.committee_note.strip():
                raise IntakeRuntimeError("--committee-note is required when recording committee state.")
            results.append(
                record_committee_state(
                    paths,
                    actor=actor,
                    committee_status="closed_superseded_by_review",
                    note=args.committee_note,
                    dry_run=args.dry_run,
                )
            )
        elif args.author_revision_complete:
            status = load_status(paths)
            if not status:
                raise IntakeRuntimeError("Intake must be initialized before author revision completion is recorded.")
            results.append(
                mark_author_revision_complete(
                    paths,
                    actor=actor,
                    dry_run=args.dry_run,
                    round_number=args.round or _default_round(status),
                )
            )
        elif args.kernel_skipped:
            results.append(
                record_kernel_review(
                    paths,
                    actor=actor,
                    completed=False,
                    skipped=True,
                    skip_reason=args.kernel_skip_reason,
                    dry_run=args.dry_run,
                )
            )
        elif args.kernel_complete:
            results.append(
                record_kernel_review(
                    paths,
                    actor=actor,
                    completed=True,
                    skipped=False,
                    skip_reason="",
                    dry_run=args.dry_run,
                )
            )
        elif args.prepare_ratification_handoff:
            results.append(prepare_ratification_handoff(paths, actor=actor, dry_run=args.dry_run))

        phase_map: dict[str, Callable[[], PhaseResult]] = {
            "evidence": lambda: refresh_evidence(paths, actor=actor, dry_run=args.dry_run),
            "architect": lambda: run_architect(
                paths,
                actor=actor,
                dry_run=args.dry_run,
                bundle_override=args.architect_bundle,
                manifest_override=args.architect_manifest,
            ),
            "ui": lambda: run_ui(paths, actor=actor, dry_run=args.dry_run),
            "committee": lambda: prepare_committee(paths, actor=actor, dry_run=args.dry_run),
            "author_revision": lambda: flag_author_revision(paths, actor=actor, dry_run=args.dry_run),
            "peer_review": lambda: run_peer_review(
                paths,
                actor=actor,
                round_number=args.round or _default_round(load_status(paths)),
                dry_run=args.dry_run,
            ),
            "validate_packet": lambda: validate_peer_review_packet(
                paths,
                actor=actor,
                round_number=args.round or _default_round(load_status(paths)),
                dry_run=args.dry_run,
            ),
            "kernel": lambda: prepare_kernel_review(paths, actor=actor, dry_run=args.dry_run),
            "ratification_handoff": lambda: prepare_ratification_handoff(paths, actor=actor, dry_run=args.dry_run),
        }

        if args.phase:
            results.append(phase_map[args.phase]())

        if args.through:
            for phase in PHASE_ORDER:
                results.append(phase_map[phase]())
                if phase == args.through:
                    break

        if not results:
            raise IntakeRuntimeError("No action requested. Use --status, --init, --phase, --through, or a manual gate flag.")

        for result in results:
            print(_result_to_json(result))
        return 0

    except (FileNotFoundError, IntakeRuntimeError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())


#!/usr/bin/env python3
"""
Ratification handoff preparation for the amendment intake scaffold.

Stage 2 prepares handoff artifacts only. It does not ratify doctrine.
"""

from __future__ import annotations

from intake_paths import IntakePaths
from intake_templates import ensure_ratification_handoff


def prepare_ratification_artifacts(paths: IntakePaths) -> list[str]:
    return ensure_ratification_handoff(paths)


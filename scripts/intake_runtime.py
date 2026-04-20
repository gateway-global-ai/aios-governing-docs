#!/usr/bin/env python3
"""
Runtime helpers for the amendment intake scaffold.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

from intake_paths import BASE_DIR


class IntakeRuntimeError(RuntimeError):
    """Raised when a subprocess or runtime precondition fails."""


@dataclass(frozen=True)
class CommandResult:
    command: list[str]
    returncode: int
    stdout: str
    stderr: str


def current_actor(explicit: str | None = None) -> str:
    actor = explicit or os.environ.get("AIOS_INTAKE_ACTOR") or os.environ.get("USERNAME") or os.environ.get("USER")
    if not actor:
        raise IntakeRuntimeError("Actor identity is required. Pass --actor or set AIOS_INTAKE_ACTOR.")
    return actor


def ensure_exists(path: Path, *, kind: str = "path") -> None:
    if not path.exists():
        raise IntakeRuntimeError(f"Required {kind} missing: {path}")


def ensure_executable_on_path(name: str) -> str:
    exe = shutil.which(name)
    if not exe:
        raise IntakeRuntimeError(f"Required executable not found on PATH: {name}")
    return exe


def env_has_peer_review_credentials() -> bool:
    return bool(
        os.environ.get("OPENAI_API_KEY")
        and os.environ.get("GEMINI_API_KEY")
        and os.environ.get("DEEPSEEK_API_KEY")
    )


def run_command(
    args: Sequence[str],
    *,
    cwd: Path | None = None,
    dry_run: bool = False,
    env: dict[str, str] | None = None,
) -> CommandResult:
    cmd = [str(a) for a in args]
    workdir = cwd or BASE_DIR
    if dry_run:
        return CommandResult(command=cmd, returncode=0, stdout="[dry-run]", stderr="")

    completed = subprocess.run(
        cmd,
        cwd=str(workdir),
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )
    result = CommandResult(
        command=cmd,
        returncode=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
    )
    if completed.returncode != 0:
        raise IntakeRuntimeError(
            "Command failed with non-zero exit code:\n"
            + json.dumps(
                {
                    "command": result.command,
                    "returncode": result.returncode,
                    "stdout": result.stdout[-4000:],
                    "stderr": result.stderr[-4000:],
                },
                indent=2,
            )
        )
    return result


def python_command(*args: str) -> list[str]:
    return ["py", "-3", *args]


#!/usr/bin/env python3
"""
Preflight for local Ollama-based planning agents (Architect / UI).

Reports explicit status: not installed, installed, reachable, model present,
smoke-tested (optional), operational.

Usage (repo root):
  py -3 scripts/preflight_local_agents.py
  py -3 scripts/preflight_local_agents.py --smoke

Env: OLLAMA_HOST (default http://127.0.0.1:11434), OLLAMA_MODEL (default llama3.2)
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from pathlib import Path

import httpx

SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR.parent


def main() -> None:
    parser = argparse.ArgumentParser(description="Ollama local agent preflight")
    parser.add_argument(
        "--smoke",
        action="store_true",
        help="POST /api/chat with a one-token style prompt (adds latency)",
    )
    args = parser.parse_args()

    host = os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434")
    model = os.environ.get("OLLAMA_MODEL", "llama3.2")
    exe = shutil.which("ollama")

    lines: list[str] = []
    status = "not_installed"
    if exe:
        lines.append(f"ollama executable: {exe}")
        status = "installed"
    else:
        lines.append("ollama executable: NOT FOUND on PATH")

    reachable = False
    tags_models: list[str] = []
    try:
        with httpx.Client(timeout=8.0) as client:
            r = client.get(f"{host.rstrip('/')}/api/tags")
            reachable = r.status_code == 200
            if reachable:
                data = r.json()
                tags_models = [m.get("name", "") for m in data.get("models") or []]
                status = "reachable"
    except (httpx.HTTPError, OSError) as e:
        lines.append(f"HTTP reachability: FAIL ({e})")

    model_ok = False
    if reachable:
        lines.append(f"OLLAMA_HOST: {host} OK")
        lines.append(f"Models on host: {tags_models or '(none)'}")
        base = model.split(":")[0]
        model_ok = any(
            m == model or m.startswith(base + ":") or m == base for m in tags_models if m
        )
        if model_ok:
            status = "model_present"
            lines.append(f"Desired model '{model}': present")
        else:
            lines.append(f"Desired model '{model}': NOT pulled — run: ollama pull {base}")

    smoke_ok: bool | None = None
    if args.smoke and reachable:
        try:
            with httpx.Client(timeout=120.0) as client:
                r = client.post(
                    f"{host.rstrip('/')}/api/chat",
                    json={
                        "model": model,
                        "messages": [
                            {"role": "user", "content": "Reply with exactly: OK"},
                        ],
                        "stream": False,
                    },
                )
                r.raise_for_status()
                msg = (r.json().get("message") or {}).get("content") or ""
                smoke_ok = "OK" in msg or len(msg) < 200
                lines.append(f"Smoke chat: {'OK' if smoke_ok else 'unexpected output'}")
                status = "smoke_tested" if smoke_ok else "smoke_failed"
        except (httpx.HTTPError, OSError) as e:
            lines.append(f"Smoke chat: FAIL ({e})")
            smoke_ok = False
            status = "smoke_failed"

    # The planning and authoring runners call Ollama over HTTP. A local
    # executable on PATH is helpful for manual pull/debug workflows, but it is
    # not required when the host is reachable and already serves the requested
    # model.
    if reachable and model_ok:
        if args.smoke:
            if smoke_ok:
                status = "operational"
        else:
            status = "operational"

    out = {
        "status": status,
        "ollama_host": host,
        "ollama_model": model,
        "lines": lines,
    }
    print(json.dumps(out, indent=2))
    if status == "smoke_failed":
        sys.exit(2)
    if status not in ("operational",):
        sys.exit(1)


if __name__ == "__main__":
    main()

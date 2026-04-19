#!/usr/bin/env python3
"""
Run the bounded JT governed authoring agent through local Ollama.

This runner is intentionally narrower than freeform chat:
  - mode is explicit
  - manifest is explicit
  - required documents are loaded from governed repo paths
  - optional includes must be declared by the manifest
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import httpx
import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR.parent

DEFAULT_MODEL = "jt_authoring_agent"
DEFAULT_MANIFESTS = {
    "editorial": BASE_DIR / "reference/knowledge_base/agents/style/JT_EDITORIAL_REQUIRED_KNOWLEDGE_MANIFEST.yaml",
    "technical": BASE_DIR / "reference/knowledge_base/agents/style/JT_EDITORIAL_REQUIRED_KNOWLEDGE_MANIFEST.yaml",
    "narration": BASE_DIR / "reference/knowledge_base/agents/style/JT_NARRATION_REQUIRED_KNOWLEDGE_MANIFEST.yaml",
    "book": BASE_DIR / "reference/knowledge_base/agents/style/JT_NARRATION_REQUIRED_KNOWLEDGE_MANIFEST.yaml",
}

MODE_MANIFEST_FAMILY = {
    "editorial": "editorial",
    "technical": "editorial",
    "narration": "narration",
    "book": "narration",
}

MODE_INSTRUCTIONS = {
    "editorial": "Write in governed editorial mode: thesis-first, contrast-driven, strategic, and readable.",
    "narration": "Write in governed narration mode: connective, explanatory, and continuity-driven.",
    "technical": "Write in governed technical mode: precise, readable, and operator-useful with reduced flourish.",
    "book": "Write in governed book mode: long-form continuity, worldview-building structure, and strong transitions.",
}

MODE_OUTPUT_CONTRACTS = {
    "editorial": [
        "Lead with the main claim instead of scene-setting.",
        "Use short emphatic paragraphs, not bullet summaries, unless the task asks for bullets.",
        "Turn abstract ideas into concrete software, governance, or business consequence.",
        "Do not enumerate the source documents unless the task asks for a source summary.",
    ],
    "narration": [
        "Open with a smooth framing line, then build continuity across the piece.",
        "Use flowing prose paragraphs rather than bullet summaries unless the task asks for bullets.",
        "Carry one clear thread from tension to implication.",
        "Do not enumerate the source documents unless the task asks for a source summary.",
    ],
    "technical": [
        "Stay precise and readable.",
        "Favor clean explanation over flourish.",
        "Do not enumerate the source documents unless the task asks for a source summary.",
    ],
    "book": [
        "Use flowing long-form prose with strong transitions.",
        "Accumulate a worldview rather than producing isolated points.",
        "Do not enumerate the source documents unless the task asks for a source summary.",
    ],
}


def _resolve_repo_path(path: str | Path) -> Path:
    candidate = Path(path)
    if not candidate.is_absolute():
        candidate = (BASE_DIR / str(candidate).replace("\\", "/")).resolve()
    else:
        candidate = candidate.resolve()
    try:
        candidate.relative_to(BASE_DIR.resolve())
    except ValueError as exc:
        raise ValueError(f"Path is outside repo root: {path}") from exc
    return candidate


def _repo_rel(path: Path) -> str:
    return path.resolve().relative_to(BASE_DIR.resolve()).as_posix()


def _read_manifest(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(f"Manifest not found: {path}")
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise ValueError(f"Manifest must be a YAML object: {path}")
    return data


def _read_text(path: Path) -> str:
    if not path.is_file():
        raise FileNotFoundError(f"Required input missing: {path}")
    return path.read_text(encoding="utf-8", errors="replace")


def _validate_manifest_mode(mode: str, manifest_path: Path, manifest: dict[str, Any]) -> None:
    declared_mode = str(manifest.get("mode") or "").strip()
    expected_family = MODE_MANIFEST_FAMILY[mode]
    if declared_mode != expected_family:
        raise ValueError(
            "Manifest mode mismatch: "
            f"selected mode {mode!r} requires manifest family {expected_family!r}, "
            f"but { _repo_rel(manifest_path) } declares mode {declared_mode!r}"
        )


def _load_context_from_manifest(
    mode: str, manifest_path: Path, requested_includes: list[str]
) -> tuple[dict[str, Any], list[tuple[str, str]]]:
    manifest = _read_manifest(manifest_path)
    _validate_manifest_mode(mode=mode, manifest_path=manifest_path, manifest=manifest)
    required = [str(p) for p in manifest.get("required_documents") or []]
    optional = [str(p) for p in manifest.get("allowed_optional_documents") or []]
    style_cards = [str(p) for p in manifest.get("style_cards") or []]
    boundaries = [str(p) for p in manifest.get("boundaries") or []]
    allowed_requested = {p.replace("\\", "/") for p in optional}

    for inc in requested_includes:
        normalized = inc.replace("\\", "/")
        if normalized not in allowed_requested:
            raise ValueError(f"Optional include not declared by manifest: {inc}")

    load_list: list[str] = []
    for path in [*style_cards, *boundaries, *required]:
        normalized = path.replace("\\", "/")
        if normalized not in load_list:
            load_list.append(normalized)
    for path in requested_includes:
        normalized = path.replace("\\", "/")
        if normalized not in load_list:
            load_list.append(normalized)

    docs: list[tuple[str, str]] = []
    for rel in load_list:
        docs.append((rel, _read_text(_resolve_repo_path(rel))))
    return manifest, docs


def _build_system_prompt(mode: str, manifest_path: Path, manifest: dict[str, Any]) -> str:
    label = str(manifest.get("label") or "unnamed_manifest")
    prohibited = ", ".join(str(x) for x in manifest.get("prohibited_source_classes") or [])
    output_contract = "\n".join(f"- {line}" for line in MODE_OUTPUT_CONTRACTS[mode])
    return (
        "You are running as the JT governed authoring agent.\n\n"
        f"Mode: {mode}\n"
        f"Mode instruction: {MODE_INSTRUCTIONS[mode]}\n"
        f"Manifest: {_repo_rel(manifest_path)}\n"
        f"Manifest label: {label}\n"
        "Hard rules:\n"
        "- Use only the declared repository documents provided in this run.\n"
        "- Repo truth overrides stylistic preference.\n"
        "- Do not invent personal memory, private discussions, or unpublished decisions.\n"
        "- Do not claim governance authority or ratification authority.\n"
        "- Do not use prohibited source classes.\n"
        f"- Prohibited source classes: {prohibited or 'none declared'}\n"
        "Output contract:\n"
        f"{output_contract}\n"
        "- Write the requested artifact itself rather than recapping the repository packet.\n"
    )


def _build_user_prompt(mode: str, prompt: str, docs: list[tuple[str, str]]) -> str:
    parts = ["## Declared repository inputs"]
    for rel, text in docs:
        parts.append(f"\n### Source: `{rel}`\n\n{text}")
    parts.extend(
        [
            "## Writing assignment",
            f"Task: {prompt}",
            f"Mode: {mode}",
            "Response rules:",
            "- Use the repository inputs only for grounding.",
            "- Do not summarize or inventory the source set unless the task explicitly asks for a summary.",
            "- Write the requested prose directly.",
            "- Do not add headings, bullets, or notes unless the task asks for them.",
            "- If support is missing, stay conditional rather than inventing facts.",
            "## Response",
            "Write the requested prose now.",
        ]
    )
    return "\n\n".join(parts)


def _default_run_record_path(mode: str, output_path: Path | None) -> Path:
    if output_path is not None:
        return output_path.with_suffix(output_path.suffix + ".run_record.json")
    timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    return (
        BASE_DIR
        / "reference"
        / "knowledge_base"
        / "agents"
        / "run_records"
        / f"{timestamp}__{mode}.run_record.json"
    )


def _write_run_record(
    *,
    mode: str,
    manifest_path: Path,
    requested_includes: list[str],
    output_path: Path | None,
    run_record_path: Path,
    model: str,
    host: str,
) -> None:
    payload = {
        "mode": mode,
        "recorded_at": datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "manifest_path": _repo_rel(manifest_path),
        "optional_include_paths": [inc.replace("\\", "/") for inc in requested_includes],
        "tool_invocation_identity": "scripts/ollama_authoring_agent.py",
        "output_path": _repo_rel(output_path) if output_path else None,
        "run_record_path": _repo_rel(run_record_path),
        "model": model,
        "ollama_host": host,
    }
    run_record_path.parent.mkdir(parents=True, exist_ok=True)
    run_record_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def _call_ollama(host: str, model: str, system: str, user: str, timeout: float = 600.0) -> str:
    with httpx.Client(timeout=timeout) as client:
        response = client.post(
            f"{host.rstrip('/')}/api/chat",
            json={
                "model": model,
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
                "stream": False,
            },
        )
        response.raise_for_status()
        data = response.json()
    message = data.get("message") or {}
    return message.get("content") or data.get("response") or str(data)


def _write_stdout(text: str) -> None:
    payload = text.strip() + "\n"
    try:
        sys.stdout.write(payload)
    except UnicodeEncodeError:
        encoding = sys.stdout.encoding or "utf-8"
        sys.stdout.buffer.write(payload.encode(encoding, errors="replace"))
        sys.stdout.buffer.flush()


def main() -> int:
    parser = argparse.ArgumentParser(description="Governed JT authoring agent")
    parser.add_argument("--mode", choices=sorted(MODE_INSTRUCTIONS.keys()), required=True)
    parser.add_argument("--prompt", required=True, help="Writing instruction for the run")
    parser.add_argument("--manifest", type=Path, help="Override manifest path inside repo")
    parser.add_argument(
        "--include",
        action="append",
        default=[],
        help="Optional extra repo-relative input declared under allowed_optional_documents",
    )
    parser.add_argument("--output", type=Path, help="Optional repo-relative output file")
    parser.add_argument("--run-record", type=Path, help="Optional repo-relative run-record output path")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--dry-run", action="store_true", help="Print selected inputs and prompt sizes only")
    args = parser.parse_args()

    host = os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434")
    manifest_path = _resolve_repo_path(args.manifest or DEFAULT_MANIFESTS[args.mode])
    output_path = _resolve_repo_path(args.output) if args.output else None
    run_record_path = _resolve_repo_path(args.run_record) if args.run_record else _default_run_record_path(args.mode, output_path)
    manifest, docs = _load_context_from_manifest(args.mode, manifest_path, args.include)
    system = _build_system_prompt(args.mode, manifest_path, manifest)
    user = _build_user_prompt(args.mode, args.prompt, docs)

    print(f"Mode: {args.mode}")
    print(f"Manifest: {_repo_rel(manifest_path)}")
    print(f"Inputs loaded: {len(docs)}")
    print(f"Run record: {_repo_rel(run_record_path)}")
    print(f"System prompt chars: {len(system):,}")
    print(f"User prompt chars: {len(user):,}")

    if args.dry_run:
        print("Dry run: not calling Ollama.")
        return 0

    text = _call_ollama(host, args.model, system, user)
    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(text.strip() + "\n", encoding="utf-8")
        print(f"Wrote {_repo_rel(output_path)}")
    else:
        _write_stdout(text)
    _write_run_record(
        mode=args.mode,
        manifest_path=manifest_path,
        requested_includes=args.include,
        output_path=output_path,
        run_record_path=run_record_path,
        model=args.model,
        host=host,
    )
    print(f"Wrote {_repo_rel(run_record_path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

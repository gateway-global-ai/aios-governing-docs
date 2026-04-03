"""
AIOS Governance System -- Interactive CLI

Single entry point for all governance operations.
Run from anywhere -- the script locates the governing_docs root automatically.

Usage:
    py C:\\Apps\\governing_docs\\scripts\\govern.py
"""

import asyncio
import io
import json
import os
import sys
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
os.chdir(SCRIPT_DIR.parent)

from context_assembler import BASE_DIR, read_file, parse_front_matter

BANNER = """
    +----------------------------------------------------------+
    |           AIOS Governance System  v1.0                    |
    |           Gateway Global -- Document Authority            |
    +----------------------------------------------------------+
"""

MAIN_MENU = """
    What would you like to do?

    -- Documents -----------------------------------------------
     1.  Create a new document
     2.  Run full lifecycle (5-stage: draft > review > ratify)
     3.  Run quick lifecycle (3-stage: draft > review > ratify)
     4.  Peer review an existing document
     5.  Revise a document from review feedback

    -- Analysis & Quality --------------------------------------
     6.  Analyze external source material
     7.  Check source quarantine status
     8.  Run cross-document conflict scan

    -- Registry & Schemas --------------------------------------
     9.  Regenerate the document registry
    10.  Extract / refresh JSON schemas from specs
    11.  List all documents in the registry
    12.  List available primitive schemas

    -- Servers -------------------------------------------------
    13.  Start the MCP server (for AI agents / Cursor)
    14.  Start the REST API (Swagger at localhost:8100/docs)

    -- Compliance ----------------------------------------------
    15.  Validate a primitive (NodeContract / PolicyRecord)
    16.  Validate a Kit manifest

     0.  Exit
"""


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\n    Press Enter to continue...")


def ask(prompt: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    result = input(f"    {prompt}{suffix}: ").strip()
    return result if result else default


def ask_choice(prompt: str, options: list[str]) -> str:
    print(f"\n    {prompt}")
    for i, opt in enumerate(options, 1):
        print(f"      {i}. {opt}")
    while True:
        choice = input(f"    Choice [1-{len(options)}]: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        print(f"    Please enter a number between 1 and {len(options)}.")


def pick_document() -> str | None:
    """Let the user pick a document from the registry."""
    registry_path = BASE_DIR / "DOCUMENT_REGISTRY.json"
    if not registry_path.exists():
        print("\n    Registry not found. Generating...")
        from registry_generator import main as regen
        regen()

    docs = json.loads(registry_path.read_text(encoding="utf-8"))
    if not docs:
        print("\n    No documents found in registry.")
        return None

    print("\n    Available documents:\n")
    for i, doc in enumerate(docs, 1):
        status = doc.get("status", "?")
        title = doc.get("title", doc.get("_path", "Unknown"))
        doc_id = doc.get("document_id", "")
        print(f"      {i:>2}. [{status:>12}]  {title}  ({doc_id})")

    print(f"\n      Or type a path directly (e.g., core/technical_manifesto.md)")

    while True:
        choice = input("\n    Select document: ").strip()
        if not choice:
            return None
        if choice.isdigit() and 1 <= int(choice) <= len(docs):
            return docs[int(choice) - 1].get("_path")
        if "/" in choice or "\\" in choice:
            if (BASE_DIR / choice).exists():
                return choice
            print(f"    File not found: {choice}")
        else:
            print(f"    Enter a number (1-{len(docs)}) or a file path.")


# ── Actions ───────────────────────────────────────────────────────

def action_create_document():
    print("\n    ── Create New Document ──\n")
    title = ask("Document title")
    if not title:
        print("    Cancelled.")
        return

    category = ask_choice("Category:", ["core", "specification", "commercial", "amendment", "reference"])
    description = ask("Brief description of the document's purpose")
    audience = ask("Target audience (optional)", "")

    print(f"\n    Creating: {title} ({category})")
    print(f"    Description: {description}")
    confirm = ask("Proceed? [Y/n]", "Y")
    if confirm.lower() not in ("y", "yes", ""):
        print("    Cancelled.")
        return

    from lifecycle import run_lifecycle
    asyncio.run(run_lifecycle(
        None,
        create_args={"title": title, "category": category, "description": description, "audience": audience},
    ))


def action_full_lifecycle():
    print("\n    ── Full Lifecycle (5-stage) ──\n")
    doc_path = pick_document()
    if not doc_path:
        return
    auto = ask("Run without stage confirmations? [y/N]", "N").lower() in ("y", "yes")

    from lifecycle import run_lifecycle
    asyncio.run(run_lifecycle(doc_path, auto=auto, quick=False))


def action_quick_lifecycle():
    print("\n    ── Quick Lifecycle (3-stage) ──\n")
    doc_path = pick_document()
    if not doc_path:
        return
    auto = ask("Run without stage confirmations? [y/N]", "N").lower() in ("y", "yes")

    from lifecycle import run_lifecycle
    asyncio.run(run_lifecycle(doc_path, auto=auto, quick=True))


def action_peer_review():
    print("\n    ── Peer Review ──\n")
    doc_path = pick_document()
    if not doc_path:
        return

    round_num = int(ask_choice("Review round:", ["1", "2"]))
    rubric = ask_choice("Rubric:", ["full (11 dimensions)", "light (5 dimensions)"])
    rubric_key = "light" if "light" in rubric else "full"
    smart = ask("Use smart context (only cross-referenced docs)? [y/N]", "N").lower() in ("y", "yes")

    from peer_review import run_review
    asyncio.run(run_review(doc_path, review_round=round_num, rubric_override=rubric_key, smart_context=smart))


def action_revise():
    print("\n    ── Revise Document ──\n")
    doc_path = pick_document()
    if not doc_path:
        return

    from revise_document import run_revision
    asyncio.run(run_revision(doc_path))


def action_analyze_source():
    print("\n    ── Analyze External Source Material ──\n")
    source_path = ask("Path to source file (.md)")
    if not source_path:
        return
    name = ask("Name for this analysis (used as folder name)")
    if not name:
        return

    from analyze_source import run_analysis
    asyncio.run(run_analysis(source_path, name))


def action_source_status():
    print("\n    ── Source Quarantine Status ──\n")
    name = ask("Source name")
    if not name:
        return

    quarantine_path = BASE_DIR / "sources" / name / "quarantine.json"
    if not quarantine_path.exists():
        print(f"\n    No quarantine record found for '{name}'.")
        print("\n    Known sources:")
        sources_dir = BASE_DIR / "sources"
        if sources_dir.exists():
            for d in sorted(sources_dir.iterdir()):
                if d.is_dir() and (d / "quarantine.json").exists():
                    q = json.loads((d / "quarantine.json").read_text(encoding="utf-8"))
                    print(f"      - {d.name}  [{q.get('status', '?')}]")
        return

    data = json.loads(quarantine_path.read_text(encoding="utf-8"))
    print(f"\n    Source: {name}")
    print(f"    Status: {data.get('status', '?')}")
    print(f"    Submitted: {data.get('submitted', '?')}")
    print(f"    Hash: {data.get('source_hash', '?')}")
    if data.get("cleared_at"):
        print(f"    Cleared at: {data['cleared_at']}")
        print(f"    Cleared by: {data.get('cleared_by', '?')}")

    if data.get("status") == "analyzed":
        action = ask_choice("\n    Action:", ["Clear for use", "Reject", "Do nothing"])
        if action == "Clear for use":
            from analyze_source import _update_quarantine_status
            _update_quarantine_status(name, "cleared")
        elif action == "Reject":
            from analyze_source import _update_quarantine_status
            _update_quarantine_status(name, "rejected")


def action_conflict_scan():
    print("\n    ── Cross-Document Conflict Scan ──\n")
    scope = ask_choice("Scope:", ["All documents", "Single document"])
    doc_id = None
    if scope == "Single document":
        doc_id = ask("Document ID (e.g., AIOS-CORE-001)")
    fmt = ask_choice("Output format:", ["text", "json"])

    from conflict_detector import run_conflict_scan
    result = run_conflict_scan(doc_id)

    if fmt == "json":
        print(json.dumps(result, indent=2))
    else:
        print(f"\n    Documents scanned: {result['documents_scanned']}")
        print(f"    Findings: {result['findings_count']}")
        if not result["findings"]:
            print("\n    No conflicts detected.")
        else:
            for f in result["findings"]:
                print(f"\n    [{f['severity'].upper()}] {f['type']}")
                print(f"      {f['message']}")
                if "occurrences" in f:
                    for occ in f["occurrences"]:
                        print(f"        - {occ['document_id']} (line {occ.get('line', '?')})")


def action_regen_registry():
    print("\n    ── Regenerate Document Registry ──\n")
    from registry_generator import main as regen
    regen()
    print("\n    Done.")


def action_extract_schemas():
    print("\n    ── Extract JSON Schemas ──\n")
    from schema_extractor import main as extract
    sys.argv = ["schema_extractor.py"]
    extract()
    print("\n    Done.")


def action_list_documents():
    print("\n    ── Document Registry ──\n")
    registry_path = BASE_DIR / "DOCUMENT_REGISTRY.json"
    if not registry_path.exists():
        print("    Registry not found. Run option 9 first.")
        return

    docs = json.loads(registry_path.read_text(encoding="utf-8"))
    print(f"    {'ID':<16} {'Status':<14} {'Category':<14} Title")
    print(f"    {'─'*16} {'─'*14} {'─'*14} {'─'*30}")
    for doc in docs:
        doc_id = doc.get("document_id", "—")[:16]
        status = doc.get("status", "—")[:14]
        cat = doc.get("category", "—")[:14]
        title = doc.get("title", doc.get("_path", "?"))
        print(f"    {doc_id:<16} {status:<14} {cat:<14} {title}")
    print(f"\n    Total: {len(docs)} documents")


def action_list_schemas():
    print("\n    ── Available Primitive Schemas ──\n")
    from schema_extractor import list_available_schemas
    names = list_available_schemas()
    if not names:
        print("    No schemas found. Run option 10 first.")
        return
    for n in names:
        print(f"      - {n}")
    print(f"\n    Total: {len(names)} schemas")


def action_start_mcp():
    print("\n    ── Starting MCP Server ──\n")
    print("    The MCP server will start in this terminal.")
    print("    Press Ctrl+C to stop.\n")
    import subprocess
    subprocess.run([sys.executable, str(Path(__file__).parent / "governance_mcp_server.py")])


def action_start_api():
    print("\n    ── Starting REST API Server ──\n")
    print("    Swagger UI: http://localhost:8100/docs")
    print("    Press Ctrl+C to stop.\n")
    import subprocess
    subprocess.run([sys.executable, str(Path(__file__).parent / "governance_api.py")])


def action_validate_primitive():
    print("\n    ── Validate Primitive ──\n")
    from schema_extractor import list_available_schemas
    names = list_available_schemas()
    if not names:
        print("    No schemas found. Run option 10 first.")
        return

    ptype = ask_choice("Primitive type:", names)
    json_path = ask("Path to JSON file to validate")
    if not json_path:
        return

    full_path = Path(json_path)
    if not full_path.is_absolute():
        full_path = BASE_DIR / json_path
    if not full_path.exists():
        print(f"    File not found: {json_path}")
        return

    content = json.loads(full_path.read_text(encoding="utf-8"))
    from compliance_engine import validate_primitive
    result = validate_primitive(ptype, content)

    if result["valid"]:
        print("\n    VALID — No violations found.")
    else:
        print(f"\n    INVALID — {len(result['violations'])} violation(s):")
        for v in result["violations"]:
            print(f"\n      [{v['severity'].upper()}] {v['rule']}")
            print(f"        {v['message']}")


def action_validate_kit():
    print("\n    ── Validate Kit Manifest ──\n")
    json_path = ask("Path to kit-manifest.json")
    if not json_path:
        return

    full_path = Path(json_path)
    if not full_path.is_absolute():
        full_path = BASE_DIR / json_path
    if not full_path.exists():
        print(f"    File not found: {json_path}")
        return

    manifest = json.loads(full_path.read_text(encoding="utf-8"))
    from compliance_engine import validate_kit_manifest
    result = validate_kit_manifest(manifest)

    if result["valid"]:
        print("\n    VALID — Kit manifest passes all governance checks.")
    else:
        print(f"\n    INVALID — {len(result['violations'])} violation(s):")
        for v in result["violations"]:
            print(f"\n      [{v['severity'].upper()}] {v['rule']}")
            print(f"        {v['message']}")


ACTIONS = {
    "1": action_create_document,
    "2": action_full_lifecycle,
    "3": action_quick_lifecycle,
    "4": action_peer_review,
    "5": action_revise,
    "6": action_analyze_source,
    "7": action_source_status,
    "8": action_conflict_scan,
    "9": action_regen_registry,
    "10": action_extract_schemas,
    "11": action_list_documents,
    "12": action_list_schemas,
    "13": action_start_mcp,
    "14": action_start_api,
    "15": action_validate_primitive,
    "16": action_validate_kit,
}


def main():
    clear_screen()
    print(BANNER)

    while True:
        print(MAIN_MENU)
        choice = input("    Enter choice: ").strip()

        if choice == "0":
            print("\n    Goodbye.\n")
            break

        action = ACTIONS.get(choice)
        if action:
            try:
                action()
            except KeyboardInterrupt:
                print("\n\n    Interrupted.")
            except Exception as e:
                print(f"\n    Error: {e}")
            pause()
            clear_screen()
            print(BANNER)
        else:
            print(f"\n    Invalid choice: {choice}")


if __name__ == "__main__":
    main()

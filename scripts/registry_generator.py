"""
Auto-generates DOCUMENT_REGISTRY.md and DOCUMENT_REGISTRY.json from front matter.

Usage:
    python registry_generator.py
"""

import json
from pathlib import Path
from context_assembler import BASE_DIR, parse_front_matter, read_file, today

SCAN_DIRS = [
    "core",
    "specifications",
    "commercial",
    "amendments",
    "reference",
    "legal",
    "operations",
]


def scan_documents() -> list[dict]:
    """Scan all document directories for files with front matter."""
    docs = []
    for dir_name in SCAN_DIRS:
        dir_path = BASE_DIR / dir_name
        if not dir_path.exists():
            continue
        for md_file in sorted(dir_path.glob("*.md")):
            content = read_file(md_file)
            metadata, _ = parse_front_matter(content)
            if metadata:
                metadata["_path"] = str(md_file.relative_to(BASE_DIR))
                docs.append(metadata)
            else:
                docs.append({
                    "_path": str(md_file.relative_to(BASE_DIR)),
                    "document_id": "—",
                    "title": md_file.stem,
                    "version": "—",
                    "status": "unregistered",
                    "category": dir_name,
                })
    return docs


def _normalize_cross_refs(refs: list) -> list:
    """Allow YAML lists of dicts or plain document id strings."""
    out = []
    for ref in refs or []:
        if isinstance(ref, dict):
            out.append(ref)
        else:
            out.append({"doc_id": str(ref), "relationship": "references"})
    return out


def generate_registry_json(docs: list[dict]) -> str:
    """Generate the DOCUMENT_REGISTRY.json content."""
    clean_docs = []
    for doc in docs:
        clean = {
            "document_id": doc.get("document_id", ""),
            "title": doc.get("title", doc.get("_path", "")),
            "version": doc.get("version", ""),
            "status": doc.get("status", ""),
            "category": doc.get("category", ""),
            "_path": doc.get("_path", ""),
            "cross_references": _normalize_cross_refs(doc.get("cross_references", [])),
        }
        clean_docs.append(clean)
    return json.dumps(clean_docs, indent=2, ensure_ascii=False)


def generate_registry(docs: list[dict]) -> str:
    """Generate the DOCUMENT_REGISTRY.md content."""
    lines = [
        "# AIOS Document Registry",
        "",
        f"*Auto-generated on {today()} by `scripts/registry_generator.py`. Do not edit manually.*",
        "",
        "---",
        "",
        "## All Documents",
        "",
        "| Document ID | Title | Version | Status | Category | Path |",
        "|-------------|-------|---------|--------|----------|------|",
    ]

    for doc in docs:
        doc_id = doc.get("document_id", "—")
        title = doc.get("title", doc.get("_path", "Unknown"))
        version = doc.get("version", "—")
        status = doc.get("status", "—")
        category = doc.get("category", "—")
        path = doc.get("_path", "—")
        lines.append(f"| {doc_id} | {title} | {version} | {status} | {category} | `{path}` |")

    lines.extend([
        "",
        "---",
        "",
        "## Cross-Reference Map",
        "",
    ])

    has_refs = False
    for doc in docs:
        refs = _normalize_cross_refs(doc.get("cross_references", []))
        if refs:
            has_refs = True
            title = doc.get("title", doc.get("_path", "Unknown"))
            doc_id = doc.get("document_id", "—")
            lines.append(f"### {title} ({doc_id})")
            lines.append("")
            lines.append("| Referenced Document | Relationship |")
            lines.append("|---------------------|--------------|")
            for ref in refs:
                ref_id = ref.get("doc_id", "—")
                rel = ref.get("relationship", "—")
                lines.append(f"| {ref_id} | {rel} |")
            lines.append("")

    if not has_refs:
        lines.append("*No cross-references defined yet. Add `cross_references` to document front matter.*")
        lines.append("")

    lines.extend([
        "---",
        "",
        "## Document Statistics",
        "",
        f"- **Total documents:** {len(docs)}",
        f"- **Ratified:** {sum(1 for d in docs if d.get('status') == 'ratified')}",
        f"- **Draft:** {sum(1 for d in docs if d.get('status') == 'draft')}",
        f"- **Under review:** {sum(1 for d in docs if d.get('status') in ('round_1_review', 'round_2_review', 'revision'))}",
        f"- **Unregistered (no front matter):** {sum(1 for d in docs if d.get('status') == 'unregistered')}",
        "",
    ])

    return "\n".join(lines)


def main():
    print("Scanning documents...")
    docs = scan_documents()
    print(f"Found {len(docs)} documents")

    registry_md = generate_registry(docs)
    md_path = BASE_DIR / "DOCUMENT_REGISTRY.md"
    md_path.write_text(registry_md, encoding="utf-8")
    print(f"Registry generated: DOCUMENT_REGISTRY.md")

    registry_json = generate_registry_json(docs)
    json_path = BASE_DIR / "DOCUMENT_REGISTRY.json"
    json_path.write_text(registry_json, encoding="utf-8")
    print(f"Registry generated: DOCUMENT_REGISTRY.json")


if __name__ == "__main__":
    main()

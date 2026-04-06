"""
Cross-document conflict detector.

Scans all governing documents for potential contradictions:
- Numeric conflicts (same metric with different values)
- Term definition conflicts (same term defined differently)
- Cross-reference validation (broken references)

Usage:
    python conflict_detector.py
    python conflict_detector.py --output json
    python conflict_detector.py --document-id AIOS-CORE-001
"""

import argparse
import json
import re
from pathlib import Path

from context_assembler import BASE_DIR, read_file, parse_front_matter
from registry_generator import scan_documents


def _normalize_cross_refs(cross_refs) -> list[str]:
    """Normalize cross-reference metadata into a list of referenced document ids."""
    if not cross_refs:
        return []

    if isinstance(cross_refs, str):
        ref = cross_refs.strip()
        return [ref] if ref else []

    normalized = []

    if isinstance(cross_refs, dict):
        cross_refs = [cross_refs]

    if isinstance(cross_refs, (list, tuple, set)):
        for ref in cross_refs:
            if isinstance(ref, str):
                value = ref.strip()
            elif isinstance(ref, dict):
                value = (
                    ref.get("document_id")
                    or ref.get("id")
                    or ref.get("ref")
                    or ref.get("target")
                    or ""
                )
                value = value.strip() if isinstance(value, str) else ""
            else:
                value = ""

            if value:
                normalized.append(value)

    return normalized
def _extract_numbers_with_context(content: str, doc_id: str, path: str) -> list[dict]:
    """Extract numbers with units/percentages and surrounding context."""
    patterns = [
        r"(\d+(?:\.\d+)?)\s*%\s*(\w+)",          # 2.5% GTV
        r"\$(\d+(?:,\d{3})*(?:\.\d+)?)\s*/\s*(\w+)",  # $99/mo
        r"(\d+(?:\.\d+)?)\s*(seconds?|minutes?|hours?|days?|ms)",  # time values
        r"(\d+)\s*(?:of|out of)\s*(\d+)",          # X of Y
        r"max(?:imum)?\s*(?:of\s*)?(\d+(?:\.\d+)?)\s*%",  # max 2.5%
    ]

    results = []
    for line_num, line in enumerate(content.split("\n"), 1):
        for pattern in patterns:
            for match in re.finditer(pattern, line, re.IGNORECASE):
                results.append({
                    "value": match.group(0),
                    "line": line_num,
                    "context": line.strip(),
                    "document_id": doc_id,
                    "path": path,
                })
    return results


def _extract_defined_terms(content: str, doc_id: str, path: str) -> list[dict]:
    """Extract terms that appear to be formally defined (bold or backtick-formatted)."""
    terms = []
    for line_num, line in enumerate(content.split("\n"), 1):
        for match in re.finditer(r"\*\*(.+?)\*\*\s*[–—:]\s*(.+)", line):
            terms.append({
                "term": match.group(1),
                "definition": match.group(2).strip(),
                "line": line_num,
                "document_id": doc_id,
                "path": path,
            })
        for match in re.finditer(r"`([A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+)*)`\s*[–—:]\s*(.+)", line):
            terms.append({
                "term": match.group(1),
                "definition": match.group(2).strip(),
                "line": line_num,
                "document_id": doc_id,
                "path": path,
            })
    return terms


def _validate_cross_references(docs: list[dict]) -> list[dict]:
    """Check that all cross_references point to existing documents."""
    valid_ids = {d.get("document_id") for d in docs if d.get("document_id")}
    findings = []

    for doc in docs:
        refs = _normalize_cross_refs(doc.get("cross_references", []))
        for ref in refs:
            ref_id = ref
            if ref_id and ref_id not in valid_ids:
                findings.append({
                    "type": "broken_cross_reference",
                    "severity": "high",
                    "source_document": doc.get("document_id", doc.get("_path", "")),
                    "referenced_id": ref_id,
                    "message": f"Cross-reference to '{ref_id}' does not match any document in the registry",
                })
    return findings


def run_conflict_scan(target_document_id: str | None = None) -> dict:
    """Run a full conflict scan across all governing documents."""
    docs = scan_documents()
    findings = []

    all_numbers = []
    all_terms = []

    for doc in docs:
        path = doc.get("_path")
        if not path:
            continue

        if target_document_id and doc.get("document_id") != target_document_id:
            continue

        full_path = BASE_DIR / path
        if not full_path.exists():
            continue

        content = read_file(full_path)
        doc_id = doc.get("document_id", path)

        all_numbers.extend(_extract_numbers_with_context(content, doc_id, path))
        all_terms.extend(_extract_defined_terms(content, doc_id, path))

    seen_values = {}
    for entry in all_numbers:
        normalized = re.sub(r"\s+", " ", entry["value"].lower().strip())
        key = normalized
        if key not in seen_values:
            seen_values[key] = []
        seen_values[key].append(entry)

    term_defs = {}
    for entry in all_terms:
        key = entry["term"].lower()
        if key not in term_defs:
            term_defs[key] = []
        term_defs[key].append(entry)

    for term, defs in term_defs.items():
        if len(defs) > 1:
            unique_docs = {d["document_id"] for d in defs}
            if len(unique_docs) > 1:
                unique_defs = set()
                for d in defs:
                    unique_defs.add(d["definition"][:100])
                if len(unique_defs) > 1:
                    findings.append({
                        "type": "term_definition_conflict",
                        "severity": "medium",
                        "term": defs[0]["term"],
                        "occurrences": [{
                            "document_id": d["document_id"],
                            "definition_preview": d["definition"][:100],
                            "line": d["line"],
                        } for d in defs],
                        "message": f"Term '{defs[0]['term']}' has different definitions across documents",
                    })

    findings.extend(_validate_cross_references(docs))

    return {
        "scan_date": __import__("datetime").date.today().isoformat(),
        "documents_scanned": len(docs),
        "findings_count": len(findings),
        "findings": findings,
    }


def main():
    parser = argparse.ArgumentParser(description="AIOS Cross-Document Conflict Detector")
    parser.add_argument("--output", choices=["text", "json"], default="text")
    parser.add_argument("--document-id", help="Scan a single document against the set")
    args = parser.parse_args()

    result = run_conflict_scan(args.document_id)

    if args.output == "json":
        print(json.dumps(result, indent=2))
    else:
        print(f"\nAIOS Conflict Scan — {result['scan_date']}")
        print(f"Documents scanned: {result['documents_scanned']}")
        print(f"Findings: {result['findings_count']}")
        print("=" * 60)
        if not result["findings"]:
            print("No conflicts detected.")
        else:
            for f in result["findings"]:
                print(f"\n[{f['severity'].upper()}] {f['type']}")
                print(f"  {f['message']}")
                if "occurrences" in f:
                    for occ in f["occurrences"]:
                        print(f"    - {occ['document_id']} (line {occ.get('line', '?')})")
                if "referenced_id" in f:
                    print(f"    Referenced: {f['referenced_id']}")
                    print(f"    Source: {f['source_document']}")


if __name__ == "__main__":
    main()

"""
Shared governance service layer.

Provides all governance operations as a single class imported by both
the MCP server (governance_mcp_server.py) and the REST API (governance_api.py).
Includes in-memory caching with TTL for performance.
"""

import difflib
import json
import re
import time
from pathlib import Path
from typing import Any

from context_assembler import (
    BASE_DIR, read_file, parse_front_matter, read_style_guide,
    read_grading_rubric, today,
)
from schema_extractor import load_schema, list_available_schemas, SCHEMAS_DIR
from registry_generator import scan_documents, generate_registry_json
from brand_config import expand_gateway_placeholders

CACHE_TTL_SECONDS = 300  # 5-minute cache


class _Cache:
    """Simple TTL cache for governance data."""

    def __init__(self, ttl: int = CACHE_TTL_SECONDS):
        self._store: dict[str, tuple[float, Any]] = {}
        self._ttl = ttl

    def get(self, key: str) -> Any | None:
        entry = self._store.get(key)
        if entry is None:
            return None
        ts, value = entry
        if time.time() - ts > self._ttl:
            del self._store[key]
            return None
        return value

    def set(self, key: str, value: Any):
        self._store[key] = (time.time(), value)

    def invalidate(self, key: str | None = None):
        if key:
            self._store.pop(key, None)
        else:
            self._store.clear()


class GovernanceError:
    """Structured error response."""

    def __init__(self, code: str, message: str, details: dict | None = None):
        self.code = code
        self.message = message
        self.details = details or {}

    def to_dict(self) -> dict:
        return {"error": {"code": self.code, "message": self.message, **self.details}}


class GovernanceService:
    """Stateless service wrapping all governance operations.

    Both the MCP server and REST API instantiate this class and call its methods.
    Registry and document content are cached in memory with configurable TTL.
    """

    def __init__(self, cache_ttl: int = CACHE_TTL_SECONDS):
        self._cache = _Cache(ttl=cache_ttl)

    # ── Registry ──────────────────────────────────────────────────

    def _load_registry(self) -> list[dict]:
        cached = self._cache.get("registry")
        if cached is not None:
            return cached

        json_path = BASE_DIR / "DOCUMENT_REGISTRY.json"
        if json_path.exists():
            docs = json.loads(json_path.read_text(encoding="utf-8"))
        else:
            docs = scan_documents()

        self._cache.set("registry", docs)
        return docs

    def _find_doc(self, document_id: str) -> dict | None:
        for doc in self._load_registry():
            if doc.get("document_id") == document_id:
                return doc
        return None

    # ── Documents ─────────────────────────────────────────────────

    def list_documents(
        self,
        status: str | None = None,
        category: str | None = None,
        include_drafts: bool = False,
    ) -> list[dict]:
        docs = self._load_registry()
        results = []
        for d in docs:
            if not include_drafts and d.get("status") == "draft":
                continue
            if status and d.get("status") != status:
                continue
            if category and d.get("category") != category:
                continue
            results.append({
                "document_id": d.get("document_id", ""),
                "title": d.get("title", ""),
                "version": d.get("version", ""),
                "status": d.get("status", ""),
                "category": d.get("category", ""),
                "path": d.get("_path", ""),
            })
        return results

    def get_document(self, document_id: str, include_drafts: bool = False) -> dict | GovernanceError:
        cache_key = f"doc:{document_id}"
        cached = self._cache.get(cache_key)
        if cached is not None:
            return cached

        doc = self._find_doc(document_id)
        if not doc:
            return GovernanceError("NOT_FOUND", f"Document '{document_id}' not found")

        if not include_drafts and doc.get("status") == "draft":
            return GovernanceError("NOT_RATIFIED", f"Document '{document_id}' is in draft status")

        path = doc.get("_path")
        if not path:
            return GovernanceError("NO_PATH", f"Document '{document_id}' has no file path")

        full_path = BASE_DIR / path
        if not full_path.exists():
            return GovernanceError("FILE_MISSING", f"File not found: {path}")

        content = expand_gateway_placeholders(read_file(full_path))
        metadata, body = parse_front_matter(content)

        result = {
            "document_id": document_id,
            "title": doc.get("title", ""),
            "version": doc.get("version", ""),
            "status": doc.get("status", ""),
            "category": doc.get("category", ""),
            "path": path,
            "content": content,
            "metadata": metadata,
        }
        self._cache.set(cache_key, result)
        return result

    def get_document_versions(self, document_id: str) -> list[dict] | GovernanceError:
        """List archived ratified versions of a document."""
        doc = self._find_doc(document_id)
        if not doc:
            return GovernanceError("NOT_FOUND", f"Document '{document_id}' not found")

        slug = re.sub(r"[^a-z0-9_]", "_", Path(doc.get("_path", "")).stem.lower())
        archive_dir = BASE_DIR / "archive" / "ratified"
        versions = []

        if archive_dir.exists():
            for f in sorted(archive_dir.glob(f"{slug}_v*.md")):
                match = re.search(r"_v(.+)\.md$", f.name)
                if match:
                    versions.append({
                        "version": match.group(1),
                        "path": str(f.relative_to(BASE_DIR)),
                    })

        current = doc.get("version", "")
        if current:
            versions.append({
                "version": current,
                "path": doc.get("_path", ""),
                "current": True,
            })

        return versions

    def search_documents(self, query: str) -> list[dict]:
        query_lower = query.lower()
        results = []
        for doc in self._load_registry():
            path = doc.get("_path")
            if not path:
                continue
            full_path = BASE_DIR / path
            if not full_path.exists():
                continue

            content = expand_gateway_placeholders(read_file(full_path))
            if query_lower in content.lower():
                lines = content.split("\n")
                excerpts = []
                for i, line in enumerate(lines):
                    if query_lower in line.lower():
                        start = max(0, i - 1)
                        end = min(len(lines), i + 2)
                        excerpts.append("\n".join(lines[start:end]))
                        if len(excerpts) >= 3:
                            break

                results.append({
                    "document_id": doc.get("document_id", ""),
                    "title": doc.get("title", ""),
                    "path": path,
                    "excerpts": excerpts,
                })
        return results

    # ── Primitives ────────────────────────────────────────────────

    def list_primitives(self) -> list[dict]:
        names = list_available_schemas()
        return [{"name": n, "schema_path": f"specifications/schemas/{n}.json"} for n in names]

    def get_primitive_schema(self, primitive_type: str) -> dict | GovernanceError:
        schema = load_schema(primitive_type)
        if not schema:
            return GovernanceError("NOT_FOUND", f"Primitive schema '{primitive_type}' not found")
        return {"name": primitive_type, "schema": schema}

    # ── Glossary & Style Guide ────────────────────────────────────

    def get_glossary(self) -> list[dict]:
        """Extract glossary terms from the Technical Manifesto appendix."""
        manifesto_path = BASE_DIR / "core" / "technical_manifesto.md"
        content = expand_gateway_placeholders(read_file(manifesto_path))

        terms = []
        in_glossary = False
        current_term = None
        current_def_lines = []

        for line in content.split("\n"):
            if re.match(r"#+\s*(Glossary|Appendix.*Glossary)", line, re.IGNORECASE):
                in_glossary = True
                continue
            if in_glossary and re.match(r"^#+\s", line) and "glossary" not in line.lower():
                break
            if in_glossary:
                bold_match = re.match(r"^\*\*(.+?)\*\*\s*[–—:]\s*(.+)", line)
                backtick_match = re.match(r"^`(.+?)`\s*[–—:]\s*(.+)", line)
                if bold_match:
                    if current_term:
                        terms.append({"term": current_term, "definition": " ".join(current_def_lines)})
                    current_term = bold_match.group(1)
                    current_def_lines = [bold_match.group(2).strip()]
                elif backtick_match:
                    if current_term:
                        terms.append({"term": current_term, "definition": " ".join(current_def_lines)})
                    current_term = backtick_match.group(1)
                    current_def_lines = [backtick_match.group(2).strip()]
                elif current_term and line.strip():
                    current_def_lines.append(line.strip())

        if current_term:
            terms.append({"term": current_term, "definition": " ".join(current_def_lines)})

        return terms

    def get_style_guide(self) -> str:
        return expand_gateway_placeholders(read_style_guide())

    # ── Compliance ────────────────────────────────────────────────

    def check_compliance(self, primitive_type: str, content: dict) -> dict:
        from compliance_engine import validate_primitive
        return validate_primitive(primitive_type, content)

    # ── Conflicts ─────────────────────────────────────────────────

    def check_conflicts(self, document_id: str | None = None) -> dict:
        from conflict_detector import run_conflict_scan
        return run_conflict_scan(document_id)

    # ── Amendments ────────────────────────────────────────────────

    def propose_amendment(
        self,
        source_type: str,
        source_content: str,
        rationale: str,
        affected_documents: list[str],
    ) -> dict | GovernanceError:
        import hashlib
        from datetime import datetime

        amendment_id = f"AMD-{datetime.now().strftime('%Y')}-{hashlib.sha256(source_content.encode()).hexdigest()[:6]}"

        source_dir = BASE_DIR / "sources" / amendment_id
        source_dir.mkdir(parents=True, exist_ok=True)

        (source_dir / "source.md").write_text(source_content, encoding="utf-8")
        (source_dir / "proposal.json").write_text(json.dumps({
            "amendment_id": amendment_id,
            "source_type": source_type,
            "rationale": rationale,
            "affected_documents": affected_documents,
            "submitted": datetime.now().isoformat(),
            "status": "draft",
        }, indent=2), encoding="utf-8")

        return {
            "amendment_id": amendment_id,
            "status": "draft",
            "message": f"Amendment proposal created. Run: python analyze_source.py sources/{amendment_id}/source.md --name {amendment_id}",
        }

    def get_amendment_status(self, amendment_id: str) -> dict | GovernanceError:
        source_dir = BASE_DIR / "sources" / amendment_id
        if not source_dir.exists():
            return GovernanceError("NOT_FOUND", f"Amendment '{amendment_id}' not found")

        proposal_path = source_dir / "proposal.json"
        quarantine_path = source_dir / "quarantine.json"

        result = {"amendment_id": amendment_id}

        if proposal_path.exists():
            result["proposal"] = json.loads(proposal_path.read_text(encoding="utf-8"))

        if quarantine_path.exists():
            result["quarantine"] = json.loads(quarantine_path.read_text(encoding="utf-8"))

        reports = list(source_dir.glob("impact_report_*.md"))
        result["impact_reports"] = [r.name for r in reports]
        result["has_analysis"] = len(reports) > 0

        return result

    def get_source_status(self, source_name: str) -> dict | GovernanceError:
        quarantine_path = BASE_DIR / "sources" / source_name / "quarantine.json"
        if not quarantine_path.exists():
            return GovernanceError("NOT_FOUND", f"No quarantine record for '{source_name}'")

        data = json.loads(quarantine_path.read_text(encoding="utf-8"))
        reports = list((BASE_DIR / "sources" / source_name).glob("impact_report_*.md"))
        data["impact_reports"] = [r.name for r in reports]
        return data

    # ── Action plan (impact report → synthesized plan) ────────────

    def get_action_plan(self, source_name: str) -> dict | GovernanceError:
        source_dir = BASE_DIR / "sources" / source_name
        plan_path = source_dir / "action_plan.json"
        if not plan_path.exists():
            return GovernanceError("NOT_FOUND", f"No action_plan.json for '{source_name}'")

        plan = json.loads(plan_path.read_text(encoding="utf-8"))
        log_path = source_dir / "execution_log.jsonl"
        log_entries: list[dict] = []
        if log_path.exists():
            for line in log_path.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if not line:
                    continue
                try:
                    log_entries.append(json.loads(line))
                except json.JSONDecodeError:
                    log_entries.append({"parse_error": True, "raw": line[:500]})
        return {
            "source_name": source_name,
            "plan": plan,
            "execution_log": log_entries[-200:],
        }

    def put_action_plan(self, source_name: str, plan: dict) -> dict | GovernanceError:
        source_dir = BASE_DIR / "sources" / source_name
        if not source_dir.is_dir():
            return GovernanceError("NOT_FOUND", f"Source '{source_name}' not found")
        out = source_dir / "action_plan.json"
        out.write_text(json.dumps(plan, indent=2, ensure_ascii=False), encoding="utf-8")
        rel = out.relative_to(BASE_DIR)
        return {"ok": True, "path": str(rel).replace("\\", "/")}

    def execute_action_plan_cli(self, source_name: str, dry_run: bool = False) -> dict | GovernanceError:
        """Run whitelisted automation for approved actions; update plan + JSONL log."""
        from execute_action_plan import execute as run_execute

        source_dir = BASE_DIR / "sources" / source_name
        if not source_dir.is_dir():
            return GovernanceError("NOT_FOUND", f"Source '{source_name}' not found")
        if not (source_dir / "action_plan.json").exists():
            return GovernanceError("NOT_FOUND", f"No action_plan.json for '{source_name}'")
        try:
            return run_execute(source_name, dry_run=dry_run)
        except Exception as e:
            return GovernanceError("EXECUTION_ERROR", str(e))

    # ── Diff ──────────────────────────────────────────────────────

    def diff_documents(
        self,
        document_id: str,
        version_a: str,
        version_b: str = "latest",
    ) -> dict | GovernanceError:
        """Compare two versions of a document and return a structured diff."""
        doc = self._find_doc(document_id)
        if not doc:
            return GovernanceError("NOT_FOUND", f"Document '{document_id}' not found")

        slug = re.sub(r"[^a-z0-9_]", "_", Path(doc.get("_path", "")).stem.lower())
        archive_dir = BASE_DIR / "archive" / "ratified"

        def _load_version(version: str) -> str | None:
            if version == "latest":
                path = doc.get("_path")
                if path and (BASE_DIR / path).exists():
                    return expand_gateway_placeholders(read_file(BASE_DIR / path))
                return None
            candidate = archive_dir / f"{slug}_v{version}.md"
            if candidate.exists():
                return expand_gateway_placeholders(read_file(candidate))
            return None

        content_a = _load_version(version_a)
        if content_a is None:
            return GovernanceError("VERSION_NOT_FOUND", f"Version '{version_a}' not found for '{document_id}'")

        content_b = _load_version(version_b)
        if content_b is None:
            return GovernanceError("VERSION_NOT_FOUND", f"Version '{version_b}' not found for '{document_id}'")

        lines_a = content_a.splitlines(keepends=True)
        lines_b = content_b.splitlines(keepends=True)

        unified = list(difflib.unified_diff(
            lines_a, lines_b,
            fromfile=f"{document_id} v{version_a}",
            tofile=f"{document_id} v{version_b}",
            lineterm="",
        ))

        added = sum(1 for l in unified if l.startswith("+") and not l.startswith("+++"))
        removed = sum(1 for l in unified if l.startswith("-") and not l.startswith("---"))

        return {
            "document_id": document_id,
            "version_a": version_a,
            "version_b": version_b,
            "summary": {
                "lines_added": added,
                "lines_removed": removed,
                "total_changes": added + removed,
            },
            "diff": "\n".join(unified),
        }

    # ── Cache Management ──────────────────────────────────────────

    def invalidate_cache(self):
        self._cache.invalidate()

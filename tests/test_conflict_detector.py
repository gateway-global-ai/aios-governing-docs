"""Unit tests for conflict detection."""

import pytest

from conflict_detector import run_conflict_scan, _extract_defined_terms, _extract_numbers_with_context


class TestExtractNumbers:
    def test_finds_percentages(self):
        content = "The platform takes 2.5% GTV from each transaction."
        results = _extract_numbers_with_context(content, "TEST-001", "test.md")
        assert len(results) >= 1
        assert any("2.5" in r["value"] for r in results)

    def test_finds_time_values(self):
        content = "Timeout is set to 30 seconds for all operations."
        results = _extract_numbers_with_context(content, "TEST-001", "test.md")
        assert len(results) >= 1


class TestExtractTerms:
    def test_finds_bold_definitions(self):
        content = "**Node** — A stateless compute unit that processes requests."
        results = _extract_defined_terms(content, "TEST-001", "test.md")
        assert len(results) == 1
        assert results[0]["term"] == "Node"

    def test_finds_backtick_definitions(self):
        content = "`NodeContract` — Immutable JSON schema defining a Node's interface."
        results = _extract_defined_terms(content, "TEST-001", "test.md")
        assert len(results) == 1
        assert results[0]["term"] == "NodeContract"

    def test_empty_content(self):
        results = _extract_defined_terms("", "TEST-001", "test.md")
        assert results == []


class TestRunConflictScan:
    def test_returns_structure(self):
        result = run_conflict_scan()
        assert "scan_date" in result
        assert "documents_scanned" in result
        assert "findings_count" in result
        assert "findings" in result
        assert isinstance(result["findings"], list)

    def test_scans_multiple_docs(self):
        result = run_conflict_scan()
        assert result["documents_scanned"] > 0

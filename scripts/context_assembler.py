"""
Shared module for assembling prompts with full governing context.
Used by all pipeline scripts (peer_review, revise_document, create_document, analyze_source).
"""

import asyncio
import json
import os
import re
from pathlib import Path
from datetime import date
from dotenv import load_dotenv
import yaml

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")
# Repo-local secrets (e.g. Cursor workspace); overrides .env for the same keys.
load_dotenv(BASE_DIR / ".env.local", override=True)
# Optional: share LLM keys with ai-os-voice-interface (single .env.local in Apps).
# override=True so newer keys in .env.local win over stale copies in governing_docs/.env.
_voice_env = BASE_DIR.parent / "ai-os-voice-interface" / ".env.local"
if _voice_env.exists():
    load_dotenv(_voice_env, override=True)

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

CORE_DOCS = {
    "technical_manifesto": BASE_DIR / "core" / "technical_manifesto.md",
    "governance_constitution": BASE_DIR / "core" / "governance_constitution.md",
    "mpoa": BASE_DIR / "core" / "master_platform_operating_agreement.md",
}

CATEGORY_DIRS = {
    "core": "core",
    "specification": "specifications",
    "commercial": "commercial",
    "amendment": "amendments",
    "reference": "reference",
}

STYLE_GUIDE_PATH = BASE_DIR / "STYLE_GUIDE.md"
GRADING_RUBRIC_PATH = BASE_DIR / "templates" / "grading_rubric.md"
GRADING_RUBRIC_LIGHT_PATH = BASE_DIR / "templates" / "grading_rubric_light.md"
PEER_REVIEW_TEMPLATE_PATH = BASE_DIR / "templates" / "peer_review_template.md"
DOCUMENT_TEMPLATE_PATH = BASE_DIR / "templates" / "document_template.md"
AMENDMENT_TEMPLATE_PATH = BASE_DIR / "templates" / "amendment_template.md"
INTRODUCTION_PATH = BASE_DIR / "introduction.md"
DOCUMENT_REGISTRY_PATH = BASE_DIR / "DOCUMENT_REGISTRY.md"
DOCUMENT_REGISTRY_JSON_PATH = BASE_DIR / "DOCUMENT_REGISTRY.json"

DEFAULT_PRODUCT_CONTEXT_BUNDLE = (
    BASE_DIR / "reference" / "knowledge_base" / "snapshots" / "product_context_bundle.md"
)

# YAML cross_references sometimes use short names; registry uses canonical document_id.
CROSS_REF_ALIAS_TO_REGISTRY_ID = {
    "MPOA": "AIOS-CORE-003",
}


def _resolve_registry_doc_id(doc_id: str) -> str:
    return CROSS_REF_ALIAS_TO_REGISTRY_ID.get(doc_id, doc_id)


def read_file(path: Path) -> str:
    if path.exists():
        return path.read_text(encoding="utf-8")
    return f"[File not found: {path}]"


def read_core_docs() -> dict[str, str]:
    return {name: read_file(path) for name, path in CORE_DOCS.items()}


def load_registry_json() -> list[dict]:
    """Load the JSON document registry. Falls back to scanning if JSON doesn't exist."""
    if DOCUMENT_REGISTRY_JSON_PATH.exists():
        return json.loads(DOCUMENT_REGISTRY_JSON_PATH.read_text(encoding="utf-8"))
    return []


def _smart_context_bundle_banner(doc_id: str, raw: str) -> str:
    """Prepend explicit version metadata so peer-review models do not misread bundled ops/specs."""
    meta, _ = parse_front_matter(raw)
    ver = meta.get("version", "?")
    reg = meta.get("registry_id")
    bits = [f"**`{doc_id}`**", f"**version** **`{ver}`**"]
    if reg:
        bits.append(f"**registry_id** **`{reg}`**")
    banner = "**[Bundled cross-reference — use this file’s version]** " + " — ".join(bits) + "\n\n---\n\n"
    return banner + raw


def read_relevant_context(doc_path: str) -> dict[str, str]:
    """Read only the documents referenced in the target doc's front-matter cross_references.

    Uses the JSON registry to map document IDs to file paths. For core documents
    that cross-reference each other, this still returns all related core docs.
    For specifications, it returns only the specific docs they reference.
    """
    content = read_file(BASE_DIR / doc_path)
    metadata, _ = parse_front_matter(content)
    refs = metadata.get("cross_references", [])
    ref_ids = {r.get("doc_id") for r in refs if r.get("doc_id")}

    if not ref_ids:
        return read_core_docs()

    registry = load_registry_json()
    id_to_path = {d.get("document_id"): d.get("_path") for d in registry if d.get("document_id")}

    context = {}
    for doc_id in ref_ids:
        lookup = _resolve_registry_doc_id(doc_id)
        path = id_to_path.get(lookup)
        if path:
            raw = read_file(BASE_DIR / path)
            context[doc_id] = _smart_context_bundle_banner(doc_id, raw)

    return context


def _is_core_doc_path(doc_path: str) -> bool:
    return doc_path.startswith("core/") or doc_path.startswith("core\\")


def peer_review_context_bundle_info(doc_path: str, smart_context: bool) -> dict:
    """Metadata for prompt-manifest logging: which files were bundled and what was skipped."""
    content = read_file(BASE_DIR / doc_path)
    metadata, _ = parse_front_matter(content)
    refs = metadata.get("cross_references", [])
    ref_ids = [r.get("doc_id") for r in refs if r.get("doc_id")]
    registry = load_registry_json()
    id_to_path = {d.get("document_id"): d.get("_path") for d in registry if d.get("document_id")}
    missing_registry = [
        rid for rid in ref_ids if _resolve_registry_doc_id(rid) not in id_to_path
    ]

    included: list[dict] = []

    def add_entry(doc_id: str, rel_path: str, raw: str) -> None:
        p = BASE_DIR / rel_path
        st = p.stat() if p.is_file() else None
        meta2, _ = parse_front_matter(raw)
        included.append(
            {
                "document_id": doc_id,
                "path": rel_path.replace("\\", "/"),
                "bytes": len(raw.encode("utf-8")),
                "version": meta2.get("version"),
                "registry_id": meta2.get("registry_id"),
                "mtime_utc": st.st_mtime if st else None,
            }
        )

    if smart_context and not _is_core_doc_path(doc_path):
        if not ref_ids:
            for name, path in CORE_DOCS.items():
                raw = read_file(path)
                add_entry(name, str(path.relative_to(BASE_DIR)), raw)
        else:
            for rid in ref_ids:
                lookup = _resolve_registry_doc_id(rid)
                rp = id_to_path.get(lookup)
                if not rp:
                    continue
                raw = read_file(BASE_DIR / rp)
                add_entry(rid, rp, raw)
    else:
        for name, path in CORE_DOCS.items():
            raw = read_file(path)
            add_entry(name, str(path.relative_to(BASE_DIR)), raw)

    mode = "smart_cross_refs" if smart_context and not _is_core_doc_path(doc_path) else "full_core_three"
    if smart_context and not _is_core_doc_path(doc_path) and not ref_ids:
        mode = "smart_fallback_core_empty_refs"

    return {
        "context_mode": mode,
        "cross_reference_doc_ids_requested": ref_ids,
        "missing_registry_ids": missing_registry,
        "included_documents": included,
    }


def product_context_bundle_info(product_context_arg: str | None) -> dict:
    """Resolved product snapshot path and size for manifest logging."""
    if product_context_arg is None:
        return {"loaded": False, "path": None, "bytes": 0, "mtime_utc": None}
    if product_context_arg == "default":
        path = DEFAULT_PRODUCT_CONTEXT_BUNDLE
    else:
        rel = product_context_arg.replace("\\", "/").lstrip("/")
        path = (BASE_DIR / rel).resolve()
    if not path.is_file():
        try:
            disp = str(path.relative_to(BASE_DIR.resolve()))
        except ValueError:
            disp = str(path)
        return {"loaded": False, "path": disp, "bytes": 0, "mtime_utc": None, "error": "missing_file"}
    st = path.stat()
    try:
        disp = str(path.relative_to(BASE_DIR.resolve()))
    except ValueError:
        disp = str(path)
    return {"loaded": True, "path": disp, "bytes": st.st_size, "mtime_utc": st.st_mtime}


def classify_peer_review_output(content: str) -> str:
    """Coarse bucket for manifest logging — not a legal determination."""
    c = (content or "").strip()
    if c.startswith("[ERROR:"):
        return "api_error"
    low = c.lower()
    if len(c) < 160 and (
        "sorry" in low
        or "can't assist" in low
        or "cannot assist" in low
        or "i'm unable" in low
    ):
        return "refusal_or_empty"
    if len(c) < 200:
        return "short_or_truncated"
    return "review_like"


def read_style_guide() -> str:
    return read_file(STYLE_GUIDE_PATH)


def read_grading_rubric(variant: str = "full") -> str:
    if variant == "light":
        return read_file(GRADING_RUBRIC_LIGHT_PATH)
    return read_file(GRADING_RUBRIC_PATH)


def read_peer_review_template() -> str:
    return read_file(PEER_REVIEW_TEMPLATE_PATH)


def read_document_template() -> str:
    return read_file(DOCUMENT_TEMPLATE_PATH)


def read_introduction() -> str:
    return read_file(INTRODUCTION_PATH)


def resolve_product_implementation_text(product_context_arg: str | None) -> str:
    """Load optional ai-os-voice-interface snapshot for peer review prompts.

    ``product_context_arg``:
    - ``None`` — placeholder instructing coordinator to generate/load bundle.
    - ``\"default\"`` — ``reference/knowledge_base/snapshots/product_context_bundle.md``.
    - any other string — path relative to ``BASE_DIR`` (POSIX slashes).
    """
    if product_context_arg is None:
        return (
            "[**Not loaded.**] For Workspace / integration amendments, run "
            "`py -3 scripts/generate_product_context_bundle.py` then re-run "
            "`peer_review.py` with `--product-context` (see `reference/knowledge_base/README.md`)."
        )
    if product_context_arg == "default":
        path = DEFAULT_PRODUCT_CONTEXT_BUNDLE
    else:
        rel = product_context_arg.replace("\\", "/").lstrip("/")
        path = (BASE_DIR / rel).resolve()
        try:
            path.relative_to(BASE_DIR.resolve())
        except ValueError:
            return f"[**Rejected path** — outside governing_docs root: {product_context_arg}]"
    if not path.is_file():
        try:
            rel_disp = path.relative_to(BASE_DIR.resolve())
        except ValueError:
            rel_disp = path
        return f"[**Missing file:** `{rel_disp}`]"
    return read_file(path)


def read_document_registry() -> str:
    return read_file(DOCUMENT_REGISTRY_PATH)


def read_prompt_template(prompt_name: str) -> str:
    path = BASE_DIR / "prompts" / prompt_name
    return read_file(path)


def get_doc_slug(doc_path: str) -> str:
    """Extract a slug from a document path for use in review folder names."""
    name = Path(doc_path).stem
    return re.sub(r"[^a-z0-9_]", "_", name.lower())


def find_reviews(doc_path: str, review_round: int | None = None) -> list[str]:
    """Find existing peer reviews for prior-round context (e.g. Round 2 prompt).

    When ``review_round`` is set, only loads files named ``review_<NNN>_<model>.md``.
    If more than three index values exist (historical triads), only the **latest triad**
    (three highest **NNN** values) is included so prompts stay within model context limits
    (e.g. DeepSeek 131k) while still giving Round 2 models the most recent triangulation.
    """
    slug = get_doc_slug(doc_path)
    reviews_dir = BASE_DIR / "reviews" / slug

    if not reviews_dir.exists():
        return []

    results = []
    if review_round:
        round_dir = reviews_dir / f"round_{review_round}"
        if round_dir.exists():
            by_num: dict[int, list[Path]] = {}
            for f in round_dir.glob("review_*.md"):
                m = re.match(r"^review_(\d+)_", f.name, re.IGNORECASE)
                if m:
                    by_num.setdefault(int(m.group(1)), []).append(f)
            if by_num:
                top_nums = sorted(by_num.keys(), reverse=True)[:3]
                for n in sorted(top_nums):
                    for f in sorted(by_num[n]):
                        results.append(read_file(f))
            else:
                for f in sorted(round_dir.glob("*.md")):
                    results.append(read_file(f))
    else:
        for round_dir in sorted(reviews_dir.glob("round_*")):
            for f in sorted(round_dir.glob("*.md")):
                results.append(read_file(f))

    return results


def find_revision_log(doc_path: str) -> str | None:
    """Find the revision log for a document, if it exists."""
    slug = get_doc_slug(doc_path)
    log_path = BASE_DIR / "reviews" / slug / "revision_log.md"
    if log_path.exists():
        return read_file(log_path)
    return None


def read_existing_specs() -> str:
    """Read all specification documents for cross-reference context."""
    specs_dir = BASE_DIR / "specifications"
    if not specs_dir.exists():
        return "[No specifications found]"

    parts = []
    for f in sorted(specs_dir.glob("*.md")):
        content = read_file(f)
        parts.append(f"### {f.stem}\n\n{content}")
    return "\n\n---\n\n".join(parts)


def get_next_review_number(doc_path: str, review_round: int) -> int:
    """Get the next sequential review number for a document and round."""
    slug = get_doc_slug(doc_path)
    round_dir = BASE_DIR / "reviews" / slug / f"round_{review_round}"
    round_dir.mkdir(parents=True, exist_ok=True)

    existing = list(round_dir.glob("review_*.md"))
    if not existing:
        return 1

    numbers = []
    for f in existing:
        match = re.search(r"review_(\d+)", f.stem)
        if match:
            numbers.append(int(match.group(1)))
    return max(numbers, default=0) + 1


def assemble_prompt(template_content: str, replacements: dict[str, str]) -> str:
    """Replace {{PLACEHOLDER}} tokens in a template with actual content."""
    result = template_content
    for key, value in replacements.items():
        result = result.replace(f"{{{{{key}}}}}", value)
    return result


def parse_front_matter(content: str) -> tuple[dict, str]:
    """Parse YAML front matter from a markdown document."""
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                metadata = yaml.safe_load(parts[1])
                body = parts[2].strip()
                return metadata or {}, body
            except yaml.YAMLError:
                pass
    return {}, content


def add_front_matter(content: str, metadata: dict) -> str:
    """Add or replace YAML front matter in a markdown document."""
    _, body = parse_front_matter(content)
    fm = yaml.dump(metadata, default_flow_style=False, sort_keys=False, allow_unicode=True)
    return f"---\n{fm}---\n\n{body}"


# --- API Clients ---

async def call_openai(
    system_prompt: str,
    user_prompt: str,
    model: str | None = None,
    *,
    max_tokens: int = 16000,
) -> str:
    from openai import AsyncOpenAI
    resolved = model or os.environ.get("OPENAI_PEER_REVIEW_MODEL", "gpt-5.4")
    client = AsyncOpenAI(api_key=OPENAI_API_KEY)
    # gpt-5.x and newer OpenAI models require max_completion_tokens (not max_tokens).
    response = await client.chat.completions.create(
        model=resolved,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        max_completion_tokens=max_tokens,
        temperature=0.3,
    )
    return response.choices[0].message.content


async def call_deepseek(system_prompt: str, user_prompt: str, model: str | None = None) -> str:
    from openai import AsyncOpenAI
    resolved = model or os.environ.get("DEEPSEEK_PEER_REVIEW_MODEL", "deepseek-chat")
    client = AsyncOpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")
    response = await client.chat.completions.create(
        model=resolved,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        # DeepSeek API allows max_tokens in [1, 8192] (stricter than OpenAI).
        max_tokens=8192,
        temperature=0.3,
    )
    return response.choices[0].message.content


async def call_gemini(system_prompt: str, user_prompt: str, model: str | None = None) -> str:
    from google import genai
    resolved = model or os.environ.get("GEMINI_PEER_REVIEW_MODEL", "gemini-2.5-pro")
    client = genai.Client(api_key=GEMINI_API_KEY)
    response = await asyncio.to_thread(
        client.models.generate_content,
        model=resolved,
        contents=f"{system_prompt}\n\n---\n\n{user_prompt}",
    )
    return response.text


MODEL_CALLERS = {
    "deepseek": call_deepseek,
    "openai": call_openai,
    "gemini": call_gemini,
}


async def call_models_parallel(
    models: list[str],
    system_prompt: str,
    user_prompt: str,
) -> dict[str, str]:
    """Call multiple models in parallel, return dict of model_name -> response."""
    tasks = {}
    for model_name in models:
        caller = MODEL_CALLERS[model_name]
        tasks[model_name] = asyncio.create_task(caller(system_prompt, user_prompt))

    results = {}
    for model_name, task in tasks.items():
        try:
            results[model_name] = await task
        except Exception as e:
            results[model_name] = f"[ERROR calling {model_name}: {e}]"

    return results


def save_review(doc_path: str, review_round: int, model_name: str, content: str) -> Path:
    """Save a review to the appropriate location and return the path."""
    slug = get_doc_slug(doc_path)
    num = get_next_review_number(doc_path, review_round)
    round_dir = BASE_DIR / "reviews" / slug / f"round_{review_round}"
    round_dir.mkdir(parents=True, exist_ok=True)

    filename = f"review_{num:03d}_{model_name}.md"
    out_path = round_dir / filename
    out_path.write_text(content, encoding="utf-8")
    return out_path


def today() -> str:
    return date.today().isoformat()

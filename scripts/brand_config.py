"""
Gateway Global public URLs and contact emails — driven by environment variables.

Defaults match production intent: public site + docs subdomain for governance corpus.
Used when serving documents via GovernanceService (API/MCP) so markdown can use placeholders.
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

_BASE = Path(__file__).resolve().parent.parent
load_dotenv(_BASE / ".env")
_voice_env = _BASE.parent / "ai-os-voice-interface" / ".env.local"
if _voice_env.exists():
    load_dotenv(_voice_env, override=True)


def gateway_placeholders() -> dict[str, str]:
    """Placeholders use double braces in markdown/source, e.g. {{GATEWAY_DOCS_SITE_URL}}."""
    public = os.getenv("GATEWAY_PUBLIC_SITE_URL", "http://www.gatewayglobal.ai").rstrip("/")
    docs = os.getenv("GATEWAY_DOCS_SITE_URL", "http://docs.gatewayglobal.ai").rstrip("/")
    schema_base = os.getenv("GATEWAY_SCHEMA_BASE_URL", f"{docs}/schemas").rstrip("/")
    registry_url = os.getenv(
        "GATEWAY_COMPONENT_REGISTRY_URL",
        f"{docs}/registry/components.json",
    )
    roadmap_url = os.getenv("GATEWAY_ROADMAP_URL", f"{docs}/roadmap")
    transparency_url = os.getenv(
        "GATEWAY_TRANSPARENCY_URL",
        f"{docs}/governance/transparency",
    )
    return {
        "{{GATEWAY_PUBLIC_SITE_URL}}": public,
        "{{GATEWAY_DOCS_SITE_URL}}": docs,
        "{{GATEWAY_SCHEMA_BASE_URL}}": schema_base,
        "{{GATEWAY_COMPONENT_REGISTRY_URL}}": registry_url,
        "{{GATEWAY_ROADMAP_URL}}": roadmap_url,
        "{{GATEWAY_TRANSPARENCY_URL}}": transparency_url,
        "{{GATEWAY_EMAIL_GOVERNANCE}}": os.getenv(
            "GATEWAY_EMAIL_GOVERNANCE", "governance@gatewayglobal.ai"
        ),
        "{{GATEWAY_EMAIL_RFC}}": os.getenv("GATEWAY_EMAIL_RFC", "rfcs@gatewayglobal.ai"),
        "{{GATEWAY_EMAIL_VENDOR}}": os.getenv("GATEWAY_EMAIL_VENDOR", "vendor@gatewayglobal.ai"),
        "{{GATEWAY_EMAIL_ONBOARDING}}": os.getenv(
            "GATEWAY_EMAIL_ONBOARDING", "onboarding@gatewayglobal.ai"
        ),
    }


def expand_gateway_placeholders(text: str) -> str:
    if not text:
        return text
    out = text
    for key, val in gateway_placeholders().items():
        out = out.replace(key, val)
    return out

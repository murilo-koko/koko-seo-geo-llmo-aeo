#!/usr/bin/env python3
"""Run a real URL smoke test using only public repo helpers."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from urllib.parse import urlparse

from lite_audit_utils import ai_citation_readiness, fetch_llms_txt_status, fetch_snapshot


def run_lighthouse(url: str, preset: str = "mobile", timeout_s: int = 120) -> dict:
    """Collect a minimal Lighthouse performance snapshot via npx."""
    cmd = [
        "npx",
        "-y",
        "lighthouse",
        url,
        "--output=json",
        "--output-path=stdout",
        "--only-categories=performance",
        "--chrome-flags=--headless=new --no-sandbox",
        "--quiet",
    ]
    if preset == "desktop":
        cmd.append("--preset=desktop")

    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout_s)
    except subprocess.TimeoutExpired:
        return {"preset": preset, "performance_score": None, "metrics": {}, "top_opportunities": [], "error": "Lighthouse timeout"}
    except FileNotFoundError:
        return {"preset": preset, "performance_score": None, "metrics": {}, "top_opportunities": [], "error": "npx not found"}

    if proc.returncode != 0:
        return {
            "preset": preset,
            "performance_score": None,
            "metrics": {},
            "top_opportunities": [],
            "error": f"Lighthouse exit {proc.returncode}",
        }

    report = json.loads(proc.stdout)
    audits = report.get("audits", {})
    categories = report.get("categories", {})
    performance = categories.get("performance", {}).get("score")
    performance_score = round(performance * 100) if isinstance(performance, (int, float)) else None

    def _numeric(audit_key: str) -> float | None:
        value = audits.get(audit_key, {}).get("numericValue")
        return value if isinstance(value, (int, float)) else None

    opportunities = []
    for audit_id, audit in audits.items():
        details = audit.get("details", {})
        savings = details.get("overallSavingsMs")
        if details.get("type") == "opportunity" and savings and savings > 50:
            opportunities.append(
                {
                    "id": audit_id,
                    "title": audit.get("title", audit_id),
                    "savings_ms": savings,
                }
            )
    opportunities.sort(key=lambda item: item["savings_ms"], reverse=True)

    return {
        "preset": preset,
        "performance_score": performance_score,
        "metrics": {
            "lcp_s": (_numeric("largest-contentful-paint") or 0) / 1000 if _numeric("largest-contentful-paint") is not None else None,
            "fcp_s": (_numeric("first-contentful-paint") or 0) / 1000 if _numeric("first-contentful-paint") is not None else None,
            "tbt_ms": _numeric("total-blocking-time"),
            "cls": _numeric("cumulative-layout-shift"),
            "inp_ms": _numeric("interaction-to-next-paint") or _numeric("max-potential-fid"),
        },
        "top_opportunities": opportunities[:3],
        "error": None,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Collect raw evidence for a URL using render audit and Lighthouse.",
    )
    parser.add_argument("url", help="Full URL to audit")
    parser.add_argument(
        "--preset",
        default="mobile",
        choices=["mobile", "desktop"],
        help="Lighthouse preset",
    )
    args = parser.parse_args()

    snapshot = fetch_snapshot(args.url)
    lighthouse = run_lighthouse(args.url, preset=args.preset, timeout_s=120)
    llms_status = fetch_llms_txt_status(snapshot.final_url)
    ai_readiness = ai_citation_readiness(snapshot, llms_status)
    parsed = urlparse(snapshot.final_url)
    internal_links = 0
    external_links = 0
    for link in snapshot.links:
        target = urlparse(link if "://" in link else "")
        if target.netloc and target.netloc != parsed.netloc:
            external_links += 1
        else:
            internal_links += 1

    payload = {
        "url": args.url,
        "final_url": snapshot.final_url,
        "status_code": snapshot.status_code,
        "word_count": snapshot.word_count,
        "page_type": snapshot.page_type,
        "title": snapshot.title,
        "meta_description_present": bool(snapshot.meta_description),
        "canonical": snapshot.canonical,
        "structured_data_count": snapshot.schema_count,
        "images": {
            "total": None,
            "missing_alt": None,
        },
        "links": {
            "internal": internal_links,
            "external": external_links,
        },
        "top_terms": snapshot.top_terms,
        "h1_count": snapshot.h1_count,
        "h1_texts": snapshot.h1_texts,
        "h2_count": snapshot.h2_count,
        "h3_count": snapshot.h3_count,
        "list_count": snapshot.list_count,
        "short_paragraph_count": snapshot.short_paragraph_count,
        "faq_hint": snapshot.faq_hint,
        "llms_txt": llms_status,
        "ai_citation_readiness": ai_readiness,
        "lighthouse": lighthouse,
    }
    json.dump(payload, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

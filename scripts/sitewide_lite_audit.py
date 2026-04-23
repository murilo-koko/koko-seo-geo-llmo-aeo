#!/usr/bin/env python3
"""Crawl a small set of internal URLs and summarize sitewide SEO health signals."""

from __future__ import annotations

import argparse
import json
import sys
from collections import deque

from lite_audit_utils import (
    ai_citation_readiness,
    fetch_llms_txt_status,
    fetch_snapshot,
    normalize_internal_links,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run a lightweight crawl over a small set of internal pages.",
    )
    parser.add_argument("url", help="Root URL to crawl")
    parser.add_argument(
        "--max-pages",
        type=int,
        default=5,
        help="Maximum number of internal pages to include",
    )
    args = parser.parse_args()

    max_pages = max(2, min(args.max_pages, 12))
    queue = deque([args.url])
    visited: set[str] = set()
    pages = []
    llms_status = fetch_llms_txt_status(args.url)

    while queue and len(pages) < max_pages:
        url = queue.popleft()
        if url in visited:
            continue
        visited.add(url)
        try:
            snapshot = fetch_snapshot(url)
        except Exception as exc:  # pragma: no cover - network behavior
            pages.append(
                {
                    "url": url,
                    "status_code": 0,
                    "error": str(exc),
                }
            )
            continue

        pages.append(
            {
                "url": snapshot.final_url,
                "status_code": snapshot.status_code,
                "page_type": snapshot.page_type,
                "title": snapshot.title,
                "word_count": snapshot.word_count,
                "h1_count": snapshot.h1_count,
                "meta_description_present": bool(snapshot.meta_description),
                "schema_count": snapshot.schema_count,
                "ai_citation_readiness": ai_citation_readiness(snapshot, llms_status),
                "top_terms": snapshot.top_terms[:8],
            }
        )

        for link in normalize_internal_links(snapshot.final_url, snapshot.links):
            if link not in visited and link not in queue and len(visited) + len(queue) < 50:
                queue.append(link)

    broken_pages = [page["url"] for page in pages if page.get("status_code", 0) >= 400 or page.get("status_code") == 0]
    thin_pages = [page["url"] for page in pages if page.get("word_count", 0) and page.get("word_count", 0) < 250]
    missing_meta = [page["url"] for page in pages if page.get("status_code") == 200 and not page.get("meta_description_present")]
    weak_structure = [page["url"] for page in pages if page.get("status_code") == 200 and page.get("h1_count", 0) != 1]
    weak_ai_readiness = [
        page["url"]
        for page in pages
        if page.get("status_code") == 200 and page.get("ai_citation_readiness", {}).get("score", 0) < 55
    ]

    top_issues = []
    if broken_pages:
        top_issues.append(f"{len(broken_pages)} page(s) returned 4xx/0 status and need immediate review.")
    if thin_pages:
        top_issues.append(f"{len(thin_pages)} page(s) look thin for their likely purpose.")
    if missing_meta:
        top_issues.append(f"{len(missing_meta)} page(s) are missing a meta description.")
    if weak_structure:
        top_issues.append(f"{len(weak_structure)} page(s) do not have exactly one H1.")
    if weak_ai_readiness:
        top_issues.append(f"{len(weak_ai_readiness)} page(s) have weak AI citation readiness signals.")
    if not llms_status.get("present"):
        top_issues.append("llms.txt was not found at the site root.")
    if not top_issues:
        top_issues.append("No major structural issues were detected in the sampled pages.")

    payload = {
        "mode": "sitewide-lite",
        "root_url": args.url,
        "pages_crawled": len(pages),
        "summary": {
            "broken_pages": broken_pages,
            "thin_pages": thin_pages,
            "missing_meta_description": missing_meta,
            "weak_h1_structure": weak_structure,
            "weak_ai_citation_readiness": weak_ai_readiness,
            "llms_txt": llms_status,
            "top_issues": top_issues,
        },
        "pages": pages,
    }
    json.dump(payload, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Compare multiple URLs and flag overlap, intent conflicts, and cannibalization risk."""

from __future__ import annotations

import argparse
import json
import sys
from itertools import combinations

from lite_audit_utils import fetch_snapshot, jaccard_similarity


def _risk_label(score: float, same_type: bool) -> str:
    if score >= 0.7 and same_type:
        return "high"
    if score >= 0.45:
        return "medium"
    return "low"


def _intent_note(left_type: str, right_type: str, score: float) -> str:
    if left_type == right_type and score >= 0.45:
        return "The pages appear to target a similar intent and should be differentiated."
    if left_type != right_type and score >= 0.45:
        return "The pages overlap semantically but likely serve different jobs."
    return "The overlap is limited and unlikely to cause serious cannibalization."


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compare 2 to 5 URLs for overlap and cannibalization-lite risk.",
    )
    parser.add_argument("urls", nargs="+", help="Two to five URLs to compare")
    args = parser.parse_args()

    if not 2 <= len(args.urls) <= 5:
        raise SystemExit("Provide between 2 and 5 URLs.")

    snapshots = [fetch_snapshot(url) for url in args.urls]
    comparisons = []
    high_risk_pairs = 0

    for left, right in combinations(snapshots, 2):
        title_overlap = jaccard_similarity(left.title.split(), right.title.split())
        h1_overlap = jaccard_similarity(left.h1_texts, right.h1_texts)
        term_overlap = jaccard_similarity(left.top_terms, right.top_terms)
        weighted_overlap = round((title_overlap * 0.25) + (h1_overlap * 0.25) + (term_overlap * 0.5), 2)
        risk = _risk_label(weighted_overlap, left.page_type == right.page_type)
        if risk == "high":
            high_risk_pairs += 1

        shared_terms = sorted(set(left.top_terms) & set(right.top_terms))[:8]
        comparisons.append(
            {
                "left_url": left.final_url,
                "right_url": right.final_url,
                "left_page_type": left.page_type,
                "right_page_type": right.page_type,
                "overlap_score": weighted_overlap,
                "risk": risk,
                "shared_terms": shared_terms,
                "note": _intent_note(left.page_type, right.page_type, weighted_overlap),
            }
        )

    payload = {
        "mode": "compare-pages",
        "url_count": len(snapshots),
        "pages": [
            {
                "url": snapshot.final_url,
                "status_code": snapshot.status_code,
                "page_type": snapshot.page_type,
                "title": snapshot.title,
                "word_count": snapshot.word_count,
                "top_terms": snapshot.top_terms,
            }
            for snapshot in snapshots
        ],
        "comparisons": comparisons,
        "summary": {
            "high_risk_pairs": high_risk_pairs,
            "medium_or_higher_pairs": sum(
                1 for item in comparisons if item["risk"] in {"high", "medium"}
            ),
            "recommendation": (
                "Differentiate page intent, headings, and supporting terms before scaling content."
                if high_risk_pairs
                else "The set is reasonably differentiated, but medium-overlap pairs still deserve review."
            ),
        },
    }
    json.dump(payload, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

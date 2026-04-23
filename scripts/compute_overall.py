#!/usr/bin/env python3
"""Compute the weighted overall score for a search intelligence audit."""

from __future__ import annotations

import argparse
import json
import sys

WEIGHTS = {
    "blog": {"seo": 0.30, "geo": 0.25, "aeo": 0.25, "llmo": 0.20},
    "landing-page": {"seo": 0.25, "geo": 0.20, "aeo": 0.25, "llmo": 0.30},
    "other": {"seo": 0.30, "geo": 0.25, "aeo": 0.20, "llmo": 0.25},
}


def _bounded_score(value: int) -> int:
    if value < 0 or value > 100:
        raise ValueError(f"Scores must be between 0 and 100. Got {value}.")
    return value


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compute weighted overall score from SEO/GEO/AEO/LLMO pillar scores.",
    )
    parser.add_argument(
        "--page-type",
        choices=sorted(WEIGHTS),
        required=True,
        help="Page type used to select weights.",
    )
    parser.add_argument("--seo", type=int, required=True)
    parser.add_argument("--geo", type=int, required=True)
    parser.add_argument("--aeo", type=int, required=True)
    parser.add_argument("--llmo", type=int, required=True)
    args = parser.parse_args()

    scores = {
        "seo": _bounded_score(args.seo),
        "geo": _bounded_score(args.geo),
        "aeo": _bounded_score(args.aeo),
        "llmo": _bounded_score(args.llmo),
    }
    weights = WEIGHTS[args.page_type]
    overall = round(sum(scores[key] * weights[key] for key in scores))

    json.dump(
        {
            "page_type": args.page_type,
            "weights": weights,
            "scores": scores,
            "overall_score": overall,
        },
        sys.stdout,
        indent=2,
    )
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

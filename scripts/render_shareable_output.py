#!/usr/bin/env python3
"""Render shareable markdown from a structured audit summary JSON."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def _load_input(path: str | None) -> dict:
    if path:
        return json.loads(Path(path).read_text())
    return json.load(sys.stdin)


def _best_and_weakest(scores: dict[str, int]) -> tuple[str, str]:
    ordered = sorted(scores.items(), key=lambda item: (-item[1], item[0]))
    reverse_ordered = sorted(scores.items(), key=lambda item: (item[1], item[0]))
    return ordered[0][0].upper(), reverse_ordered[0][0].upper()


def _require(data: dict, key: str):
    if key not in data:
        raise KeyError(f"Missing required key: {key}")
    return data[key]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Turn a JSON audit summary into public scorecard and carousel markdown.",
    )
    parser.add_argument(
        "input",
        nargs="?",
        help="Optional path to a JSON file. If omitted, reads JSON from stdin.",
    )
    args = parser.parse_args()

    data = _load_input(args.input)
    url = _require(data, "url")
    overall = _require(data, "overall_score")
    scores = _require(data, "scores")
    confidence = data.get("confidence", "medium")
    biggest_win = data.get("biggest_win")
    biggest_leak = data.get("biggest_leak")
    if not biggest_win or not biggest_leak:
        top_wins = data.get("top_wins") or []
        top_blockers = data.get("top_blockers") or []
        biggest_win = biggest_win or (top_wins[0] if top_wins else "Clear strengths were identified.")
        biggest_leak = biggest_leak or (
            top_blockers[0] if top_blockers else "A clear improvement opportunity remains."
        )

    best_pillar, weakest_pillar = _best_and_weakest(scores)
    title = data.get("title") or data.get("page_type", "page").replace("-", " ").title()
    verdict = data.get("verdict", "")
    next_actions = data.get("next_actions") or []
    top_actions = [item["action"] for item in next_actions[:3] if isinstance(item, dict) and item.get("action")]

    lines = [
        "## Public Scorecard",
        f"- URL: {url}",
        f"- Overall: {overall}/100",
        f"- SEO: {scores['seo']}",
        f"- GEO: {scores['geo']}",
        f"- AEO: {scores['aeo']}",
        f"- LLMO: {scores['llmo']}",
        f"- Confidence: {confidence}",
        f"- Best pillar: {best_pillar}",
        f"- Weakest pillar: {weakest_pillar}",
        f"- Biggest win: {biggest_win}",
        f"- Biggest leak: {biggest_leak}",
        "",
        "## Carousel Summary",
        "### Slide 1",
        f"{title} scored {overall}/100 for SEO, GEO, AEO, and LLMO.",
        "",
        "### Slide 2",
        "What is working:",
        f"- Best pillar: {best_pillar}",
        f"- {biggest_win}",
    ]

    if verdict:
        lines.append(f"- Verdict: {verdict}")

    lines.extend([
        "",
        "### Slide 3",
        "What is leaking:",
        f"- Weakest pillar: {weakest_pillar}",
        f"- {biggest_leak}",
        "",
        "### Slide 4",
        "Top fixes:",
    ])

    if top_actions:
        for action in top_actions:
            lines.append(f"- {action}")
    else:
        lines.append("- Add a tighter action list to the JSON summary for richer output.")

    lines.extend([
        "",
        "### Slide 5",
        "Takeaway:",
        f"Strong pages still lose reach when their weakest pillar stays behind. This one is strongest in {best_pillar} and still leaking through {weakest_pillar}.",
    ])

    sys.stdout.write("\n".join(lines) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

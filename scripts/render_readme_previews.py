#!/usr/bin/env python3
"""Generate README SVG previews from demo JSON files."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


BG = "#062B2B"
PANEL = "#0B3B3B"
SURFACE = "#071E1E"
TEXT = "#CCFBF1"
MUTED = "#99F6E4"
BODY = "#D1FAE5"
CARD_A = "#0F766E"
CARD_B = "#134E4A"
CARD_C = "#115E59"


def _escape(value: str) -> str:
    return (
        value.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def _trim(value: str, limit: int) -> str:
    if len(value) <= limit:
        return value
    return value[: limit - 1].rstrip() + "…"


def render_audit_preview(audit_data: dict) -> str:
    scores = audit_data["scores"]
    wins = audit_data.get("top_wins") or []
    blockers = audit_data.get("top_blockers") or []
    actions = audit_data.get("next_actions") or []

    biggest_win = wins[0] if wins else "Strong structure and machine-readable signals."
    biggest_leak = blockers[0] if blockers else "A clear optimization opportunity remains."
    action_lines = [
        item.get("action", "")
        for item in actions[:3]
        if isinstance(item, dict) and item.get("action")
    ]

    return f"""<svg width="1280" height="860" viewBox="0 0 1280 860" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="1280" height="860" rx="36" fill="{BG}"/>
  <rect x="44" y="42" width="1192" height="776" rx="28" fill="{PANEL}"/>
  <rect x="78" y="78" width="1124" height="704" rx="22" fill="{SURFACE}"/>
  <text x="112" y="132" fill="{TEXT}" font-family="Menlo, Monaco, monospace" font-size="34" font-weight="700">Audit Snapshot</text>
  <text x="112" y="182" fill="{MUTED}" font-family="Menlo, Monaco, monospace" font-size="24">URL: {_escape(_trim(audit_data["url"], 76))}</text>
  <text x="112" y="220" fill="{MUTED}" font-family="Menlo, Monaco, monospace" font-size="24">Page type: {_escape(audit_data.get("page_type", "page"))}</text>
  <text x="112" y="258" fill="{MUTED}" font-family="Menlo, Monaco, monospace" font-size="24">Audit mode: {_escape(audit_data.get("audit_mode", "url-evidence"))}</text>
  <g>
    <rect x="112" y="304" width="220" height="112" rx="18" fill="{CARD_A}"/>
    <text x="140" y="350" fill="#E6FFFB" font-family="Menlo, Monaco, monospace" font-size="24">Overall</text>
    <text x="140" y="392" fill="#E6FFFB" font-family="Menlo, Monaco, monospace" font-size="42" font-weight="700">{audit_data["overall_score"]}/100</text>
  </g>
  <g>
    <rect x="360" y="304" width="180" height="112" rx="18" fill="{CARD_B}"/>
    <text x="390" y="350" fill="{TEXT}" font-family="Menlo, Monaco, monospace" font-size="24">SEO</text>
    <text x="390" y="392" fill="{TEXT}" font-family="Menlo, Monaco, monospace" font-size="42" font-weight="700">{scores["seo"]}</text>
  </g>
  <g>
    <rect x="560" y="304" width="180" height="112" rx="18" fill="{CARD_C}"/>
    <text x="590" y="350" fill="{TEXT}" font-family="Menlo, Monaco, monospace" font-size="24">GEO</text>
    <text x="590" y="392" fill="{TEXT}" font-family="Menlo, Monaco, monospace" font-size="42" font-weight="700">{scores["geo"]}</text>
  </g>
  <g>
    <rect x="760" y="304" width="180" height="112" rx="18" fill="{CARD_A}"/>
    <text x="790" y="350" fill="{TEXT}" font-family="Menlo, Monaco, monospace" font-size="24">AEO</text>
    <text x="790" y="392" fill="{TEXT}" font-family="Menlo, Monaco, monospace" font-size="42" font-weight="700">{scores["aeo"]}</text>
  </g>
  <g>
    <rect x="960" y="304" width="180" height="112" rx="18" fill="{CARD_B}"/>
    <text x="990" y="350" fill="{TEXT}" font-family="Menlo, Monaco, monospace" font-size="24">LLMO</text>
    <text x="990" y="392" fill="{TEXT}" font-family="Menlo, Monaco, monospace" font-size="42" font-weight="700">{scores["llmo"]}</text>
  </g>
  <text x="112" y="478" fill="{TEXT}" font-family="Menlo, Monaco, monospace" font-size="28" font-weight="700">Top Leaks</text>
  <text x="112" y="526" fill="{BODY}" font-family="Menlo, Monaco, monospace" font-size="24">- {_escape(_trim(biggest_leak, 78))}</text>
  <text x="112" y="564" fill="{BODY}" font-family="Menlo, Monaco, monospace" font-size="24">- {_escape(_trim(biggest_win, 78))}</text>
  <text x="112" y="624" fill="{TEXT}" font-family="Menlo, Monaco, monospace" font-size="28" font-weight="700">Priority Roadmap</text>
  <text x="112" y="672" fill="{BODY}" font-family="Menlo, Monaco, monospace" font-size="24">- {_escape(_trim(action_lines[0] if len(action_lines) > 0 else "Improve the weakest pillar first.", 78))}</text>
  <text x="112" y="710" fill="{BODY}" font-family="Menlo, Monaco, monospace" font-size="24">- {_escape(_trim(action_lines[1] if len(action_lines) > 1 else "Add stronger answer-first packaging.", 78))}</text>
  <text x="112" y="748" fill="{BODY}" font-family="Menlo, Monaco, monospace" font-size="24">- {_escape(_trim(action_lines[2] if len(action_lines) > 2 else "Strengthen reusable quoteable blocks.", 78))}</text>
</svg>
"""


def render_compare_preview(compare_data: dict) -> str:
    comparisons = compare_data.get("comparisons", [])[:3]
    blocks = []
    y = 226
    fills = [CARD_B, CARD_C, CARD_A]
    for index, item in enumerate(comparisons):
        blocks.append(
            f"""
  <rect x="112" y="{y}" width="1056" height="92" rx="18" fill="{fills[index % len(fills)]}"/>
  <text x="144" y="{y + 40}" fill="{TEXT}" font-family="Menlo, Monaco, monospace" font-size="24">{_escape(_trim(item["left_url"], 36))}</text>
  <text x="660" y="{y + 40}" fill="{TEXT}" font-family="Menlo, Monaco, monospace" font-size="24">{_escape(_trim(item["right_url"], 36))}</text>
  <text x="144" y="{y + 74}" fill="{BODY}" font-family="Menlo, Monaco, monospace" font-size="24">Overlap: {item["overlap_score"]:.2f}  ·  Risk: {item["risk"]}  ·  {_escape(_trim(item["note"], 62))}</text>
"""
        )
        y += 116

    recommendation = compare_data.get("summary", {}).get(
        "recommendation",
        "The set is reasonably differentiated, but medium-overlap pairs still deserve review.",
    )

    return f"""<svg width="1280" height="760" viewBox="0 0 1280 760" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="1280" height="760" rx="36" fill="{BG}"/>
  <rect x="44" y="42" width="1192" height="676" rx="28" fill="{PANEL}"/>
  <rect x="78" y="78" width="1124" height="604" rx="22" fill="{SURFACE}"/>
  <text x="112" y="132" fill="{TEXT}" font-family="Menlo, Monaco, monospace" font-size="34" font-weight="700">Compare Mode</text>
  <text x="112" y="182" fill="{MUTED}" font-family="Menlo, Monaco, monospace" font-size="24">{compare_data.get("url_count", 0)} URLs compared · overlap score · cannibalization-lite risk</text>
  {"".join(blocks)}
  <text x="112" y="614" fill="{TEXT}" font-family="Menlo, Monaco, monospace" font-size="28" font-weight="700">Recommendation</text>
  <text x="112" y="658" fill="{BODY}" font-family="Menlo, Monaco, monospace" font-size="24">{_escape(_trim(recommendation, 92))}</text>
</svg>
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate README SVG previews from demo JSON.")
    parser.add_argument("--audit-json", required=True)
    parser.add_argument("--compare-json", required=True)
    parser.add_argument("--audit-output", required=True)
    parser.add_argument("--compare-output", required=True)
    args = parser.parse_args()

    audit_data = json.loads(Path(args.audit_json).read_text())
    compare_data = json.loads(Path(args.compare_json).read_text())

    Path(args.audit_output).write_text(render_audit_preview(audit_data))
    Path(args.compare_output).write_text(render_compare_preview(compare_data))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

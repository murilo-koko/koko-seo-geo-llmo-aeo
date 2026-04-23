#!/usr/bin/env python3
"""Run a real URL smoke test using the repo's audit tooling."""

from __future__ import annotations

import argparse
import json
import sys

from server.integrations.seo_audit.lighthouse import run_lighthouse
from server.integrations.seo_audit.service import run_render_audit


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

    render = run_render_audit(args.url)
    lighthouse = run_lighthouse(args.url, preset=args.preset, timeout_s=120)

    payload = {
        "url": args.url,
        "final_url": render.final_url,
        "status_code": render.status_code,
        "ssr_words": render.ssr_words,
        "rendered_words": render.rendered_words,
        "flags": render.flags,
        "structured_data_types": [item.get("@type") for item in render.structured_data],
        "images": {
            "total": render.images.total,
            "missing_alt": render.images.missing_alt,
        },
        "links": {
            "internal": render.links.internal,
            "external": render.links.external,
        },
        "lighthouse": {
            "preset": args.preset,
            "performance_score": lighthouse.performance_score,
            "metrics": lighthouse.metrics,
            "top_opportunities": lighthouse.opportunities[:3],
            "error": lighthouse.error,
        },
    }
    json.dump(payload, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

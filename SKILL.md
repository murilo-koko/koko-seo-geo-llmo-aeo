---
name: koko-seo-geo-llmo-aeo
description: Audit a landing page, blog post, or draft content and score SEO, GEO, AEO, and LLMO with evidence-backed reasoning, clear confidence levels, and prioritized actions. Use this skill when the user wants an answer-engine readiness scorecard, a publishable content audit, or a shareable evaluation of how well a page performs for search, snippets, and LLM retrieval.
---

# Search Intelligence Audit

## Overview

Use this skill to evaluate a live URL or draft content for four dimensions:

- SEO: crawlability, structure, metadata, internal linking, schema, and technical performance
- GEO: generative engine optimization, including entity clarity, topical completeness, authority signals, and factual grounding
- AEO: answer engine optimization, including answer-first formatting, snippet readiness, FAQs, and extraction clarity
- LLMO: large language model optimization, including chunkability, quoteability, retrieval anchors, and semantic clarity

This skill is designed to produce a professional scorecard rather than vague commentary. It should prefer real evidence over intuition, separate hard findings from model judgment, and always explain why a score was assigned.

## Quick Start

This skill should work well for non-technical users.

Default input types:

- a live URL
- a draft article pasted into chat
- landing page copy pasted into chat
- 2 to 5 URLs for comparison
- a homepage URL for a sitewide-lite pass

Default expectation:

- do not ask the user to connect APIs
- do not require analytics access
- do not block on external setup

Preferred prompts:

- "Audit this URL for SEO, GEO, AEO, and LLMO"
- "Score this landing page and tell me what is leaking"
- "Review this blog draft before I publish it"
- "Compare these pages and tell me if they risk cannibalization"
- "Run a sitewide-lite audit from this homepage"

Read [references/public-prompts.md](references/public-prompts.md) when you need polished prompts for end users, demos, or marketplace copy.

## Workflow Decision Tree

Pick the strongest audit mode available:

1. `url-evidence`
   Use when a live URL is available.
   Base the analysis on rendered HTML, CWV, visible page structure, and on-page content.
   In this repo, prefer:
   - `seo_render_audit(url)`
   - `seo_cwv_audit(url, preset="mobile")`

2. `compare-pages`
   Use when the user provides 2 to 5 URLs and wants to understand overlap, differentiation, or cannibalization-lite risk.
   Read [references/compare-mode.md](references/compare-mode.md) before writing the final answer.

3. `sitewide-lite`
   Use when the user wants a first-pass website audit from a homepage or root URL.
   Read [references/sitewide-lite.md](references/sitewide-lite.md) before writing the final answer.

4. `content-only`
   Use when the user shares draft copy, markdown, or notes without a live URL.
   Score only what can be inferred from the content itself and reduce confidence accordingly.

Always state the chosen audit mode in the report.

## Evidence Collection

Collect evidence in this order:

1. Identify the page type: `blog`, `landing-page`, or `other`.
2. Capture the page goal in one sentence.
3. Gather technical evidence from the page or tools.
4. Gather content evidence from headings, body copy, FAQs, schema, and linking patterns.
5. Only then assign scores.

For `compare-pages`, collect evidence for each page first, then compare intent, overlap, and differentiation.

For `sitewide-lite`, inspect a small set of internal pages and prioritize the biggest structural issues over completeness.

Do not invent:

- page speed data
- rankings
- SERP features
- competitor coverage
- analytics evidence you did not actually observe

If evidence is missing, lower confidence and say what is missing.

## Scoring Method

Read [references/scoring-rubric.md](references/scoring-rubric.md) before scoring.

Apply the rubric as follows:

1. Score each sub-signal from `0` to `5`.
2. Sum the five sub-signals for each dimension.
3. Multiply by `4` to get a `0-100` score for that dimension.
4. Use the page-type weights from [references/page-modes.md](references/page-modes.md) to compute the overall score.

Scoring discipline:

- `90-100`: strong and difficult to improve without specialization
- `75-89`: solid but still leaving meaningful upside
- `55-74`: mixed, workable, but missing important signals
- `35-54`: weak and likely underperforming
- `0-34`: structurally compromised or largely absent

Never use decimals in the four pillar scores. Round the overall score to the nearest integer.

## Output Requirements

Read [references/output-contract.md](references/output-contract.md) before writing the final answer.

Every audit must return three layers:

1. A compact scorecard that looks clean in chat and in screenshots
2. A diagnostic breakdown with evidence
3. A prioritized action plan

Use [references/example-output.md](references/example-output.md) as the quality bar for tone and structure.

Always include:

- page type
- audit mode
- overall score
- SEO score
- GEO score
- AEO score
- LLMO score
- confidence: `low`, `medium`, or `high`
- short verdict
- top wins
- top blockers
- next actions

For `compare-pages`, also include:

- overlap score by page pair
- risk label by page pair
- what each page should own

For `sitewide-lite`, also include:

- pages sampled
- sitewide top issues
- pages that need attention first

When the user wants something shareable, also include the short `Public Scorecard` variant defined in the output contract.
If the user wants a format suitable for Instagram, screenshots, or a carousel, read [references/shareable-output.md](references/shareable-output.md) and shape the output accordingly.

## Evidence Sources

Read [references/evidence-sources.md](references/evidence-sources.md) before using outside data.

Rules:

- Prefer page evidence and repo-native technical evidence first.
- If you use live external evidence, name the source and make clear it is source-backed.
- If a source is unavailable, do not simulate its output.
- External sources should deepen the audit, not become a setup requirement.

## Practical Defaults

- For blog posts, reward answer-first structure, FAQs, internal linking, entity clarity, and durable topical coverage.
- For landing pages, reward offer clarity, proof, objection handling, retrieval-friendly sections, and tight semantic alignment between promise and page structure.
- Penalize content that is stylish but hard to extract, quote, or summarize.
- Penalize content that depends on visual context without enough textual grounding.
- Penalize pages that appear strong semantically but have weak crawl/index/performance evidence.

## Machine-Readable Summary

If the answer can support it, include the JSON object defined in [references/output-contract.md](references/output-contract.md). This keeps the audit reusable in automation, dashboards, and comparison workflows.

If the user wants shareable copy from the structured summary, you can also use [scripts/render_shareable_output.py](scripts/render_shareable_output.py) to turn a JSON audit summary into a public scorecard and carousel-ready markdown.

## Scope Guardrail

This public skill is intentionally integration-free by default.

- Do not require Search Console
- Do not require Google Analytics
- Do not require API keys
- Do not reduce the usefulness of the audit just because the user only has a URL

If the user later asks for an advanced or source-enriched version, you may mention that stronger evidence sources exist. But the default product experience should remain simple: provide a URL or content, receive a professional audit.

## Publishing Notes

For launch materials and positioning, use:

- [references/calibration-cases.md](references/calibration-cases.md) for example score bands grounded in real pages
- [references/instagram-launch-kit.md](references/instagram-launch-kit.md) for carousels, captions, and CTA copy

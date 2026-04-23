# Koko SEO GEO LLMO AEO

A public Codex skill that audits a landing page, blog post, or draft content and scores it across four dimensions:

- SEO
- GEO
- AEO
- LLMO

The goal is simple: paste a URL or draft, receive a professional scorecard, understand what is strong, what is leaking, and what to fix first.

## What It Does

This skill is designed for non-technical use by default.

It can:

- audit a live URL
- review a draft article before publishing
- review a landing page copy
- generate a compact scorecard
- generate a public scorecard for screenshots or social posts
- generate a carousel-ready summary for Instagram

It does not require Search Console, Google Analytics, or API setup to be useful.

## Scoring Model

The skill scores pages from `0-100` across:

- `SEO`: crawlability, structure, metadata, internal linking, schema, and performance
- `GEO`: generative engine optimization, including entity clarity and topical completeness
- `AEO`: answer engine optimization, including answer-first formatting and snippet readiness
- `LLMO`: large language model optimization, including chunkability, quoteability, and retrieval clarity

It returns:

- an Audit Snapshot
- a diagnostic breakdown
- a priority roadmap
- an optional Public Scorecard

## Installation

Clone this repository and link it into your Codex skills directory:

```bash
git clone https://github.com/murilo-koko/koko-seo-geo-llmo-aeo.git
ln -s /absolute/path/to/koko-seo-geo-llmo-aeo ~/.codex/skills/koko-seo-geo-llmo-aeo
```

Restart Codex after linking the skill.

## Example Prompts

Audit a live URL:

```text
Use $koko-seo-geo-llmo-aeo to audit https://example.com for SEO, GEO, AEO, and LLMO. Return the Audit Snapshot, top leaks, priority roadmap, and Public Scorecard.
```

Review a landing page:

```text
Use $koko-seo-geo-llmo-aeo to score this landing page and tell me what is leaking first.
```

Review a draft:

```text
Use $koko-seo-geo-llmo-aeo to review this draft before publication. Score SEO, GEO, AEO, and LLMO, then give me the top fixes.
```

## Repository Structure

- [SKILL.md](./SKILL.md): the main skill behavior and workflow
- [agents/openai.yaml](./agents/openai.yaml): Codex skill metadata
- [references/](./references/): rubric, demos, prompts, output contract, launch kit
- [scripts/](./scripts/): helper scripts for score computation, shareable output, and smoke tests
- [assets/](./assets/): skill icons

## Real Smoke Test

If you are working from the repo and want to test the URL-evidence layer directly:

```bash
uv run python scripts/smoke_test_url.py https://koko.ag/blog/grafico-de-retencao-reels-instagram
```

This collects render-audit and Lighthouse evidence and returns JSON.

## Included References

This repo already includes:

- public prompts in PT-BR and English
- demo audits
- score calibration examples
- Instagram launch copy

## Status

This is the first public release of the skill and is intentionally optimized for a no-integration workflow.

# Sitewide Lite

Use `sitewide-lite` when the user wants a lightweight site audit without a heavy crawler or API integrations.

## Scope

The goal is not to crawl hundreds of pages.

The goal is to:

- start from a root URL
- inspect a small set of internal pages
- surface the biggest structural issues quickly

Recommended sample size:

- `5` pages for a quick check
- `8-12` pages for a deeper lightweight pass

## Best Uses

- first-pass website audit
- homepage-led audit
- rapid pre-launch check
- identify the biggest leak on a site
- triage where a full audit would matter most

## What To Surface

- broken pages
- thin pages
- missing titles or descriptions
- weak H1 structure
- schema coverage patterns
- obvious page-type imbalance

## Output Requirements

Return:

- sampled pages
- top issues
- which pages need attention first
- whether the site looks structurally healthy or fragmented

## Example Prompt

```text
Use $koko-seo-geo-llmo-aeo to run a sitewide-lite audit from this homepage. Crawl a small set of internal pages and tell me the biggest structural issues first.
```

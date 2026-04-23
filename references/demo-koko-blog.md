# Demo Audit: Koko Blog Post

Audit date: `2026-04-23`
Source type: live URL
Audit mode: `url-evidence`
Page type: `blog`
Confidence: `medium`

Evidence snapshot gathered from the repo tooling:

- URL: `https://koko.ag/blog/grafico-de-retencao-reels-instagram`
- HTTP status: `200`
- Word count: `2448 SSR`, `2448 rendered`
- Flags: `1 image missing alt`
- Structured data types seen: `Organization`, `Article`, `BreadcrumbList`
- Links: `33 internal`, `7 external`
- Images: `19 total`, `1 missing alt`
- Mobile Lighthouse score: `64`
- CWV snapshot: `LCP 14.66s`, `FCP 3.76s`, `TBT 67ms`, `CLS 0`, `INP 80ms`
- Top Lighthouse opportunity: `Reduce unused JavaScript` with `1060ms` savings

Suggested scores:

- SEO: `76`
- GEO: `84`
- AEO: `88`
- LLMO: `79`
- Overall: `82`

Example report:

```markdown
## Audit Snapshot
- URL: https://koko.ag/blog/grafico-de-retencao-reels-instagram
- Page type: blog
- Audit mode: url-evidence
- Overall: 82/100
- SEO: 76
- GEO: 84
- AEO: 88
- LLMO: 79
- Confidence: medium
- Verdict: This is a strong answer-first article with excellent educational packaging, but its mobile speed still leaks more performance than the content quality deserves.

## What Is Working
- The article exposes all of its substance in SSR and rendered HTML, so search systems can access the full content cleanly.
- The page is structured as an explanatory asset instead of a vague opinion piece, which strongly helps AEO and GEO.
- The presence of `Article` and `BreadcrumbList` schema reinforces machine readability for a content page.

## What Is Limiting The Score
- Mobile performance is still the weakest area, with `LCP 14.66s` dragging down the technical side.
- The article is rich and practical, but some insights could be repackaged into tighter takeaway blocks for easier reuse in LLM-generated answers.
- There is still minor image hygiene debt with one missing alt.

## Priority Roadmap
- P1: Improve JS efficiency and above-the-fold loading on mobile. Impact: stronger SEO. Effort: M
- P1: Add a short takeaway or FAQ block near the end. Impact: stronger AEO and LLMO. Effort: S
- P2: Convert dense sections into more quoteable diagnostic statements. Impact: stronger LLMO and snippet extraction. Effort: S

## Public Scorecard
- Overall: 82/100
- Best pillar: AEO
- Weakest pillar: SEO
- Biggest win: The article answers a real user question clearly and structures the explanation in a reusable way.
- Biggest leak: Mobile performance is still too slow for a content asset this strong.
```


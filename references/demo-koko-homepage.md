# Demo Audit: Koko Homepage

Audit date: `2026-04-23`
Source type: live URL
Audit mode: `url-evidence`
Page type: `landing-page`
Confidence: `medium`

Evidence snapshot gathered from the repo tooling:

- URL: `https://koko.ag/`
- HTTP status: `200`
- Word count: `2246 SSR`, `2246 rendered`
- Flags: `1 image missing alt`
- Structured data types seen: `Organization`, `WebSite`, `ProfessionalService`, `FAQPage`
- Links: `40 internal`, `54 external`
- Images: `127 total`, `1 missing alt`
- Mobile Lighthouse score: `57`
- CWV snapshot: `LCP 13.37s`, `FCP 3.91s`, `TBT 292.5ms`, `CLS 0.0097`, `INP 261ms`
- Top Lighthouse opportunity: `Reduce unused JavaScript` with `890ms` savings

Suggested scores:

- SEO: `68`
- GEO: `78`
- AEO: `74`
- LLMO: `76`
- Overall: `74`

Example report:

```markdown
## Audit Snapshot
- URL: https://koko.ag/
- Page type: landing-page
- Audit mode: url-evidence
- Overall: 74/100
- SEO: 68
- GEO: 78
- AEO: 74
- LLMO: 76
- Confidence: medium
- Verdict: The homepage has strong semantic framing and useful answer structure, but mobile performance is weak enough to suppress a better overall score.

## What Is Working
- The page exposes its content fully in SSR and rendered HTML, which is a strong technical base for crawlability.
- The semantic layer is rich for a homepage, with `Organization`, `WebSite`, `ProfessionalService`, and `FAQPage` schema visible.
- The offer is described in accessible language rather than pure brand slogans, which helps GEO and LLM retrieval.

## What Is Limiting The Score
- Mobile performance is the main drag: `LCP 13.37s` is too high for a page meant to make a strong first impression.
- The page is broad and credible, but still not as explicit as it could be about who the offer is for and when a visitor should choose Koko.
- The homepage is visually rich, which helps persuasion, but some of the strongest claims could be packaged into more quoteable blocks for better reuse by answer engines and LLMs.

## Priority Roadmap
- P1: Reduce unused JavaScript and improve above-the-fold delivery. Impact: stronger SEO and first-visit conversion. Effort: M
- P1: Add a tighter one-sentence audience and offer definition near the hero. Impact: stronger GEO and AEO. Effort: S
- P2: Turn core differentiators into short standalone proof blocks. Impact: stronger LLMO and retrieval reuse. Effort: S

## Public Scorecard
- Overall: 74/100
- Best pillar: GEO
- Weakest pillar: SEO
- Biggest win: The page explains the business clearly and exposes rich semantic signals.
- Biggest leak: Mobile speed is too weak for the quality of the offer being presented.
```


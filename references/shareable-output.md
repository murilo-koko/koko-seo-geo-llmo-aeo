# Shareable Output

This skill should not stop at an internal audit. When the user wants something that is easy to publish, compare, or screenshot, compress the audit into one of these formats.

## 1. Screenshot Scorecard

Use this when the result will likely be shared as a single screenshot.

```markdown
## Public Scorecard
- URL: https://example.com/page
- Overall: 82/100
- SEO: 76
- GEO: 84
- AEO: 88
- LLMO: 79
- Confidence: medium
- Best pillar: AEO
- Weakest pillar: SEO
- Biggest win: The article answers the core question quickly and structures the topic in reusable sections.
- Biggest leak: Mobile performance is weak enough to drag down an otherwise strong content asset.
```

Rules:

- Keep it under 10 lines if possible.
- Avoid internal-only metrics.
- Use one sharp sentence for the win and one for the leak.

## 2. Comparison View

Use this when comparing multiple URLs.

```markdown
## Comparison
| Page | Overall | SEO | GEO | AEO | LLMO | Confidence |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| /blog/aeo-guide | 82 | 76 | 84 | 88 | 79 | medium |
| /demo | 74 | 68 | 78 | 74 | 76 | medium |
```

Rules:

- Order by overall score unless the user asks for a different sort.
- Use the same evidence standard across all compared URLs.

## 3. Carousel Summary

Use this when the user wants an Instagram-ready or carousel-ready version.

Recommended five-slide structure:

1. Slide 1: headline
   Example: `This page scores 82/100 for SEO, GEO, AEO, and LLMO`
2. Slide 2: what is working
3. Slide 3: what is leaking
4. Slide 4: top fixes
5. Slide 5: takeaway and CTA

Example:

```markdown
## Carousel Summary
### Slide 1
This article scored 82/100 for search and AI answer readiness.

### Slide 2
What is working:
- The answer appears early.
- The topic coverage is strong.
- The structure is easy to scan.

### Slide 3
What is leaking:
- Mobile performance is weak.
- Key takeaways are not packaged into enough quoteable blocks.

### Slide 4
Top fixes:
- Add an FAQ.
- Turn dense paragraphs into answer blocks.
- Improve JS efficiency on mobile.

### Slide 5
Takeaway:
Strong content can still leak reach if it is hard to load, extract, and reuse.
```

Rules:

- Keep each slide short enough to design without rewriting.
- Favor simple statements over technical jargon.
- Preserve the core score and one clear message.

## 4. Caption Variant

Use this when the user wants a social caption under the graphic.

Structure:

- first line: score + verdict
- short explanation of the best pillar
- short explanation of the weakest pillar
- one takeaway
- CTA

Example:

```markdown
Scored 82/100 for SEO, GEO, AEO, and LLMO.

Best pillar: AEO. The page answers the question quickly and clearly.
Weakest pillar: SEO. Mobile performance is still holding it back.

Takeaway: good content is not enough if search engines and LLMs cannot consume it efficiently.

Want me to score your page too?
```


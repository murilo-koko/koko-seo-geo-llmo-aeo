# Example Output

Use these examples as quality targets. Keep the structure, not the literal wording.

## Example 1: Blog Audit

```markdown
## Audit Snapshot
- URL: https://example.com/blog/aeo-guide
- Page type: blog
- Audit mode: full-evidence
- Overall: 81/100
- SEO: 84
- GEO: 79
- AEO: 86
- LLMO: 74
- Confidence: high
- Verdict: The article is highly answer-friendly and technically solid, but it still misses some retrieval-friendly packaging that would help LLM citation and reuse.

## What Is Working
- The page answers the main question near the top instead of hiding it in a long intro.
- H2 structure maps cleanly to adjacent user intents, which improves both scanability and topic coverage.
- Rendered HTML exposes the main body content, so search systems can see the substance without relying on client-side hydration.

## What Is Limiting The Score
- Definitions and takeaways are buried inside longer paragraphs instead of being packaged into standalone quoteable blocks.
- Internal links support navigation, but do not reinforce the next-step intents a reader would likely search next.
- There is no FAQ section to capture variants of the main query.

## Priority Roadmap
- P1: Add a 3-5 question FAQ below the core answer block. Impact: higher AEO and query coverage. Effort: S
- P1: Rewrite 3 dense sections into short definition or takeaway blocks. Impact: stronger LLMO and snippet extraction. Effort: S
- P2: Add internal links to adjacent intent pages. Impact: better SEO and GEO breadth. Effort: M

## Public Scorecard
- Overall: 81/100
- Best pillar: AEO
- Weakest pillar: LLMO
- Biggest win: The article gives a direct answer fast and backs it with useful structure.
- Biggest leak: Strong ideas are present, but not yet packaged into highly reusable answer blocks.
```

## Example 2: Landing Page Audit

```markdown
## Audit Snapshot
- URL: https://example.com/demo
- Page type: landing-page
- Audit mode: url-evidence
- Overall: 68/100
- SEO: 70
- GEO: 62
- AEO: 66
- LLMO: 73
- Confidence: medium
- Verdict: The offer is visible, but the page still relies too heavily on brand language and visuals instead of explicit, retrieval-friendly explanation.

## What Is Working
- The page has a clear primary CTA and a readable section hierarchy.
- Core benefits are visible above the fold.
- Product terminology is consistent enough to support retrieval.

## What Is Limiting The Score
- The page does not define the product clearly in one sentence for a first-time visitor.
- Proof exists, but it is scattered and not tied to concrete claims.
- Objections are implied rather than answered directly, which reduces answer-engine usefulness.

## Priority Roadmap
- P1: Add a one-sentence product definition and audience qualifier near the hero. Impact: stronger GEO and AEO. Effort: S
- P1: Add a proof section with explicit numbers, customer type, and outcome framing. Impact: stronger GEO and trust. Effort: M
- P2: Add a short FAQ covering pricing, fit, and implementation. Impact: stronger AEO and LLMO. Effort: M
```


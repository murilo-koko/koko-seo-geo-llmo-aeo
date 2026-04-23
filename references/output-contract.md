# Output Contract

Every audit should be usable in three contexts:

- decision-making inside a workflow
- comparison across multiple pages
- public demo or screenshot

Use this structure.

## 1. Audit Snapshot

Start with a compact scorecard:

```markdown
## Audit Snapshot
- URL: https://example.com/page
- Page type: blog
- Audit mode: full-evidence
- Overall: 78/100
- SEO: 82
- GEO: 74
- AEO: 80
- LLMO: 73
- Confidence: high
- Verdict: Strong organic foundation, but the page still hides some of its best answers from both snippets and LLM retrieval.
```

This first block should be tight and screenshot-friendly.

## 2. Why It Scored This Way

Follow with:

- `What is working`
- `What is limiting the score`
- `Evidence used`

Each point should be concrete, not generic.

Good:

- "The page answers the core question in the first screen and repeats it in list form later."
- "There is no visible FAQ or definition block, which lowers snippet readiness."

Weak:

- "The content could be better optimized."
- "SEO needs improvement."

## 3. Priority Roadmap

Group actions by urgency:

- `P1`: highest-leverage fixes
- `P2`: meaningful upgrades
- `P3`: polish or scaling work

Each action should include:

- action
- expected impact
- effort: `S`, `M`, or `L`

## 4. Public Scorecard

When the user wants something shareable, add this short variant:

```markdown
## Public Scorecard
- Overall: 78/100
- Best pillar: SEO
- Weakest pillar: LLMO
- Biggest win: Direct answer appears early and the page is technically clean.
- Biggest leak: Key expertise is present, but not packaged into quoteable, retrieval-friendly blocks.
```

Do not include sensitive metrics or internal account details in the public variant.

## 5. JSON Summary

When the context supports it, include this JSON object:

```json
{
  "url": "https://example.com/page",
  "page_type": "blog",
  "audit_mode": "full-evidence",
  "overall_score": 78,
  "scores": {
    "seo": 82,
    "geo": 74,
    "aeo": 80,
    "llmo": 73
  },
  "confidence": "high",
  "verdict": "Strong organic foundation, but the page still hides some of its best answers from both snippets and LLM retrieval.",
  "top_wins": [
    "Direct answer appears early.",
    "Heading structure is easy to scan.",
    "Technical rendering exposes most of the content."
  ],
  "top_blockers": [
    "Few quoteable standalone blocks.",
    "Weak FAQ coverage.",
    "Internal links do not reinforce adjacent intents."
  ],
  "next_actions": [
    {
      "priority": "P1",
      "owner": "content",
      "action": "Add a short answer block and FAQ near the top of the page.",
      "impact": "Increase snippet readiness and AEO.",
      "effort": "S"
    }
  ],
  "evidence": {
    "technical": [
      "Rendered HTML exposes the main content.",
      "Mobile CWV is acceptable but not elite."
    ],
    "search": [
      "Search Console shows traction on long-tail queries."
    ],
    "content": [
      "Definitions exist but are spread across long paragraphs."
    ],
    "external": []
  }
}
```

## Writing Style

- Be decisive without pretending to know what you do not know.
- Prefer one strong sentence over three vague ones.
- Name uncertainty explicitly.
- Keep the first screen clean enough that a founder or marketer can understand it in seconds.


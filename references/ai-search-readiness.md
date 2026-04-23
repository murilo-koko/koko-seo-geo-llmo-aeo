# AI Search Readiness

This skill now treats AI search readiness as a practical layer inside the audit, even without third-party APIs.

## What It Checks

- `llms.txt` presence at the site root
- quoteable short paragraph blocks
- list structure that improves chunkability
- FAQ-style headings
- structured data presence
- clean heading structure
- enough textual substance for passage-level reuse

## Why It Matters

Pages that are easy to crawl are not always easy to cite.

The goal here is not to pretend we can fully measure AI visibility from outside. The goal is to identify whether the page is structured in a way that improves reuse by answer engines and LLM-driven search products.

## Heuristic Score

The `ai_citation_readiness` heuristic is not a ranking metric.

Use it as:

- a packaging score
- a retrieval-friendliness score
- a prompt for what to restructure next

## Good Signs

- exactly one H1
- multiple short paragraphs with standalone meaning
- FAQ framing
- list blocks
- schema present
- canonical present
- `llms.txt` present

## Bad Signs

- dense unbroken paragraphs
- no list structure
- no FAQ or answer-first blocks
- no schema
- no canonical
- no `llms.txt`

# Compare Mode

Use `compare-pages` when the user provides 2 to 5 URLs and wants to know whether the pages overlap too much or compete for the same intent.

## Best Uses

- identify keyword cannibalization risk
- compare two landing pages
- compare similar blog posts
- separate parent page intent from child page intent
- review whether two pages should be merged, differentiated, or retargeted

## What To Look For

- similar page type
- similar title framing
- similar H1 framing
- overlapping top terms
- overlapping question or promise
- weak differentiation in audience, stage, or job-to-be-done

## Output Requirements

Return:

- short comparison summary
- overlap score by pair
- risk label: `low`, `medium`, or `high`
- why the pair overlaps
- what to do next

Good recommendations:

- differentiate by intent
- merge overlapping pages
- reposition one page as comparison, use case, or alternative
- shift one page to a narrower audience or keyword family

## Example Prompt

```text
Use $koko-seo-geo-llmo-aeo to compare these two URLs and tell me whether they risk cannibalization. I want overlap score, risk label, and what each page should own.
```


# Calibration Cases

Use these cases to keep score ranges grounded. They are not absolute truths. They are anchor examples for how the current rubric behaves on real pages.

Audit date: `2026-04-23`
Method: render audit plus Lighthouse mobile

## Suggested Bands

| URL | Page Type | Overall | SEO | GEO | AEO | LLMO | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `https://koko.ag/` | landing-page | 74 | 68 | 78 | 74 | 76 | Strong semantic framing, but mobile speed is a real drag |
| `https://koko.ag/blog/` | other | 71 | 74 | 66 | 68 | 72 | Fast enough and crawlable, but less content depth and answer packaging |
| `https://koko.ag/blog/grafico-de-retencao-reels-instagram` | blog | 82 | 76 | 84 | 88 | 79 | Strong answer-first article with solid reusable structure |
| `https://koko.ag/contato` | other | 69 | 78 | 60 | 72 | 64 | Technically healthy, but naturally limited for deep topical coverage |
| `https://koko.ag/servicos` | other | 73 | 74 | 72 | 70 | 76 | Good commercial framing with room for more retrieval-friendly specificity |
| `https://koko.ag/sobre` | other | 22 | 18 | 28 | 20 | 24 | Live 404 case, useful lower-bound anchor for broken URLs |

## Evidence Notes

- `https://koko.ag/` returned `200`, `2246` SSR words, `2246` rendered words, and mobile Lighthouse score `52`
- `https://koko.ag/blog/` returned `200`, `736` SSR words, `736` rendered words, and mobile Lighthouse score `75`
- `https://koko.ag/blog/grafico-de-retencao-reels-instagram` returned `200`, `2448` SSR words, `2448` rendered words, and mobile Lighthouse score `70`
- `https://koko.ag/contato` returned `200`, `687` SSR words, `687` rendered words, and mobile Lighthouse score `87`
- `https://koko.ag/servicos` returned `200`, `558` SSR words, `558` rendered words, and mobile Lighthouse score `76`
- `https://koko.ag/sobre` returned `404`, which makes it a useful failure-case anchor even without a fresh CWV run

## How To Use These Cases

- If a page is clearly stronger than the Koko blog example, it likely belongs above `82`
- If a page feels semantically strong but technically shaky like the homepage, it likely falls in the low-to-mid `70s`
- If a page is technically healthy but purposefully narrow like a contact page, avoid inflating GEO or LLMO
- If a URL is broken, missing, or non-indexable, keep the score harsh even if the visual shell looks acceptable


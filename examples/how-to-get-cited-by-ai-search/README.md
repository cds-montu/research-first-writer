# Example: "How to get cited by AI search" (blog, how-to)

A full, unattended run of the method on a competitive marketing keyword (en-US, run on 2026-11-01). Every step's output is kept, so you can trace any sentence in the article back to a page.

| Step | File | What happened |
|---|---|---|
| 1 Brief | [01-brief.md](01-brief.md) | How-to for marketers; no first-hand notes, so no testing claims |
| 2 Discover | [02-discover.md](02-discover.md) | 1 query, 20 results, 5 candidates kept; 4 primary sources added |
| 3 Score | [03-scores.md](03-scores.md) · [pages.json](pages.json) | 5 of 5 pages fetched; top score 91.2; engagement not observable (85% coverage) |
| 4 Analyse | [04-analysis.md](04-analysis.md) | **3 of 5 ranking pages contradict Google's own documentation**: that became the angle |
| 5 Baselines | [05-baselines.md](05-baselines.md) | benchmark, freshest, contrarian, gap |
| 6 Research brief | [06-research-brief.md](06-research-brief.md) | 6 must-covers, 4 differentiators, 24 facts with verbatim quotes |
| 7 Outline | [07-outline.md](07-outline.md) | 10 sections, crawler table, FAQ, checklist |
| 8–9 Write and edit | [article.md](article.md) | 1,530 words; the edit fixed one ungrounded number |
| 10–11 Judge and report | [review-report.md](review-report.md) | **0.85, pass**; not ready: 1 proof slot and the hero image wait for a person |

**What it teaches:** information gain often comes from checking the ranking pages against primary sources, not from writing more. None of the four baselines told readers that Googlebot, not Google-Extended, controls whether they can appear in AI Overviews.

Re-run the checks yourself:

```bash
python3 skills/research-first-writer/scripts/check_article.py examples/how-to-get-cited-by-ai-search/article.md
python3 skills/research-first-writer/scripts/score_pages.py examples/how-to-get-cited-by-ai-search/pages.json
```

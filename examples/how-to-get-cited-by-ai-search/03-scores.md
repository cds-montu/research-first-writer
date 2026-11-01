# 3. Read and score

All 5 shortlisted pages fetched (HTTP 200, none blocked). Signals observed on 2026-11-01 and scored with `skills/research-first-writer/scripts/score_pages.py pages.json`:

```

  score  cover  page
   91.2    85%  aioseo.com/how-to-get-cited-by-ai-search-tools/
               serp_rank=0.90  serp_coverage=1.00  depth=1.00  engagement=—  freshness=0.75  structure=0.80  eeat=0.90  media=1.00  ai_citation=—
   80.2    85%  sproutworth.com/how-to-get-cited-by-ai-search-engines/
               serp_rank=0.30  serp_coverage=1.00  depth=0.96  engagement=—  freshness=1.00  structure=1.00  eeat=0.90  media=0.75  ai_citation=—
   70.0    85%  magnet.co/posts/how-to-get-cited-by-ai-search
               serp_rank=1.00  serp_coverage=1.00  depth=0.40  engagement=—  freshness=0.75  structure=0.60  eeat=0.50  media=0.00  ai_citation=—
   69.1    85%  rohitprabhakar.com/blog/how-to-get-cited-by-ai-search-engines/
               serp_rank=0.00  serp_coverage=1.00  depth=1.00  engagement=—  freshness=1.00  structure=1.00  eeat=0.75  media=0.25  ai_citation=—
   61.8    85%  seojuice.com/blog/how-to-make-your-brand-come-up-in-chatgpt/
               serp_rank=0.00  serp_coverage=1.00  depth=1.00  engagement=—  freshness=0.25  structure=1.00  eeat=0.50  media=1.00  ai_citation=—

  — = not observable on a public page (left out, never guessed)

```

How the signals were read:
- **serp_rank:** position in q1 (1 is full marks, 0 from position 11). **serp_coverage:** 1 of 1 queries.
- **depth:** words against the median of the five (about 2,400). Magnet has about 950 words, so it scores 0.40.
- **engagement:** not visible on any page, so it is left out. Coverage is 85% for every page as a result.
- **freshness:** within 90 days scores 1, within a year 0.75, two years 0.5, older 0.25. SEOJuice's markup dates it to 2024-10-27, although its body text refers to 2026.
- **eeat:** named author, dates, and links out to sources. **media:** image count.

Set aside: none on quality grounds. Rohit Prabhakar's page is analysed but not chosen as a baseline (see step 5).

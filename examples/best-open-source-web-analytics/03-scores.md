# 3. Read and score

3 of 3 pages fetched. `python3 skills/research-first-writer/scripts/score_pages.py pages.json`:

```

  score  cover  page
   82.5   100%  alternativeto.net/software/google-analytics
               serp_rank=1.00  serp_coverage=1.00  depth=1.00  engagement=0.60  freshness=1.00  structure=0.60  eeat=0.25  media=1.00  ai_citation=—
   72.4    85%  zeabur.com/blogs/self-host-open-source-alternatives-to-google-analytics
               serp_rank=0.90  serp_coverage=1.00  depth=0.67  engagement=—  freshness=0.25  structure=0.60  eeat=0.50  media=1.00  ai_citation=—
   65.3    75%  selfhostyourself.com/alternative-to/google-analytics
               serp_rank=0.40  serp_coverage=1.00  depth=1.00  engagement=—  freshness=—  structure=0.50  eeat=0.10  media=1.00  ai_citation=—

  — = not observable on a public page (left out, never guessed)

```

- AlternativeTo is the only page with visible engagement (user likes and comments), scored medium confidence. It was last updated Aug 25, 2026.
- SelfHostYourself shows no publish date, so freshness is left out. Its per-tool commit dates describe the tools, not the page.
- Zeabur is dated December 8, 2023 and has no update, so it falls in the oldest freshness band.
- Median depth is about 750 words. All three pages are thin on analysis; the length comes from metadata.

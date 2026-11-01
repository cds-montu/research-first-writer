# 3. Read and score

5 of 5 pages fetched. `python3 skills/research-first-writer/scripts/score_pages.py pages.json`:

```

  score  cover  page
   80.4    85%  dev.to/nayankyada/nextjs-vs-astro-for-content-sites-and-blogs-an-honest-comparison-4jp5
               serp_rank=0.80  serp_coverage=1.00  depth=0.87  engagement=—  freshness=1.00  structure=0.80  eeat=0.50  media=0.25  ai_citation=—
   78.2    85%  blog.logrocket.com/astro-vs-next-js-ssg-vs-react/
               serp_rank=0.60  serp_coverage=1.00  depth=1.00  engagement=—  freshness=0.75  structure=0.60  eeat=0.60  media=1.00  ai_citation=—
   76.2    85%  eastondev.com/blog/en/posts/dev/20251202-astro-vs-nextjs-comparison/
               serp_rank=0.50  serp_coverage=1.00  depth=1.00  engagement=—  freshness=0.75  structure=1.00  eeat=0.60  media=0.25  ai_citation=—
   53.8    85%  cloudcannon.com/blog/astro-vs-next-js/
               serp_rank=0.00  serp_coverage=1.00  depth=1.00  engagement=—  freshness=0.25  structure=0.60  eeat=0.60  media=0.25  ai_citation=—
   48.1    75%  bejamas.com/stack/framework/astro-vs-next-js
               serp_rank=0.20  serp_coverage=1.00  depth=0.47  engagement=—  freshness=—  structure=0.90  eeat=0.10  media=0.00  ai_citation=—

  — = not observable on a public page (left out, never guessed)

```

- CloudCannon's dates conflict: the header says "Updated 12 Oct 2026" but the body says "Last updated September 1st 2023", and the page names Next.js 13.4 as the latest release. Freshness was scored from the body (the conservative reading).
- The dev.to post shows "edited Oct 14" with no year; its body refers to 2026. Scored fresh, at medium confidence.
- Bejamas shows no author or date, so freshness is left out (75% coverage).

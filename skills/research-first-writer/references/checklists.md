# Checklists and scoring

## Contents
1. Page-scoring signals
2. Choosing pages to read, and baseline roles
3. Outline checks
4. Draft checks
5. Number grounding
6. Originality
7. What "ready" means

## 1. Page-scoring signals

Score each page per signal from 0 to 1; the page score is the weighted mean of the signals that could be observed (weights renormalise over what exists). Always report **coverage** (how much of the core weight was observable) and **confidence** per signal.

| Signal | Weight | Measures | Confidence |
|---|---|---|---|
| serp_rank | 0.20 | Best search position: 1 is full marks, falling to 0 by position 11 | medium |
| serp_coverage | 0.15 | How many of the research queries returned the page | medium |
| depth | 0.15 | Word count against the median of the pages compared; under 300 words scaled down hard | high |
| engagement | 0.15 | Visible comments, shares, likes, views: structured data (high), the page (medium), text like "N views" (low) | varies |
| freshness | 0.10 | Last modified or published: within 90 days full marks, then 1 year, 2 years, older | medium or high |
| structure | 0.10 | H2 count (up to six), lists, tables, FAQ markup, H3s | high |
| eeat | 0.10 | Named author, dates, outside links, Article markup | medium |
| media | 0.05 | Images; videos count double | high |
| ai_citation | +0.20 bonus | Cited in AI answers (when a data source exists) | medium |

Engagement is missing on most public pages: show it as lower coverage, never guess it. Traffic and backlinks need paid data; leave them out rather than estimate.

## 2. Choosing pages to read, and baseline roles

Before spending effort reading a page: keep pages the requester named first, then the best scores; skip video, social, marketplace and community pages, pages under 300 words, pages that build their content in the browser (they come back thin), and a second page from a site already chosen. Read more candidates than you need, because some will block you.

Baselines: 3 to 5 pages, one per site, each with one role:
- **benchmark**: the page to match (exactly one)
- **depth**: the most thorough
- **freshest**: the most recently updated
- **gap**: covers what the others skip
- **contrarian**: a different angle worth answering
- **ai_cited**: cited in AI answers (only with data that shows it)

## 3. Outline checks

**Block** means fix it before writing. **Warn** goes in the report.

| Area | Check | Severity |
|---|---|---|
| Search | Title contains the keyword | block |
| | Meta title 60 characters or fewer, with the keyword | warn |
| | Meta description 70 to 160 characters | warn |
| | Slug: lower-case words joined by hyphens, 80 characters at most | block |
| Structure | First section is an H2; headings unique | block |
| | Number of H2s within the research advice | warn |
| | Keyword in at least one H2, but not in more than half (no stuffing) | warn |
| | At least 60% of sections open with a direct answer | warn |
| | Every secondary keyword placed somewhere | warn |
| Length | Word budgets add up to the target within 10% | warn; block beyond 25% |
| | No section over 35% of the words | warn |
| Kind | Listicle or alternatives: enough numbered entries; a number in the title matches | block |
| | Comparison: a table | block |
| | FAQ: at least 5 questions | block |
| | Review: a pros and cons section | block |
| | An FAQ or table when the research calls for one | warn |
| Research | At least 80% of must-cover topics addressed | block below |
| | High-priority reader questions answered | warn |
| | At least 2 differentiators delivered | block if none |
| | A proof slot when the research calls for first-hand or original data | block |
| | Every fact id used exists in the ledger | block |
| Media | Image and proof slots point at real sections; a hero image slot | block |
| Language and policy | No banned terms or claims | block |
| | Title and headings in the right script; no English leaking into other Latin-script languages | warn |
| | Expert-review note for medical, financial, legal or safety topics | block |
| | No heading copied word for word from a baseline | warn |

## 4. Draft checks

| Area | Check | Severity |
|---|---|---|
| Completeness | Every planned section written | block |
| | Total within 10% of target | warn; block beyond 25% |
| | Each section within 60 to 140% of its budget | warn |
| Keywords | Keyword in the first 100 words | warn |
| | Exact-keyword density 2.5% or less | warn; block above 4% |
| | Keyword or a close variant in at least two places | warn |
| Grounding | Every number grounded (section 5) | block |
| | Links only to the sources of facts used and the requester's own pages | block |
| | No banned terms; no placeholder text | block |
| Honesty | Every `[[NEEDS_HUMAN]]` item listed; proof slots without notes show a visible marker | warn |
| Format | Each section matches its planned format: list, table, steps, pros and cons, FAQ | block |
| Originality | See section 6 | block / warn |
| Style (English) | Reading ease 45 or more, grade 12 or less; the right US or British spelling; fewer than two stock phrases ("in today's fast-paced world"); opening sentences under 45 words; paragraphs under 130 words | warn |
| Language | Written in the right script | warn |

Allowed HTML for a clean CMS fragment: `p`, `ul`, `ol`, `li`, `strong`, `em`, `a`, `blockquote`, `br`, tables, and `h3` inside an H2 section. No classes, styles or scripts.

## 5. Number grounding

A number in the article must come from: a vetted fact in the ledger, the brand's facts, anything the requester wrote (notes, prompt, details, title, keyword), or the article's own title and headings.
- Whole numbers under 10 count as ordinary prose.
- Percentages, money amounts and decimals always need a source.
- A year within one of today is fine.
- A plain calculation on vetted numbers is allowed: a product ("5 seats at $12 is $60 a month"), a yearly total (×12), a clean quotient, or a sum or difference of two figures that are both 10 or more. A percentage can never be calculated.
- If the number cannot be traced: leave it out, or write `[[NEEDS_HUMAN: the figure for X]]`.

## 6. Originality

Against every page the research read:
- Block at a verbatim run of 14 words or more; warn from 10.
- Block when more than 20% of 5-word phrases are shared with any one source; warn from 10%.
- FAQ questions the outline requires are exempt (people phrase them the same way).
- Quotes of 25 words or fewer, credited, are fine.

## 7. What "ready" means

Ready for a human read-through only when all hold:
- nothing waits for a person (no `[[NEEDS_HUMAN]]` left),
- an image exists,
- no required check fails and the editor left nothing unresolved,
- the judge passed (overall ≥ 0.75, no dimension < 0.5, grounding ≥ 0.7).

Otherwise: "Not ready", with the reasons first, and the work kept.

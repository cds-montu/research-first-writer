# 2. Discover

## Reader questions
- Which is faster for a mostly static blog, and are the benchmark numbers real?
- How do I manage Markdown/MDX or CMS content in each?
- How do new posts go live without a full rebuild?
- Where can I host each, and what breaks with a pure static export?
- What changed recently (Next.js 16, Astro joining Cloudflare)?
- How hard is it to switch later?

## Queries (en-US)
| # | Query |
|---|---|
| q1 | Astro vs Next.js for blog content site |

## Ranking pages (q1)
| Pos | Page | Kept? |
|---|---|---|
| 1 | dev.to/whoffagents/… | no: a second dev.to page; the better-structured one (pos 3) was kept |
| 2 | reliasoftware.com | no: an agency services page |
| 3 | dev.to/nayankyada/… | yes |
| 5 | blog.logrocket.com/astro-vs-next-js-ssg-vs-react/ | yes |
| 6 | eastondev.com/…/20251202-astro-vs-nextjs-comparison/ | yes |
| 9 | bejamas.com/stack/framework/astro-vs-next-js | yes |
| 13 | cloudcannon.com/blog/astro-vs-next-js/ | yes (well known; check whether it is current) |

## Primary sources added
Astro docs (islands, content collections), Next.js docs (static exports, ISR), the Next.js 16 release post, both GitHub repositories, and the Cloudflare blog post on Astro.

**Checkpoint 1:** the pages agree on the verdict (Astro for content, Next.js for apps) but disagree on numbers and are often out of date. Decision: a comparison built on documented behaviour and current versions, with every benchmark claim checked for its method.

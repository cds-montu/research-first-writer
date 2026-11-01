# Review report

**Verdict: Not ready, but close.** The judge passed it (0.85). Two things wait for a person: one proof slot and the hero image.

## What needs a person
1. `[[NEEDS_HUMAN]]` in "How to tell whether it's working": before-and-after citation results from your own site. The run had no first-hand notes, so the article does not claim any testing.
2. Hero image: a diagram of reach → retrieve → choose (slot in the outline; not generated in this run).

## At a glance
1,530 words against a 1,500 target · 11 H2s · about 7 minutes to read · judge 0.85 (pass) · rule checks: 17 passed, 1 warning, 0 blocking

## Rule checks (`skills/research-first-writer/scripts/check_article.py`)
- **Edit pass 1:** the draft failed *Grounding*. The figure "2.5" in the before/after example was not in the ledger. Fixed by adding F24 with Plausible's own source.
- **Warning left open:** the NEEDS_HUMAN marker above.

## Judge
| Dimension | Score | Evidence (quoted from the article) | Issue |
|---|---|---|---|
| helpfulness (0.25) | 0.85 | "A robots.txt that stays visible in AI search but opts out of OpenAI's training looks like this" | No screenshots of where to find referral data in analytics |
| information gain (0.20) | 0.85 | "Two of the ranking guides tell readers to allow Google-Extended to appear in AI Overviews. Google's documentation does not support that." | None of the 4 baselines has the crawler map or the myth check |
| grounding (0.20) | 0.85 | "Ahrefs data, as reported by SEOJuice… These are vendor figures passed on second-hand" | F21–F23 are second-hand; a person could replace them with the primary Ahrefs reports |
| structure (0.10) | 0.85 | Every H2 opens with its answer; a table, code, steps and an FAQ | The FAQ partly repeats §2 |
| voice (0.10) | 0.80 | "The direction is solid: specific, sourced writing helps." | Slightly dry in §6 |
| trust (0.10) | 0.85 | "The precise percentages describe one experimental setup, not your site." | No first-hand data (see NEEDS_HUMAN) |
| originality (0.05) | 0.90 | Its own structure; no baseline heading reused | — |

**Overall 0.85**. Pass: at least 0.75, no dimension under 0.5, grounding at least 0.7.

## Must fix before publishing (most important first)
1. Supply the before-and-after citation data, or delete that paragraph.
2. Add the hero diagram.
3. Optional: replace the second-hand Ahrefs figures with links to Ahrefs' own reports.

## What it rests on
- Baselines: aioseo (benchmark), sproutworth (freshest), seojuice (contrarian), magnet (gap).
- Facts used: F1–F24 from `06-research-brief.md`. Every quote was checked against its page on 2026-11-01.

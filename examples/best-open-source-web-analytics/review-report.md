# Review report

**Verdict: Not ready.** The judge passed it (0.86), but one proof slot and the hero image wait for a person.

## What needs a person
1. `[[NEEDS_HUMAN]]` in "How these tools were chosen": setup time for each tool on the same VPS. The run had no first-hand install notes, so the article makes no "we installed" claims.
2. Hero image: screenshots from each tool's public demo (check each licence first).
3. Re-check prices before publishing. They were read on 2026-11-01 and change often.

## At a glance
1,594 words against a 1,800 target · 7 numbered picks plus a comparison table and FAQ · judge 0.86 (pass) · rule checks: 17 passed, 2 warnings, 0 blocking

## Rule checks (`skills/research-first-writer/scripts/check_article.py`)
- **Edit pass 1:** the exact keyword was missing from the first 100 words, and the draft was 24% under target (1,371 words). The edit rewrote the opening and added "What self-hosting really involves", a must-cover only one baseline touched, with 2 new ledger facts (R4, H5).
- **Warning left open on purpose:** 11% under target. Every pick is covered; padding to 1,800 would lower helpfulness, and the method throws away edits that make things worse.

## Judge
| Dimension | Score | Evidence | Issue |
|---|---|---|---|
| helpfulness (0.25) | 0.85 | "Do you want to run a server at all? If not, pick Plausible or Umami Cloud" | No screenshots of the dashboards |
| information gain (0.20) | 0.85 | "One popular directory says "less than 1KB", which is wrong." | Prices, licences and self-host limits appear in none of the baselines |
| grounding (0.20) | 0.90 | Every figure is from the vendor's own page and listed in the ledger | PostHog paid prices could not be read, so they are left out rather than guessed |
| structure (0.10) | 0.90 | Identical fields for every pick, then a table | — |
| voice (0.10) | 0.80 | "a small project means a small bus factor" | Some entries read like spec sheets |
| trust (0.10) | 0.85 | "Every figure below comes from the project's own repository or pricing page, read on November 1, 2026." | No first-hand use |
| originality (0.05) | 0.90 | No baseline heading reused | — |

**Overall 0.86**. Pass.

## What it rests on
Baselines: alternativeto (benchmark), selfhostyourself (depth), zeabur (gap). 27 facts (U1–O2, plus R4 and H5), each with a verbatim quote and URL.

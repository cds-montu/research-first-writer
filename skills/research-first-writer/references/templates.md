# Templates

## Contents
1. Brief
2. Research brief
3. Outline
4. Review report
5. Worked example (short)

## 1. Brief

```
Keyword / topic:
Kind: blog | listicle | comparison | alternatives | faq | review
Goal: teach | help choose | get sign-ups | build trust | other: ...
Kind-specific: (listicle: number of picks / comparison: criteria / alternatives: for whom / faq: number of questions / review: verdict style / blog: angle)
Readers: who, how much they know, their biggest worry
Tone of voice:
Length: ~800 | ~1,500 | ~2,500 | default for the kind
Market: country, language
Brand: name, how to mention it, facts that may be stated, words to avoid, claims to avoid
First-hand notes (the only first-hand material): ...
Competitor pages to read first:
Own pages the article may link to (URL | anchor idea):
```

## 2. Research brief

```
Intent: informational | commercial | transactional | navigational | mixed
Target length: N words (and why, from the baselines' median)
Baselines: page — role — one-line reason (3 to 5)

Must cover (topic — why — seen in N of M baselines)
Differentiators (idea — why it sets us apart — type: gap | original data | first-hand | angle | format)
Reader questions (question — priority high | medium | low)
Terms (term — plain definition)
Pitfalls (what the ranking pages get wrong or what to avoid)
Facts ledger (id — fact — kind — source URL — credited to — quote ≤ 25 words)
Structure advice: format; H2 min–max; comparison table yes/no; FAQ yes/no
Sensitive topic (medical, financial, legal, safety): yes/no
```

## 3. Outline

```
Title:                      Meta title (≤ 60):
Meta description (70–160):  Slug:
Search intent:              Target keyword:   Secondary keywords:
Intro: hook — direct answer (1–2 sentences) — words
Sections (in order):
  H2/H3 — heading — purpose — direct answer — points (3–6) — words — format (prose | list | table | steps | faq | pros_cons)
         — covers (must-covers) — answers (questions) — differentiators — fact ids
Image slots: placement (intro or a heading) — kind (hero | diagram | chart | illustration | screenshot) — idea
Proof slots: placement — kind (first-hand | original data | expert quote) — what the person must supply
Sensitive-topic note (if needed):
Check: budgets add up to the target ±10%; no section > 35%; kind rules met; ≥ 80% must-covers; ≥ 2 differentiators
```

## 4. Review report

```
Verdict: Ready for a human read-through | Not ready — reasons first
What needs a person: each [[NEEDS_HUMAN]] item and where it goes; missing image; unresolved checks
At a glance: words vs target · sections · reading time · judge score · checks passed
Judge: overall, pass/fail, and per dimension: score — quoted evidence — issues
Must fix (most important first): section — problem — suggestion
Checks failing: id — severity — message
What it rests on: baselines and their roles; facts used with sources
```

## 5. Worked example (short)

From an early automated run: keyword "best crm for small business", listicle, en-US. Full runs with every step written out live in this repository's `examples/` folder.

- Discover: 4 reader questions, 4 queries, 6 candidate pages.
- Read and score: 5 of 6 pages fetched (one refused), 5 scored, 4 chosen to read; top score 81.5.
- Analyse: 4 of 4 pages analysed, 44 verified claims; 1 claim dropped because its quote was not on the page.
- Baselines: 3, with the roles benchmark, freshest and contrarian.
- Research brief: 9 must-cover topics, 7 differentiators, 20 facts in the ledger, about 1,800 words.
- Outline: "Best CRM for Small Business: 8 Picks for Teams of 1–20 (2026)", 8 H2 sections, about 1,805 words, 25 of 27 checks passing.
- Draft and edit: 2,196 words in 17 sections, edited down to 1,969 in 2 passes; 19 of 20 final checks pass.
- Judge: overall 0.67, so not passed: below 0.75 overall and grounding 0.6, below 0.7. One revision was tried.
- Report: Not ready. The judge's reasons come first, then 12 items marked for a person (proof the writer could not supply without first-hand notes) and 2 issues the editor left open. The article and report were still produced, so a person can finish it.

The lesson it teaches: without first-hand notes, an honest article leaves many proof markers, and grounding is where a draft most often falls short. Collect the notes at the brief.

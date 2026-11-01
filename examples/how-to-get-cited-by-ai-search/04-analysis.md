# 4. Analyse

Quotes are verbatim, 25 words or fewer, and were checked against the fetched page.

## aioseo.com: "How to Get Cited by ChatGPT, Perplexity, and AI Search Tools"
- **Angle:** a WordPress and plugin how-to covering crawler access, llms.txt, schema, answer-first structure and tracking. **Format:** about 2,400 words, 6 H2s, 4 FAQs. **Level:** beginner.
- **Strengths:** concrete robots.txt `Allow` lines; concrete tracking steps (GA4 referral sources, server logs); a named author and reviewer, with an update date (Jun 25, 2026).
- **Weaknesses:** heavy product promotion. The 3.2x schema figure links to a Medium post. It treats Google-Extended as the switch for AI Overviews, which Google's own documentation contradicts.
- **Claims:**
  - "Only 11% of domains receive citations from both ChatGPT and Perplexity" (credited to Averi)
  - "sites using structured data markup are cited 3.2 times more often than those without it" (Medium post; **not used**, weak source)

## sproutworth.com: "How to Get Cited by AI Search Engines: A B2B Playbook"
- **Angle:** a B2B framework of "7 content signals", with a table of engine differences. About 2,300 words, 7 FAQs. Updated Oct 13, 2026.
- **Strengths:** a clear step framework, a cross-engine comparison table, and linked sources for several statistics.
- **Weaknesses:** "Google AI Overviews responds most strongly to schema markup signals" has no source and conflicts with Google. A 2024 Gartner forecast is presented as current fact. Crawler access is not covered at all.

## seojuice.com: "How to Get Your Brand Cited by ChatGPT, Perplexity, and Google AI"
- **Angle:** contrarian, retrieval first. Citations depend on entering the engine's fan-out searches, and schema is secondary. About 2,900 words.
- **Strengths:** a clear explanation of fan-out, honest caveats about schema, and a sample tracking sheet.
- **Weaknesses:** links to none of the research it cites, and gives no crawler guidance.
- **Claims (Ahrefs data, as reported here, second-hand):**
  - "found that 76% of AI Overview citations came from pages already ranking in Google’s top 10 organic results"
  - "only 12% of URLs cited by ChatGPT, Gemini, Copilot, and Perplexity ranked in Google’s top 10 for the original prompt"

## magnet.co: "How to Get Cited by AI Search"
- **Angle:** an agency editorial: "be the source", with evidence and standalone passages. About 950 words, no statistics.
- **Strengths:** matches Google's guidance and links to it; gives a usable "lift test" for standalone passages; invents no numbers.
- **Weaknesses:** thin on mechanics (no crawler names, robots.txt or measurement tools); no named author.

## rohitprabhakar.com: "How to Get Cited by AI Search Engines in 2026"
- **Strengths:** a ready robots.txt block, tactics for each platform, and a measurement framework.
- **Weaknesses:** tells readers to "Allow `Google-Extended` in robots.txt" to appear in AI Overviews. It credits "Adding statistics alone improves AI citation visibility by 41%" to "Princeton/Georgia Tech". In the paper, 41% is the best method's figure, and Georgia Tech is not among the authors' affiliations. Most of its statistics are unlinked.

## Cross-check against primary sources (the gap)
| Claim on ranking pages | Primary source says | Pages making the claim |
|---|---|---|
| Allow Google-Extended to appear in AI Overviews | Googlebot's robots.txt rules control Search; Google-Extended covers "AI training and grounding in some of Google's other systems" | aioseo, rohitprabhakar |
| Schema markup drives AI Overview citations | "There's also no special schema.org structured data that you need to add." | sproutworth, rohitprabhakar |
| Add llms.txt | "You don't need to create new machine readable files, AI text files, or markup" | aioseo, rohitprabhakar |
| Statistics alone give 41% | Best methods 30–40%; 41% is the best method on one metric | rohitprabhakar |

1 claim dropped: Magnet's attribution of an llms.txt statement to Google could not be found on the Google page that was read.

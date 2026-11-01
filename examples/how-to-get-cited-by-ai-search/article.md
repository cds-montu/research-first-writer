---
title: "How to Get Cited by AI Search: A Source-Checked Guide (2026)"
meta_title: "How to Get Cited by AI Search: A Source-Checked Guide"
meta_description: "Which crawlers to allow, how answer engines choose passages, and which AI-SEO tips Google, OpenAI and Perplexity contradict. With a 30-minute checklist."
slug: how-to-get-cited-by-ai-search
keyword: get cited by ai search
kind: blog
target_words: 1500
---

## The short answer

To get cited by AI search, a page has to clear three hurdles. The engine must be able to reach it, find it when it searches, and lift a clear, specific answer from it. That means letting the right crawlers in, covering the sub-questions behind a prompt, and writing passages that make sense on their own and name their sources.

Much of the "AI SEO" advice in circulation goes further than the engines do. Google states that "there are no additional requirements to appear in AI Overviews or AI Mode, nor other special optimizations necessary." This guide checks the advice that ranks for this topic against what Google, OpenAI and Perplexity document, and against the research paper most guides cite. Where the two disagree, this guide follows the primary source.

## What it takes to get cited by AI search

An answer engine cites a page in three stages, and each stage fails in its own way.

1. **Reach.** A crawler must be allowed to fetch the page. If it is blocked, nothing else matters.
2. **Retrieve.** For one prompt, the engine runs several searches (often called fan-out) and collects candidate pages. A page that ranks for none of those searches is never considered.
3. **Choose.** From the candidates, the engine picks passages that answer the question and links them. Vague passages lose to specific ones.

The data on stage 2 is easy to misread. Ahrefs data, as reported by SEOJuice, found that 76% of AI Overview citations came from pages already in Google's top 10. The same report says only 12% of URLs cited by ChatGPT, Gemini, Copilot and Perplexity ranked in the top 10 *for the original prompt*. Both can be true: the engines search for more than the words the user typed. These are vendor figures passed on second-hand, so treat them as direction rather than law. Engines also differ from each other: a vendor analysis cited by AIOSEO found that only 11% of domains were cited by both ChatGPT and Perplexity.

## Step 1: Let the right crawlers in

Each engine runs separate crawlers for search, for model training and for fetches a user asks for. Only the search crawler decides whether you can be cited, and the engines document each one:

| Engine | Crawler behind citations | Separate training crawler | User-triggered fetcher |
|---|---|---|---|
| Google AI Overviews, AI Mode | **Googlebot** (normal Search crawling) | Google-Extended: covers "AI training and grounding in some of Google's other systems" | — |
| ChatGPT search | **OAI-SearchBot** | GPTBot | ChatGPT-User: "robots.txt rules may not apply" |
| Perplexity | **PerplexityBot** | none: PerplexityBot "is not used to crawl content for AI foundation models" | Perplexity-User: "generally ignores robots.txt rules" |

Two consequences follow. First, blocking a training crawler does not remove you from answers. OpenAI says a site can "allow OAI-SearchBot in order to appear in search results while disallowing GPTBot." Second, for Google, Search access runs through Googlebot. Google calls Googlebot's robots.txt rules "the control for site owners to manage access to how their sites are crawled for Search." Two of the ranking guides tell readers to allow Google-Extended to appear in AI Overviews. Google's documentation does not support that.

A robots.txt that stays visible in AI search but opts out of OpenAI's training looks like this:

```
User-agent: OAI-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: GPTBot
Disallow: /
```

OpenAI says changes take about 24 hours to apply; Perplexity says up to 24 hours. For Google, a page must be "indexed and eligible to be shown in Google Search with a snippet". A `nosnippet` tag therefore removes the very text an AI answer would quote.

## Step 2: Rank for the questions behind the question

Engines cite pages that answer the sub-questions, not only the headline query. To cover them:

1. Write down the prompt your reader would type, in their words.
2. List the 5 to 10 questions hidden inside it. For "best CRM for a small team", that includes price per seat, whether it has a free plan, how hard the setup is, and whether it works with the email tools the team already uses.
3. For each question, find the passage on your site that answers it. Where none exists, write one.
4. Search each sub-question yourself and note who ranks. Those pages are the competition at the retrieve stage.

This is ordinary SEO aimed at a wider set of queries, which is why Google says its usual guidance applies.

## Step 3: Write passages an engine can lift

An engine quotes passages, not pages. A good passage passes a lift test: copy it into a blank document and check that it still says what it means, about what, and according to whom.

- **Answer first.** Put the direct answer in the opening sentence of the section, then explain.
- **Name the subject.** Write "Plausible's script" and not "it", so the passage survives being cut out.
- **Be specific and attributed.** A number with a source and a date beats an adjective.

Compare these two passages:

> *Before:* It's really lightweight, so your site will stay fast.
>
> *After:* Plausible's tracking script is 2.5 KB, according to Plausible's own documentation.

Only the second can stand alone as an answer. (The figure comes from Plausible's own page: see the [open-source analytics example](../best-open-source-web-analytics/article.md).)

## What the GEO research shows, and what it doesn't

Most guides cite one study: *GEO: Generative Engine Optimization* by Aggarwal and colleagues, published at KDD 2024. It is worth reading the study itself.

- **What it found.** The paper reports that optimisation "can boost visibility by up to 40% in generative engine responses." Its best methods were citing sources, adding quotations and adding statistics, which "achieved a relative improvement of 30-40%" on its main metric. Keyword stuffing "don't perform well." A test on Perplexity.ai showed improvements "up to 37%".
- **How it measured.** The main experiments used a simulated engine. It drew on the top five Google results, generated answers with GPT-3.5, and scored visibility with GPT-3.5 as well. "Visibility" means how much of the answer draws on your text. It does not count clicks or traffic.
- **A common misquote.** One ranking guide says adding statistics alone raises visibility by 41%. In the paper, 41% is the improvement of the *best* methods on one metric. The guide also credits Georgia Tech, which is not among the authors' affiliations (Princeton, IIT Delhi and independent researchers).

The direction is solid: specific, sourced writing helps. The precise percentages describe one experimental setup, not your site.

## Four myths the ranking guides repeat

- **"Add llms.txt."** Google says: "You don't need to create new machine readable files, AI text files, or markup to appear in these features." OpenAI's and Perplexity's crawler documentation does not mention llms.txt either.
- **"AI Overviews favour schema."** Google says: "There's also no special schema.org structured data that you need to add." Structured data describes your page; it does not buy entry to AI answers.
- **"Allow Google-Extended to appear in AI Overviews."** As shown above, Google ties Search to Googlebot. Google-Extended limits training and grounding in other Google systems.
- **"Citations take 4 to 8 weeks."** None of the guides that say this gives a source. Google's own wording is that crawling "can take anywhere from several days to several months."

## How to tell whether it's working

1. Pick 10 prompts your readers really ask. Run them in ChatGPT search, Perplexity and Google every month, and record which URLs are cited.
2. Watch for referral visits from the answer engines in your analytics.
3. Check your server logs for OAI-SearchBot and PerplexityBot hits on the pages you care about. No hits means a problem at the reach stage.

[[NEEDS_HUMAN: before-and-after citation results from running your own priority prompts, with dates, to show the method working on a real site]]

## A 30-minute checklist

1. Open robots.txt and confirm that Googlebot, OAI-SearchBot and PerplexityBot are not blocked.
2. Decide separately whether to allow the training crawlers (GPTBot, Google-Extended).
3. Remove `nosnippet` from pages you want quoted.
4. Pick one priority page and list the sub-questions it should answer.
5. Rewrite each section to answer first, in a passage that survives the lift test.
6. Replace every unsourced adjective with a number and its source, or cut it.
7. Set up the monthly prompt check above.

## FAQ

### Do I need to rank on Google to be cited by ChatGPT?

Not for the exact prompt. Ahrefs data reported by SEOJuice found that only 12% of cited URLs ranked in the top 10 for the original prompt. Ranking for the sub-questions the engine searches is what counts.

### Does blocking GPTBot remove me from ChatGPT search?

No. OpenAI documents GPTBot (training) and OAI-SearchBot (search) as independent settings, so you can block one and allow the other.

### Is llms.txt worth adding?

Not for Google: it says no AI text files are needed. Neither OpenAI's nor Perplexity's crawler documentation mentions it. It costs little, but do not expect it to change anything.

### How long until changes show up?

Robots.txt changes reach OpenAI in about 24 hours and Perplexity in up to 24 hours. Recrawling and re-ranking take longer: Google says from several days to several months.

## Sources

- Aggarwal et al., [GEO: Generative Engine Optimization](https://arxiv.org/abs/2311.09735), KDD 2024
- Google Search Central, [AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)
- OpenAI, [Overview of OpenAI crawlers](https://developers.openai.com/api/docs/bots)
- Perplexity, [Perplexity crawlers](https://docs.perplexity.ai/guides/bots)
- SEOJuice, [How to get your brand cited by ChatGPT, Perplexity, and Google AI](https://seojuice.com/blog/how-to-make-your-brand-come-up-in-chatgpt/) (reporting Ahrefs data)
- AIOSEO, [How to get cited by ChatGPT, Perplexity, and AI search tools](https://aioseo.com/how-to-get-cited-by-ai-search-tools/) (reporting Averi data)

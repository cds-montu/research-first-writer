---
title: "Best Open Source Web Analytics Tools: 7 Picks Compared (2026)"
meta_title: "7 Best Open Source Web Analytics Tools (2026)"
meta_description: "Umami, Plausible, Matomo, PostHog and three more, compared on licence, stack, cookies and hosted price, all taken from each project's own pages."
slug: best-open-source-web-analytics-tools
keyword: open source web analytics tools
kind: listicle
target_words: 1800
---

## The short answer

Of the open source web analytics tools worth running in 2026, **Umami** is the easiest for most small sites to host yourself: it is MIT-licensed, cookieless, and needs only Node.js and PostgreSQL. Choose **Plausible** if you would rather pay a little for a hosted, lightweight service. Choose **Matomo** if you need Google Analytics-level depth, and **PostHog** if you are measuring a product rather than a website.

The pages that rank for this topic are directories and older roundups. They list tools without the facts that decide whether you will still be happy with one in a year: the licence, the server it needs, whether it sets cookies, and what the hosted plan costs. Every figure below comes from the project's own repository or pricing page, read on November 1, 2026.

## How these open source web analytics tools were chosen

- **Open source code you can self-host.** The tool has a public repository and a documented self-hosted install.
- **Built for website traffic.** Product-analytics suites are included only if they also do page analytics well (PostHog). Tools that are mainly for mobile apps, surveys or log files were left out.
- **Alive.** Every pick has an active repository.
- **Ordered by fit for a typical small or mid-size site,** not by GitHub stars.

[[NEEDS_HUMAN: setup time for each tool on the same small VPS, from a real install, to back up the "easy to run" claims with first-hand data]]

## 1. Umami: the simplest to run yourself

Umami shows the essentials (pages, referrers, countries, devices) on one clean dashboard, and it is the lightest pick to operate.

- **Licence:** MIT, so you can use, modify and resell it freely. 39.8k GitHub stars.
- **Stack:** "A server with Node.js version 18.18+" and "a PostgreSQL database version v12.14+".
- **Cookies:** none. Umami says it "does not use cookies or collect any personally identifiable information."
- **Hosted:** a free Hobby plan for up to 100K events a month; Pro costs $20 a month.

**The catch:** reporting is deliberately simple. If your marketing team relies on funnels and custom reports, look at Matomo or PostHog instead.

## 2. Plausible: the best hosted option, with a script that stays small

Plausible is privacy-first analytics with a polished hosted service and a self-hosted Community Edition.

- **Licence:** AGPL-3.0. You can self-host and modify it. If you change it and offer it to others over a network, the AGPL requires you to share your changes.
- **Stack:** Elixir and Phoenix, with "PostgreSQL (general data), ClickHouse (analytics)". Running two databases is the main self-hosting cost.
- **Cookies:** "no cookies or persistent identifiers are used."
- **Script size:** Plausible's own figure is 2.5KB, against 135KB gzipped for the Google Analytics script. One popular directory says "less than 1KB", which is wrong.
- **Hosted:** from $9 a month for up to 10k monthly pageviews, with a 30-day free trial.

**The catch:** the self-hosted edition has fewer features. Plausible says "marketing funnels, user journeys, ecommerce revenue goals, SSO and sites API are not available" there.

## 3. Matomo: the full Google Analytics replacement

Matomo is the long-standing, full-featured option, with goals, e-commerce tracking, segments and a plugin system. It is the tool most directories put first.

- **Licence:** GPL v3 or later. 22.0k GitHub stars.
- **Stack:** PHP 8.1.0 or greater, and MySQL 8.0+ or MariaDB 10.6+. Any ordinary PHP host can run it.
- **Cookies:** matomo.org's own deployment sets a visitor-ID cookie (`_pk_id`) for 13 months. Check your configuration and consent requirements before launch.
- **Hosted:** Matomo Cloud lists 29 a month (excluding tax) for 50,000 hits; the pricing page doesn't show the currency. There is a 21-day trial, and On-Premise is "Free forever".

**The catch:** depth brings weight. Expect more setup, more settings and more database growth than with the lighter tools.

## 4. PostHog: for products, not just pages

PostHog combines web analytics with product analytics, session replay, feature flags and experiments in one platform.

- **Licence:** MIT expat for most of the repository; the `ee` directory is licensed separately. 40.6k GitHub stars.
- **Hosted:** the cloud plan includes your first 1 million events and 5k recordings each month for free.
- **Self-hosting:** PostHog says open source deployments "should scale to approximately 100k events per month". They need something like 4 vCPU, 16GB RAM and more than 30GB of storage, and come with no customer support.

**The catch:** self-hosting PostHog is a project in itself. For most teams, the free cloud tier is the sensible way in. Choose it only if you need product analytics; it is more than a traffic counter needs.

## 5. Rybbit: the newer all-rounder

Rybbit is a newer, cookieless tool that covers both web and product analytics, and has grown quickly to 13.2k GitHub stars.

- **Licence:** AGPL-3.
- **Stack:** built on ClickHouse. The self-hosting guide asks for a VPS with at least 2GB of RAM.
- **Cookies:** "No cookies & privacy friendly."
- **Script size:** 11 KB, per Rybbit's site. That is larger than Plausible or GoatCounter.
- **Hosted:** Standard costs $13 a month billed annually and Pro $26 a month, with a 7-day free trial.

**The catch:** it is younger than Matomo or Plausible, so it has a shorter track record and a smaller ecosystem.

## 6. GoatCounter: the smallest footprint, free to host

GoatCounter is a one-developer project in Go that does simple counting extremely well.

- **Licence:** a slightly modified EUPL 1.2. Read it if you plan to redistribute the code. 6.1k GitHub stars.
- **Stack:** a single Go binary. It needs only "somewhere to store a SQLite database file or a PostgreSQL connection."
- **Cookies:** it identifies unique visits "without cookies".
- **Script size:** about 3.5KB.
- **Hosted:** goatcounter.com is "offered for free for reasonable public usage". A directory still says "free for non-commercial use", which is out of date.

**The catch:** a small project means a small bus factor. Donate if you rely on it.

## 7. Open Web Analytics: for PHP shops that want a framework

Open Web Analytics (OWA) is a framework-style tool with CMS integrations, aimed at people who want to extend their analytics in PHP.

- **Licence:** GNU GPL v2 or later. 2.7k GitHub stars.
- **Stack:** PHP 8.2 or later and MySQL 5.7 or later.
- **Cookies:** yes. Its tracker sets a visitor-id cookie for 364 days by default.
- **Hosted:** none. It is self-hosted only.

**The catch:** it has the smallest community on this list and sets cookies by default. Choose it for PHP extensibility, not for privacy.

## What self-hosting really involves

Every tool on this list is free to download, but self-hosting is not free to run. What you take on depends mostly on the database underneath.

- **One ordinary database (Umami, Matomo, Open Web Analytics, GoatCounter).** PostgreSQL, MySQL or even a single SQLite file. Any small server or shared host your team already uses can carry these, and backups are routine.
- **ClickHouse (Plausible, Rybbit).** A column store built for fast analytics queries. It is excellent at scale but adds a second database to patch, monitor and back up. It also has hardware demands: Rybbit's guide notes that ARM servers need at least ARMv8.2-A for ClickHouse support.
- **A full service stack (PostHog).** The self-hosted deployment runs PostgreSQL, ClickHouse, Redis, Kafka and more in Docker Compose. That is why PostHog asks for 4 vCPU and 16GB RAM, and why it caps its guidance at about 100k events a month.

Then come the chores no directory lists: applying security updates, testing restores from backup, renewing TLS certificates, and noticing when the tracker silently stops recording. If nobody on the team will own those tasks, a hosted plan is usually cheaper than the hours. Plausible, Umami, Matomo and Rybbit all sell one, and GoatCounter hosts reasonable public use for free.

## Side-by-side comparison

| Tool | Licence | Stack | Cookies by default | Cheapest hosted plan |
|---|---|---|---|---|
| Umami | MIT | Node.js + PostgreSQL | No | Free (100K events/mo); Pro $20/mo |
| Plausible | AGPL-3.0 | Elixir + PostgreSQL + ClickHouse | No | $9/mo (10k pageviews) |
| Matomo | GPL-3.0 | PHP + MySQL/MariaDB | Yes (on matomo.org) | 29/mo, currency not shown (50,000 hits) |
| PostHog | MIT (except `ee`) | Docker Compose stack | Not stated | Free (1 million events/mo) |
| Rybbit | AGPL-3.0 | ClickHouse | No | $13/mo billed annually |
| GoatCounter | Modified EUPL 1.2 | Go + SQLite or PostgreSQL | No | Free, reasonable public use |
| Open Web Analytics | GPL-2.0+ | PHP + MySQL | Yes (364 days) | None |

## How to choose in two minutes

1. **Do you want to run a server at all?** If not, pick Plausible or Umami Cloud, or GoatCounter for a free option.
2. **Do you need funnels, e-commerce or GA-style reports?** Pick Matomo.
3. **Are you measuring a product (sign-ups, feature use, replays)?** Pick PostHog, starting on the cloud tier.
4. **Do you just want traffic numbers on your own small VPS?** Pick Umami.
5. **Will you modify the code and offer it to others?** Prefer the MIT tools (Umami, PostHog), or read the AGPL and GPL terms first.

## FAQ

### Do open source analytics tools need a cookie banner?

That depends on the tool and your jurisdiction. Umami, Plausible, Rybbit and GoatCounter say they work without cookies, which removes the most common reason for a banner. Matomo and Open Web Analytics set visitor cookies in the setups described above. Check your local rules.

### Is self-hosting really free?

The software is, but the server, backups and updates are on you. As one directory puts it: "In exchange you take on hosting, backups and updates yourself."

### Which one has the smallest tracking script?

Of the sizes the vendors publish, Plausible's is 2.5KB and GoatCounter's about 3.5KB. Umami and Matomo do not state a size on the pages we read.

### Can I self-host PostHog for a busy site?

PostHog's own guidance puts open source deployments at about 100k events a month, without support. For more traffic, use PostHog Cloud.

## Sources

Repositories: [Umami](https://github.com/umami-software/umami) · [Plausible](https://github.com/plausible/analytics) · [Matomo](https://github.com/matomo-org/matomo) · [PostHog](https://github.com/PostHog/posthog) · [Rybbit](https://github.com/rybbit-io/rybbit) · [GoatCounter](https://github.com/arp242/goatcounter) · [Open Web Analytics](https://github.com/Open-Web-Analytics/Open-Web-Analytics)

Pricing and documentation: [Umami pricing](https://umami.is/pricing) · [Plausible pricing](https://plausible.io/#pricing) · [Plausible script size](https://plausible.io/lightweight-web-analytics) · [Plausible self-hosted](https://plausible.io/self-hosted-web-analytics) · [Matomo pricing](https://matomo.org/pricing/) · [Matomo cookies](https://matomo.org/privacy-policy/cookies/) · [PostHog self-host](https://posthog.com/docs/self-host) · [Rybbit pricing](https://rybbit.com/pricing) · [GoatCounter](https://www.goatcounter.com/)

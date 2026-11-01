# 6. Research brief

```
Intent:         commercial investigation
Target length:  1,800 words (the listicle default; the baselines' median of 750 is metadata, not analysis)
Baselines:      alternativeto (benchmark) · selfhostyourself (depth) · zeabur (gap)
Sensitive topic: no (privacy law is mentioned only as "check your consent needs"; no legal advice)
```

## Must cover
| Topic | Why | Seen in |
|---|---|---|
| Matomo, Plausible, Umami | the core picks | 3 of 3 |
| Licence per tool | decides whether you can modify it and offer it as a service | 2 of 3 (labels only) |
| Self-hosting effort | the hidden cost | 1 of 3 |
| Cookies / privacy | decides whether you need a consent banner | 2 of 3 |
| Who each tool suits | turns a list into a choice | 1 of 3 |

## Differentiators
1. **Hosted prices and free tiers from the vendors' own pricing pages.** *gap*
2. **Limits of self-hosted editions** (Plausible features, PostHog scale and support). *gap*
3. **A licence column with plain consequences** (MIT vs AGPL vs GPL vs EUPL). *angle*
4. **Corrections of directory errors** (Plausible script size, GoatCounter terms). *gap*
5. **One comparison table** covering every pick. *format*

## Facts ledger (all fetched 2026-11-01)
| id | Fact | Source | Quote (≤ 25 words) |
|---|---|---|---|
| U1 | Umami: MIT licence; 39.8k stars | https://github.com/umami-software/umami | "MIT license" |
| U2 | Umami needs Node.js 18.18+ and PostgreSQL 12.14+ | same (README) | "A server with Node.js version 18.18+." / "A PostgreSQL database version v12.14+." |
| U3 | Umami uses no cookies | https://umami.is/pricing | "Umami does not use cookies or collect any personally identifiable information." |
| U4 | Umami Cloud: Hobby $0 up to 100K events a month; Pro $20/month | same | "$0/ month" "Up to 100K events per month" "$20/ month" |
| P1 | Plausible: AGPL-3.0; 29.7k stars | https://github.com/plausible/analytics | "GNU Affero General Public License Version 3 (AGPLv3) or any later version." |
| P2 | Plausible stack: Elixir + Phoenix; PostgreSQL and ClickHouse | same | "PostgreSQL (general data), ClickHouse (analytics)" |
| P3 | Plausible: no cookies | same | "no cookies or persistent identifiers are used." |
| P4 | Plausible Starter $9/month up to 10k pageviews; 30-day trial | https://plausible.io/#pricing | "$9 /month" "Up to 10k monthly pageviews" "Sign up for 30-day free trial. No credit card required." |
| P5 | Plausible script 2.5KB; GA script 135KB gzipped | https://plausible.io/lightweight-web-analytics | "The Plausible tracking script is 2.5KB, which is 54 times smaller." / "The Google Analytics script is 135KB gzipped." |
| P6 | Self-hosted Plausible lacks some features | https://plausible.io/self-hosted-web-analytics | "Marketing funnels, user journeys, ecommerce revenue goals, SSO and sites API are not available" |
| M1 | Matomo: GPL v3; 22.0k stars; PHP 8.1.0+ | https://github.com/matomo-org/matomo | "Matomo is released under the GPL v3 (or later) license" / "PHP 8.1.0 or greater" |
| M2 | Matomo database: MySQL 8.0+ or MariaDB 10.6+ | same | "MySQL version 8.0 or greater, or MariaDB version 10.6 or greater" |
| M3 | matomo.org's own deployment sets a visitor-ID cookie, _pk_id, for 13 months | https://matomo.org/privacy-policy/cookies/ | "_pk_id" "To store a unique visitor ID." |
| M4 | Matomo Cloud: 29 a month for 50,000 hits (no currency shown); 21-day trial; On-Premise free | https://matomo.org/pricing/ | "29 Per month (excl. tax)" / "Matomo Cloud service (21 day free trial)" / "Free forever" |
| H1 | PostHog: MIT expat except the ee directory; 40.6k stars | https://github.com/PostHog/posthog | "This repo is available under the MIT expat license" |
| H2 | PostHog Cloud free: first 1 million events, 5k recordings | same | "Your first 1 million events, 5k recordings, 1M flag requests, 100k exceptions, 10GB of logs" |
| H3 | Self-hosted PostHog scales to about 100k events a month; no support | same | "Open source deployments should scale to approximately 100k events per month" / "We _do not_ provide customer support" |
| H4 | Self-hosted PostHog needs about 4 vCPU, 16GB RAM, 30GB+ storage | https://posthog.com/docs/self-host | "something equivalent to a Hetzner VM with 4 vCPU, 16GB RAM, and more than 30GB storage." |
| R1 | Rybbit: AGPL-3; 13.2k stars; no cookies; ClickHouse | https://github.com/rybbit-io/rybbit | "No cookies & privacy friendly" |
| R2 | Rybbit Cloud Standard $13/month billed annually, Pro $26/month, 7-day trial | https://rybbit.com/pricing | "$13/month" "Billed annually" "$26/month" "Start your 7-day free trial." |
| R4 | Rybbit self-host on ARM needs ARMv8.2-A for ClickHouse (added in edit) | https://rybbit.com/docs/self-hosting | "it must be at least ARMv8.2-A for Clickhouse support" |
| H5 | Self-hosted PostHog runs postgres, clickhouse, redis, kafka, zookeeper, minio containers (added in edit) | https://posthog.com/docs/self-host | "postgres:12-alpine" "clickhouse/clickhouse-server:22.3" |
| R3 | Rybbit script 11 KB; self-host VPS with at least 2GB RAM | https://rybbit.com/ ; https://rybbit.com/docs/self-hosting | "a lightweight 11 KB tracking script" / "at least 2GB of RAM." |
| G1 | GoatCounter: modified EUPL 1.2; 6.1k stars; Go; SQLite or PostgreSQL | https://github.com/arp242/goatcounter | "slightly modified version of European Union Public License (EUPL) 1.2" / "somewhere to store a SQLite database file or a PostgreSQL connection." |
| G2 | GoatCounter: no cookies; free hosted for reasonable public use; about 3.5KB | https://www.goatcounter.com/ | "Identify unique visits without cookies" / "offered for free for reasonable public usage." / "adds just ~3.5KB of extra data to your site." |
| O1 | Open Web Analytics: GPL v2+; 2.7k stars; PHP 8.2+; MySQL 5.7+ | https://github.com/Open-Web-Analytics/Open-Web-Analytics | "licensed under the GNU GPL, version 2 or later." / "PHP 8.2 or later is required." / "MySQL 5.7 or later is supported." |
| O2 | OWA sets a visitor-id cookie for 364 days | same | "364 days for the visitor id" |

Not found, so not stated in the article: PostHog paid prices (the pricing page did not render), script sizes for Umami, Matomo and PostHog, and Matomo's default cookie behaviour on a fresh self-hosted install.

## Structure advice
7 numbered H2 entries, each with: best for, licence, stack, cookies, hosted price, the catch. Then one comparison table, a "how to choose" section and an FAQ.

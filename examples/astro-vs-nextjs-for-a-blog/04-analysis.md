# 4. Analyse

## dev.to (Nayan Kyada): "Next.js vs Astro for content sites and blogs: an honest comparison"
- **Angle:** a practitioner's view built on Sanity CMS. **Strengths:** working Sanity webhook code with `revalidateTag`, a decision matrix, and a warning about piling React islands onto Astro. **Weaknesses:** no method behind its numbers ("45–70 kB gzipped", "30–90 seconds"); specific to Sanity.
- Claims: "Astro's default output is zero-JavaScript HTML." · "ISR with granular tag-based invalidation is not a first-class feature the way it is in Next.js."

## LogRocket (Muhammed Ali): "Astro vs Next.js: SSG vs React"
- **Angle:** builds the same blog in both frameworks and measures what each ships. **Strengths:** reproducible steps, and the honest ISR trade-off: "ISR only works if there's a Next.js server in the loop." **Weaknesses:** contradicts itself ("around 90–130 KB" vs "~2 KB"); uses pages-router `getStaticProps` and synchronous params, which Next.js 16 replaced with async params.

## Easton: "Astro vs Next.js: The Technical Truth Behind 40% Faster Static Site Performance"
- **Angle:** benchmark-driven. **Strengths:** the most measurements, a decision tree, deployment notes. **Weaknesses:** "Source: Real-world testing data" with no hardware, versions or run count; inconsistent figures ("~8KB" vs "5KB"; Next.js 14 vs 15); a docs-site build comparison between two different themes.
- Claim: "Astro delivers 40% faster load times and 90% less JavaScript (8KB vs 85KB)": method not stated, **not used**.

## Bejamas: "Astro vs Next.js"
- **Angle:** an agency's verdict. **Strengths:** a clear content-vs-app line; switching costs. **Weaknesses:** no author, date or data; sells development services in both frameworks.
- Claim: "Moving between the two is a real project, not a swap."

## CloudCannon: "Astro vs. Next.js"
- **Stale:** "with the latest Next.js 13.4 release". It calls Next.js an SPA and never covers ISR. Its "40% faster with 90% less JavaScript" figure is sourced to a tweet.

## The gap
No baseline mentions Next.js 16's changes, Astro joining Cloudflare, Astro live content collections, or the full list of features a Next.js static export loses. Every speed number comes either without a method or from a self-contradicting measurement.

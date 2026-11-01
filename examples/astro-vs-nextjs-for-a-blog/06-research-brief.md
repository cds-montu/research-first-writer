# 6. Research brief

```
Intent:         commercial investigation (a framework choice)
Target length:  1,800 words
Baselines:      dev.to/nayankyada (benchmark) · eastondev (depth) · logrocket (gap)
Sensitive topic: no
```

## Must cover
| Topic | Seen in |
|---|---|
| Rendering model and JavaScript shipped | 3 of 3 |
| Content authoring (collections, MDX, CMS) | 3 of 3 |
| Publishing new posts: rebuild vs ISR | 3 of 3 |
| Hosting and deployment | 2 of 3 |
| Decision rules: choose A if, choose B if | 3 of 3 |

## Differentiators
1. **Current versions and 2025–2026 changes** (Next.js 16, Astro 7.x, Astro joining Cloudflare). *gap*
2. **The full list of features a Next.js static export loses**, from the docs. *gap*
3. **Why the benchmark numbers disagree**, and what to trust instead. *angle*
4. **The cost of switching later**. *gap*

## Facts ledger (fetched 2026-11-01)
| id | Fact | Source | Quote (≤ 25 words) |
|---|---|---|---|
| A1 | Astro renders components to HTML and CSS and strips client JS by default | https://docs.astro.build/en/concepts/islands/ | "By default, Astro will automatically render every UI component to just HTML & CSS, stripping out all client-side JavaScript automatically." |
| A2 | An island is opted into with a client:* directive | same | "Turning any static UI component into an interactive island requires only a `client:*` directive." |
| A3 | client:idle and client:visible | same | "`client:visible` tells a component to load only once it enters the viewport." |
| A4 | Collections are defined in src/content.config.ts; glob() and file() loaders | https://docs.astro.build/en/guides/content-collections/ | "Astro provides two built-in loaders (`glob()` and `file()`) for fetching your local content at build time." |
| A5 | Collections give Zod validation and type checking | same | "Content collections rely on TypeScript to provide Zod validation, Intellisense, and type checking in your editor." |
| A6 | Live content collections fetch at runtime | same | "Live content collections fetch their data at runtime rather than build time." |
| A7 | Astro is MIT-licensed; 63.6k stars; latest release post Astro 7.4 (Oct 15, 2026) | https://github.com/withastro/astro ; https://astro.build/blog/ | "License (MIT)" |
| A8 | The Astro company joined Cloudflare (Jan 16, 2026); Astro stays MIT and open | https://blog.cloudflare.com/astro-joins-cloudflare/ | "Astro will remain open source, MIT-licensed, and open to contributions, with a public roadmap and open governance." |
| N1 | A static export writes HTML/CSS/JS to an out folder and can be hosted on any static server | https://nextjs.org/docs/app/guides/static-exports | "it can be deployed and hosted on any web server that can serve HTML/CSS/JS static assets." |
| N2 | A static export does not support ISR, default image optimisation, Server Actions, Draft Mode, cookies, rewrites, redirects, headers or proxy | same | "Features that require a Node.js server, or dynamic logic that cannot be computed during the build process, are not supported" |
| N3 | next/image in a static export needs a custom loader | same | "can be used with a static export by defining a custom image loader in `next.config.js`." |
| N4 | ISR updates static content without a full rebuild; time-based and on-demand | https://nextjs.org/docs/app/guides/incremental-static-regeneration | "Update static content without rebuilding the entire site" / "invalidate cached pages on-demand with the `revalidatePath` function." |
| N5 | ISR needs the Node.js runtime; no static export | same | "ISR is only supported when using the Node.js runtime (default)." / "ISR is not supported when creating a Static Export." |
| N6 | Next.js 16 (Oct 21, 2025): Turbopack is the default bundler | https://nextjs.org/blog/next-16 | "Turbopack has reached stability for both development and production builds, and is now the default bundler for all new Next.js projects." |
| N7 | Next.js 16: Cache Components; proxy.ts replaces middleware.ts; Node.js 20.9+; async params | same | "Minimum version now 20.9.0 (LTS); Node.js 18 no longer supported" |
| N8 | Next.js is MIT-licensed; 143.5k stars | https://github.com/vercel/next.js | "MIT license" |
| B1 | ISR needs a running Next.js server | https://blog.logrocket.com/astro-vs-next-js-ssg-vs-react/ | "ISR only works if there's a Next.js server in the loop." |
| B2 | Benchmark figures vary: LogRocket gives "around 90–130 KB" and later "~2 KB"; Easton "8KB vs 85KB" with "Real-world testing data" as its only method | logrocket; eastondev | "Summing those chunks gives you the ~2 KB figure." |
| B3 | Tag-based invalidation is not first-class in Astro | dev.to/nayankyada | "ISR with granular tag-based invalidation is not a first-class feature the way it is in Next.js." |
| B6 | Claims quoted in order to be debunked (added in edit): Easton's "40% faster" and CloudCannon's tweet-sourced "40% faster" | eastondev; cloudcannon | "Astro delivers 40% faster load times and 90% less JavaScript (8KB vs 85KB)" / "Astro sites can load 40% faster with 90% less JavaScript compared to Next.js." |
| B4 | Switching is a real project | https://bejamas.com/stack/framework/astro-vs-next-js | "Moving between the two is a real project, not a swap." |
| B5 | A widely read comparison still calls Next.js 13.4 the latest | https://cloudcannon.com/blog/astro-vs-next-js/ | "with the latest Next.js 13.4 release boasting major improvements." |

## Structure advice
A comparison table near the top; one H2 per criterion; "choose A if / choose B if"; an FAQ; a sources list.

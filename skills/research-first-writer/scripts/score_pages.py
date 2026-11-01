#!/usr/bin/env python3
"""Transparent page scores from references/checklists.md (section 1).

Usage:
    python3 scripts/score_pages.py pages.json [--json]

pages.json is a list of pages; each signal is a number from 0 to 1, or null
when it could not be observed (it is then left out and the weights renormalise):

    [{"url": "https://...", "signals": {"serp_rank": 0.9, "serp_coverage": 0.5,
      "depth": 0.8, "engagement": null, "freshness": 1, "structure": 0.7,
      "eeat": 0.6, "media": 0.4, "ai_citation": null}}]

Prints each page's score out of 100, its coverage (share of the core weight
that was observable) and the breakdown, best first. Standard library only.
"""
import json
import sys

WEIGHTS = {"serp_rank": .20, "serp_coverage": .15, "depth": .15, "engagement": .15,
           "freshness": .10, "structure": .10, "eeat": .10, "media": .05}
AI_BONUS = .20


def score(signals):
    seen = {k: v for k, v in signals.items() if k in WEIGHTS and v is not None}
    total_w = sum(WEIGHTS[k] for k in seen)
    base = sum(WEIGHTS[k] * v for k, v in seen.items()) / total_w if total_w else 0
    bonus = AI_BONUS * signals["ai_citation"] if signals.get("ai_citation") is not None else 0
    return min(1, base + bonus) * 100, total_w / sum(WEIGHTS.values())


def main(path, as_json=False):
    pages = json.load(open(path, encoding="utf-8"))
    rows = []
    for p in pages:
        s, cov = score(p["signals"])
        rows.append((s, cov, p))
    rows.sort(key=lambda r: -r[0])
    if as_json:
        print(json.dumps([{"url": p["url"], "score": round(s, 1), "coverage": round(cov, 3), "signals": p["signals"]}
                          for s, cov, p in rows], indent=2))
        return
    print(f"\n  {'score':>5}  {'cover':>5}  page")
    for s, cov, p in rows:
        print(f"  {s:5.1f}  {cov:5.0%}  {p['url']}")
        parts = [f"{k}={v:.2f}" if v is not None else f"{k}=—" for k, v in p["signals"].items()]
        print("               " + "  ".join(parts))
    print("\n  — = not observable on a public page (left out, never guessed)\n")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--json"]
    if len(args) != 1:
        sys.exit(__doc__)
    main(args[0], as_json="--json" in sys.argv)

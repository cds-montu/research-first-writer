#!/usr/bin/env python3
"""Scaffold a run folder from the templates in references/templates.md.

Usage:
    python3 scripts/new_run.py <slug> [--dir articles]

Creates <dir>/<slug>/ with 01-brief.md, 02-discover.md, 03-scores.md, 04-analysis.md,
05-baselines.md, 06-research-brief.md, 07-outline.md, article.md and review-report.md.
The brief, research brief, outline and review report are pre-filled from the templates;
the rest get a one-line prompt. Refuses to overwrite an existing folder.
Standard library only.
"""
import argparse
import re
import sys
from pathlib import Path

TEMPLATES = Path(__file__).resolve().parent.parent / "references" / "templates.md"

STUBS = {
    "02-discover.md": "# 2. Discover\n\nReader questions grouped by angle; queries in the reader's language; every ranking page with its query and position.\n",
    "03-scores.md": "# 3. Read and score\n\nPages fetched and scored. Put the signals in pages.json and run scripts/score_pages.py. Say which signals could not be observed.\n",
    "04-analysis.md": "# 4. Analyse\n\nPer page: angle, format, strengths, weaknesses, gaps, and claims, each with a verbatim quote of 25 words or fewer.\n",
    "05-baselines.md": "# 5. Choose baselines\n\n3 to 5 pages, one per site, each with a role and a reason.\n",
    "article.md": "---\ntitle: \nmeta_title: \nmeta_description: \nslug: \nkeyword: \nkind: blog\ntarget_words: 1500\n---\n\n## \n",
}


def template_blocks():
    """The four fenced blocks in templates.md, in order: brief, research brief, outline, review."""
    text = TEMPLATES.read_text(encoding="utf-8")
    blocks = re.findall(r"^```\n(.*?)^```", text, re.S | re.M)
    if len(blocks) < 4:
        sys.exit(f"expected 4 template blocks in {TEMPLATES}, found {len(blocks)}")
    return blocks[:4]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug")
    ap.add_argument("--dir", default="articles")
    args = ap.parse_args()
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", args.slug):
        sys.exit("slug must be lower-case words joined by hyphens")
    root = Path(args.dir) / args.slug
    if root.exists():
        sys.exit(f"{root} already exists; refusing to overwrite")
    brief, research, outline, review = template_blocks()
    files = {
        "01-brief.md": f"# 1. Brief\n\n```\n{brief}```\n",
        "06-research-brief.md": f"# 6. Research brief\n\n```\n{research}```\n\n## Facts ledger\n\n| id | Fact | Source | Quote (≤ 25 words) |\n|---|---|---|---|\n",
        "07-outline.md": f"# 7. Outline\n\n```\n{outline}```\n",
        "review-report.md": f"# Review report\n\n```\n{review}```\n",
        **STUBS,
    }
    root.mkdir(parents=True)
    for name in sorted(files):
        (root / name).write_text(files[name], encoding="utf-8")
    print(f"created {root}/")
    for name in sorted(files):
        print(f"  {name}")


if __name__ == "__main__":
    main()

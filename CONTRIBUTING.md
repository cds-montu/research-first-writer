# Contributing

Thanks for helping. Contributions are welcome in these four areas, most valuable first.

## 1. Add an example run

An example is a folder in `examples/<slug>/` containing the files the skill produces:

```
01-brief.md  02-discover.md  03-scores.md  pages.json  04-analysis.md
05-baselines.md  06-research-brief.md  07-outline.md  article.md  review-report.md  README.md
```

Rules for examples:
- **Real research only.** Fetch the pages you score. Every quote must be verbatim, 25 words or fewer, and appear on the page. Write the date you read it.
- **No invented experience.** Without first-hand notes, leave `[[NEEDS_HUMAN: …]]`. Never write "we tested".
- **Every %, price and decimal goes in the ledger** (`06-research-brief.md`). CI enforces this.
- **Report honestly.** If the judge fails it, keep the example: failures teach too.
- Avoid YMYL topics (medical, financial, legal) unless you have the expertise and add an expert-review note.

Start with `python3 skills/research-first-writer/scripts/new_run.py <slug> --dir examples` to create the folder with the templates filled in. The easiest way is to let Claude Code do the run, then check it yourself:

```bash
claude --plugin-dir .
> Use research-first-writer to write a FAQ article on "<keyword>" for <market>. Save each step to examples/<slug>/.
```

## 2. Improve the checks

`skills/research-first-writer/scripts/` is standard-library Python 3.9+. Keep it that way, with no dependencies.
- Each check maps to a row in `references/checklists.md`. If you add a check, add the row too.
- Run every example before opening a PR: `for f in examples/*/article.md; do python3 skills/research-first-writer/scripts/check_article.py "$f"; done`

## 3. Improve the method

Changes to `SKILL.md` or the references change how every user's agent behaves. In the PR description, include:
- what failure you saw (a link to a run or transcript is ideal),
- the change, and why it generalises beyond your case,
- a before and after on at least one example.

Keep `SKILL.md` under about 500 lines; put detail in `references/`.

## 4. Docs, translations, screenshots

Screenshots are generated, never hand-edited: `pip install markdown && python3 docs/render_screenshots.py`.

## Pull requests

- One topic per PR. Use a conventional title (`feat:`, `fix:`, `docs:`, `example:`).
- CI must pass: plugin validation, checks on every example, script smoke tests.
- By contributing you agree that your work is released under the MIT License.

Please follow the [Code of Conduct](CODE_OF_CONDUCT.md).

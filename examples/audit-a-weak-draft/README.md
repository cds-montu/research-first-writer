# Example: auditing a weak draft (review mode)

[`draft.md`](draft.md) is a deliberately bad, typical AI-written listicle. It contains invented "we tested" claims, five unsourced statistics, keyword stuffing and ten stock phrases. It shows what the skill catches when someone asks a plain question.

**Prompt** (in a real Claude Code session, with the plugin loaded via `--plugin-dir .`):

> Is this post good enough to publish? examples/audit-a-weak-draft/draft.md

The skill triggered on its own, ran `check_article.py` (6 blocking checks), then judged what a script can't: the entries give no reason to choose, and it scores 0.17 against a 0.75 pass mark.

- Full answer: [claude-review.md](claude-review.md)
- Raw session log: [docs/runs/audit-weak-draft.jsonl](../../docs/runs/audit-weak-draft.jsonl)
- Screenshot: [docs/screenshots/claude-code-audit.png](../../docs/screenshots/claude-code-audit.png)

Run the rule checks yourself:

```bash
python3 skills/research-first-writer/scripts/check_article.py examples/audit-a-weak-draft/draft.md
```

Note: the CRM claims in the draft were invented for this test. Do not quote them.

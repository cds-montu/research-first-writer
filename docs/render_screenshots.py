#!/usr/bin/env python3
"""Regenerate docs/screenshots/*.png from real outputs in this repository.

Nothing here is mocked: each image renders either the live output of a script,
a recorded Claude Code session (docs/runs/*.jsonl, from `claude -p
--output-format stream-json`), or an example article as a browser would show it.

    pip install markdown
    python3 docs/render_screenshots.py

Needs Google Chrome (or Chromium) for headless screenshots. Set CHROME=/path/to/chrome
if it is not in the default macOS location.
"""
import html
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "screenshots"
CHECKER = ROOT / "skills" / "research-first-writer" / "scripts" / "check_article.py"
CHROME = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")

ANSI = {"1": "font-weight:700", "2": "opacity:.55", "31": "color:#ff6b6b", "32": "color:#5fd38d", "33": "color:#ffcc66"}

TERM_CSS = """
body{margin:0;background:#0d1117;font:15px/1.55 ui-monospace,SFMono-Regular,Menlo,monospace;color:#e6edf3}
.win{margin:28px;border-radius:12px;overflow:hidden;box-shadow:0 18px 50px rgba(0,0,0,.5);background:#161b22;border:1px solid #30363d}
.bar{background:#21262d;padding:10px 14px;display:flex;gap:8px;align-items:center}
.dot{width:12px;height:12px;border-radius:50%}
.title{color:#8b949e;font-size:13px;margin-left:10px}
pre{margin:0;padding:18px 22px;white-space:pre-wrap;word-break:break-word}
.prompt{color:#79c0ff}.tool{color:#d2a8ff}.dim{opacity:.6}.ok{color:#5fd38d}
.md h2{font-size:16px;color:#ffa657;margin:14px 0 4px}.md p{margin:6px 0}.md table{border-collapse:collapse;margin:8px 0;font-size:13px}
.md td,.md th{border:1px solid #30363d;padding:4px 8px;vertical-align:top}.md code{color:#ffa657}.md li{margin:2px 0}
"""

PAGE_CSS = """
body{margin:0;background:#f6f7f9;font:17px/1.65 Georgia,'Iowan Old Style',serif;color:#1f2328}
main{max-width:760px;margin:0 auto;background:#fff;padding:48px 64px;box-shadow:0 0 0 1px #e5e7eb}
h1{font:700 34px/1.2 -apple-system,Segoe UI,sans-serif;margin:0 0 8px}
.meta{font:13px -apple-system,sans-serif;color:#57606a;margin-bottom:24px}
h2{font:700 23px/1.3 -apple-system,Segoe UI,sans-serif;margin:34px 0 10px}
h3{font:600 18px -apple-system,sans-serif}
table{border-collapse:collapse;font:14px/1.45 -apple-system,sans-serif;width:100%}
td,th{border:1px solid #d0d7de;padding:6px 8px;vertical-align:top}th{background:#f6f8fa}
code{background:#f3f4f6;padding:1px 4px;border-radius:4px;font-size:14px}
pre{background:#0d1117;color:#e6edf3;padding:14px;border-radius:8px;overflow:auto}
pre code{background:none;color:inherit;padding:0}
blockquote{border-left:4px solid #d0d7de;margin:0;padding:0 16px;color:#57606a}
.needs{background:#fff4d6;border:1px dashed #d4a72c;padding:2px 6px;border-radius:4px;font:13px -apple-system,sans-serif}
"""


def ansi_to_html(text):
    out, open_spans = [], 0
    for part in re.split(r"(\x1b\[[0-9;]*m)", text):
        m = re.fullmatch(r"\x1b\[([0-9;]*)m", part)
        if m:
            codes = m.group(1)
            if codes in ("", "0"):
                out.append("</span>" * open_spans)
                open_spans = 0
            else:
                style = ";".join(ANSI.get(c, "") for c in codes.split(";"))
                out.append(f'<span style="{style}">')
                open_spans += 1
        else:
            out.append(html.escape(part))
    return "".join(out) + "</span>" * open_spans


def window(title, body_html):
    dots = "".join(f'<span class="dot" style="background:{c}"></span>' for c in ("#ff5f57", "#febc2e", "#28c840"))
    return (f"<!doctype html><meta charset=utf-8><style>{TERM_CSS}</style>"
            f'<div class="win"><div class="bar">{dots}<span class="title">{html.escape(title)}</span></div>{body_html}</div>')


def shoot(html_doc, name, width, height):
    OUT.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html_doc)
    target = OUT / name
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--window-size={width},{height}",
                    "--force-device-scale-factor=2", f"--screenshot={target}", f"file://{f.name}"],
                   check=True, capture_output=True)
    print("wrote", target.relative_to(ROOT))


def checker_shot(article, name, height):
    env = dict(os.environ, FORCE_COLOR="1")
    res = subprocess.run([sys.executable, str(CHECKER), article], cwd=ROOT, capture_output=True, text=True, env=env)
    cmd = f'<span class="prompt">$</span> python3 skills/research-first-writer/scripts/check_article.py {html.escape(article)}\n'
    shoot(window("check_article.py", f"<pre>{cmd}{ansi_to_html(res.stdout)}</pre>"), name, 1100, height)


def session_shot(jsonl, name, height):
    lines = [json.loads(l) for l in Path(jsonl).read_text(encoding="utf-8").splitlines() if l.strip()]
    init = next(d for d in lines if d.get("type") == "system" and d.get("subtype") == "init")
    prompt = ""
    rows = []
    for d in lines:
        if d.get("type") == "assistant":
            for c in d["message"]["content"]:
                if c["type"] == "tool_use":
                    inp = c["input"]
                    arg = inp.get("skill") or inp.get("file_path") or inp.get("command") or ""
                    arg = arg.replace(str(ROOT) + "/", "").replace(str(ROOT), ".")
                    rows.append(f'<span class="tool">⏺ {html.escape(c["name"])}</span><span class="dim">({html.escape(arg[:110])})</span>')
        elif d.get("type") == "result":
            result = d["result"]
            meta = f'{d.get("num_turns")} turns · {d.get("duration_ms", 0) / 1000:.0f}s · model {init.get("model")}'
    prompt = "Is this post good enough to publish? examples/audit-a-weak-draft/draft.md"
    md = markdown.markdown(result, extensions=["tables"])
    body = (f'<pre><span class="prompt">❯</span> claude -p --plugin-dir . "{html.escape(prompt)}"\n\n' + "\n".join(rows) +
            f'\n</pre><div class="md" style="padding:0 22px 18px">{md}</div>'
            f'<pre class="dim">✻ {html.escape(meta)} · recorded in {html.escape(Path(jsonl).name)}</pre>')
    shoot(window("Claude Code: research-first-writer skill (headless run)", body), name, 1100, height)


def article_shot(article, name, height):
    text = Path(ROOT / article).read_text(encoding="utf-8")
    meta = dict(re.findall(r"^(\w+):\s*\"?(.*?)\"?$", text.split("---")[1], re.M))
    body = text.split("---", 2)[2]
    body = re.sub(r"\[\[NEEDS_HUMAN:([^\]]+)\]\]", r'<span class="needs">NEEDS_HUMAN:\1</span>', body)
    md = markdown.markdown(body, extensions=["tables", "fenced_code"])
    doc = (f"<!doctype html><meta charset=utf-8><style>{PAGE_CSS}</style><main><h1>{html.escape(meta['title'])}</h1>"
           f"<div class=meta>/{meta['slug']} · {meta['kind']} · target {meta['target_words']} words</div>{md}</main>")
    shoot(doc, name, 1000, height)


if __name__ == "__main__":
    checker_shot("examples/audit-a-weak-draft/draft.md", "checker-weak-draft.png", 1050)
    checker_shot("examples/how-to-get-cited-by-ai-search/article.md", "checker-good-article.png", 1000)
    session_shot(ROOT / "docs/runs/audit-weak-draft.jsonl", "claude-code-audit.png", 1420)
    article_shot("examples/how-to-get-cited-by-ai-search/article.md", "article-ai-citations.png", 2200)
    article_shot("examples/best-open-source-web-analytics/article.md", "article-analytics.png", 2200)
    article_shot("examples/astro-vs-nextjs-for-a-blog/article.md", "article-astro-nextjs.png", 1800)

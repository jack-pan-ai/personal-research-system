#!/usr/bin/env python3
"""Build the static research dashboard from JSON source files."""

from __future__ import annotations

import html
import json
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "Research" / "07_Dashboard" / "index.html"


def load_json(name: str, fallback):
    path = DATA / name
    if not path.exists():
        return fallback
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def esc(value) -> str:
    return html.escape(str(value if value is not None else ""))


def link_or_text(title: str, link: str) -> str:
    title = esc(title)
    if link:
        return f'<a href="{esc(link)}">{title}</a>'
    return title


def item(title: str, body: str, meta: str = "") -> str:
    meta_html = f'<p class="muted">{meta}</p>' if meta else ""
    return f'<article class="item"><h3>{title}</h3>{meta_html}{body}</article>'


def list_items(values) -> str:
    if not values:
        return "<p class=\"muted\">No entries yet.</p>"
    return "<ul>" + "".join(f"<li>{esc(v)}</li>" for v in values) + "</ul>"


def build() -> str:
    papers = load_json("papers.json", [])
    ideas = load_json("ideas.json", [])
    experiments = load_json("experiments.json", [])
    weekly = load_json("weekly.json", {})
    research_map = load_json("research_map.json", {})

    deep_papers = [p for p in papers if p.get("status") == "deep"]
    active_ideas = [i for i in ideas if i.get("status") == "active"]
    running_experiments = [
        e for e in experiments if e.get("status") in {"running", "planned"}
    ]

    paper_html = "\n".join(
        item(
            link_or_text(p.get("title", "Untitled"), p.get("link", "")),
            (
                f"<p>{esc(p.get('why_it_matters', ''))}</p>"
                f"<p><strong>Next:</strong> {esc(p.get('next', ''))}</p>"
            ),
            (
                f"<span class=\"tag\">{esc(p.get('area', ''))}</span> "
                f"<span class=\"tag\">{esc(p.get('status', ''))}</span> "
                f"<span class=\"score\">I {esc(p.get('interesting', '-'))} / "
                f"U {esc(p.get('useful', '-'))}</span>"
            ),
        )
        for p in papers
    ) or '<p class="muted">No papers yet.</p>'

    idea_html = "\n".join(
        item(
            esc(i.get("title", "Untitled")),
            (
                f"<p><strong>Interesting:</strong> {esc(i.get('why_interesting', ''))}</p>"
                f"<p><strong>Useful:</strong> {esc(i.get('why_useful', ''))}</p>"
                f"<p><strong>Minimal test:</strong> {esc(i.get('minimal_test', ''))}</p>"
                f"<p><strong>Next:</strong> {esc(i.get('next', ''))}</p>"
            ),
            f"<span class=\"tag\">{esc(i.get('status', ''))}</span>",
        )
        for i in ideas
    ) or '<p class="muted">No ideas yet.</p>'

    experiment_html = "\n".join(
        item(
            esc(e.get("title", "Untitled")),
            (
                f"<p><strong>Question:</strong> {esc(e.get('question', ''))}</p>"
                f"<p><strong>Motivation:</strong> {esc(e.get('motivation', ''))}</p>"
                f"<p><strong>Result:</strong> {esc(e.get('result', ''))}</p>"
                f"<p><strong>Decision:</strong> {esc(e.get('decision', ''))}</p>"
            ),
            f"<span class=\"tag\">{esc(e.get('status', ''))}</span>",
        )
        for e in experiments
    ) or '<p class="muted">No experiments yet.</p>'

    generated = datetime.now().strftime("%Y-%m-%d %H:%M")

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Research Dashboard</title>
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>
  <header>
    <h1>Research Dashboard</h1>
    <p class="subtitle">Audio LLM research system. Optimized for interesting and useful work first.</p>
  </header>
  <main>
    <section class="grid">
      <div class="panel span-12">
        <h2>This Week</h2>
        <div class="metric-row">
          <div class="metric"><strong>{esc(len(papers))}</strong><span>Papers tracked</span></div>
          <div class="metric"><strong>{esc(len(deep_papers))}</strong><span>Deep reads</span></div>
          <div class="metric"><strong>{esc(len(active_ideas))}</strong><span>Active ideas</span></div>
          <div class="metric"><strong>{esc(len(running_experiments))}</strong><span>Planned/running experiments</span></div>
        </div>
      </div>

      <div class="panel span-6">
        <h2>Weekly Review</h2>
        <p><strong>Most interesting:</strong> {esc(weekly.get("most_interesting", "TBD"))}</p>
        <p><strong>Most useful:</strong> {esc(weekly.get("most_useful", "TBD"))}</p>
        <p><strong>Best idea:</strong> {esc(weekly.get("best_idea", "TBD"))}</p>
        <p><strong>Best paper/repo:</strong> {esc(weekly.get("best_paper_or_repo", "TBD"))}</p>
        <p><strong>Stop thinking about:</strong> {esc(weekly.get("stop_thinking_about", "TBD"))}</p>
        <p><strong>Push next week:</strong> {esc(weekly.get("push_next_week", "TBD"))}</p>
      </div>

      <div class="panel span-6">
        <h2>Research Map</h2>
        <h3>Big Questions</h3>
        {list_items(research_map.get("big_questions", []))}
        <h3>Interesting Gaps</h3>
        {list_items(research_map.get("interesting_gaps", []))}
        <h3>Useful Problems</h3>
        {list_items(research_map.get("useful_problems", []))}
      </div>

      <div class="panel span-4">
        <h2>Papers</h2>
        {paper_html}
      </div>

      <div class="panel span-4">
        <h2>Ideas</h2>
        {idea_html}
      </div>

      <div class="panel span-4">
        <h2>Experiments</h2>
        {experiment_html}
      </div>
    </section>
    <footer>Generated {esc(generated)} from JSON sources in <code>data/</code>.</footer>
  </main>
</body>
</html>
"""


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(build(), encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()


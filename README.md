# Personal Research System

This is a lightweight research system for long-running AI research work.

The system optimizes for:

- finding research directions that are interesting and useful
- turning papers and ideas into decisions
- keeping experiments tied to research questions
- reviewing progress through a local HTML dashboard

## Structure

```text
Research/
  00_Inbox/             Capture first, sort later.
  01_Research_Map/      Long-lived maps of audio LLM questions and gaps.
  02_Papers/            Paper pipeline and memos.
  03_Ideas/             Idea bank, active ideas, parked ideas, killed ideas.
  04_Experiments/       Experiment log and results.
  05_Outputs/           Memos, talks, drafts, repo notes, HTML exports.
  06_Weekly_Reviews/    Weekly review notes.
  07_Dashboard/         Generated HTML dashboard.
  99_Archive/           Cold storage.
data/                   JSON source data for the dashboard.
scripts/                Build and maintenance scripts.
```

## Build Dashboard

From this directory:

```bash
python3 scripts/build_dashboard.py
```

Open:

```text
Research/07_Dashboard/index.html
```

## GitHub Sync

Do not put secrets, private company data, raw PDFs, or unpublished confidential material in this repo.

Recommended flow when ready:

```bash
git init
git add .
git commit -m "Initialize personal research system"
```

Then create a private GitHub repository and connect the remote.


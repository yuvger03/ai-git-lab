# Instructions for coding agents

These rules apply to every coding agent working in this repository (Gemini, Claude, Copilot, others) and to the humans who drive them. Antigravity reads this file automatically. Claude Code reads it when there is no CLAUDE.md; if you add a CLAUDE.md, make its first line `@AGENTS.md`.

## Project

- Python 3.10 or newer, standard library only. Do not add dependencies.
- Code: `gradebook/`. Tests: `tests/`. Course policy numbers: `gradebook/config.py`.

## Commands

- Run all tests: `python -m unittest -v`
- Run the app: `python -m gradebook report data/course.csv` and `python -m gradebook stats data/course.csv`

## Rules

1. Change only the files the task names. If another file needs to change, ask first and say why.
2. Do not edit anything in `tests/` unless the task asks for new tests. Never weaken, skip or delete an existing test to make it pass.
3. Keep changes small. After editing, list each changed file with one sentence on what changed.
4. Run the tests after every change and report the result honestly, including failures that remain.
5. Git: read-only commands (`git status`, `git diff`, `git log`, `git show`) are fine. Commit only when the human asks. Never push, pull, merge, rebase, reset, revert or use `--force`; the human does those in PyCharm.
6. Never put secrets (API keys, tokens, passwords) in code, commits, or chat. Code reads keys from environment variables (see `tasks/secrets.md`); never open, print or change `.env`.

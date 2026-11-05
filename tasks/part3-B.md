# Part 3, Partner B: add `--top N` to the report (AI on a branch)

**Feature.** `python -m gradebook report data/course.csv --top 3` prints the header and only the 3 students with the highest final grades, highest first. Without `--top`, the report is unchanged (students in file order).

**Branch.** `feature/top-n`

**Files the agent may change.** `gradebook/cli.py`, and `tests/test_cli.py` for new tests only (existing tests stay as they are).

**Done when.**

- `--top 3` shows exactly 3 students, highest final grade first.
- `--top 0` or a negative number stops with a clear error message.
- New tests cover both cases, and all tests pass.

**Prompt to start with.**

> Read AGENTS.md and tasks/part3-B.md. First show me a short plan and wait for my OK. Then implement it, add new tests to tests/test_cli.py without changing the existing ones, run all tests, and show me the diff.

When your pull request is open, review your partner's pull request (`fix/letter-boundaries`) with the AI's help. The lab sheet has the prompt.

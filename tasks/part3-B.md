# Part 3, Partner B: add `--top N` to the report (30 minutes)

For 10 minutes you watch the instructor drive Claude Code inside PyCharm. Then, for 20 minutes, you have Gemini make one change on your own branch, review it, and merge it through a pull request your partner approves.

## During the demo, note your answers

- Where do Claude's proposed edits appear, and who accepts them?
- What does the commit Claude makes say about who wrote it?
- What stops the agent from editing `tests/` or force-pushing?
- What can Claude's rewind undo that git cannot, and the other way round?

## The task

This section is what the agent reads.

- **Feature.** `python -m gradebook report data/course.csv --top 3` prints the header and only the 3 students with the highest final grades, highest first. Without `--top`, the report is unchanged (students in file order).
- **Files the agent may change.** `gradebook/cli.py`, and `tests/test_cli.py` for new tests only. Existing tests stay as they are.
- **Done when.**
  - `--top 3` shows exactly 3 students, highest final grade first.
  - `--top 0` or a negative number stops with a clear error message.
  - New tests cover both cases, and all of them pass.

## Your steps

### 1. Start clean

Update `main` (Ctrl+T · Cmd+T). The Commit tool window should list no changes.

### 2. Branch

Click the branch name in the toolbar, then **New Branch**, and name it `feature/top-n`.

Git: `git switch -c feature/top-n`

### 3. Prompt the agent (rung 3)

In `agy`, paste:

> Read AGENTS.md and the section "The task" in tasks/part3-B.md. First show me a short plan and wait for my OK. Then implement it, add new tests to tests/test_cli.py without changing the existing ones, run all tests, and show me the diff.

Read the plan before you say OK. Approve edits only to `cli.py` and `test_cli.py`; approve test runs. Shift+Tab cycles the agent's mode (default, accept-edits, plan). Stay in default, which asks before every edit and every command.

### 4. Review like a reviewer, not a passenger

- Commit tool window: which files changed? Anything except `cli.py` and `test_cli.py` gets rolled back (select it, Rollback).
- Double-click each file and read every line of the diff. Do the new tests check the order, or only the count? Did any existing test change?
- Run `python -m unittest` yourself; do not take the agent's word for it. One test still fails on your branch, `test_grades_exactly_on_a_boundary`: that fix lives on A's branch. All your new tests pass.
- Try it: `python -m gradebook report data/course.csv --top 3`, then `--top 0`.

### 5. Commit

Ask the agent: "Write a one-line commit message for these changes." Then you commit, with Ctrl+K · Cmd+K.

### 6. Push the branch

Ctrl+Shift+K · Cmd+Shift+K. **Predict:** will this push be rejected? (Nobody else has pushed to your branch.)

Git: `git push -u origin feature/top-n`

### 7. Open a pull request

On your repository's GitHub page, click **Compare & pull request** (or in PyCharm: Git → GitHub → Create Pull Request). Base: `main`. Write two lines: what changed and how you tested it, and say that an AI agent wrote the code.

### 8. Review A's pull request (rung 4)

Run **Git → Fetch**, then ask the agent:

> Review the changes on origin/fix/letter-boundaries compared with main, using git diff main...origin/fix/letter-boundaries. Check them against the section "The task" in tasks/part3-A.md. List bugs, missing tests, and anything outside that scope. Do not change any files.

On GitHub, open A's pull request, go to the **Files changed** tab, leave at least one comment you agree with, and approve it.

### 9. Merge

Once A has approved yours, click **Merge pull request**, then confirm. Then switch to `main` (branch name in the toolbar → `main` → Checkout) and update.

## Checkpoint

On `main`, after both merges:

- `python -m unittest` prints `OK` (13 tests plus your new ones).
- `python -m gradebook report data/course.csv --top 3` lists Maya, Avi and Dana, all with an A.

If GitHub says a pull request has conflicts, that is Part 2 again: merge `main` into your branch in PyCharm, resolve, and push.

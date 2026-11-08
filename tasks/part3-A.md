# Part 3, Partner A: letters on the boundaries (30 minutes)

For 10 minutes you watch the instructor drive Claude Code inside PyCharm. Then, for 20 minutes, you have Gemini make one change on your own branch, review it, and merge it through a pull request your partner approves.

## During the demo, note your answers

- Where do Claude's proposed edits appear, and who accepts them?
- What does the commit Claude makes say about who wrote it?
- What stops the agent from editing `tests/` or force-pushing?
- What can Claude's rewind undo that git cannot, and the other way round?

## The task

This section is what the agent reads.

- **Bug.** A final grade exactly on a boundary gets the lower letter. Dana has 90.0 and gets a B; Hila has 80.0 and gets a C.
- **Failing test.** `LetterGradeTests.test_grades_exactly_on_a_boundary` in `tests/test_grades.py`.
- **Files the agent may change.** `gradebook/grades.py` only. Do not touch the tests.
- **Done when.** All tests pass, and the diff touches only `gradebook/grades.py`.

## Your steps

### 1. Start clean

Update `main` (Ctrl+T · Cmd+T). The Commit tool window should list no changes.

### 2. Branch

Click the branch name in the toolbar, then **New Branch**, and name it `fix/letter-boundaries`.

Git: `git switch -c fix/letter-boundaries`

### 3. Prompt the agent (rung 3)

In `agy`, paste:

> Read AGENTS.md and the section "The task" in tasks/part3-A.md. Fix that bug. Change only gradebook/grades.py and do not touch the tests. Then run all tests and show me the diff.

Approve edits only to `grades.py`; approve test runs. Shift+Tab cycles the agent's mode (default, accept-edits, plan). Stay in default, which asks before every edit and every command.

### 4. Review like a reviewer, not a passenger

- Commit tool window: which files changed? Anything except `grades.py` gets rolled back (select it, Rollback).
- Double-click `grades.py` and read every line of the diff.
- Run `python -m unittest` yourself; do not take the agent's word for it. Everything passes.

### 5. Commit

Ask the agent: "Write a one-line commit message for these changes." Then you commit, with Ctrl+K · Cmd+K.

### 6. Push the branch

Ctrl+Shift+K · Cmd+Shift+K. **Predict:** will this push be rejected? (Nobody else has pushed to your branch.)

Git: `git push -u origin fix/letter-boundaries`

### 7. Open a pull request

On your repository's GitHub page, click **Compare & pull request** (or in PyCharm: Git → GitHub → Create Pull Request). Base: `main`. Write two lines: what changed and how you tested it, and say that an AI agent wrote the code.

### 8. Review B's pull request (rung 4)

Run **Git → Fetch**, then ask the agent:

> Review the changes on origin/feature/top-n compared with main, using git diff main...origin/feature/top-n. Check them against the section "The task" in tasks/part3-B.md. List bugs, missing tests, and anything outside that scope. Do not change any files.

On GitHub, open B's pull request, go to the **Files changed** tab, leave at least one comment you agree with, and approve it.

### 9. Merge

Once B has approved yours, click **Merge pull request**, then confirm. Then switch to `main` (branch name in the toolbar → `main` → Checkout) and update.

## Checkpoint

On `main`, after both merges:

- `python -m unittest` prints `OK` (13 tests plus the new ones from B's branch).
- `python -m gradebook report data/course.csv --top 3` lists Maya, Avi and Dana, all with an A.

If GitHub says a pull request has conflicts, that is Part 2 again: merge `main` into your branch in PyCharm, resolve, and push.

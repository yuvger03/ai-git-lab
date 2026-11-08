# Part 1, Partner A: the final grade is wrong (25 minutes)

Each of you fixes one bug by hand and commits it. **You push first.**

- **Symptom.** `python -m gradebook report data/course.csv` fails the whole class. Dana scored 90 on every component, but her final grade is 30.0.
- **Failing tests.** `FinalGradeTests` in `tests/test_grades.py` (two tests).
- **File you change.** `gradebook/grades.py`, only the `final_grade` function.
- **Commit message.** `Fix final grade weighting`

## Step 1. Ask the AI to explain (rung 1)

Open PyCharm's terminal (Alt+F12 · Option+F12) in the project folder and start the agent:

```
agy
```

The first time, it asks whether to trust this workspace: yes. Then paste:

> Read AGENTS.md. Explain why FinalGradeTests in tests/test_grades.py fail. Do not change any files.

Read every request before you answer `y` or `n`. Running the tests: `y`. Editing a file: `n`, because in Part 1 the fix is yours. Check the explanation against the test output you saw.

## Step 2. Fix it by hand, then look at the diff

Make the one-line fix. A coloured bar appears in the gutter next to the line; click it to see the old version. Open the Commit tool window (Alt+0 · Cmd+0): `grades.py` is listed under Changes. Double-click it to read the diff.

Run `python -m unittest` again: both `FinalGradeTests` pass. The failures that remain belong to your partner or to Part 3.

Git: `git status`, `git diff`

## Step 3. Commit

Press Ctrl+K · Cmd+K, tick only `grades.py`, type the commit message, and click **Commit** (not Commit and Push). Open the Git tool window (Alt+9 · Cmd+9), Log tab: your commit sits on top of the first commit.

Git: `git add gradebook/grades.py`, then `git commit -m "Fix final grade weighting"`

## Step 4. Push first

**Predict:** will your push work? Then push: Ctrl+Shift+K · Cmd+Shift+K, then **Push**. Say "pushed" out loud.

Git: `git push`

## Step 5. Watch your partner, then update

B pushes next. Watch B's screen and help B read what git and the agent say; B's card has B's steps.

When B tells you their fix is on GitHub, **predict** what you will receive. Then update: **Git → Update Project** (Ctrl+T · Cmd+T), choose **Merge**, OK.

Git: `git pull`, which is `git fetch` followed by `git merge origin/main`

## Checkpoint

- Both Git logs show the same picture: your two commits side by side, joined by a merge commit.
- `python -m unittest` ends with `FAILED (failures=1)`. That last failure is saved for Part 3.
- The report now passes six of the eight students.

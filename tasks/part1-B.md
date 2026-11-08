# Part 1, Partner B: the median is wrong (25 minutes)

Each of you fixes one bug by hand and commits it. **Partner A pushes first.**

- **Symptom.** For an even number of grades, `median` returns the upper middle value instead of the average of the two middle values. `median([4, 1, 3, 2])` returns 3; it should return 2.5.
- **Failing test.** `MedianTests.test_even_number_of_values` in `tests/test_stats.py`.
- **File you change.** `gradebook/stats.py`, only the `median` function.
- **Commit message.** `Fix median for an even number of grades`

## Step 1. Ask the AI to explain (rung 1)

Open PyCharm's terminal (Alt+F12 · Option+F12) in the project folder and start the agent:

```
agy
```

The first time, it asks whether to trust this workspace: yes. Then paste:

> Read AGENTS.md. Explain why MedianTests.test_even_number_of_values fails. Do not change any files.

Read every request before you answer `y` or `n`. Running the tests: `y`. Editing a file: `n`, because in Part 1 the fix is yours. Check the explanation against the test output you saw.

## Step 2. Fix it by hand, then look at the diff

Make the fix. A coloured bar appears in the gutter next to the changed lines; click it to see the old version. Open the Commit tool window (Alt+0 · Cmd+0): `stats.py` is listed under Changes. Double-click it to read the diff.

Run `python -m unittest` again: both `MedianTests` pass. The failures that remain belong to your partner or to Part 3.

Git: `git status`, `git diff`

## Step 3. Commit

Press Ctrl+K · Cmd+K, tick only `stats.py`, type the commit message, and click **Commit** (not Commit and Push). Open the Git tool window (Alt+9 · Cmd+9), Log tab: your commit sits on top of the first commit.

Git: `git add gradebook/stats.py`, then `git commit -m "Fix median for an even number of grades"`

## Step 4. Wait, predict, push

Wait until A says "pushed". **Predict** what will happen when you push now, and write it down. Then push: Ctrl+Shift+K · Cmd+Shift+K, then **Push**.

> **Stop here.** Push before you read on.

---

## Step 5. What just happened

Your push was rejected. Click **Cancel** in PyCharm's dialog for now. In a terminal, git says:

```
 ! [rejected]        main -> main (fetch first)
hint: Updates were rejected because the remote contains work that you do not
hint: have locally.
```

GitHub has A's commit and you do not. If git accepted your push, A's fix would disappear from GitHub, so git refuses.

Ask the agent (rung 1):

> My git push was just rejected. You may run git fetch, git status and git log --oneline --graph --all. Explain what happened and tell me the safest fix. Do not run anything else that changes the repository.

If it suggests `git push --force`, say no and tell the instructor: that would delete A's commit from GitHub.

## Step 6. Update, then push again

**Predict:** will there be a conflict? Then update: **Git → Update Project** (Ctrl+T · Cmd+T), choose **Merge**, OK. If a commit message editor opens for the merge commit, accept it.

Push again (Ctrl+Shift+K · Cmd+Shift+K). It works now. Tell A your fix is on GitHub.

Git: `git pull` (that is `git fetch`, then `git merge origin/main`), then `git push`

## Checkpoint

- Both Git logs show the same picture: your two commits side by side, joined by a merge commit. There was no conflict because you changed different lines.
- `python -m unittest` ends with `FAILED (failures=1)`. That last failure is saved for Part 3.
- The report now passes six of the eight students.

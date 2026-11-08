# Part 2, Partner A: the department raised the pass mark (20 minutes)

You both change the same two lines of `gradebook/config.py`, in different ways. **This time B pushes first.**

**Email from the department (to you).** "From now on the pass mark is 60."

Your partner received a different email. That is on purpose.

## Step 1. Start from the latest main

Update first: **Git → Update Project** (Ctrl+T · Cmd+T).

## Step 2. Change, check, commit

In `gradebook/config.py`, replace these two lines:

```python
# Minimum final grade (0-100) needed to pass the course.
PASSING_GRADE = 56
```

with exactly these two lines:

```python
# Pass mark raised by the department, November 2026.
PASSING_GRADE = 60
```

Run the tests (they fail exactly as before) and the report: Lior now fails. Commit with the message `Raise pass mark to 60`. Do not push yet.

## Step 3. Wait, predict, push

Wait until B says "pushed". **Predict** what happens when you push, and what happens when you then update. Write both down. Then push.

> **Stop here.** Push before you read on.

---

## Step 4. Rejected again, so update with Merge

The push is rejected, as in Part 1. Click **Cancel**, then update: **Git → Update Project** (Ctrl+T · Cmd+T), **Merge**.

This time PyCharm opens the **Conflicts** dialog with `gradebook/config.py` in it. Click **Close** for now and open the file in the editor:

```
<<<<<<< HEAD
# Pass mark raised by the department, November 2026.
PASSING_GRADE = 60
=======
# Pass mark lowered for this semester only.
PASSING_GRADE = 55
>>>>>>> 3f1c2ab
```

Between `<<<<<<<` and `=======` is your version (`HEAD`, what you had). Between `=======` and `>>>>>>>` is the version that came from GitHub, here B's. The last marker shows a commit ID or a branch name.

In a terminal, git says `CONFLICT (content): Merge conflict in gradebook/config.py` and `Automatic merge failed; fix conflicts and then commit the result.`

## Step 5. Predict, then run the tests

**Predict** what the tests do now, then run `python -m unittest`. Every test file that imports the config fails with `SyntaxError`, because conflict markers are not Python.

## Step 6. Ask the agent (rung 2, suggest only)

> There is a merge conflict in gradebook/config.py. Explain both sides and what each choice changes for the students in data/course.csv. Suggest a resolution, but do not edit any files.

The agent can work out the consequences. It cannot know which email is right: policy is a human decision. Ask the instructor for the department's final decision.

## Step 7. Resolve it in PyCharm

In the Commit tool window, under **Merge Conflicts**, click **Resolve**, select `config.py` and click **Merge**. Left: your local version. Right: the version from GitHub. Middle: the result, which you can also type in. Read the pane titles, take the side the department chose, and click **Apply**.

Git: delete the markers by hand, then `git add gradebook/config.py`

## Step 8. Test, commit the merge, push

Run `python -m unittest`: back to `FAILED (failures=1)`. Run the report. Commit (Ctrl+K · Cmd+K; keep the pre-filled merge message), then push and say "pushed".

Git: `git commit`, then `git push`

## Checkpoint

- Both copies of `config.py` hold the department's decision.
- The Git log shows two diamonds, one from each part.
- If you picked Rebase instead of Merge, the left and right panes swap meaning: that is why you read the titles.

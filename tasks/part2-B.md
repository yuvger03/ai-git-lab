# Part 2, Partner B: the department lowered the pass mark (20 minutes)

You both change the same two lines of `gradebook/config.py`, in different ways. **This time you push first.**

**Email from the department (to you).** "This semester the pass mark is 55."

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
# Pass mark lowered for this semester only.
PASSING_GRADE = 55
```

Run the tests (they fail exactly as before) and the report: Noam now passes. Commit with the message `Lower pass mark to 55`.

## Step 3. Push first

Push (Ctrl+Shift+K · Cmd+Shift+K) and say "pushed" out loud.

## Step 4. Watch your partner

Watch A's screen while A pushes and updates, and help A read what git and the agent say. A's card has A's steps.

## Step 5. Update

When A tells you their work is on GitHub, **predict** whether your update will stop with a conflict too. Then update: Ctrl+T · Cmd+T.

> **Stop here.** Update before you read on.

---

No conflict this time: A's merge commit already contains the resolution, so you simply receive it.

## Checkpoint

- Both copies of `config.py` hold the department's decision.
- The Git log shows two diamonds, one from each part.
- `python -m unittest` ends with `FAILED (failures=1)`, the failure saved for Part 3.

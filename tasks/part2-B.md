# Part 2, Partner B: the department lowered the pass mark

**Email from the department (to you).** "This semester the pass mark is 55."

**File you change.** `gradebook/config.py`. Replace these two lines:

```python
# Minimum final grade (0-100) needed to pass the course.
PASSING_GRADE = 56
```

with exactly these two lines:

```python
# Pass mark lowered for this semester only.
PASSING_GRADE = 55
```

**Steps.**

1. Pull first, so you start from the latest `main`.
2. Make the change, run the tests (they still pass or fail exactly as before), and run the report: Noam now passes.
3. Commit with the message `Lower pass mark to 55`.
4. **You push first this time.** Tell your partner "pushed" out loud.

Your partner received a different email. That is on purpose.

# Part 2, Partner A: the department raised the pass mark

**Email from the department (to you).** "From now on the pass mark is 60."

**File you change.** `gradebook/config.py`. Replace these two lines:

```python
# Minimum final grade (0-100) needed to pass the course.
PASSING_GRADE = 56
```

with exactly these two lines:

```python
# Pass mark raised by the department, November 2026.
PASSING_GRADE = 60
```

**Steps.**

1. Pull first, so you start from the latest `main`.
2. Make the change, run the tests (they still pass or fail exactly as before), and run the report: Lior now fails.
3. Commit with the message `Raise pass mark to 60`.
4. **Wait** until Partner B says "pushed". Predict, then push.

Your partner received a different email. That is on purpose.

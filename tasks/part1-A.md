# Part 1, Partner A: the final grade is wrong

**Symptom.** `python -m gradebook report data/course.csv` fails the whole class. Dana scored 90 on every component but her final grade is 30.0.

**Failing tests.** `FinalGradeTests` in `tests/test_grades.py` (two tests).

**File you change.** `gradebook/grades.py`, only the `final_grade` function.

**Steps.**

1. Ask the AI to explain the bug, and tell it not to change any files (rung 1 of the trust ladder). Suggested prompt:
   > Read AGENTS.md. Explain why FinalGradeTests in tests/test_grades.py fail. Do not change any files.
2. Fix it yourself, by hand. It is a one-line fix.
3. Run the tests. Both `FinalGradeTests` pass. The failures that remain are your partner's or belong to later parts.
4. Commit with the message `Fix final grade weighting`.
5. Push. **You push first.** Tell your partner "pushed" out loud.

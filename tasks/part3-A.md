# Part 3, Partner A: letters on the boundaries (AI on a branch)

**Bug.** A final grade exactly on a boundary gets the lower letter. Dana has 90.0 and gets a B; Hila has 80.0 and gets a C.

**Failing test.** `LetterGradeTests.test_grades_exactly_on_a_boundary` in `tests/test_grades.py`.

**Branch.** `fix/letter-boundaries`

**Files the agent may change.** `gradebook/grades.py` only.

**Done when.** All tests pass, and the diff touches only `gradebook/grades.py`.

**Prompt to start with.**

> Read AGENTS.md and tasks/part3-A.md. Fix the bug described there. Change only gradebook/grades.py and do not touch the tests. Then run all tests and show me the diff.

When your pull request is open, review your partner's pull request (`feature/top-n`) with the AI's help. The lab sheet has the prompt.

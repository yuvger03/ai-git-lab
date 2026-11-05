# Part 1, Partner B: the median is wrong

**Symptom.** For an even number of grades, `median` returns the upper middle value instead of the average of the two middle values. `median([4, 1, 3, 2])` returns 3; it should return 2.5.

**Failing test.** `MedianTests.test_even_number_of_values` in `tests/test_stats.py`.

**File you change.** `gradebook/stats.py`, only the `median` function.

**Steps.**

1. Ask the AI to explain the bug, and tell it not to change any files (rung 1 of the trust ladder). Suggested prompt:
   > Read AGENTS.md. Explain why MedianTests.test_even_number_of_values fails. Do not change any files.
2. Fix it yourself, by hand.
3. Run the tests. Both `MedianTests` pass. The failures that remain are your partner's or belong to later parts.
4. Commit with the message `Fix median for an even number of grades`.
5. **Wait** until Partner A says "pushed". Then predict what will happen, write your prediction down, and push.

"""Course policy. Change the numbers here, not the code that uses them."""

# Minimum final grade (0-100) needed to pass the course.
PASSING_GRADE = 56

# Lowest final grade that earns each letter, highest letter first.
# The lowest passing letter always starts at the pass mark.
LETTER_BOUNDS = [
    (90, "A"),
    (80, "B"),
    (70, "C"),
    (PASSING_GRADE, "D"),
]
FAIL_LETTER = "F"

# How much each component counts toward the final grade (sums to 1.0).
WEIGHTS = {
    "homework": 0.3,
    "midterm": 0.2,
    "final": 0.5,
}

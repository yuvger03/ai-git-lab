"""Turning component scores into a final grade, a letter, and pass/fail."""

from .config import FAIL_LETTER, LETTER_BOUNDS, PASSING_GRADE, WEIGHTS


def final_grade(scores: dict[str, float]) -> float:
    """Weighted final grade from 0 to 100, rounded to one decimal."""
    total = 0.0
    for component, weight in WEIGHTS.items():
        total += scores[component] * weight
    return round(total / len(WEIGHTS), 1)


def letter_grade(grade: float) -> str:
    """Letter for a final grade, using the bounds in config.py."""
    for bound, letter in LETTER_BOUNDS:
        if grade > bound:
            return letter
    return FAIL_LETTER


def passed(grade: float) -> bool:
    """True if the final grade reaches the pass mark."""
    return grade >= PASSING_GRADE

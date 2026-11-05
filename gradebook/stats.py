"""Course statistics over a list of final grades."""


def mean(values: list[float]) -> float:
    """Arithmetic mean."""
    return sum(values) / len(values)


def median(values: list[float]) -> float:
    """Middle value; for an even count, the average of the two middle values."""
    ordered = sorted(values)
    middle = len(ordered) // 2
    return ordered[middle]

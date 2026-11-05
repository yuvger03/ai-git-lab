"""Reading the course CSV file."""

import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Student:
    name: str
    scores: dict[str, float]


def load_students(path: str | Path) -> list[Student]:
    """One Student per CSV row. Columns: name, then one column per component."""
    students = []
    with open(path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            name = row.pop("name").strip()
            scores = {column.strip(): float(value) for column, value in row.items()}
            students.append(Student(name=name, scores=scores))
    return students

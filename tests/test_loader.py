import unittest
from pathlib import Path

from gradebook.loader import load_students

DATA = Path(__file__).resolve().parent.parent / "data" / "course.csv"


class LoaderTests(unittest.TestCase):
    def test_loads_every_student(self):
        students = load_students(DATA)
        self.assertEqual(len(students), 8)
        self.assertEqual(students[0].name, "Avi")

    def test_scores_are_numbers(self):
        for student in load_students(DATA):
            for score in student.scores.values():
                self.assertIsInstance(score, float)


if __name__ == "__main__":
    unittest.main()

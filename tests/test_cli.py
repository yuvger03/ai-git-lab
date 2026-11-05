import contextlib
import io
import unittest
from pathlib import Path

from gradebook.cli import main

DATA = str(Path(__file__).resolve().parent.parent / "data" / "course.csv")
NAMES = ["Avi", "Dana", "Eitan", "Hila", "Lior", "Maya", "Noam", "Tal"]


def run(*argv: str) -> tuple[int, str]:
    """Run the CLI in-process and return (exit code, printed output)."""
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        code = main(list(argv))
    return code, out.getvalue()


class ReportTests(unittest.TestCase):
    def test_report_lists_every_student(self):
        code, out = run("report", DATA)
        self.assertEqual(code, 0)
        for name in NAMES:
            self.assertIn(name, out)


class StatsTests(unittest.TestCase):
    def test_stats_counts_the_students(self):
        code, out = run("stats", DATA)
        self.assertEqual(code, 0)
        self.assertIn("Students:  8", out)


if __name__ == "__main__":
    unittest.main()

import unittest

from gradebook import config
from gradebook.grades import final_grade, letter_grade, passed


class FinalGradeTests(unittest.TestCase):
    def test_equal_scores_give_that_score(self):
        self.assertEqual(final_grade({"homework": 90, "midterm": 90, "final": 90}), 90.0)

    def test_components_are_weighted(self):
        # 0.3 * 100 + 0.2 * 50 + 0.5 * 80 = 30 + 10 + 40 = 80
        self.assertEqual(final_grade({"homework": 100, "midterm": 50, "final": 80}), 80.0)


class LetterGradeTests(unittest.TestCase):
    def test_grades_inside_a_range(self):
        self.assertEqual(letter_grade(95), "A")
        self.assertEqual(letter_grade(85), "B")
        self.assertEqual(letter_grade(75), "C")
        self.assertEqual(letter_grade(config.PASSING_GRADE + 1), "D")
        self.assertEqual(letter_grade(30), "F")

    def test_grades_exactly_on_a_boundary(self):
        self.assertEqual(letter_grade(90), "A")
        self.assertEqual(letter_grade(80), "B")
        self.assertEqual(letter_grade(70), "C")
        self.assertEqual(letter_grade(config.PASSING_GRADE), "D")


class PassedTests(unittest.TestCase):
    def test_the_pass_mark_passes(self):
        self.assertTrue(passed(config.PASSING_GRADE))

    def test_just_below_the_pass_mark_fails(self):
        self.assertFalse(passed(config.PASSING_GRADE - 0.1))


if __name__ == "__main__":
    unittest.main()

import unittest

from gradebook.stats import mean, median


class MeanTests(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(mean([70, 80, 90]), 80)


class MedianTests(unittest.TestCase):
    def test_odd_number_of_values(self):
        self.assertEqual(median([3, 1, 2]), 2)

    def test_even_number_of_values(self):
        self.assertEqual(median([4, 1, 3, 2]), 2.5)


if __name__ == "__main__":
    unittest.main()


import unittest

from day1.part1 import get_most_calories
from part2 import get_most_calories_3elves


TEST_INPUT = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


class TestDay1(unittest.TestCase):
    def test_most_calories_computation(self):
        lines = TEST_INPUT.splitlines()
        most_calories = get_most_calories(lines)
        print(f"{most_calories = }")
        self.assertEqual(most_calories, 24000)

    def test_get_most_calories_3elves(self):
        lines = TEST_INPUT.splitlines()
        most_calories = get_most_calories_3elves(lines)
        print(f"{most_calories = }")
        self.assertEqual(most_calories, 45000)

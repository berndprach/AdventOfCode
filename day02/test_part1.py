
import unittest

from part1 import get_score


TEST_INPUT = """A Y
B X
C Z
"""


class TestPart1(unittest.TestCase):
    def test_get_score(self):
        lines = TEST_INPUT.splitlines()
        my_score = get_score(lines)
        print(f"{my_score = }")
        self.assertEqual(my_score, 15)


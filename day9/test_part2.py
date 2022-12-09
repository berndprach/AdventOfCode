
import unittest

from part2 import solve
from test_part1 import TEST_INPUT

TEST_INPUT2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""


class TestPart2(unittest.TestCase):
    def test_solve(self):
        lines = TEST_INPUT.splitlines()
        solution = solve(lines)
        print(f"{solution = }")
        self.assertEqual(solution, 1)

        lines = TEST_INPUT2.splitlines()
        solution = solve(lines)
        print(f"{solution = }")
        self.assertEqual(solution, 36)


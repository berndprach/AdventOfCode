
import unittest

from part2 import solve
from test_part1 import TEST_INPUT


class TestPart2(unittest.TestCase):
    def test_solve(self):
        lines = TEST_INPUT.splitlines()
        solution = solve(lines)
        print(f"{solution = }")
        self.assertEqual(solution, 24933642)


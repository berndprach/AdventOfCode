
import unittest

from test_part1 import TEST_INPUT
from part2 import solve


class TestPart2(unittest.TestCase):
    def test_solve(self):
        lines = TEST_INPUT.splitlines()
        solution = solve(lines)
        self.assertEqual(solution, 4)


import unittest

from part1 import solve


class TestPart1(unittest.TestCase):
    def test_solve(self):
        with open("test_input.txt") as f:
            lines = f.read().splitlines()
        solution = solve(lines, line_nr=10)
        print(f"\n\nSolution = {solution}")
        self.assertEqual(solution, 26)


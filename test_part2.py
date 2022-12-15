
import unittest

from part2 import solve


class TestPart1(unittest.TestCase):
    def test_solve(self):
        with open("test_input.txt") as f:
            lines = f.read().splitlines()
        solution = solve(lines, max_line_nr=20)
        print(f"\n\nSolution = {solution}")
        self.assertEqual(solution, 56000011)


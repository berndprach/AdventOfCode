
import unittest

from part1 import solve


class TestPart1(unittest.TestCase):
    def test_solve(self):
        with open("test_input.txt") as f:
            lines = f.read().splitlines()
        solution = solve(lines)
        print(f"\n\nsolution = {solution}")
        self.assertEqual(solution, "2=-1=0")


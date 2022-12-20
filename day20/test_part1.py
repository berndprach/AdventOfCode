
import unittest

from part1 import solve


class TestPart1(unittest.TestCase):
    def test_solve(self):
        with open("test_input.txt") as f:
            lines = f.read().splitlines()
        solution = solve(lines)
        print(f"{solution = }")
        self.assertEqual(solution, 3)


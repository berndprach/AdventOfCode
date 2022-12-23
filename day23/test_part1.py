
import unittest

from part1 import solve

SMALL_EXAMPLE = """\
.....
..##.
..#..
.....
..##.
....."""


class TestPart1(unittest.TestCase):
    def test_small_example(self):
        lines = SMALL_EXAMPLE.splitlines()
        solution = solve(lines)
        self.assertEqual(solution, 5 * 6 - 5)

    def test_solve(self):
        with open("test_input.txt") as f:
            lines = f.read().splitlines()
        solution = solve(lines)
        print(f"{solution = }")
        self.assertEqual(solution, 110)


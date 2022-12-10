
import unittest

from part1 import solve


TEST_INPUT = """30373
25512
65332
33549
35390"""


class TestPart1(unittest.TestCase):
    def test_solve(self):
        lines = TEST_INPUT.splitlines()
        solution = solve(lines)
        print(f"{solution = }")
        self.assertEqual(solution, 21)


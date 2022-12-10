
import unittest

from part1 import solve


TEST_INPUT = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""


class TestPart1(unittest.TestCase):
    def test_solve(self):
        lines = TEST_INPUT.splitlines()
        solution = solve(lines)
        print(f"{solution = }")
        self.assertEqual(solution, 13)


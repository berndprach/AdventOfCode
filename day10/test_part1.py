
import unittest

from part1 import solve, get_register_values


TEST_INPUT = """noop
addx 3
addx -5"""

GOAL_VALUES = [1, 1, 1, 4, 4]


class TestPart1(unittest.TestCase):
    def test_get_register_values(self):
        lines = TEST_INPUT.splitlines()
        register_values = get_register_values(lines)
        print(f"{register_values = }")
        self.assertListEqual(register_values, GOAL_VALUES)

    def test_solve(self):
        with open("test_input.txt") as f:
            lines = f.read().splitlines()
        solution = solve(lines)
        print(f"{solution = }")
        self.assertEqual(solution, 13140)


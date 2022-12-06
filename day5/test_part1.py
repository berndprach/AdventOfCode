
import unittest

from part1 import process_lines, solve


TEST_INPUT = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

TEST_STACKS = {
    1: ["Z", "N"],
    2: ["M", "C", "D"],
    3: ["P"],
}


class TestPart1(unittest.TestCase):
    def test_process_lines(self):
        lines = TEST_INPUT.splitlines()
        starting_stacks, _ = process_lines(lines)
        print(f"{starting_stacks = }")
        self.assertDictEqual(starting_stacks, TEST_STACKS)

    def test_solve(self):
        lines = TEST_INPUT.splitlines()
        solution = solve(lines)
        print(f"{solution = }")
        self.assertEqual(solution, "CMZ")


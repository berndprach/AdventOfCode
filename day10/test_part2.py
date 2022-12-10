import unittest

from part2 import get_register_values, get_pixels, solve

TEST_OUTPUT = (
    "##..##..##..##..##..##..##..##..##..##.."
    "###...###...###...###...###...###...###."
    "####....####....####....####....####...."
    "#####.....#####.....#####.....#####....."
    "######......######......######......####"
    "#######.......#######.......#######....."
)


class TestPart2(unittest.TestCase):
    def test_get_pixels(self):
        with open("test_input.txt") as f:
            lines = f.read().splitlines()
        register_values = get_register_values(lines)
        pixels = get_pixels(register_values)
        print(f"  goal = {repr(TEST_OUTPUT)}")
        print(f"{pixels = }")
        self.assertEqual(pixels, TEST_OUTPUT)

    def test_solve(self):
        with open("test_input.txt") as f:
            lines = f.read().splitlines()
        solve(lines)

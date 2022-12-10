
import unittest

from part1 import priority, split_line, get_total_priority


TEST_INPUT = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


class TestPart1(unittest.TestCase):
    def test_priority(self):
        self.assertEqual(priority("b"), 2)
        self.assertEqual(priority("B"), 28)

    def test_split_line(self):
        l1, l2 = split_line("ABCDEF")
        self.assertEqual(l1, "ABC")
        self.assertEqual(l2, "DEF")

    def test_get_total_priority(self):
        lines = TEST_INPUT.splitlines()
        total_priority = get_total_priority(lines)
        print(f"{total_priority = }")
        self.assertEqual(total_priority, 157)



import unittest

from test_part1 import TEST_INPUT
from part2 import get_total_priority


class TestPart2(unittest.TestCase):
    def test_get_total_priority(self):
        lines = TEST_INPUT.splitlines()
        total_priority = get_total_priority(lines)
        print(f"{total_priority = }")
        self.assertEqual(total_priority, 70)

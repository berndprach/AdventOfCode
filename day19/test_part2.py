import unittest

from part2 import get_blueprints, get_maximal_geodes


class TestPart2(unittest.TestCase):
    def test_solve(self):
        with open("test_input.txt") as f:
            lines = f.read().replace("\n  ", " ").replace("\n\n", "\n").splitlines()

        blueprints = get_blueprints(lines)

        s1 = get_maximal_geodes(factory_costs=blueprints[1])
        self.assertEqual(s1, 56)

        s2 = get_maximal_geodes(factory_costs=blueprints[2])
        self.assertEqual(s2, 62)

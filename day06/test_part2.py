
import unittest

from part2 import find_start_of_packet


TEST_INPUTS = {
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb": 19,
    "bvwbjplbgvbhsrlpgdmjqwftvncz": 23,
    "nppdvjthqldpwncqszvftbrmjlhg": 23,
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg": 29,
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw": 26,
}


class TestPart2(unittest.TestCase):
    def test_find_start_of_packet(self):
        for line, goal_start_of_packet in TEST_INPUTS.items():
            start_of_packet = find_start_of_packet(line)
            print(f"{start_of_packet = }")
            self.assertEqual(start_of_packet, goal_start_of_packet)


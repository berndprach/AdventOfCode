
import unittest

from part1 import find_start_of_packet


TEST_INPUTS = {
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb": 7,
    "bvwbjplbgvbhsrlpgdmjqwftvncz": 5,
    "nppdvjthqldpwncqszvftbrmjlhg": 6,
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg": 10,
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw": 11,
}


class TestPart1(unittest.TestCase):
    def test_find_start_of_packet(self):
        for line, goal_start_of_packet in TEST_INPUTS.items():
            start_of_packet = find_start_of_packet(line)
            print(f"{start_of_packet = }")
            self.assertEqual(start_of_packet, goal_start_of_packet)



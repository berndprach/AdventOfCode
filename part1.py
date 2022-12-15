import re

LINE_NR = 2000000


def read_lines():
    with open("input.txt") as f:
        return f.read().splitlines()


def parse_lines(lines):
    sensors = []
    closest_beacon = {}
    for line in lines:
        x, y, beacon_x, beacon_y = integers_in_line(line)
        sensor = (x, y)
        sensors.append(sensor)
        closest_beacon[sensor] = (beacon_x, beacon_y)
    return sensors, closest_beacon


def integers_in_line(line):
    return [int(i_str) for i_str in re.findall(r"-?\d+", line)]


def manhatten_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def solve(lines, line_nr=LINE_NR):
    """
    .###S###.
    ..#####..
    ---###---
    """
    sensors, closest_beacon = parse_lines(lines)
    goal_line_covered = set()
    for sensor in sensors:
        beacon_distance = manhatten_distance(sensor, closest_beacon[sensor])
        line_distance = abs(sensor[1] - line_nr)
        difference = beacon_distance - line_distance
        if difference >= 0:
            for x in range(-difference, difference + 1):
                goal_line_covered.add(sensor[0] + x)

    goal_line_beacons = set([beacon[0] for beacon in closest_beacon.values()
                             if beacon[1] == line_nr])
    return len(goal_line_covered) - len(goal_line_beacons)


def main():
    lines = read_lines()
    solution = solve(lines)
    print(f"{solution}")


if __name__ == "__main__":
    main()

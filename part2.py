
import timeit

from part1 import read_lines, parse_lines, manhatten_distance


def find_uncovered_in_rectangle(coordinates, sensors_and_distances):
    for sensor, beacon_distance in sensors_and_distances:
        if all_corners_covered(sensor, beacon_distance, coordinates):
            return None

    x1, x2, y1, y2 = coordinates
    if x1 == x2 and y1 == y2:
        return x1, y1

    for half in get_halves(coordinates):
        uncovered = find_uncovered_in_rectangle(half, sensors_and_distances)
        if uncovered is None:
            continue
        return uncovered

    return None


def all_corners_covered(sensor, beacon_distance, coordinates):
    x1, x2, y1, y2 = coordinates
    corner_points = [(x1, y1), (x2, y1), (x1, y2), (x2, y2)]
    for corner in corner_points:
        if manhatten_distance(sensor, corner) > beacon_distance:
            return False
    return True


def get_halves(coordinates):
    x1, x2, y1, y2 = coordinates
    if x2 - x1 > y2 - y1:
        x_mid = (x1 + x2) // 2
        return [
            (x1, x_mid, y1, y2),
            (x_mid + 1, x2, y1, y2),
        ]
    else:
        y_mid = (y1 + y2) // 2
        return [
            (x1, x2, y1, y_mid),
            (x1, x2, y_mid + 1, y2),
        ]


def solve(lines, max_line_nr=4_000_000):
    sensors, closest_beacon = parse_lines(lines)
    distances = [manhatten_distance(sensor, closest_beacon[sensor])
                 for sensor in sensors]
    sensors_with_distances = [(sensor, distance)
                              for sensor, distance in zip(sensors, distances)]
    x, y = find_uncovered_in_rectangle([0, max_line_nr, 0, max_line_nr],
                                       sensors_with_distances)
    tuning_frequency = 4000000 * x + y
    return tuning_frequency


def main():
    lines = read_lines()
    solution = solve(lines)
    print(f"{solution}")


if __name__ == "__main__":
    start = timeit.default_timer()

    main()

    stop = timeit.default_timer()
    print('Time: ', stop - start)


from part1 import read_lines, SAND_START, parse_lines, drop_grain_of_sand


def solve(lines):
    filled = parse_lines(lines)
    max_depth = max(pos[1] for pos in filled)
    floor_level = max_depth + 2
    for w in range(500-floor_level, 500+floor_level+1):
        filled.add((w, floor_level))

    number_of_grains_dropped = 0
    while True:
        did_stop, position = drop_grain_of_sand(filled)
        if not did_stop:
            raise ValueError("Grain did not stop!")
        number_of_grains_dropped += 1
        if position == SAND_START:
            break
    return number_of_grains_dropped


def main():
    lines = read_lines()
    solution = solve(lines)
    print(f"{solution = }")


if __name__ == "__main__":
    main()

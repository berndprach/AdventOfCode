

SAND_START = (500, 0)


def read_lines():
    with open("input.txt") as f:
        return f.read().splitlines()


def parse_lines(lines):
    filled: set[tuple[int, int]] = set()
    for line in lines:  # E.g. "498,4 -> 498,6 -> 496,6"
        positions = []
        for position_str in line.split(" -> "):
            w_str, h_str = position_str.split(",")
            positions.append((int(w_str), int(h_str)))

        for i in range(len(positions)-1):
            fill_with_rocks(filled, positions[i], positions[i+1])
    return filled


def fill_with_rocks(filled, start, end):
    w_start, h_start = start
    w_end, h_end = end
    if h_start == h_end:
        for w in range(min(w_start, w_end), max(w_start, w_end)+1):
            filled.add((w, h_start))
    elif w_start == w_end:
        for h in range(min(h_start, h_end), max(h_start, h_end)+1):
            filled.add((w_start, h))
    else:
        raise ValueError(f"Can not fill with rocks from {start} to {end}!s")


def drop_grain_of_sand(filled):
    position = SAND_START
    for i in range(1000):
        if down(position) not in filled:
            position = down(position)
        elif down_left(position) not in filled:
            position = down_left(position)
        elif down_right(position) not in filled:
            position = down_right(position)
        else:
            filled.add(position)
            return True, position
    return False, position


def down(position):
    return position[0], position[1] + 1


def down_left(position):
    return position[0] - 1, position[1] + 1


def down_right(position):
    return position[0] + 1, position[1] + 1


def solve(lines):
    filled = parse_lines(lines)
    number_of_grains_dropped = 0
    while True:
        did_stop, position = drop_grain_of_sand(filled)
        if not did_stop:
            break
        number_of_grains_dropped += 1
    return number_of_grains_dropped


def main():
    lines = read_lines()
    solution = solve(lines)
    print(f"{solution = }")


if __name__ == "__main__":
    main()

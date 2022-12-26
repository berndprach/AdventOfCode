
import timeit

from part1 import Position, read_lines, do_round, get_blizzards


def reach_y_of(y, starting_position, blizzards, grid):
    possible_positions = {starting_position}
    i = 0
    while True:
        i += 1
        possible_positions = do_round(possible_positions, blizzards, grid)

        for pos in possible_positions:
            if pos.y == y:
                return i, pos


def solve(lines):
    blizzards, grid, width, height = get_blizzards(lines)

    i1, pos = reach_y_of(height - 1, Position(1, 0), blizzards, grid)
    print(f"Reached position {pos} in {i1} rounds.")
    i2, pos = reach_y_of(0, pos, blizzards, grid)
    print(f"Reached position {pos} in additional {i2} rounds.")
    i3, _ = reach_y_of(height - 1, pos, blizzards, grid)
    print(f"Finished in {i1 + i2 + i3} rounds.")

    return i1 + i2 + i3


def main():
    lines = read_lines()
    solution = solve(lines)
    print(f"solution = {solution}")


if __name__ == "__main__":
    start = timeit.default_timer()

    main()

    stop = timeit.default_timer()
    print('Time: ', stop - start)

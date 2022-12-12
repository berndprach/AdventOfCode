
from part1 import read_lines, parse_grid


def do_one_step(grid: dict[tuple[int, int], int],
                current_positions: set[tuple[int, int]]
                ) -> set[tuple[int, int]]:
    """
    Sabqponm
    abcryxxl
    accszExk
    acctuvwj
    abdefghi
    """
    new_positions = set()
    for pos in current_positions:
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            new_pos = (pos[0] + dx, pos[1] + dy)
            # if new_pos in grid and grid[new_pos] <= grid[pos] + 1:
            if new_pos in grid and grid[pos] <= grid[new_pos] + 1:
                new_positions.add(new_pos)
    return new_positions


def solve(lines):
    grid, start_pos, end_pos = parse_grid(lines)
    current_positions = {end_pos}
    nrof_steps = 0
    current_heights = set()
    while 0 not in current_heights:
        current_positions = do_one_step(grid, current_positions)
        current_heights = {grid[pos] for pos in current_positions}
        nrof_steps += 1

    return nrof_steps


def main():
    lines = read_lines()
    solution = solve(lines)
    print(f"{solution = }")


if __name__ == "__main__":
    main()

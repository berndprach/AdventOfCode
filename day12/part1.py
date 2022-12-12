

def read_lines():
    with open("input.txt") as f:
        return f.read().splitlines()


def parse_grid(lines: list[str]):
    grid: dict[tuple[int, int]] = {}
    start_pos, end_pos = None, None
    for i, line in enumerate(lines):
        for j, letter in enumerate(line):
            if letter == "S":
                grid[(i, j)] = 0
                start_pos = (i, j)
            elif letter == "E":
                grid[(i, j)] = 25
                end_pos = (i, j)
            else:
                grid[(i, j)] = ord(letter) - ord("a")
    return grid, start_pos, end_pos


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
            if new_pos in grid and grid[new_pos] <= grid[pos] + 1:
                new_positions.add(new_pos)
    return new_positions


def solve(lines):
    grid, start_pos, end_pos = parse_grid(lines)
    current_positions = {start_pos}
    nrof_steps = 0
    while end_pos not in current_positions:
        current_positions = do_one_step(grid, current_positions)
        nrof_steps += 1

    return nrof_steps


def main():
    lines = read_lines()
    solution = solve(lines)
    print(f"{solution = }")


if __name__ == "__main__":
    main()

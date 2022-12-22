import timeit

from part1 import Tile, Direction, STEP, Position, read_lines, get_grid, \
    turn, opposite, step, SCORE

CUBE_SIDELENGTH = 50

"""
. # #
. # .
# # .
# . .
"""

EDGES = (
    ((2, [1, 2], Direction.RIGHT), ([2, 3], 1, Direction.DOWN)),
    ((2, [2, 3], Direction.RIGHT), (3, [1, 0], Direction.RIGHT)),
    ((1, [3, 4], Direction.RIGHT), ([1, 2], 3, Direction.DOWN)),
    (([0, 1], 4, Direction.DOWN), ([2, 3], 0, Direction.UP)),
    ((0, [3, 4], Direction.LEFT), ([1, 2], 0, Direction.UP)),
    ((0, [2, 3], Direction.LEFT), (1, [1, 0], Direction.LEFT)),
    (([0, 1], 2, Direction.UP), (1, [1, 2], Direction.LEFT)),
)


def fill(start_value, end_value):
    # Including min(s, t) and excluding max(s, t).
    if start_value < end_value:
        return range(start_value, end_value)
    else:
        return range(start_value-1, end_value-1, -1)


def edge_positions(edge, sl=CUBE_SIDELENGTH):
    x_range, y_range, d = edge
    if isinstance(x_range, int):
        if d == Direction.LEFT:
            xs = [x_range * sl + 1 for _ in range(sl)]
        else:
            xs = [x_range * sl for _ in range(sl)]
        ys = fill(y_range[0] * sl + 1,
                  y_range[1] * sl + 1)
        return [Position(x, y) for x, y in zip(xs, ys)]

    if isinstance(y_range, int):
        xs = fill(x_range[0] * sl + 1,
                  x_range[1] * sl + 1)
        if d == Direction.UP:
            ys = [y_range * sl + 1 for _ in range(sl)]
        else:
            ys = [y_range * sl for _ in range(sl)]
        return [Position(x, y) for x, y in zip(xs, ys)]


def draw_edges(edges):
    print("\n\n")

    c = 5
    outputs = {}

    for i in range(c + 1, 2 * c + 1):
        for j in range(c + 1, 2 * c + 1):
            outputs[(i, j)] = "+"

    for i, (e1, e2) in enumerate(edges):
        for e in [e1, e2]:
            for pos in edge_positions(e, sl=c):
                outputs[(pos.x, pos.y)] = i
            continue

    for j in range(4 * c + 1):
        for i in range(3 * c + 1):
            letter = outputs.get((i + 1, j + 1), ".")
            print(letter, end=" ")
        print()


draw_edges(EDGES)


def get_edge_jumps(edges, sl=CUBE_SIDELENGTH):
    edge_jumps: dict[
        tuple[Position, Direction], tuple[Position, Direction]] = {}
    for e1, e2 in edges:
        d1, d2 = e1[2], e2[2]
        for p1, p2 in zip(edge_positions(e1, sl), edge_positions(e2, sl)):
            edge_jumps[(p1, d1)] = (p2, opposite(d2))
            edge_jumps[(p2, d2)] = (p1, opposite(d1))

    return edge_jumps


def draw_edge_jumps(edges, sl=CUBE_SIDELENGTH):
    print("\n\n")
    edge_jumps = get_edge_jumps(edges, sl=sl)

    edge_pairs = {}
    for i, ((p1, d1), (p2, d2)) in enumerate(edge_jumps.items()):
        edge_pairs[(p1.x, p1.y)] = i // 2
        edge_pairs[(p2.x, p2.y)] = i // 2

    c = 5
    for j in range(4 * c + 1):
        for i in range(3 * c + 1):
            letter = edge_pairs.get((i + 1, j + 1), ".")
            print(f"{str(letter):>2}", end=" ")
        print()


draw_edge_jumps(EDGES, sl=5)


EDGE_JUMPS = get_edge_jumps(EDGES)


def walk(grid, starting_position, instructions):
    current_direction: Direction = Direction.RIGHT
    current_position: Position = starting_position

    for instruction in instructions:
        if isinstance(instruction, str):
            current_direction = turn(current_direction, instruction)
        elif isinstance(instruction, int):
            current_position, current_direction = walk_straight(
                grid,
                current_position,
                current_direction,
                nrof_steps=instruction
            )
        else:
            raise ValueError(f"Unknown instruction: {instruction}")
    return current_position, current_direction


def walk_straight(grid, current_position, current_direction, nrof_steps: int):
    for _ in range(nrof_steps):
        new_position = step(current_position, current_direction)
        new_tile = grid.get(new_position, Tile.NONE)

        if new_tile == Tile.SOLID:
            return current_position, current_direction

        if new_tile == Tile.OPEN:
            current_position = new_position

        if new_tile == Tile.NONE:
            """
            . . . . . .    
            . . . . V .   
            . . .   
            . . <
            . . .
            """

            new_position, new_direction = EDGE_JUMPS[(current_position,
                                                      current_direction)]
            if grid[new_position] == Tile.SOLID:
                return current_position, current_direction

            current_position = new_position
            current_direction = new_direction

    return current_position, current_direction


def solve(lines):
    grid, starting_position, instructions = get_grid(lines)
    print(f"{starting_position = }")
    final_position, final_direction = walk(grid, starting_position,
                                           instructions)
    print(f"{final_position = }")
    return (
            1000 * final_position.y
            + 4 * final_position.x
            + SCORE[final_direction]
    )


def main():
    lines = read_lines()
    solution = solve(lines)
    print(f"{solution = }")


if __name__ == "__main__":
    start = timeit.default_timer()

    main()

    stop = timeit.default_timer()
    print('Time: ', stop - start)

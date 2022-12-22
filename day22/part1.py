import timeit
from enum import Enum
from dataclasses import dataclass


class Tile(Enum):
    OPEN = "."
    SOLID = "#"
    NONE = " "


class Direction(Enum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3


SCORE: dict[Direction, int] = {Direction(i): i for i in range(4)}


def turn(direction: Direction, instruction: str):
    if instruction == "L":
        return Direction((SCORE[direction] - 1) % 4)
    elif instruction == "R":
        return Direction((SCORE[direction] + 1) % 4)
    else:
        raise ValueError(f"Unknown instruction for turning: {instruction}")


def opposite(direction: Direction):
    return turn(turn(direction, "L"), "L")


@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)


STEP = {
    Direction.RIGHT: Position(1, 0),
    Direction.DOWN: Position(0, 1),
    Direction.LEFT: Position(-1, 0),
    Direction.UP: Position(0, -1),
}


def read_lines():
    with open("input.txt") as f:
        return f.read().splitlines()


def get_grid(lines):
    grid = {}
    starting_position = None
    for j, line in enumerate(lines):
        if line == "":
            break
        for i, c in enumerate(line):
            pos = Position(i + 1, j + 1)
            grid[pos] = Tile(c)

            if starting_position is None and grid[pos] != Tile.NONE:
                starting_position = pos

    instructions_str = lines[-1]
    instructions = []
    current_number = 0
    for i in instructions_str:  # E.g. "10R5L5R10L4R5L5"
        if i.isdigit():
            current_number = 10 * current_number + int(i)
        else:
            instructions.append(current_number)
            current_number = 0
            instructions.append(i)
    instructions.append(current_number)

    return grid, starting_position, instructions


def step(position: Position, direction: Direction):
    return position + STEP[direction]


def walk(grid, starting_position, instructions):
    current_direction: Direction = Direction.RIGHT
    current_position: Position = starting_position

    for instruction in instructions:
        if isinstance(instruction, str):
            current_direction = turn(current_direction, instruction)
        elif isinstance(instruction, int):
            current_position = walk_straight(grid,
                                             current_position,
                                             current_direction,
                                             nrof_steps=instruction)
        else:
            raise ValueError(f"Unknown instruction: {instruction}")
    return current_position, current_direction


def walk_straight(grid, current_position, current_direction, nrof_steps: int):
    for _ in range(nrof_steps):
        new_position = step(current_position, current_direction)
        new_tile = grid.get(new_position, Tile.NONE)

        if new_tile == Tile.SOLID:
            return current_position

        if new_tile == Tile.OPEN:
            current_position = new_position

        if new_tile == Tile.NONE:
            """
            . . . # . .    
            . . . . . .   
            X . # . . >   
            . . . V . . 
            """
            opposite_direction = opposite(current_direction)
            fly_back_position = current_position
            while grid.get(fly_back_position, Tile.NONE) != Tile.NONE:
                fly_back_position = step(fly_back_position,
                                         opposite_direction)
            new_position = step(fly_back_position, current_direction)

            if grid[new_position] == Tile.SOLID:
                return current_position

            current_position = new_position

    return current_position


def solve(lines):
    grid, starting_position, instructions = get_grid(lines)
    print(f"{starting_position = }")
    final_position, final_direction = walk(grid,
                                           starting_position,
                                           instructions)
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

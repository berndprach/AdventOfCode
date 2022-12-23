import timeit
from enum import Enum
from dataclasses import dataclass


@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)


class Direction(Enum):
    N = "north"
    NE = "northeast"
    E = "east"
    SE = "southeast"
    S = "south"
    SW = "southwest"
    W = "west"
    NW = "northwest"


VECTOR = {
    Direction.N: Position(0, 1),
    Direction.NE: Position(1, 1),
    Direction.E: Position(1, 0),
    Direction.SE: Position(1, -1),
    Direction.S: Position(0, -1),
    Direction.SW: Position(-1, -1),
    Direction.W: Position(-1, 0),
    Direction.NW: Position(-1, 1),
}


ADJACENT = {
    Direction.N: [Direction.NW, Direction.NE],
    Direction.E: [Direction.NE, Direction.SE],
    Direction.S: [Direction.SE, Direction.SW],
    Direction.W: [Direction.SW, Direction.NW],
}

CHECK_DIRECTION = [Direction.N, Direction.S, Direction.W, Direction.E]


def read_lines():
    with open("input.txt") as f:
        return f.read().splitlines()


def get_elf_positions(lines):
    elf_positions: list[Position] = []
    for j, line in enumerate(reversed(lines)):
        for i, c in enumerate(line):
            if c == "#":
                elf_positions.append(Position(i, j))

    print(f"Found {len(elf_positions)} elves.")
    return elf_positions


def do_round(elf_positions: list[Position], first_considered=0):
    proposed_positions: list[Position] = []
    proposed_so_far: set[Position] = set()
    duplicates: set[Position] = set()

    elf_set = set(elf_positions)

    for elf_position in elf_positions:

        if no_neighbours(elf_position, elf_set):
            proposed_positions.append(elf_position)
            continue

        for check_nr in range(4):
            check_id = (first_considered + check_nr) % 4
            check_direction = CHECK_DIRECTION[check_id]

            if is_valid(check_direction, elf_position, elf_set):
                proposed_position = elf_position + VECTOR[check_direction]
                proposed_positions.append(proposed_position)
                if proposed_position in proposed_so_far:
                    duplicates.add(proposed_position)
                proposed_so_far.add(proposed_position)
                break
        else:  # No direction valid
            proposed_positions.append(elf_position)

    new_elf_positions = []
    for elf_position, proposed_position in zip(elf_positions,
                                               proposed_positions):
        if proposed_position in duplicates:
            new_elf_positions.append(elf_position)
        else:
            new_elf_positions.append(proposed_position)

    return new_elf_positions


def no_neighbours(elf_position, elf_positions):
    for direction in Direction:
        check_position = elf_position + VECTOR[direction]
        if check_position in elf_positions:
            return False
    return True


def is_valid(check_direction: Direction, position: Position, elf_positions):
    for direction in [check_direction] + ADJACENT[check_direction]:
        proposed_position = position + VECTOR[direction]
        if proposed_position in elf_positions:
            return False
    return True


def print_elf_positions(elf_positions):
    min_x = min(elf_position.x for elf_position in elf_positions)
    max_x = max(elf_position.x for elf_position in elf_positions)
    min_y = min(elf_position.y for elf_position in elf_positions)
    max_y = max(elf_position.y for elf_position in elf_positions)

    for y in range(max_y, min_y -1, -1):
        for x in range(min_x, max_x+1):
            if Position(x, y) in elf_positions:
                print("#", end="")
            else:
                print(".", end="")
        print()


def solve(lines):
    elf_positions = get_elf_positions(lines)

    for i in range(10):
        elf_positions = do_round(elf_positions, first_considered=i % 4)

    min_x = min(elf_position.x for elf_position in elf_positions)
    min_y = min(elf_position.y for elf_position in elf_positions)
    max_x = max(elf_position.x for elf_position in elf_positions)
    max_y = max(elf_position.y for elf_position in elf_positions)

    area = (max_x - min_x + 1) * (max_y - min_y + 1)
    return area - len(elf_positions)


def main():
    lines = read_lines()
    solution = solve(lines)
    print(f"{solution = }")


if __name__ == "__main__":
    start = timeit.default_timer()

    main()

    stop = timeit.default_timer()
    print('Time: ', stop - start)

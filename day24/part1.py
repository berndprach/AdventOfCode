
import timeit
from dataclasses import dataclass


@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)


STEP = {
    ">": Position(1, 0),
    "<": Position(-1, 0),
    "v": Position(0, 1),
    "^": Position(0, -1),
}


class Blizzard:
    width = None
    height = None

    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def move(self):
        self.position += self.direction

        x, y = self.position.x, self.position.y
        if x < 1:
            x = self.width-2
        if x > self.width-2:
            x = 1
        if y < 1:
            y = self.height-2
        if y > self.height-2:
            y = 1
        self.position = Position(x, y)


def read_lines():
    with open("input.txt") as f:
        return f.read().splitlines()


def get_blizzards(lines):
    """
    #.######
    #>>.<^<#
    #.<..<<#
    #>v.><>#
    #<^v^^>#
    ######.#
    """
    blizzards = []
    height = len(lines)
    width = len(lines[0])

    Blizzard.width = width
    Blizzard.height = height

    valley = set()

    for j, line in enumerate(lines):
        for i, c in enumerate(line):
            if c == "#":
                continue

            pos = Position(i, j)
            valley.add(pos)

            if c == ".":
                continue

            blizzard = Blizzard(pos, direction=STEP[c])
            blizzards.append(blizzard)

    print(f"\nFound {len(blizzards)} blizzards.")
    return blizzards, valley, width, height


def do_round(possible_positions, blizzards, valley):
    for blizzard in blizzards:
        blizzard.move()

    blizzard_positions = {blizzard.position for blizzard in blizzards}
    clear_positions = valley - blizzard_positions

    reachable = {pos for pos in possible_positions}
    for position in possible_positions:
        for step in STEP.values():
            reachable.add(position + step)

    new_possible_positions = reachable.intersection(clear_positions)
    return new_possible_positions


def show(possible_positions, blizzards, valley, width, height):
    symbols = {}
    for x in range(width):
        for y in range(height):
            position = Position(x, y)
            if position in valley:
                symbols[position] = "."
            else:
                symbols[position] = "#"

    REPRESENTATION = {v: k for k, v in STEP.items()}
    for blizzard in blizzards:
        if symbols[blizzard.position] == ".":
            symbols[blizzard.position] = REPRESENTATION[blizzard.direction]
        else:
            try:
                count = int(symbols[blizzard.position])
                symbols[blizzard.position] = str(count + 1)
            except ValueError:
                symbols[blizzard.position] = "2"

    for y in range(height):
        for x in range(0, width):
            pos = Position(x, y)
            if pos in possible_positions:
                print("E", end="")
            else:
                print(symbols[pos], end="")
        print()


def solve(lines):
    blizzards, valley, width, height = get_blizzards(lines)

    possible_positions = {Position(1, 0)}

    i = 0
    while True:
        i += 1
        possible_positions = do_round(possible_positions, blizzards, valley)

        for pos in possible_positions:
            if pos.y == height - 1:
                return i


def main():
    lines = read_lines()
    solution = solve(lines)
    print(f"solution = {solution}")


if __name__ == "__main__":
    start = timeit.default_timer()

    main()

    stop = timeit.default_timer()
    print('Time: ', stop - start)


from dataclasses import dataclass
from itertools import cycle

NROF_DROPS = 2022
WIDTH = 7
ALL_ROCK_DRAWINGS = """####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
"""


@dataclass
class Position:
    x: int
    y: int

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __hash__(self):
        return hash((self.x, self.y))


def get_rock_shapes(all_rock_drawings):
    rock_drawings = all_rock_drawings.split("\n\n")
    return [get_rock_shape(rock_drawing.splitlines())
            for rock_drawing in rock_drawings]


def get_rock_shape(rock_drawing: list[str]) -> set[Position]:
    rock_shape = set()
    for h, line in enumerate(reversed(rock_drawing)):
        for w, char in enumerate(line):
            if char == "#":
                rock_shape.add(Position(w, h))
    return rock_shape


ROCK_SHAPES = get_rock_shapes(ALL_ROCK_DRAWINGS)


class Rock:
    def __init__(self, left_edge, bottom_edge, index):
        self.bottom_left = Position(left_edge, bottom_edge)
        self.rock_shape = ROCK_SHAPES[index % len(ROCK_SHAPES)]

    @property
    def width(self):
        return max([pos.x for pos in self.rock_shape]) + 1

    @property
    def rock_positions(self):
        return {self.bottom_left + pos for pos in self.rock_shape}

    def __repr__(self):
        return f"Rock({self.bottom_left = })"


PUSH = {
    ">": Position(1, 0),
    "<": Position(-1, 0),
    "v": Position(0, -1),
    "^": Position(0, 1),
}


def read_lines():
    with open("input.txt") as f:
        return f.read().splitlines()


def drop(rock: Rock, rock_covered: set[Position], tower_height: int, pushes):
    while True:
        push = next(pushes)
        old_bottom_left = rock.bottom_left
        rock.bottom_left += push

        if (
                left_wall_overlaps(rock)
                or right_wall_overlaps(rock)
                or other_rock_overlaps(rock, rock_covered)
        ):
            rock.bottom_left = old_bottom_left

        old_bottom_left = rock.bottom_left
        rock.bottom_left += PUSH["v"]
        if floor_overlaps(rock) or other_rock_overlaps(rock, rock_covered):
            rock.bottom_left = old_bottom_left
            for rock_position in rock.rock_positions:
                rock_covered.add(rock_position)
                tower_height = max(tower_height, rock_position.y+1)
            return tower_height


def left_wall_overlaps(rock):
    return rock.bottom_left.x < 0


def right_wall_overlaps(rock):
    right_edge = rock.bottom_left.x + rock.width - 1
    return right_edge >= WIDTH


def floor_overlaps(rock):
    return rock.bottom_left.y < 0


def other_rock_overlaps(rock, filled):
    for position in rock.rock_positions:
        if position in filled:
            return True
    return False


def solve(lines):
    pushes = cycle([PUSH[c] for c in lines[0]])
    tower_height = 0
    rock_covered: set[Position] = set()

    for i in range(NROF_DROPS):
        rock = Rock(left_edge=2, bottom_edge=tower_height+3, index=i)
        tower_height = drop(rock, rock_covered, tower_height, pushes)

    return tower_height


def show_filled(filled, highest_filled):
    for y in range(highest_filled, -1, -1):
        for x in range(WIDTH):
            if Position(x, y) in filled:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()


def main():
    lines = read_lines()
    solution = solve(lines)
    print(f"{solution = }")


if __name__ == "__main__":
    main()

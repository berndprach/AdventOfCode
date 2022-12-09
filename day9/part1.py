
def read_lines():
    with open("input.txt") as f:
        return f.read().splitlines()


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x,
                      self.y - other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    @property
    def max_norm(self):
        return max(abs(self.x), abs(self.y))

    @property
    def l2_norm_squared(self):
        return self.x**2 + self.y**2


DIRECTIONS = {
    "R": Vector(1, 0),
    "L": Vector(-1, 0),
    "U": Vector(0, 1),
    "D": Vector(0, -1),
}


def get_head_moves(lines):
    moves: list[Vector] = []
    for line in lines:  # E.g. "R 4"
        direction, amount_str = line.split(" ")
        move: Vector = DIRECTIONS[direction]
        for _ in range(int(amount_str)):
            moves.append(move)
    return moves


POSSIBLE_TAIL_STEPS = [Vector(x, y)
                       for x in [-1, 0, 1]
                       for y in [-1, 0, 1]
                       if (x, y) != (0, 0)]


def chase(head: Vector, tail: Vector):
    """
    . . . . .
    . . . . .
    . . T . .
    . . . . .
    . . . . .
    """
    difference = head - tail
    if difference.max_norm <= 1:
        return tail
    best_step = get_best_step(goal_position=difference)
    return tail + best_step


def get_best_step(goal_position: Vector) -> Vector:
    best_step = Vector(0, 0)
    best_l2_norm_sq = 100
    for step in POSSIBLE_TAIL_STEPS:
        l2_norm_sq = (goal_position - step).l2_norm_squared
        if l2_norm_sq < best_l2_norm_sq:
            best_step = step
            best_l2_norm_sq = l2_norm_sq
    return best_step


def solve(lines):
    head_position = Vector(0, 0)
    tail_position = Vector(0, 0)
    tail_positions: set[Vector] = {tail_position}
    head_moves = get_head_moves(lines)
    for head_move in head_moves:
        head_position += head_move
        tail_position = chase(head_position, tail_position)
        tail_positions.add(tail_position)

    return len(tail_positions)


def main():
    lines = read_lines()
    solution = solve(lines)
    print(f"{solution = }")


if __name__ == "__main__":
    main()


from part1 import Vector, read_lines, get_head_moves, chase


def solve(lines):
    rope = [Vector(0, 0) for _ in range(10)]
    tail_positions: set[Vector] = {rope[9]}
    head_moves = get_head_moves(lines)
    for head_move in head_moves:
        rope[0] += head_move
        for i in range(1, 10):
            rope[i] = chase(rope[i-1], rope[i])
        tail_positions.add(rope[9])

    return len(tail_positions)


def main():
    lines = read_lines()
    solution = solve(lines)
    print(f"{solution = }")


if __name__ == "__main__":
    main()

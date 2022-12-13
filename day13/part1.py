
import ast
from enum import Enum


def read_lines():
    with open("input.txt") as f:
        return f.read().splitlines()


class First(Enum):
    LARGER = "larger"
    SAME = "same"
    SMALLER = "smaller"


def compare_integers(a: int, b: int) -> First:
    if a > b:
        return First.LARGER
    elif a == b:
        return First.SAME
    else:
        return First.SMALLER


def compare_lists(a: list[any], b: list[any]) -> First:
    for ai, bi in zip(a, b):
        relation = compare(ai, bi)
        if relation == First.SAME:
            continue
        return relation

    if len(a) > len(b):
        return First.LARGER
    elif len(a) == len(b):
        return First.SAME
    else:
        return First.SMALLER


def compare(a: any, b: any) -> First:
    if isinstance(a, int) and isinstance(b, int):
        return compare_integers(a, b)

    if isinstance(a, int):
        a = [a]
    if isinstance(b, int):
        b = [b]

    return compare_lists(a, b)


def solve(lines):
    index = 1
    solution = 0
    while 3*index-3 < len(lines):
        packet1 = ast.literal_eval(lines[3*index-3])
        packet2 = ast.literal_eval(lines[3*index-2])
        relation = compare(packet1, packet2)
        if relation == First.SMALLER:
            solution += index
        index += 1

    return solution


def main():
    lines = read_lines()
    solution = solve(lines)
    print(f"{solution = }")


if __name__ == "__main__":
    main()

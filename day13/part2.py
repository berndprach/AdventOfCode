
import ast
from part1 import read_lines, First, compare

from functools import cmp_to_key


def solve(lines):
    packets = [ast.literal_eval(line) for line in lines if line != ""]
    packets.append([[2]])
    packets.append([[6]])

    indices = [i for i in range(len(packets))]
    divider_indices = {len(packets) - 2, len(packets) - 1}

    def compare_indices(i: int, j: int) -> int:
        return -1 if compare(packets[i], packets[j]) == First.SMALLER else 1

    indices.sort(key=cmp_to_key(compare_indices))

    solution = 1
    for order, index in enumerate(indices):
        if index in divider_indices:
            solution *= (order + 1)

    return solution


def main():
    lines = read_lines()
    solution = solve(lines)
    print(f"{solution = }")


if __name__ == "__main__":
    main()


import timeit

from typing import Callable


def read_lines():
    with open("input.txt") as f:
        return f.read().splitlines()


def get_operations(lines):
    operations: dict[str, str] = {}
    for line in lines:
        name, operation = line.split(": ")
        operations[name] = operation
    return operations


def division(a, b):
    assert b != 0
    assert a % b == 0
    return a // b


OPERATION: dict[str, Callable] = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": division,
}


def set_value(monkey: str, monkey_values: dict[str, int], operations):
    if monkey in monkey_values.keys():
        return

    operation_str = operations[monkey]
    try:
        monkey_values[monkey] = int(operation_str)
        return
    except ValueError:
        pass

    m1, op_name, m2 = operation_str.split(" ")
    op = OPERATION[op_name]
    set_value(m1, monkey_values, operations)
    set_value(m2, monkey_values, operations)
    monkey_values[monkey] = op(monkey_values[m1], monkey_values[m2])


def solve(lines):
    operations = get_operations(lines)
    monkey_values = {}
    set_value("root", monkey_values, operations)
    return monkey_values["root"]


def main():
    lines = read_lines()
    solution = solve(lines)
    print(f"{solution = }")


if __name__ == "__main__":
    start = timeit.default_timer()

    main()

    stop = timeit.default_timer()
    print('Time: ', stop - start)

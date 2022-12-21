import timeit

from typing import Callable, Union

from part1 import read_lines, get_operations, OPERATION

MY_NAME = "humn"


def set_value(monkey: str,
              monkey_values: dict[str, Union[int, str]],
              operations):
    if monkey in monkey_values.keys():
        return

    if monkey == MY_NAME:
        monkey_values[monkey] = "x"
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

    if (
            isinstance(monkey_values[m1], int)
            and isinstance(monkey_values[m2], int)
    ):
        monkey_values[monkey] = op(monkey_values[m1], monkey_values[m2])
        return

    op_str = f"({monkey_values[m1]} {op_name} {monkey_values[m2]})"
    monkey_values[monkey] = op_str


def solve(lines):
    operations = get_operations(lines)
    root_op = operations["root"]
    m1, op_name, m2 = root_op.split(" ")
    operations["root"] = f"{m1} - {m2}"

    monkey_values = {}
    set_value("root", monkey_values, operations)
    root_equation = monkey_values["root"]
    print(f"\n{root_equation = }\n")

    return go_backwards("root", 0, monkey_values, operations)


def division(a, b):
    assert b != 0
    assert a % b == 0
    return a // b


GET_LEFT_GOAL: dict[str, Callable] = {
    "+": lambda r, s: s - r,  # x + r = s  =>  x = s - r
    "-": lambda r, s: s + r,  # x - r = s  =>  x = s + r
    "*": lambda r, s: division(s, r),  # x * r = s  =>  x = s / r
    "/": lambda r, s: s * r,  # x / r = s  =>  x = s * r
}

GET_RIGHT_GOAL: dict[str, Callable] = {
    "+": lambda l, s: s - l,  # l + x = s  =>  x = s - l
    "-": lambda l, s: l - s,  # l - x = s  =>  x = l - s
    "*": lambda l, s: division(s, l),  # l * x = s  =>  x = s / l
    "/": lambda l, s: division(l, s),  # l / x = s  =>  x = l / s
}


def go_backwards(monkey: str,
                 goal_value: int,
                 monkey_values: dict[str, Union[int, str]],
                 operations):

    if monkey == MY_NAME:
        print(f"Solved! Shouting {goal_value}.\n")
        return goal_value

    operation_str = operations[monkey]
    m1, op_name, m2 = operation_str.split(" ")
    m1_value, m2_value = monkey_values[m1], monkey_values[m2]

    if isinstance(m1_value, str):  # E.g. (...) - m2_value = goal_value
        get_left_goal = GET_LEFT_GOAL[op_name]
        new_goal = get_left_goal(r=m2_value, s=goal_value)
        return go_backwards(m1, new_goal, monkey_values, operations)

    if isinstance(m2_value, str):  # E.g. m1_value / (...) = goal_value
        get_right_goal = GET_RIGHT_GOAL[op_name]
        new_goal = get_right_goal(l=m1_value, s=goal_value)
        return go_backwards(m2, new_goal, monkey_values, operations)

    raise ValueError(f"Both {m1} and {m2} are integers")


def main():
    lines = read_lines()
    solution = solve(lines)
    print(f"{solution = }")


if __name__ == "__main__":
    start = timeit.default_timer()

    main()

    stop = timeit.default_timer()
    print('Time: ', stop - start)

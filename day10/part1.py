
def read_lines():
    with open("input.txt") as f:
        return f.read().splitlines()


def get_register_values(instructions):
    register_values = [1]
    for instruction in instructions:
        current_value = register_values[-1]
        if instruction == "noop":
            value_after = current_value
            register_values.append(value_after)
        else:  # E.g. "addx 15"
            addition_value = int(instruction.split()[1])
            value_after = current_value + addition_value
            register_values.append(current_value)
            register_values.append(value_after)
    return register_values[:-1]


def solve(lines):
    register_values = get_register_values(lines)
    cycle_number = 20
    solution = 0
    while cycle_number < len(register_values):
        register_value = register_values[cycle_number-1]
        signal_strength = cycle_number * register_value
        solution += signal_strength
        cycle_number += 40
    return solution


def main():
    lines = read_lines()
    solution = solve(lines)
    print(f"{solution = }")


if __name__ == "__main__":
    main()

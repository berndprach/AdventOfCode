import re
from dataclasses import dataclass
from typing import Callable


def read_lines():
    with open("input.txt") as f:
        return f.read().splitlines()


def all_integers_in(line: str):
    return [int(x_str) for x_str in re.findall(r"\d+", line)]


def first_integer_in(line: str):
    integers = all_integers_in(line)
    if len(integers) == 0:
        raise ValueError(f"No integer in {line}")
    return integers[0]


@dataclass
class Monkey:
    monkey_id: int
    current_items: list[int]
    update_worry_score: Callable[[int], int]
    get_throw_to_id: Callable[[int], int]
    all_monkeys: list["Monkey"]

    nrof_inspections: int = 0

    def throw_first_item(self):
        worry_score = self.current_items.pop(0)
        new_score = self.update_worry_score(worry_score)
        new_monkey_id = self.get_throw_to_id(new_score)
        self.all_monkeys[new_monkey_id].recieve(new_score)
        self.nrof_inspections += 1
        # print(f"Monkey {self.monkey_id} threw {worry_score} "
        #       f"to monkey {new_monkey_id} and got {new_score}")

    def throw_all_items(self):
        while len(self.current_items) > 0:
            self.throw_first_item()

    def recieve(self, item: int):
        self.current_items.append(item)


def parse_monkey(lines: list[str], all_monkeys: list[Monkey]):
    """
    Monkey 0:
      Starting items: 79, 98
      Operation: new = old * 19
      Test: divisible by 23
        If true: throw to monkey 2
        If false: throw to monkey 3
    """
    lines_iter = iter(lines)

    line = next(lines_iter)
    monkey_id = first_integer_in(line)

    line = next(lines_iter)
    starting_items = all_integers_in(line)

    line = next(lines_iter)
    operation_str = line.replace("  Operation: ", "")
    operation = parse_operation(operation_str)

    def update_worry_score(worry_score: int):
        return operation(worry_score) // 3

    get_throw_to_id = parse_get_throw_to_id(next(lines_iter),
                                            next(lines_iter),
                                            next(lines_iter))

    monkey = Monkey(monkey_id, starting_items, update_worry_score,
                    get_throw_to_id, all_monkeys)
    return monkey


def parse_operation(operation_str: str):
    if operation_str == "new = old * old":
        return lambda x: x * x
    elif operation_str.startswith("new = old + "):
        addend = first_integer_in(operation_str)
        return lambda x: x + addend
    elif operation_str.startswith("new = old * "):
        factor = first_integer_in(operation_str)
        return lambda x: x * factor
    else:
        raise ValueError(f"Unknown operation: {operation_str}")


def parse_get_throw_to_id(line1, line2, line3):
    if not line1.startswith("  Test: divisible by "):
        raise ValueError(f"Unknown Condition: {line1}")
    if not line2.startswith("    If true: throw to monkey "):
        raise ValueError(f"Unknown True Action: {line2}")
    if not line3.startswith("    If false: throw to monkey "):
        raise ValueError(f"Unknown False Action: {line3}")

    test_divisor = first_integer_in(line1)
    true_monkey_id = first_integer_in(line2)
    false_monkey_id = first_integer_in(line3)

    return TestModulo(test_divisor, true_monkey_id, false_monkey_id)


@dataclass
class TestModulo:
    test_modulo: int
    true_value: int
    false_value: int

    def __call__(self, worry_score: int):
        if worry_score % self.test_modulo == 0:
            return self.true_value
        else:
            return self.false_value


def parse_lines(lines: list[str]):
    next_monkey_start_line = 0
    all_monkeys = []
    while next_monkey_start_line < len(lines):
        monkey_lines = lines[next_monkey_start_line:next_monkey_start_line + 6]
        monkey = parse_monkey(monkey_lines, all_monkeys)
        all_monkeys.append(monkey)
        next_monkey_start_line += 7
    return all_monkeys


def do_round(all_monkeys: list[Monkey]):
    for monkey in all_monkeys:
        monkey.throw_all_items()


def solve(lines):
    all_monkeys = parse_lines(lines)
    for i in range(20):
        do_round(all_monkeys)

    inspection_counts = [monkey.nrof_inspections for monkey in all_monkeys]
    # print(f"{inspection_counts = }")
    inspection_counts.sort(reverse=True)
    return inspection_counts[0] * inspection_counts[1]


def main():
    lines = read_lines()
    solution = solve(lines)
    print(f"{solution = }")


if __name__ == "__main__":
    main()

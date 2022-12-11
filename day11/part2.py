
from part1 import read_lines, first_integer_in, all_integers_in, \
    Monkey, parse_operation, parse_get_throw_to_id, do_round


NROF_ROUNDS = 10_000


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

    # def update_worry_score(worry_score: int):
    #     return operation(worry_score) // 3
    update_worry_score = operation

    get_throw_to_id = parse_get_throw_to_id(next(lines_iter),
                                            next(lines_iter),
                                            next(lines_iter))

    monkey = Monkey(monkey_id, starting_items, update_worry_score,
                    get_throw_to_id, all_monkeys)
    return monkey


def parse_lines(lines: list[str]):
    next_monkey_start_line = 0
    all_monkeys = []
    while next_monkey_start_line < len(lines):
        monkey_lines = lines[next_monkey_start_line:next_monkey_start_line + 6]
        monkey = parse_monkey(monkey_lines, all_monkeys)
        all_monkeys.append(monkey)
        next_monkey_start_line += 7
    return all_monkeys


def solve(lines):
    all_monkeys = parse_lines(lines)

    test_modulos = [monkey.get_throw_to_id.test_modulo
                    for monkey in all_monkeys]
    modulo_product = 1
    for tm in test_modulos:
        modulo_product *= tm

    for i in range(NROF_ROUNDS):
        do_round(all_monkeys)

        for monkey in all_monkeys:
            monkey.current_items = [worry_score % modulo_product
                                    for worry_score in monkey.current_items]

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

from dataclasses import dataclass
import re


def read_lines():
    with open("input.txt") as f:
        return f.read().splitlines()


def find_empty_line_index(lines):
    for i, line in enumerate(lines):
        if line == "":
            return i


def process_lines(lines):
    empty_line_index = find_empty_line_index(lines)
    starting_stacks_lines = lines[empty_line_index - 1::-1]
    starting_stacks = process_starting_stacks_lines(starting_stacks_lines)

    move_lines = lines[empty_line_index + 1:]
    move_instructions = process_move_lines(move_lines)

    return starting_stacks, move_instructions


def process_starting_stacks_lines(starting_stack_lines):
    """
     1   2   3
    [Z] [M] [P]
    [N] [C]
        [D]
    """
    index_line = starting_stack_lines[0]
    column: dict[int, int] = {}
    for i, letter in enumerate(index_line):
        if letter == " ":
            continue
        column[int(letter)] = i

    stacks: dict[int, list[str]] = {i: [] for i in column.keys()}
    for line in starting_stack_lines[1:]:
        for stack_nr, column_nr in column.items():
            item = line[column_nr]
            if item != " ":
                stacks[stack_nr].append(item)

    return stacks


@dataclass
class MoveInstruction:
    amount: int
    from_stack_nr: int
    to_stack_nr: int


def process_move_lines(move_lines):
    move_instructions = []
    for line in move_lines:
        integer_in_line = [int(i_str) for i_str in re.findall(r"\d+", line)]
        amount, from_stack_nr, to_stack_nr = integer_in_line
        move_instruction = MoveInstruction(amount, from_stack_nr, to_stack_nr)
        move_instructions.append(move_instruction)
    return move_instructions


def move_item(stacks, mi: MoveInstruction):
    from_stack = stacks[mi.from_stack_nr]
    to_stack = stacks[mi.to_stack_nr]
    for _ in range(mi.amount):
        to_stack.append(from_stack.pop())


def move_items(stacks, move_instructions: list[MoveInstruction]):
    for move_instruction in move_instructions:
        move_item(stacks, move_instruction)


def solve(lines):
    stacks, moves = process_lines(lines)
    move_items(stacks, moves)
    return "".join(stack[-1] for stack in stacks.values())


def main():
    lines = read_lines()
    solution = solve(lines)
    print(f"{solution = }")


if __name__ == "__main__":
    main()

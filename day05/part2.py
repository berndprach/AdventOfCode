
from part1 import MoveInstruction, read_lines, process_lines


def move_item(stacks, mi: MoveInstruction):
    from_stack = stacks[mi.from_stack_nr]
    to_stack = stacks[mi.to_stack_nr]

    to_stack.extend(from_stack[-mi.amount:])
    for _ in range(mi.amount):
        from_stack.pop()


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

import timeit

from part1 import get_elf_positions, do_round, read_lines


def solve(lines):
    elf_positions = get_elf_positions(lines)

    i = 0
    while True:
        print(f"{i = }")
        new_elf_position = do_round(elf_positions, first_considered=i % 4)
        if new_elf_position == elf_positions:
            break
        i += 1
        elf_positions = new_elf_position

    return i+1


def main():
    lines = read_lines()
    solution = solve(lines)
    print(f"{solution = }")


if __name__ == "__main__":
    start = timeit.default_timer()

    main()

    stop = timeit.default_timer()
    print('Time: ', stop - start)  # 51.4s

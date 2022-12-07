
from part1 import read_input, create_file_system


AVAILABLE_SPACE = 70000000 - 30000000


def solve(lines):
    root, all_dirs = create_file_system(lines)
    need_to_free = root.get_size() - AVAILABLE_SPACE
    best_so_far = root.get_size()
    for directory in all_dirs:
        if directory.get_size() < need_to_free:
            continue
        if directory.get_size() < best_so_far:
            best_so_far = directory.get_size()
    return best_so_far


def main():
    line = read_input()
    solution = solve(line)
    print(f"{solution = }")


if __name__ == "__main__":
    main()

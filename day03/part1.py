

def read_input():
    with open("input.txt") as f:
        return f.read().splitlines()


def priority(letter: str) -> int:
    if letter.isupper():
        return ord(letter) - ord("A") + 27
    else:
        return ord(letter) - ord("a") + 1


def split_line(line: str) -> tuple[str, str]:
    return line[:len(line) // 2], line[len(line) // 2:]


def priority_of_line(line: str) -> int:
    l1, l2 = split_line(line)
    common = set(l1).intersection(set(l2))
    return priority(common.pop())


def get_total_priority(lines: list[str]) -> int:
    return sum(priority_of_line(line) for line in lines)


def main():
    lines = read_input()
    total_priority = get_total_priority(lines)
    print(f"{total_priority = }")


if __name__ == "__main__":
    main()

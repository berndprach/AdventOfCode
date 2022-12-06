
from part1 import read_input, priority


def common_item(line1: str, line2: str, line3: str) -> str:
    commons12 = set(line1).intersection(set(line2))
    common123 = commons12.intersection(set(line3))
    return common123.pop()


def get_total_priority(lines: list[str]) -> int:
    total_priority = 0
    for i in range(len(lines)//3):
        badge = common_item(lines[3*i], lines[3*i+1], lines[3*i+2])
        total_priority += priority(badge)
    return total_priority


def main():
    lines = read_input()
    sum_of_priorities = get_total_priority(lines)
    print(f"{sum_of_priorities = }")


if __name__ == "__main__":
    main()

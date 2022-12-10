
def read_input():
    with open("input.txt") as f:
        return f.read().splitlines()


def get_most_calories(lines):
    most_so_far = 0
    current = 0
    for line in lines:
        if line == "":
            most_so_far = max(most_so_far, current)
            current = 0
            continue
        current += int(line)
    most_so_far = max(most_so_far, current)
    return most_so_far


def main():
    lines = read_input()
    most_calories = get_most_calories(lines)
    print(f"{most_calories = }")


if __name__ == "__main__":
    main()

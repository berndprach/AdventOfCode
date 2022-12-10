
def read_input():
    with open("input.txt") as f:
        return f.read().splitlines()


def get_most_calories_3elves(lines):
    best_three_sorted = [0, 0, 0]
    current = 0
    for line in lines:
        if line == "":
            best_three_sorted = new_best_three_sorted(best_three_sorted,
                                                      current)
            current = 0
            continue
        current += int(line)
    best_three_sorted = new_best_three_sorted(best_three_sorted,
                                              current)
    return sum(best_three_sorted)


def new_best_three_sorted(best_three_sorted, current):
    if current > best_three_sorted[0]:
        best_three_sorted[0] = current
        best_three_sorted.sort()
    return best_three_sorted


def main():
    lines = read_input()
    most_3elves = get_most_calories_3elves(lines)
    print(f"{most_3elves = }")


if __name__ == "__main__":
    main()

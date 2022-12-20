
import timeit

from part1 import read_lines, move_all

DECRIPTION_KEY = 811589153


def solve(lines):
    numbers = [int(line) for line in lines]
    numbers = [v * DECRIPTION_KEY for v in numbers]

    next_element = {i: (i+1) % len(numbers) for i in range(len(numbers))}
    previos_element = {v: k for k, v in next_element.items()}

    for i in range(10):
        move_all(numbers, next_element, previos_element)

    solution = 0
    indices = [1000, 2000, 3000]

    current_element = 0
    while numbers[current_element] != 0:
        current_element = next_element[current_element]

    for i in range(1, 3001):
        current_element = next_element[current_element]
        if i in indices:
            print(f"{i}: {current_element} ({numbers[current_element]})")
            solution += numbers[current_element]

    return solution


def main():
    lines = read_lines()
    solution = solve(lines)
    print(f"{solution = }")


if __name__ == "__main__":
    start = timeit.default_timer()

    main()

    stop = timeit.default_timer()
    print('Time: ', stop - start)

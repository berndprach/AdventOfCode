
import timeit


def read_lines():
    with open("input.txt") as f:
        return f.read().splitlines()


def move_element(i, numbers, next_element, previos_element):

    move_for = numbers[i] % (len(numbers)-1)

    if move_for == 0:
        return

    assert move_for > 0

    old_previous = previos_element[i]
    old_next = next_element[i]

    new_next = old_next
    for _ in range(move_for):
        new_next = next_element[new_next]
    new_previous = previos_element[new_next]

    next_element[old_previous] = old_next
    previos_element[old_next] = old_previous

    next_element[new_previous] = i
    previos_element[i] = new_previous
    next_element[i] = new_next
    previos_element[new_next] = i


def move_all(numbers, next_element, previos_element):
    for element_index in range(len(numbers)):
        move_element(element_index, numbers, next_element, previos_element)


def solve(lines):
    numbers = [int(line) for line in lines]

    next_element = {i: (i+1) % len(numbers) for i in range(len(numbers))}
    previos_element = {v: k for k, v in next_element.items()}

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

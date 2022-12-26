
import timeit


def read_lines():
    with open("input.txt") as f:
        return f.read().splitlines()


VALUE = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2,
}


def to_integer(snafu_number):
    int_number = 0
    for digit in snafu_number:  # E.g. "1=-0-2"
        int_number = int_number * 5 + VALUE[digit]
    return int_number


def to_snafu(int_number):
    snafu_digit = {v % 5: k for k, v in VALUE.items()}
    snafu_number = ""
    while int_number != 0:
        remainder = int_number % 5
        digit = snafu_digit[remainder]
        snafu_number = digit + snafu_number
        value = VALUE[digit]
        int_number = (int_number - value) // 5

    return snafu_number


def solve(lines):
    int_sum = 0
    for line in lines:
        int_number = to_integer(line)
        int_sum += int_number
    snafu_sum = to_snafu(int_sum)
    return snafu_sum


def main():
    lines = read_lines()
    solution = solve(lines)
    print(f"solution = {solution}")


if __name__ == "__main__":
    start = timeit.default_timer()

    main()

    stop = timeit.default_timer()
    print('Time: ', stop - start)

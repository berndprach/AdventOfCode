
from part1 import read_input

MARKER_LENGTH = 14


def find_start_of_packet(line):
    i = MARKER_LENGTH
    last_letters = line[:MARKER_LENGTH]
    while len(set(last_letters)) < MARKER_LENGTH:
        i += 1
        last_letters = line[i-MARKER_LENGTH:i]
    return i


def main():
    line = read_input()
    solution = find_start_of_packet(line)
    print(f"{solution = }")


if __name__ == "__main__":
    main()

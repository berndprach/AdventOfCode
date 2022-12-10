

def read_input():
    with open("input.txt") as f:
        return f.read()


def find_start_of_packet(line):
    i = 4
    last_four = line[0:4]
    while len(set(last_four)) < 4:
        i += 1
        last_four = line[i-4:i]
    return i


def main():
    line = read_input()
    solution = find_start_of_packet(line)
    print(f"{solution = }")


if __name__ == "__main__":
    main()

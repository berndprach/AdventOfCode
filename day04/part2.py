

def read_input():
    with open("input.txt") as f:
        return f.read().splitlines()


class Section:
    def __init__(self, start: int, end: int):
        self.start: int = start
        self.end: int = end

    def overlaps(self, other):
        # return self.start <= other.end and self.end >= other.start
        is_before = self.end < other.start
        is_after = self.start > other.end
        disjoint = is_before or is_after
        return not disjoint


def section_from_string(section_string: str) -> Section:
    return Section(*(int(s) for s in section_string.split("-")))


def parse_line(line) -> list[Section]:
    return [section_from_string(section_string)
            for section_string in line.split(",")]


def solve(lines):
    nrof_containments = 0
    for line in lines:
        section1, section2 = parse_line(line)
        if section1.overlaps(section2):
            nrof_containments += 1
    print(f"{nrof_containments = }")
    return nrof_containments


def main():
    lines = read_input()
    solve(lines)


if __name__ == "__main__":
    main()

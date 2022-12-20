

def read_lines():
    with open("input.txt") as f:
        return f.read().splitlines()


def get_cubes(lines):
    cubes = set()
    for line in lines:  # E.g. "2,2,2"
        pos = tuple(int(i) for i in line.split(","))
        cubes.add(pos)
    return cubes


def get_neighbours(position):
    # directions: [[1, 0 0], ...]
    directions = [[1 if i == j else 0 for i in range(3)] for j in range(3)]
    neighbours = []
    for direction in directions:
        neighbours.append(tuple(p + d for p, d in zip(position, direction)))
        neighbours.append(tuple(p - d for p, d in zip(position, direction)))
    return neighbours


def solve(lines):
    cubes = get_cubes(lines)
    surface_area = 0
    for cube in cubes:
        for neighbour in get_neighbours(cube):
            if neighbour not in cubes:
                surface_area += 1
    return surface_area


def main():
    lines = read_lines()
    solution = solve(lines)
    print(f"{solution = }")


if __name__ == "__main__":
    main()

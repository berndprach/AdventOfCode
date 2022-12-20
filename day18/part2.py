
from part1 import read_lines, get_cubes, get_neighbours


def get_outside(cubes):
    """
    . . . . . . .
    . . . . # . .
    . . # # # # .
    . # # . . # .
    . # # . # # .
    . . # # # # .
    . . . . # # .
    . . . . . . .
    """

    max_coordinates = [max([cube_position[i] for cube_position in cubes])
                       for i in range(3)]
    min_coordinates = [min([cube_position[i] for cube_position in cubes])
                       for i in range(3)]

    starting_point = tuple(min_coordinates[i] - 1 for i in range(3))
    outside = set()
    queue = [starting_point]

    while len(queue) > 0:
        pos = queue.pop(0)

        if (
                pos in cubes
                or pos in outside
                or any(pos[i] < min_coordinates[i]-1 for i in range(3))
                or any(pos[i] > max_coordinates[i]+1 for i in range(3))
        ):
            continue

        outside.add(pos)
        for neighbour in get_neighbours(pos):
            queue.append(neighbour)

    return outside


def solve(lines):
    cubes = get_cubes(lines)
    outside = get_outside(cubes)

    exterior_surface_area = 0
    for cube in cubes:
        for neighbour in get_neighbours(cube):
            if neighbour in outside:
                exterior_surface_area += 1
    return exterior_surface_area


def main():
    lines = read_lines()
    solution = solve(lines)
    print(f"{solution = }")


if __name__ == "__main__":
    main()

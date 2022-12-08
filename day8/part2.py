
from part1 import read_lines, get_grid, GridIterator


def solve(lines):
    grid = get_grid(lines)
    width, height = len(lines[0]), len(lines)
    grid_iterator = GridIterator(width=width, height=height)

    trees_seen_left = get_trees_seen(
        grid,
        grid_iterator=grid_iterator.rows_from_left()
    )
    trees_seen_right = get_trees_seen(
        grid,
        grid_iterator=grid_iterator.rows_from_right()
    )
    trees_seen_up = get_trees_seen(
        grid,
        grid_iterator=grid_iterator.columns_from_top()
    )
    trees_seen_down = get_trees_seen(
        grid,
        grid_iterator=grid_iterator.columns_from_bottom()
    )

    best_scenic_score = 0
    for position in grid.keys():
        scenic_score = (trees_seen_left[position]
                        * trees_seen_right[position]
                        * trees_seen_up[position]
                        * trees_seen_down[position])
        if scenic_score > best_scenic_score:
            best_scenic_score = scenic_score

    return best_scenic_score


def get_trees_seen(grid, grid_iterator):
    """
    30373
    25512
    65332
    33549
    35390
    """
    trees_seen: dict[tuple[int, int], int] = {}

    for line in grid_iterator:
        trees_seen_per_height = {next_height: 0 for next_height in range(10)}
        for position in line:
            height = grid[position]
            trees_seen[position] = trees_seen_per_height[height]
            update_trees_seen_per_height(trees_seen_per_height, height)
    return trees_seen


def update_trees_seen_per_height(trees_seen_per_height, height):
    for next_height in range(10):
        if next_height <= height:
            trees_seen_per_height[next_height] = 1
        else:
            trees_seen_per_height[next_height] += 1


def main():
    lines = read_lines()
    solution = solve(lines)
    print(f"{solution = }")


if __name__ == "__main__":
    main()

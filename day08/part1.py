
def read_lines():
    with open("input.txt") as f:
        return f.read().splitlines()


def get_grid(lines):
    grid: dict[tuple[int, int], int] = {}
    for h, line in enumerate(lines):
        for w, tree_height_str in enumerate(line):
            grid[(h, w)] = int(tree_height_str)
    return grid


class GridIterator:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def row_from_left(self, row_number):
        return [(row_number, col_number)
                for col_number in range(self.width)]

    def row_from_right(self, row_number):
        return [(row_number, col_number)
                for col_number in range(self.width - 1, -1, -1)]

    def column_from_top(self, col_number):
        return [(row_number, col_number)
                for row_number in range(self.height)]

    def column_from_bottom(self, col_number):
        return [(row_number, col_number)
                for row_number in range(self.height - 1, -1, -1)]

    def rows_from_left(self):
        return [self.row_from_left(row_number)
                for row_number in range(self.height)]

    def rows_from_right(self):
        return [self.row_from_right(row_number)
                for row_number in range(self.height)]

    def columns_from_top(self):
        return [self.column_from_top(col_number)
                for col_number in range(self.width)]

    def columns_from_bottom(self):
        return [self.column_from_bottom(col_number)
                for col_number in range(self.width)]


def solve(lines):
    grid = get_grid(lines)
    width, height = len(lines[0]), len(lines)
    grid_iterator = GridIterator(width=width, height=height)
    is_visible = {position: False for position in grid.keys()}

    for row in grid_iterator.rows_from_left():
        update_visible(grid, is_visible, row)

    for row in grid_iterator.rows_from_right():
        update_visible(grid, is_visible, row)

    for column in grid_iterator.columns_from_top():
        update_visible(grid, is_visible, column)

    for column in grid_iterator.columns_from_bottom():
        update_visible(grid, is_visible, column)

    # for i in range(height):
    #     for j in range(width):
    #         print(is_visible[(i, j)], end=" ")
    #     print()
    return sum(is_visible.values())


def update_visible(grid, is_visible, line):
    highest_so_far = -1
    for position in line:
        if grid[position] > highest_so_far:
            is_visible[position] = True
            highest_so_far = grid[position]


def main():
    lines = read_lines()
    solution = solve(lines)
    print(f"{solution = }")


if __name__ == "__main__":
    main()

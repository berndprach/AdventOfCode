
from part1 import read_lines, get_register_values

DISPLAY_HEIGHT = 6
DISPLAY_WIDTH = 40


def get_pixels(register_values):
    pixels = []
    crt_column = 0
    for sprite_position in register_values:
        sprite_pixels = {sprite_position + i for i in {-1, 0, 1}}
        if crt_column in sprite_pixels:
            pixels.append("#")
        else:
            pixels.append(".")
        crt_column = 0 if (crt_column == DISPLAY_WIDTH-1) else crt_column + 1
    return "".join(pixels)


def solve(lines):
    register_values = get_register_values(lines)
    pixels = get_pixels(register_values)
    for line_number in range(DISPLAY_HEIGHT):
        start_index = line_number * DISPLAY_WIDTH
        print(pixels[start_index:start_index+DISPLAY_WIDTH])


def main():
    lines = read_lines()
    solve(lines)


if __name__ == "__main__":
    main()

import time
import timeit

from part1 import read_lines, ROCK_SHAPES, Rock, PUSH, Position, WIDTH, \
    left_wall_overlaps, right_wall_overlaps, \
    other_rock_overlaps, floor_overlaps

NROF_DROPS = 1_000_000_000_000


class PushIterator:
    def __init__(self, line):
        self.pushes = line
        self.push_id = 0
        self.rolled_over = False

    def __next__(self):
        push_repr = self.pushes[self.push_id]
        push = PUSH[push_repr]
        self.push_id += 1
        if self.push_id == len(self.pushes):
            self.push_id = 0
            self.rolled_over = True
        return push


class Room:
    def __init__(self):
        self.rock_covered: set[Position] = set()
        self.tower_height = 0
        self.lowest_relevant = 0

    def drop(self, rock, pushes):
        while True:
            push = next(pushes)
            old_bottom_left = rock.bottom_left
            rock.bottom_left += push
            if (
                    left_wall_overlaps(rock)
                    or right_wall_overlaps(rock)
                    or other_rock_overlaps(rock, self.rock_covered)
            ):
                rock.bottom_left = old_bottom_left

            old_bottom_left = rock.bottom_left
            rock.bottom_left += PUSH["v"]
            if (
                    floor_overlaps(rock)
                    or other_rock_overlaps(rock, self.rock_covered)
            ):
                rock.bottom_left = old_bottom_left
                for position in rock.rock_positions:
                    self.rock_covered.add(position)
                    self.tower_height = max(self.tower_height, position.y + 1)

                rocky_xs = set(position.x for position in self.rock_covered)
                if len(rocky_xs) == WIDTH:
                    self.remove_unreachable()

                return

    def remove_unreachable(self):
        """
        . . . . . . .
        . . . . . . .
        . . . X X X X
        . . . . X . .
        X X . . X # .
        . # X X # # #
        . . # # . # #
        . . . # . # #
        """
        above = Position(0, self.tower_height)
        queue = [above]
        keepers = {above}

        while len(queue) > 0:
            position = queue.pop()

            if position.x < 0 or position.x >= WIDTH:
                continue

            keepers.add(position)

            if position in self.rock_covered:
                continue

            if position.y > self.tower_height:
                continue

            # Enqueue all neighbours
            for push in PUSH.values():
                neighbour = position + push
                if neighbour not in keepers:
                    queue.append(neighbour)

        new_rock_covered = {position for position in keepers
                            if position in self.rock_covered}

        self.rock_covered = new_rock_covered
        self.lowest_relevant = min(
            position.y for position in self.rock_covered)


def solve(lines):
    pushes = PushIterator(lines[0])
    room = Room()

    saved_states = {}

    drop_nr = 0
    while drop_nr < NROF_DROPS:
        # print(f"{drop_nr = }")
        rock = Rock(left_edge=2,
                    bottom_edge=room.tower_height + 3,
                    index=drop_nr)
        room.drop(rock, pushes)
        drop_nr += 1

        if pushes.rolled_over:
            # Safe the current state:
            rock_covered_state = tuple(Position(p.x,
                                                p.y - room.lowest_relevant)
                                       for p in room.rock_covered)
            state = (drop_nr % len(ROCK_SHAPES),
                     pushes.push_id,
                     rock_covered_state)

            if state not in saved_states:
                saved_states[state] = (drop_nr, room.tower_height)
                pushes.rolled_over = False
                continue

            print(f"Found loop at drop {drop_nr}!")

            saved_drop_nr, saved_tower_height = saved_states[state]
            iteration_difference = drop_nr - saved_drop_nr
            height_difference = room.tower_height - saved_tower_height

            nrof_jumps = (NROF_DROPS - drop_nr) // iteration_difference

            drop_nr += nrof_jumps * iteration_difference
            room.tower_height += nrof_jumps * height_difference
            room.lowest_relevant += nrof_jumps * height_difference
            room.rock_covered = {Position(p.x,
                                          p.y + nrof_jumps * height_difference)
                                 for p in room.rock_covered}

            print(f"Fast forwarded from drop {saved_drop_nr} "
                  f"to drop {drop_nr}")
            time.sleep(1)

            pushes.rolled_over = False

    return room.tower_height


def main():
    lines = read_lines()
    solution = solve(lines)
    print(f"{solution = }")


if __name__ == "__main__":
    start = timeit.default_timer()

    main()

    stop = timeit.default_timer()
    print('Time: ', stop - start)

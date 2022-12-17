
import timeit

from queue import PriorityQueue
from dataclasses import dataclass

from part1 import read_lines, get_active_valves_data


# State: (time1, valve1, time2, valve2, is_open)
State = tuple[int, int, int, int, tuple[bool, ...]]
Valve = int


@dataclass
class Data:
    upper_bound: dict[State, int]
    ordered_next_moves: dict[State, PriorityQueue]
    neighbours: dict[Valve, dict[Valve, int]]
    flow_rate: dict[Valve, int]


def get_next_moves(state: State, data: Data):
    time1, valve1, time2, valve2, is_open = state
    assert time1 <= time2

    if time2 == 0:
        return []

    next_states = []
    for new_valve, distance in data.neighbours[valve2].items():
        if is_open[new_valve]:
            continue

        new_time = time2 - distance - 1
        if new_time <= 0:
            continue

        pressure_released = new_time * data.flow_rate[new_valve]

        new_is_open = list(is_open)
        new_is_open[new_valve] = True
        new_is_open = tuple(new_is_open)

        if new_time < time1:
            new_state = (new_time, new_valve, time1, valve1, new_is_open)
        else:
            new_state = (time1, valve1, new_time, new_valve, new_is_open)

        next_states.append((pressure_released, new_state))

    # Player 2 retiring:
    next_states.append((0, (0, 0, time1, valve1, is_open)))

    return next_states


def set_basic_upper_bound(state, data: Data):
    if state in data.upper_bound.keys():
        return

    upper_bound = 0
    time1, valve1, time2, valve2, is_open = state

    for to_valve, flow_rate in data.flow_rate.items():
        if is_open[to_valve]:
            continue

        remaining_time1 = time1 - data.neighbours[valve1][to_valve]
        remaining_time2 = time2 - data.neighbours[valve2][to_valve]
        better_remaining_time = max(remaining_time1, remaining_time2)

        if better_remaining_time > 1:
            upper_bound += (better_remaining_time - 1) * flow_rate

    data.upper_bound[state] = upper_bound


def recursively_improve_upper_bound(state, data: Data) -> bool:
    # returns whether some upper bound has been improved
    if state not in data.ordered_next_moves.keys():
        set_ordered_next_moves(state, data)

    if data.ordered_next_moves[state].empty():
        data.upper_bound[state] = 0
        return False

    _, next_move = data.ordered_next_moves[state].get()
    preasure_released, next_state = next_move
    has_changed = recursively_improve_upper_bound(
        next_state, data
    )

    state_upper_bound = preasure_released + data.upper_bound[next_state]
    data.ordered_next_moves[state].put((-state_upper_bound, next_move))

    priority, _ = data.ordered_next_moves[state].queue[0]
    new_upper_bound = -priority

    if new_upper_bound < data.upper_bound[state]:
        has_changed = True
        data.upper_bound[state] = new_upper_bound

    return has_changed


def set_ordered_next_moves(state, data: Data):
    if state in data.ordered_next_moves.keys():
        return

    data.ordered_next_moves[state] = PriorityQueue()
    for move in get_next_moves(state, data):
        preasure_released, new_state = move
        set_basic_upper_bound(new_state, data)
        state_upper_bound = preasure_released + data.upper_bound[new_state]
        data.ordered_next_moves[state].put((-state_upper_bound, move))


def solve(lines):
    active_distances, active_flow_rates = get_active_valves_data(lines)
    data = Data({}, {}, active_distances, active_flow_rates)

    # State: (time1, valve1, time2, valve2, is_open)
    initial_state = (26, 0, 26, 0, tuple(False for _ in active_distances))
    set_basic_upper_bound(initial_state, data)

    improvement_has_happened = True
    while improvement_has_happened:
        improvement_has_happened = recursively_improve_upper_bound(
            initial_state, data
        )
        print(data.upper_bound[initial_state])

    return data.upper_bound[initial_state]


def main():
    lines = read_lines()
    solution = solve(lines)
    print(f"{solution = }")


if __name__ == "__main__":
    start = timeit.default_timer()

    main()

    stop = timeit.default_timer()
    print('Time: ', stop - start)

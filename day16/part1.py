import re

from dataclasses import dataclass

TOTAL_TIME = 30


def read_lines():
    with open("input.txt") as f:
        return f.read().splitlines()


def parse_lines(lines):
    all_valves = set()
    active_valves = ["AA"]

    tunnels: dict[str, list[str]] = {}
    flow_rates: dict[str, int] = {}
    for line in lines:
        # E.g. "Valve AA has flow rate=0; tunnels lead to valves DD, II, BB"
        valve, *valve_tunnels = find_uppercase_letter_pairs(line)
        flow_rate = integers_in_line(line)[0]
        all_valves.add(valve)
        if flow_rate > 0 and valve != "AA":
            active_valves.append(valve)

        tunnels[valve] = valve_tunnels
        flow_rates[valve] = flow_rate

    return all_valves, active_valves, tunnels, flow_rates


def find_uppercase_letter_pairs(line):
    return re.findall(r"[A-Z]{2}", line)


def integers_in_line(line):
    return [int(i_str) for i_str in re.findall(r"-?\d+", line)]


def get_shortest_distances(valve, tunnels):
    distances = {valve: 0}
    queue = [valve]
    while queue:
        current_valve = queue.pop(0)
        for new_valve in tunnels[current_valve]:
            if new_valve in distances.keys():
                continue

            distances[new_valve] = distances[current_valve] + 1
            queue.append(new_valve)
    return distances


def get_all_shortes_distances(valves, tunnels):
    return {valve: get_shortest_distances(valve, tunnels)
            for valve in valves}


def get_active_valves_data(lines):
    all_valves, active_valves, tunnels, flow_rates = parse_lines(lines)
    shortest_distances = get_all_shortes_distances(all_valves, tunnels)
    valve_of_index = {i: v for i, v in enumerate(active_valves)}
    assert valve_of_index[0] == "AA"

    active_distances = {}
    for i, valve in enumerate(active_valves):
        active_distances[i] = {j: shortest_distances[valve][valve_of_index[j]]
                               for j in range(len(active_valves))}

    active_flow_rates = {i: flow_rates[valve_of_index[i]]
                         for i in range(len(active_valves))}

    return active_distances, active_flow_rates


# State ..  (current_valve, remaining_time, is_open)
State = tuple[int, int, tuple[bool, ...]]
Valve = int


@dataclass
class Data:
    maximal_preasure: dict[State, int]
    neighbours: dict[Valve, dict[Valve, int]]
    flow_rate: dict[Valve, int]


def solve(lines):
    neighbours, flow_rate = get_active_valves_data(lines)
    data = Data(
        maximal_preasure={},
        neighbours=neighbours,
        flow_rate=flow_rate
    )

    # State: (current_valve, remaining_time, is_open)
    initial_state = (0, TOTAL_TIME, tuple(False for _ in data.flow_rate))
    set_maximal_preasure(initial_state, data)
    return data.maximal_preasure[initial_state]


def get_next_moves(state: State, data: Data):
    current_valve, remaining_time, is_open = state

    next_states = []
    for new_valve, distance in data.neighbours[current_valve].items():
        if is_open[new_valve]:
            continue

        new_remaining_time = remaining_time - distance - 1
        if new_remaining_time <= 0:
            continue

        pressure_released = new_remaining_time * data.flow_rate[new_valve]

        new_is_open = list(is_open)
        new_is_open[new_valve] = True
        new_is_open = tuple(new_is_open)

        new_state = (new_valve, new_remaining_time, new_is_open)
        next_states.append((pressure_released, new_state))
    return next_states


def set_maximal_preasure(state: State, data: Data):
    if state in data.maximal_preasure.keys():
        return

    maximal_preasure = 0
    for preasure_released, next_state in get_next_moves(state, data):
        set_maximal_preasure(next_state, data)
        total_preasure_released = (data.maximal_preasure[next_state]
                                   + preasure_released)
        maximal_preasure = max(maximal_preasure, total_preasure_released)
    data.maximal_preasure[state] = maximal_preasure


def main():
    lines = read_lines()
    solution = solve(lines)
    print(f"{solution = }")


if __name__ == "__main__":
    main()

import re
import timeit

from dataclasses import dataclass
from enum import Enum

TOTAL_TIME = 24


class Material(Enum):
    ORE = 0
    CLAY = 1
    OBSIDIAN = 2
    GEODE = 3


def read_lines():
    with open("input.txt") as f:
        return f.read().splitlines()


def get_blueprints(lines):
    # Blueprint 1:
    # Each ore robot costs 3 ore.
    # Each clay robot costs 4 ore.
    # Each obsidian robot costs 4 ore and 18 clay.
    # Each geode robot costs 3 ore and 8 obsidian.
    blueprints = {}
    for line in lines:
        v = get_integers_in(line)
        blueprint_id = v[0]
        costs = {
            Material.ORE: AllMaterials(ore=v[1]),
            Material.CLAY: AllMaterials(ore=v[2]),
            Material.OBSIDIAN: AllMaterials(ore=v[3], clay=v[4]),
            Material.GEODE: AllMaterials(ore=v[5], obsidian=v[6]),
        }
        blueprints[blueprint_id] = costs
    return blueprints


def get_integers_in(line: str) -> list[int]:
    return [int(i_str) for i_str in re.findall(r"-?\d+", line)]


@dataclass(frozen=True)
class AllMaterials:
    ore: int = 0
    clay: int = 0
    obsidian: int = 0
    geode: int = 0

    @property
    def as_tuple(self):
        return self.ore, self.clay, self.obsidian, self.geode

    def __add__(self, other):
        return AllMaterials(*[a + b
                              for a, b in zip(self.as_tuple, other.as_tuple)])

    def __mul__(self, other: int):
        return AllMaterials(*[a * other for a in self.as_tuple])

    def __sub__(self, other):
        return self + other * -1

    def __le__(self, other):
        return all(a <= b for a, b in zip(self.as_tuple, other.as_tuple))


ROBOT = {
    Material.ORE: AllMaterials(ore=1),
    Material.CLAY: AllMaterials(clay=1),
    Material.OBSIDIAN: AllMaterials(obsidian=1),
    Material.GEODE: AllMaterials(geode=1),
}


def get_upper_bound(factory_costs, materials, robots,
                    current_time, total_time=TOTAL_TIME):
    for t in range(current_time, total_time):
        new_materials = materials + robots
        for material_type, costs in factory_costs.items():
            if costs <= materials:
                robots += ROBOT[material_type]
                # new_materials -= costs
        materials = new_materials
    return materials.geode


def get_lower_bound(factory_costs, materials, robots,
                    current_time, total_time=TOTAL_TIME):
    costs = factory_costs[Material.GEODE]
    for t in range(current_time, total_time):
        if costs <= materials:
            materials -= costs
            materials += robots
            robots += ROBOT[Material.GEODE]
        else:
            materials += robots
    return materials.geode


def get_maximal_geodes(factory_costs):
    best_result = 0
    materials = AllMaterials()
    robots = AllMaterials(ore=1)

    max_ore_required = max(factory_costs[Material.CLAY].ore,
                           factory_costs[Material.OBSIDIAN].ore,
                           factory_costs[Material.GEODE].ore)

    next_states = [(materials, robots, [])]

    for t in range(TOTAL_TIME + 1):
        current_states = eliminate_strictly_worse_states(next_states)
        next_states = []

        for state in current_states:
            materials, robots, hist = state

            upper_bound = get_upper_bound(factory_costs, materials, robots, t)
            lower_bound = get_lower_bound(factory_costs, materials, robots, t)

            if lower_bound > best_result:
                print(f"   Improved: {best_result} -> {lower_bound}")
                best_result = lower_bound

            if upper_bound <= best_result:
                continue

            # Do not build a robot at this time step:
            next_states.append((materials + robots, robots, hist))

            for robot_kind, costs in factory_costs.items():
                if (
                        robot_kind == Material.ORE
                        and robots.ore == max_ore_required
                ):
                    continue

                if costs <= materials:
                    next_states.append((
                        materials - costs + robots,
                        robots + ROBOT[robot_kind],
                        hist + [(t + 1, robot_kind)],
                    ))

    return best_result


def eliminate_strictly_worse_states(states):
    good_states = []

    for state in states:
        materials, robots, hist = state

        strictly_worse = False
        for other_state in states[:1000]:
            other_materials, other_robots, _ = other_state

            if materials == other_materials and robots == other_robots:
                continue

            if materials <= other_materials and robots <= other_robots:
                strictly_worse = True
                break

        if not strictly_worse:
            good_states.append(state)
    return good_states


def solve(lines):
    blueprints = get_blueprints(lines)

    solution = 0

    for i, factory_costs in blueprints.items():
        print(f"Blueprint {i}:")
        geodes = get_maximal_geodes(factory_costs)
        solution += geodes * i

    return solution


def main():
    lines = read_lines()
    solution = solve(lines)
    print(f"{solution = }")


if __name__ == "__main__":
    start = timeit.default_timer()

    main()

    stop = timeit.default_timer()
    print('Time: ', stop - start)


import time
import timeit


from part1 import Material, read_lines, get_blueprints, \
    get_upper_bound, get_lower_bound, AllMaterials, ROBOT

TOTAL_TIME = 32


def get_maximal_geodes(factory_costs):
    best_result = 0
    materials = AllMaterials()
    robots = AllMaterials(ore=1)

    max_ore_required = max(factory_costs[Material.CLAY].ore,
                           factory_costs[Material.OBSIDIAN].ore,
                           factory_costs[Material.GEODE].ore)

    next_states = [(materials, robots, [])]

    for t in range(TOTAL_TIME + 1):
        current_states = eliminate_strictly_worse_states(next_states,
                                                         max_ore_required)
        next_states = []
        print(f"{t = }, {len(current_states) = }")

        for state in current_states:
            materials, robots, hist = state

            upper_bound = get_upper_bound(factory_costs, materials, robots,
                                          t, TOTAL_TIME)
            lower_bound = get_lower_bound(factory_costs, materials, robots,
                                          t, TOTAL_TIME)

            # best_result = max(best_result, lower_bound.geode)
            if lower_bound > best_result:
                print(f"   Improved: {best_result} -> {lower_bound}")
                best_result = lower_bound

            if upper_bound <= best_result:
                continue

            next_states.append((materials + robots, robots, hist))

            for next_construction, costs in factory_costs.items():
                if (
                        next_construction == Material.ORE
                        and robots.ore == max_ore_required
                ):
                    continue

                if costs <= materials:
                    next_states.append((
                        materials - costs + robots,
                        robots + ROBOT[next_construction],
                        hist + [(t + 1, next_construction.name)],
                    ))

    return best_result


def eliminate_strictly_worse_states(states, max_ore_required):
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

            if (
                    materials.clay == other_materials.clay
                    and materials.obsidian == other_materials.obsidian
                    and materials.geode == other_materials.geode
                    and robots.as_tuple == other_robots.as_tuple
            ):
                continue

            if (
                    other_robots.ore == max_ore_required
                    and other_materials.ore >= max_ore_required

                    and materials.clay <= other_materials.clay
                    and materials.obsidian <= other_materials.obsidian
                    and materials.geode <= other_materials.geode

                    and robots <= other_robots
            ):
                strictly_worse = True
                break

        if not strictly_worse:
            good_states.append(state)
    return good_states


def solve(lines):
    blueprints = get_blueprints(lines)

    solution = 1

    for i in [1, 2, 3]:
        factory_costs = blueprints[i]
        print(f"Blueprint {i}:")
        geodes = get_maximal_geodes(factory_costs)
        print(f"  {geodes = }")
        time.sleep(1)

        solution *= geodes

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

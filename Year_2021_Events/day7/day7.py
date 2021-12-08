from typing import List


def get_crab_positions(filename: str) -> List[int]:
    f = open(filename, "r")
    positions = f.readline().split(",")
    f.close()
    positions = [int(i) for i in positions]
    return positions


def constant_cost_to_align_crabs(initial_positions: List[int]) -> dict:
    crabs_pos_max = max(initial_positions)
    fuel_cost_dict = {}
    for aligned_position in range(0, crabs_pos_max):
        fuel_cost = 0
        for crab in initial_positions:
            fuel_cost += abs(crab - aligned_position)
        fuel_cost_dict[str(aligned_position)] = fuel_cost
    return fuel_cost_dict


def increasing_cost_to_align_crabs(initial_positions: List[int]) -> dict:
    crabs_pos_max = max(initial_positions)
    crabs_count = len(initial_positions)
    fuel_cost_dict = {}
    for aligned_position in range(0, crabs_pos_max):
        fuel_cost = 0
        for i in range(0, crabs_count):
            diff = abs(initial_positions[i] - aligned_position)
            fuel_cost += diff * (diff + 1) / 2
        fuel_cost_dict[str(aligned_position)] = int(fuel_cost)
    return fuel_cost_dict


def get_lowest_cost(cost_list: dict) -> int:
    crabs_count = len(cost_list)

    min_cost = cost_list["0"]
    for p in range(1, crabs_count):
        if cost_list[str(p)] < min_cost:
            min_cost = cost_list[str(p)]
    return min_cost


def get_part_one(filename: str) -> int:
    pos = get_crab_positions(filename)
    cost = constant_cost_to_align_crabs(pos)
    return get_lowest_cost(cost)


def get_part_two(filename: str) -> int:
    pos = get_crab_positions(filename)
    cost = increasing_cost_to_align_crabs(pos)
    return get_lowest_cost(cost)


def main():
    print(get_part_one("day7_input.txt"))
    print(get_part_two("day7_input.txt"))


if __name__ == "__main__":
    main()

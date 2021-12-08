from typing import List


def get_crab_positions(filename: str) -> List[int]:
    f = open(filename, "r")
    positions = f.readline().split(",")
    f.close()
    positions = [int(i) for i in positions]
    return positions


def cost_to_align_crabs(initial_positions: List[int]) -> dict:
    crabs_count = max(initial_positions)
    fuel_cost_dict = {}
    for aligned_position in range(0, crabs_count):
        fuel_cost = 0
        for crab in initial_positions:
            fuel_cost += abs(crab - aligned_position)
        fuel_cost_dict[str(aligned_position)] = fuel_cost
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
    cost = cost_to_align_crabs(pos)
    return get_lowest_cost(cost)


def main():
    print(get_part_one("day7_input.txt"))


if __name__ == "__main__":
    main()

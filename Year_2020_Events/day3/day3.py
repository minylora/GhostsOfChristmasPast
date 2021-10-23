import re
from typing import List

from Year_2020_Events.myutils.myutils import get_str_list


# Part 1
def how_many_trees_for_part_one(slope_map: List[str]) -> int:
    num_trees = 0
    for row in range(0, len(slope_map)):
        pos = (row * 3) % len(slope_map[row])
        if slope_map[row][pos] == "#":
            num_trees += 1
    return num_trees


# Part 2 - Find a generic part 1, then use to solve for mixed slopes
def how_many_trees_for_single_slope(slope_map: List[str], right: int, down: int) -> int:
    num_trees = 0
    count = 0
    for row in range(0, len(slope_map), down):
        pos = count * right
        pos = pos % len(slope_map[row])
        if slope_map[row][pos] == "#":
            num_trees += 1
        count += 1
    return num_trees


def how_many_trees_for_multiple_slopes_multiplied(slope_map: List[str], slopes: List[tuple]):
    num_trees_multiplied = 1
    for right, down in slopes:
        num_trees_for_slope = how_many_trees_for_single_slope(slope_map, right, down)
        num_trees_multiplied = num_trees_multiplied*num_trees_for_slope
    return num_trees_multiplied


def main():
    slope_map = get_str_list("input.txt")
    num_trees = how_many_trees_for_part_one(slope_map)
    print(f"part_one: {num_trees}")

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    num_trees_mult = how_many_trees_for_multiple_slopes_multiplied(slope_map, slopes)
    print(f"part_two: {num_trees_mult}")


if __name__ == "__main__":
    main()

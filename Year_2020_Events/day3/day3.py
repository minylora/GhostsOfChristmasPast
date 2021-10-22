import re
from typing import List

from Year_2020_Events.myutils.myutils import get_str_list


# Part 1
def how_many_tress_for_part_one(slope_map: List[str]) -> int:
    num_tress = 0
    if slope_map[0][0] == "#":
        num_tress += 1
    for row in range(1, len(slope_map)):
        pos = (row - 1) * 3 + 3
        pos = pos % len(slope_map[row])
        if slope_map[row][pos] == "#":
            num_tress += 1
    return num_tress


def main():
    slope_map = get_str_list("input.txt")
    num_trees = how_many_tress_for_part_one(slope_map)
    print(f"part_one: {num_trees}")


if __name__ == "__main__":
    main()

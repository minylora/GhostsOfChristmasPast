import re
from typing import List

from Year_2020_Events.myutils.myutils import get_str_list


def get_digits(filename: str) -> (List[List[int]], List[List[int]]):
    str_list = get_str_list(filename)
    pattern = []
    output = []
    for line in str_list:
        values = line.split(" ")
        pattern.append(values[0:9])
        output.append(values[11:15])
    return pattern, output


def part_one(filename: str) -> int:
    pattern, output = get_digits(filename)
    thedigis = [2, 3, 4, 7]
    count = 0
    for values in output:
        for value in values:
            if len(value) in thedigis:
                count += 1
    return count


def main():
    print(part_one("day8_input.txt"))


if __name__ == "__main__":
    main()

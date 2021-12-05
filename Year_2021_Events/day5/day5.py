import re
from typing import List

from Year_2020_Events.myutils.myutils import get_str_list


def get_vent_coordinates(filename: str) -> List[List[List[int]]]:
    str_list = get_str_list(filename)
    vent_coords = []
    for line in str_list:
        values = re.search(r"(\d+),(\d+).+(\d+),(\d+)", line)
        start = [int(values.group(1)), int(values.group(2))]
        end = [int(values.group(3)), int(values.group(4))]
        vent_coords.append([start, end])
    return vent_coords


def get_horizontal_lines_from_coordinates(coordinates: List[List[List[int]]]) -> List[List[List[int]]]:
    horizontal_lines = []
    for coord in coordinates:
        if coord[0][1] == coord[1][1]:
            horizontal_lines.append(coord)
    return horizontal_lines


def get_vertical_lines_from_coordinates(coordinates: List[List[List[int]]]) -> List[List[List[int]]]:
    vertical_lines = []
    for coord in coordinates:
        if coord[0][0] == coord[1][0]:
            vertical_lines.append(coord)
    return vertical_lines


def main():
    pass


if __name__ == "__main__":
    main()

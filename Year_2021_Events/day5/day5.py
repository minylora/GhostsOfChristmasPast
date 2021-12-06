import copy
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
            if coord[0][0] > coord[1][0]:
                temp = coord[0][0]
                coord[0][0] = coord[1][0]
                coord[1][0] = temp
            horizontal_lines.append(coord)
    return horizontal_lines


def get_vertical_lines_from_coordinates(coordinates: List[List[List[int]]]) -> List[List[List[int]]]:
    vertical_lines = []
    for coord in coordinates:
        if coord[0][0] == coord[1][0]:
            if coord[0][1] > coord[1][1]:
                temp = coord[0][1]
                coord[0][1] = coord[1][1]
                coord[1][1] = temp
            vertical_lines.append(coord)
    return vertical_lines


def get_max_x(coordinates: List[List[List[int]]]) -> int:
    max_x = 0
    for coord in coordinates:
        if coord[0][0] > max_x:
            max_x = coord[0][0]
        if coord[1][0] > max_x:
            max_x = coord[1][0]
    return max_x


def get_max_y(coordinates: List[List[List[int]]]) -> int:
    max_y = 0
    for coord in coordinates:
        if coord[0][1] > max_y:
            max_y = coord[0][1]
        if coord[1][1] > max_y:
            max_y = coord[1][1]
    return max_y


def create_diagram(coordinates: List[List[List[int]]]) -> List[List[int]]:
    x_len = get_max_x(coordinates) + 1
    y_len = get_max_y(coordinates) + 1
    diagram = [[0] * x_len for y in range(0, y_len)]
    return diagram


def update_diagram_horizontally(diagram: List[List[int]], horiz_coords: List[List[List[int]]]) -> List[List[int]]:
    updated_diagram = copy.deepcopy(diagram)
    for line in horiz_coords:
        x1 = line[0][0]
        x2 = line[1][0]
        y = line[0][1]
        for i in range(x1, x2+1):
            updated_diagram[y][i] += 1
    return updated_diagram


def update_diagram_vertically(diagram: List[List[int]], vert_coords: List[List[List[int]]]) -> List[List[int]]:
    updated_diagram = copy.deepcopy(diagram)
    for line in vert_coords:
        x = line[0][0]
        y1 = line[0][1]
        y2 = line[1][1]
        for i in range(y1, y2+1):
            updated_diagram[i][x] += 1
    return updated_diagram


def calculate_part_one_answer(filename: str) -> int:
    all_coords = get_vent_coordinates(filename)
    diagram = create_diagram(all_coords)

    horiz = get_horizontal_lines_from_coordinates(all_coords)
    vert = get_vertical_lines_from_coordinates(all_coords)

    diagram_horiz = update_diagram_horizontally(diagram, horiz)
    updated_diagram = update_diagram_vertically(diagram_horiz, vert)

    count = 0
    for row in updated_diagram:
        for col in row:
            if col >= 2:
                count += 1

    print(updated_diagram)
    return count


def main():
    part_one = calculate_part_one_answer("day5_input.txt")
    print(part_one)


if __name__ == "__main__":
    main()

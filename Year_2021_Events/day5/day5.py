import re
from typing import List

from Year_2020_Events.myutils.myutils import get_str_list

COORDINATE_LIST_TYPE = "List[List[List[int]]]"
DIAGRAM_TYPE = "List[List[int]]"

# why ans wrong :( - things to consider
# # points (instead of lines) - would duplicate, so ans would be bigger not smaller
# # accounts for + crossing points because of house line crossing is tracked
# # regex doesnt care how many digits the coords are
# # coords are rearranged so [start, end] always has start as smaller values
# # does not care if map is square or rectangle
# # part one - horiz and vert are included and diag are not included
# #


def get_vent_coordinates(filename: str) -> COORDINATE_LIST_TYPE:
    str_list = get_str_list(filename)
    vent_coords = []
    for line in str_list:
        values = re.search(r"(\d+),(\d+).+(\d+),(\d+)", line)
        start = [int(values.group(1)), int(values.group(2))]
        end = [int(values.group(3)), int(values.group(4))]
        vent_coords.append([start, end])
    return vent_coords


def get_horizontal_lines_from_coordinates(
    coordinates: COORDINATE_LIST_TYPE,
) -> COORDINATE_LIST_TYPE:
    horizontal_lines = []
    for coord in coordinates:
        start_x = coord[0][0]
        end_x = coord[1][0]
        start_y = coord[0][1]
        end_y = coord[1][1]
        if start_y == end_y:
            if start_x > end_x:
                temp = start_x
                start_x = end_x
                end_x = temp
            line_coord = [[start_x, start_y], [end_x, end_y]]
            horizontal_lines.append(line_coord)
    return horizontal_lines


def get_vertical_lines_from_coordinates(
    coordinates: COORDINATE_LIST_TYPE,
) -> COORDINATE_LIST_TYPE:
    vertical_lines = []
    for coord in coordinates:
        start_x = coord[0][0]
        end_x = coord[1][0]
        start_y = coord[0][1]
        end_y = coord[1][1]
        if start_x == end_x:
            if start_y > end_y:
                temp = start_y
                start_y = end_y
                end_y = temp
            line_coord = [[start_x, start_y], [end_x, end_y]]
            vertical_lines.append(line_coord)
    return vertical_lines


def get_max_x(coordinates: COORDINATE_LIST_TYPE) -> int:
    max_x = 0
    for coord in coordinates:
        start_x = coord[0][0]
        end_x = coord[1][0]
        if start_x > max_x:
            max_x = start_x
        if end_x > max_x:
            max_x = end_x
    return max_x


def get_max_y(coordinates: COORDINATE_LIST_TYPE) -> int:
    max_y = 0
    for coord in coordinates:
        start_y = coord[0][1]
        end_y = coord[1][1]
        if start_y > max_y:
            max_y = start_y
        if end_y > max_y:
            max_y = end_y
    return max_y


def create_diagram(coordinates: COORDINATE_LIST_TYPE) -> DIAGRAM_TYPE:
    x_len = get_max_x(coordinates) + 1
    y_len = get_max_y(coordinates) + 1

    # Create the initial diagram of all zeros
    # [0]*x creates list of length x with all 0 values
    # create list of length y where each value is a list [0]*x
    diagram = [[0] * x_len for y in range(0, y_len)]
    return diagram


def update_diagram_horizontally(
    diagram: DIAGRAM_TYPE, horiz_coords: COORDINATE_LIST_TYPE
) -> DIAGRAM_TYPE:
    for line in horiz_coords:
        x1 = line[0][0]
        x2 = line[1][0]
        y = line[0][1]
        for x in range(x1, x2 + 1):
            diagram[y][x] += 1
    return diagram


def update_diagram_vertically(
    diagram: DIAGRAM_TYPE, vert_coords: COORDINATE_LIST_TYPE
) -> DIAGRAM_TYPE:
    for line in vert_coords:
        x = line[0][0]
        y1 = line[0][1]
        y2 = line[1][1]
        for y in range(y1, y2 + 1):
            diagram[y][x] += 1
    return diagram


def calculate_part_one_answer(filename: str) -> int:
    all_coords = get_vent_coordinates(filename)
    diagram = create_diagram(all_coords)

    horiz = get_horizontal_lines_from_coordinates(all_coords)
    diagram = update_diagram_horizontally(diagram, horiz)

    vert = get_vertical_lines_from_coordinates(all_coords)
    diagram = update_diagram_vertically(diagram, vert)

    print(diagram)

    count = 0
    for row in range(0, len(diagram)):
        for col in range(0, len(diagram[0])):
            if diagram[row][col] >= 2:
                count += 1
    return count


def main():
    part_one = calculate_part_one_answer("mini_vents")
    print(part_one)


if __name__ == "__main__":
    main()

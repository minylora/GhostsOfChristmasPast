from typing import List

from Year_2020_Events.myutils.myutils import get_str_list

BASIN_TYPE = List[List[int]]
LOC_TYPE = List[int]


def get_basin(filename: str) -> BASIN_TYPE:
    basin_rows = get_str_list(filename)
    basin = []
    for row in basin_rows:
        row_list = list(row)
        basin.append([int(v) for v in row_list])
    return basin


def is_edge(basin: BASIN_TYPE, row_loc: int, col_loc: int) -> bool:
    basin_row_count = len(basin)
    basin_col_count = len(basin[0])
    if row_loc == 0 or row_loc == basin_row_count - 1 or col_loc == 0 or col_loc == basin_col_count -1:
        return True
    return False


def is_corner(basin: BASIN_TYPE, row_loc: int, col_loc: int) -> bool:
    basin_row_count = len(basin)
    basin_col_count = len(basin[0])
    if (row_loc == 0 or row_loc == basin_row_count - 1) and (col_loc == 0 or col_loc == basin_col_count - 1):
        return True
    return False


def get_surrounding_points(basin: BASIN_TYPE, row_loc: int, col_loc: int) -> List[LOC_TYPE]:
    max_row_val = len(basin) - 1
    max_col_val = len(basin[0]) - 1
    surrounding_points = []

    # top corners
    if row_loc == 0 and col_loc == 0:
        surrounding_points.append([0, 1])
        surrounding_points.append([1, 0])
    elif row_loc == 0 and col_loc == max_col_val:
        surrounding_points.append([0, max_col_val - 1])
        surrounding_points.append([1, max_col_val])

    # bottom corners
    elif row_loc == max_row_val and col_loc == 0:
        surrounding_points.append([max_row_val, 1])
        surrounding_points.append([max_row_val - 1, 0])
    elif row_loc == max_row_val and col_loc == max_col_val:
        surrounding_points.append([max_row_val, max_col_val - 1])
        surrounding_points.append([max_row_val - 1, max_col_val])

    # top edge
    elif row_loc == 0:
        surrounding_points.append([row_loc, col_loc - 1])
        surrounding_points.append([row_loc, col_loc + 1])
        surrounding_points.append([1, col_loc])

    # bottom edge
    elif row_loc == max_row_val:
        surrounding_points.append([row_loc, col_loc - 1])
        surrounding_points.append([row_loc, col_loc + 1])
        surrounding_points.append([row_loc - 1, col_loc])

    # left 3dge
    elif col_loc == 0:
        surrounding_points.append([row_loc - 1, col_loc])
        surrounding_points.append([row_loc + 1, col_loc])
        surrounding_points.append([row_loc, 1])

    # right edge
    elif col_loc == max_col_val:
        surrounding_points.append([row_loc - 1, col_loc])
        surrounding_points.append([row_loc + 1, col_loc])
        surrounding_points.append([row_loc, col_loc - 1])

    # any inner point
    else:
        surrounding_points.append([row_loc, col_loc - 1])
        surrounding_points.append([row_loc, col_loc + 1])
        surrounding_points.append([row_loc - 1, col_loc])
        surrounding_points.append([row_loc + 1, col_loc])

    return surrounding_points


def calculate_part_one(filename: str) -> int:
    basin = get_basin(filename)
    total = 0
    for row_loc in range(0, len(basin)):
        for col_loc in range(len(basin[0])):
            surrounding_points = get_surrounding_points(basin, row_loc, col_loc)
            point_height = basin[row_loc][col_loc]
            lowest = True
            for point in surrounding_points:
                rloc = point[0]
                cloc = point[1]
                if point_height >= basin[rloc][cloc]:
                    lowest = False
                    break
            if lowest:
                total = total + point_height + 1
    return total


def get_low_points(basin: BASIN_TYPE) -> List[LOC_TYPE]:
    low_points = []
    for row_loc in range(0, len(basin)):
        for col_loc in range(len(basin[0])):
            surrounding_points = get_surrounding_points(basin, row_loc, col_loc)
            point_height = basin[row_loc][col_loc]
            lowest = True
            for point in surrounding_points:
                rloc = point[0]
                cloc = point[1]
                if point_height >= basin[rloc][cloc]:
                    lowest = False
                    break
            if lowest:
                low_points.append([row_loc, col_loc])
    return low_points


def calculate_part_one_with_get_low_points(filename: str) -> int:
    basin = get_basin(filename)
    low_points = get_low_points(basin)
    total = 0
    for point in low_points:
        total += 1 + basin[point[0]][point[1]]
    return total


def get_surrounding_points_that_arent_nine(basin: BASIN_TYPE, low_point: LOC_TYPE) -> List[LOC_TYPE]:
    row = low_point[0]
    col = low_point[1]
    surrounding_points = get_surrounding_points(basin, row, col)
    not_nine = []
    for point in surrounding_points:
        row = point[0]
        col = point[1]
        if basin[row][col] < 9:
            not_nine.append([row, col])
    return not_nine


def get_basin_size_for_a_low_point(basin: BASIN_TYPE, low_point: LOC_TYPE) -> int:
    surrounding_points = get_surrounding_points_that_arent_nine(basin, low_point)
    part_of_the_basin = [low_point] + surrounding_points
    basin_set = set(part_of_the_basin)


def calculate_part_two(filename: str) -> int:
    basin_values = get_basin(filename)
    low_points = get_low_points(basin_values)
    basin_sizes = []
    for point in low_points:
        sz = get_basin_size_for_a_low_point(basin_values, point)
        basin_sizes.append(sz)
    basin_sizes.sort(reverse=True)
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


def main():
    part_one = calculate_part_one_with_get_low_points("day9_input.txt")
    print(part_one)
    part_two = calculate_part_two("day9_input.txt")
    print(part_two)


if __name__ == "__main__":
    main()

import pytest
from . import day5

mini_vents = r"C:\Users\Mindy\Documents\CodeyCode\GhostsOfChristmasPast\Year_2021_Events\day5\mini_vents"
vent_coords = day5.get_vent_coordinates(mini_vents)


def test_deep_copy_coordinates():
    coords = [
        [[1, 2], [0, 0]],
        [[0, 0], [0, 0]],
        [[0, 0], [0, 0]],
    ]
    c = day5.deep_copy_coordinates(coords)
    assert len(c) == len(coords)
    assert len(c) == 3
    assert len(c[0]) == len(coords[0])
    assert len(c[0]) == 2
    assert c[0][0] == [1, 2]
    assert c[0][0][1] == 2


def test_deep_copy_diagram():
    d = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    c = day5.deep_copy_diagram(d)
    assert len(c) == len(d)
    assert len(c) == 3
    assert len(c[0]) == len(d[0])
    assert len(c[0]) == 4


def test_get_vent_coordinates():
    assert len(vent_coords) == 12
    assert len(vent_coords[0]) == 2
    assert len(vent_coords[0][1]) == 2
    assert vent_coords[9] == [[5, 5], [8, 2]]


def test_get_horizontal_lines_from_coordinates():
    coordinates = day5.get_horizontal_lines_from_coordinates(vent_coords)
    assert len(coordinates) == 4
    assert coordinates[0] == [[0, 9], [5, 9]]
    assert coordinates[1] == [[3, 4], [9, 4]]
    assert coordinates[2] == [[0, 9], [2, 9]]
    assert coordinates[3] == [[1, 4], [3, 4]]


def test_get_vertical_lines_from_coordinates():
    coordinates = day5.get_vertical_lines_from_coordinates(vent_coords)
    assert len(coordinates) == 4
    assert coordinates[0] == [[2, 1], [2, 2]]
    assert coordinates[1] == [[7, 0], [7, 6]]
    assert coordinates[2] == [[7, 3], [7, 7]]
    assert coordinates[3] == [[9, 4], [9, 5]]


def test_get_max_x():
    assert day5.get_max_x(vent_coords) == 9


def test_get_max_y():
    assert day5.get_max_y(vent_coords) == 9


def test_create_diagram():
    diagram = day5.create_diagram(vent_coords)
    assert len(diagram) == 10
    assert len(diagram[0]) == 10
    assert diagram[0].count(0) == 10


def test_update_diagram_horizontally():
    diagram = day5.create_diagram(vent_coords)
    coordinates = day5.get_horizontal_lines_from_coordinates(vent_coords)
    updated_diagram = day5.update_diagram_horizontally(diagram, coordinates)
    assert len(updated_diagram) == 10
    assert len(updated_diagram[0]) == 10


def test_update_diagram_vertically():
    diagram = day5.create_diagram(vent_coords)
    coordinates = day5.get_vertical_lines_from_coordinates(vent_coords)
    updated_diagram = day5.update_diagram_vertically(diagram, coordinates)
    assert len(updated_diagram) == 10
    assert len(updated_diagram[0]) == 10
    assert updated_diagram[1][2] == 1
    assert updated_diagram[2][2] == 1


def test_calculate_part_one_answer():
    assert day5.calculate_part_one_answer(mini_vents) == 9


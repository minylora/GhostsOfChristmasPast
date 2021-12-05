import pytest
from . import day5

mini_vents = r"C:\Users\Mindy\Documents\CodeyCode\GhostsOfChristmasPast\Year_2021_Events\day5\mini_vents"
vent_coords = day5.get_vent_coordinates(mini_vents)


def test_get_vent_coordinates():
    assert len(vent_coords) == 10
    assert len(vent_coords[0]) == 2
    assert len(vent_coords[0][1]) == 2
    assert vent_coords[9] == [[5, 5], [8, 2]]


def test_get_horizontal_lines_from_coordinates():
    coordinates = day5.get_horizontal_lines_from_coordinates(vent_coords)
    assert len(coordinates) == 4
    assert coordinates[0] == [[0, 9], [5, 9]]


def test_get_vertical_lines_from_coordinates():
    coordinates = day5.get_vertical_lines_from_coordinates(vent_coords)
    assert len(coordinates) == 2
    assert coordinates[0] == [[2, 2], [2,1]]


import pytest
from . import day9


mini_basin = r"C:\Users\Mindy\Documents\CodeyCode\GhostsOfChristmasPast\Year_2021_Events\day9\mini_map"
basin = day9.get_basin(mini_basin)
corners = [
    [0, 0],
    [0, 9],
    [4, 0],
    [4, 9]
]
surrounds_corners = [
    [[0, 1], [1, 0]],
    [[0, 8], [1, 9]],
    [[4, 1], [3, 0]],
    [[4, 8], [3, 9]],
]
edges = [
    [0, 1],
    [3, 0],
    [3, 9],
    [4, 7],
]
surrounds_edges = [
    [[0, 0], [0, 2], [1, 1]],
    [[2, 0], [4, 0], [3, 1]],
    [[2, 9], [4, 9], [3, 8]],
    [[4, 6], [4, 8], [3, 7]],
]
middle = [
    [1, 1],
    [3, 8],
]
surrounds_inner = [
    [[1, 0], [1, 2], [0, 1], [2, 1]],
    [[3, 7], [3, 9], [2, 8], [4, 8]],
]
expected_low_points = [
    [0, 1],
    [0, 9],
    [2, 2],
    [4, 6],
]
not_nine = [
    1,
    2,
    4,
    3,
]


def test_get_basin():
    actual = day9.get_basin(mini_basin)
    assert len(actual) == 5
    assert len(actual[0]) == 10
    assert isinstance(actual[0][0], int)


@pytest.mark.parametrize("xloc, yloc", edges + corners)
def test_is_edge_true(xloc, yloc):
    assert day9.is_edge(basin, xloc, yloc) is True


@pytest.mark.parametrize("xloc, yloc", middle)
def test_is_edge_false(xloc, yloc):
    assert day9.is_edge(basin, xloc, yloc) is False


@pytest.mark.parametrize("xloc, yloc", corners)
def test_is_corner_true(xloc, yloc):
    assert day9.is_corner(basin, xloc, yloc) is True


@pytest.mark.parametrize("xloc, yloc", middle + edges)
def test_is_edge_false(xloc, yloc):
    assert day9.is_corner(basin, xloc, yloc) is False


@pytest.mark.parametrize("locs, expected", zip(corners, surrounds_corners))
def test_get_surrounding_points_corners(locs, expected):
    results = day9.get_surrounding_points(basin, locs[0], locs[1])
    assert len(results) == 2
    assert results == expected


@pytest.mark.parametrize("locs, expected", zip(edges, surrounds_edges))
def test_get_surrounding_points_edges(locs, expected):
    results = day9.get_surrounding_points(basin, locs[0], locs[1])
    assert len(results) == 3
    assert results == expected


@pytest.mark.parametrize("locs, expected", zip(middle, surrounds_inner))
def test_get_surrounding_points_inside(locs, expected):
    results = day9.get_surrounding_points(basin, locs[0], locs[1])
    assert len(results) == 4
    assert results == expected


def test_calculate_part_one():
    assert day9.calculate_part_one(mini_basin) == 15


def test_get_low_points():
    results = day9.get_low_points(basin)
    assert len(results) == 4
    assert results == expected_low_points


def test_calculate_part_one_with_get_low_points():
    assert day9.calculate_part_one_with_get_low_points(mini_basin) == 15


@pytest.mark.parametrize("locs, lengths", zip(expected_low_points, not_nine))
def test_get_surrounding_points_that_arent_nine(locs, lengths):
    results = day9.get_surrounding_points_that_arent_nine(basin, locs)
    assert len(results) == lengths

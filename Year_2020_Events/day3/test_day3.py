import os
from sys import path

import pytest

from . import day3

from Year_2020_Events.myutils.myutils import get_str_list


@pytest.fixture
def slope_map_sample():
    fpath = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(fpath, "sample_input.txt")
    return get_str_list(filename)


@pytest.fixture
def slope_map_input():
    fpath = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(fpath, "input.txt")
    return get_str_list(filename)


@pytest.fixture
def sample_slopes():
    return [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


how_many_trees_part_one_data = [
    ("slope_map_sample", 7),
    ("slope_map_input", 187),
]


how_many_trees_given_slope_data = [
    ("slope_map_sample", 3, 1, 7),
    ("slope_map_input", 3, 1, 187),
    ("slope_map_sample", 1, 1, 2),
    ("slope_map_sample", 5, 1, 3),
    ("slope_map_sample", 7, 1, 4),
    ("slope_map_sample", 1, 2, 2),
]


@pytest.mark.parametrize("slope_map, result", how_many_trees_part_one_data)
def test_how_many_trees_for_part_one_with_sample(slope_map, result, request):
    slope_map = request.getfixturevalue(slope_map)
    assert day3.how_many_trees_for_part_one(slope_map) == result


@pytest.mark.parametrize(
    "slope_map, right, down, result", how_many_trees_given_slope_data
)
def test_how_many_trees_for_single_slope_sample(
    slope_map, right, down, result, request
):
    slope_map = request.getfixturevalue(slope_map)
    assert day3.how_many_trees_for_single_slope(slope_map, right, down) == result


def test_how_many_trees_for_multiple_slopes(slope_map_sample, sample_slopes):
    assert (
        day3.how_many_trees_for_multiple_slopes_multiplied(
            slope_map_sample, sample_slopes
        )
        == 336
    )


def test_how_many_trees_for_multiple_slopes(slope_map_input, sample_slopes):
    assert (
        day3.how_many_trees_for_multiple_slopes_multiplied(
            slope_map_input, sample_slopes
        )
        == 4723283400
    )

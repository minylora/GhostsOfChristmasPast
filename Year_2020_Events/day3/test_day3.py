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


def test_how_many_tress_for_part_one_with_sample_input(slope_map_sample):
    assert day3.how_many_tress_for_part_one(slope_map_sample) == 7


def test_how_many_tress_for_part_one_with_input(slope_map_input):
    assert day3.how_many_tress_for_part_one(slope_map_input) == 187

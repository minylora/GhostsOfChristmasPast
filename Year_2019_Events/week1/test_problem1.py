import pytest
from week1.week1 import *


def test_part_one_happy_path():
    input_data = [12, 14, 1969, 100756]
    result = 34241
    assert part1(input_data) == result


def test_part_two_happy_path():
    input_data = [14, 1969, 100756]
    result = 51314
    assert part2(input_data) == result

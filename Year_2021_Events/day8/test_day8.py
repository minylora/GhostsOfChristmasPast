import pytest
from . import day8


mini_digits = r"C:\Users\Mindy\Documents\CodeyCode\GhostsOfChristmasPast\Year_2021_Events\day8\ mini_digits"


def test_get_digits():
    pattern, output = day8.get_digits(mini_digits)
    assert len(pattern) == 10
    assert len(output) == 10
    assert len(output[0]) == 4


def test_part_one():
    pattern, output = day8.get_digits(mini_digits)
    assert day8.part_one(output) == 26

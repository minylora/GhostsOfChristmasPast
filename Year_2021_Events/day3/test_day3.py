import pytest
from . import day3

test_report = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]


def test_get_power_consumption():
    expected = 198
    assert day3.get_power_consumption(test_report) == expected


def test_get_life_support_rating():
    expected = 230
    assert day3.get_life_support_rating(test_report) == expected

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


def test_calculate_gamma_rate():
    expected = 22
    assert day3.calculate_gamma_rate(test_report) == expected


def test_calculate_epsilon_rate():
    expected = 9
    assert day3.calculate_epsilon_rate(test_report) == expected


def test_get_power_consumption():
    expected = 9*22
    assert day3.get_power_consumption(test_report) == expected

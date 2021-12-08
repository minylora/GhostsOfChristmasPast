import pytest
from . import day7

mini_crabs = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
expected_fuel = {
    "0": 49,
    "1": 41,
    "10": 71,
    "11": 77,
    "12": 83,
    "13": 89,
    "14": 95,
    "15": 103,
    "2": 37,
    "3": 39,
    "4": 41,
    "5": 45,
    "6": 49,
    "7": 53,
    "8": 59,
    "9": 65,
}


def test_cost_to_align_crabs():
    assert day7.cost_to_align_crabs(mini_crabs) == expected_fuel


def test_get_lowest_cost():
    assert day7.get_lowest_cost(expected_fuel) == 37

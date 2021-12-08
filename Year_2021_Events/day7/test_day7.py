import pytest
from . import day7

mini_crabs = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
expected_constant = {
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
expected_increasing = {
    "0": 290,
    "1": 242,
    "10": 311,
    "11": 370,
    "12": 439,
    "13": 518,
    "14": 607,
    "15": 707,
    "2": 206,
    "3": 183,
    "4": 170,
    "5": 168,
    "6": 176,
    "7": 194,
    "8": 223,
    "9": 262,
}


def test_cost_to_align_crabs():
    assert day7.constant_cost_to_align_crabs(mini_crabs) == expected_constant


def test_get_lowest_cost():
    assert day7.get_lowest_cost(expected_constant) == 37


def test_increasing_cost_to_align_crabs():
    assert day7.increasing_cost_to_align_crabs(mini_crabs) == expected_increasing

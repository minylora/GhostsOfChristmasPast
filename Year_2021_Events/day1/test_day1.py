import pytest
from . import day1

test_measurements = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
expected_sliding_window_values = [607, 618, 618, 617, 647, 716, 769, 792]


def test_part_one():
    expected_result = 7
    assert (
        day1.how_many_are_larger_than_the_previous(test_measurements) == expected_result
    )


def test_part_two_sliding_win_math():
    assert day1.get_sliding_window(test_measurements) == expected_sliding_window_values


def test_part_two():
    expected_result = 5
    assert (
        day1.how_many_are_larger_than_the_previous(expected_sliding_window_values)
        == expected_result
    )

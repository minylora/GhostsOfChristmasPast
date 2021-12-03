import pytest
from . import day2

test_course = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']


def test_get_multiplied_location():
    expected_result = 150
    assert day2.get_multiplied_location(test_course) == expected_result


def test_get_multiplied_location_with_aim():
    expected_result = 900
    assert day2.get_multiplied_location_with_aim(test_course) == expected_result


def test_get_course_change():
    test_change = 'forward 5'
    expected_result = ('forward', 5)
    assert day2.get_course_change(test_change) == expected_result

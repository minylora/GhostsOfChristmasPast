import pytest
from . import day6

mini_state = r"C:\Users\Mindy\Documents\CodeyCode\GhostsOfChristmasPast\Year_2021_Events\day6\mini_state"
mini_list = [3, 4, 3, 1, 2]
days = [0, 1, 2, 10, 18, 80, 256]
totals = [5, 5, 6, 12, 26, 5934, 26984457539]
expected = zip(days, totals)


def test_get_initial_state():
    assert day6.get_initial_state(mini_state) == mini_list


@pytest.mark.parametrize("day, expected_total", expected)
def test_how_many_lantern_fish(day, expected_total):
    assert day6.how_many_lantern_fish(mini_list, day) == expected_total


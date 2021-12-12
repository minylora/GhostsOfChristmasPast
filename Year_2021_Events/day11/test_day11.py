import pytest

from Year_2020_Events.myutils.myutils import get_list_of_int_lists
from . import day11

mini_energy_path = r"C:\Users\Mindy\Documents\CodeyCode\GhostsOfChristmasPast\Year_2021_Events\day11\mini_energy"
mini_energy = get_list_of_int_lists(mini_energy_path)


def test_increase_adjacent_energy():
    octos = day11.increase_adjacent_energy(mini_energy, [0, 0])
    assert octos[0][1] == 5
    assert octos[1][0] == 3
    assert octos[1][1] == 8


def test_take_2_steps():
    assert day11.take_x_steps(mini_energy, 2) == 35


def test_take_3_steps():
    assert day11.take_x_steps(mini_energy, 3) == 80


def test_take_10_steps():
    assert day11.take_x_steps(mini_energy, 10) == 204


def test_take_100_steps():
    assert day11.take_x_steps(mini_energy, 100) == 1656

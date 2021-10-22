import pytest
from . import day1

part_one_test_cases = [
    ([5, 1721, 299, 6], 514579),
    ([5, 299, 6], None),
    ([2020], None),
    ([], None),
    ([1010, 1], None),
]

part_two_test_cases = [
    ([70, 979, 366, 675, 2020], 241861950),
    ([5, 299, 6], None),
    ([2019, 1], None),
    ([2020], None),
    ([], None),
    ([1010, 505, 1], None),
]


@pytest.mark.parametrize("part_one_report,part_one_result", part_one_test_cases)
def test_part_one_example(part_one_report, part_one_result):
    assert day1.find_sum_of_two_and_mult(part_one_report) == part_one_result


@pytest.mark.parametrize("part_two_report,part_two_result", part_two_test_cases)
def test_part_two_example(part_two_report, part_two_result):
    assert day1.find_sum_of_three_and_mult(part_two_report) == part_two_result

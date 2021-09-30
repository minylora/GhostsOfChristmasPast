import pytest

from . import week2

part_one_valid_password_counter_test_cases = [
    (["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc", "2-9 c: cccccccccc"], 2),
    ([], None),
]
part_two_valid_password_counter_test_cases = [
    (["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc", "2-9 c: testc"], 1),
    ([], None),
]


@pytest.mark.parametrize(
    "pwdb_list,expected_result", part_one_valid_password_counter_test_cases
)
def test_part_one_valid_password_counter(pwdb_list, expected_result):
    assert week2.part_one_valid_password_counter(pwdb_list) == expected_result


@pytest.mark.parametrize(
    "pwdb_list,expected_result", part_two_valid_password_counter_test_cases
)
def test_part_two_valid_password_counter(pwdb_list, expected_result):
    assert week2.part_one_valid_password_counter(pwdb_list) == expected_result

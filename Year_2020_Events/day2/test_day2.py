import pytest

from . import day2

part_one_valid_password_counter_test_cases = [
    (["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc", "2-9 c: cccccccccc"], 2),
    ([], 0),
]
part_two_valid_password_counter_test_cases = [
    (
        [
            "1-3 x: a",
            "2-5 x: xaxxb",
            "2-9 x: axcdefghx",
            "2-9 x: abcdefghx",
            "1-3 x: x",
        ],
        2,
    ),
    ([], 0),
]


@pytest.mark.parametrize(
    "pwdb_list,expected_result", part_one_valid_password_counter_test_cases
)
def test_part_one_valid_password_counter(pwdb_list, expected_result):
    assert day2.part_one_valid_password_counter(pwdb_list) == expected_result


@pytest.mark.parametrize(
    "pwdb_list,expected_result", part_two_valid_password_counter_test_cases
)
def test_part_two_valid_password_counter(pwdb_list, expected_result):
    assert day2.part_two_valid_password_counter(pwdb_list) == expected_result

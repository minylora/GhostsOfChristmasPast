import pytest

pwdb_list = [
    '1-3 a: abcde',
    '1-3 b: cdefg',
    '2-9 c: ccccccccc',
    '2-9 c: cccccccccc'
]
valid_password_counter_test_cases = [
    (pwdb_list, 2),
    ([], None)
]


@pytest.mark.parametrize("pwdb_list, expected_result", valid_password_counter_test_cases)
def test_valid_password_counter(pwdb_list, expected_result):
    assert test_valid_password_counter(pwdb_list) == expected_result

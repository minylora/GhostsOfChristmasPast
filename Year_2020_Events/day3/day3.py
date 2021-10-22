import re
from typing import List

from Year_2020_Events.myutils.myutils import get_str_list


# Part 1
def part_one_valid_password_counter(pwdb: List[str]) -> int:
    num_valid_passwords = 0
    for line in pwdb:
        values = re.search(r"(\d+)-(\d+)\s(\w):\s(\w+)", line)
        num_policy_occurances = values.group(4).count(values.group(3))
        if int(values.group(1)) <= num_policy_occurances <= int(values.group(2)):
            num_valid_passwords += 1
    return num_valid_passwords


# Part 2
def part_two_valid_password_counter(pwdb: List[str]) -> int:
    num_valid_passwords = 0
    for line in pwdb:
        values = re.search(r"(\d+)-(\d+)\s(\w):\s(\w+)", line)
        policy_indx_1 = int(values.group(1)) - 1
        policy_indx_2 = int(values.group(2)) - 1
        policy = values.group(3)
        password = values.group(4)
        #
        if len(password) > policy_indx_2:
            if password[policy_indx_1] != password[policy_indx_2] and policy in (
                password[policy_indx_1],
                password[policy_indx_2],
            ):
                num_valid_passwords += 1
        else:
            if policy == password[policy_indx_1]:
                num_valid_passwords += 1
    return num_valid_passwords


def main():
    pwdb_list = get_str_list("input.txt")
    part_one_ans = part_one_valid_password_counter(pwdb_list)
    print(part_one_ans)

    part_two_ans = part_two_valid_password_counter(pwdb_list)
    print(part_two_ans)


if __name__ == "__main__":
    main()

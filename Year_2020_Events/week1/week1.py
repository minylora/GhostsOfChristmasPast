from typing import List
from myutils.myutils import get_int_list


# Part 1 - initial solution
# def find_sum_of_two_and_mult(report: List[int]) -> int:
#     for num in report:
#         diff = 2020 - num
#         if diff in report:
#             return diff * num

# Part 1 - attempt to account for edge case test ([1010, 1], None)
def find_sum_of_two_and_mult(report: List[int]) -> int:
    for i in range(0, len(report)-2):
        diff = 2020 - report[i]
        for j in range(i+1, len(report)-1):
            if report[j] == diff:
                return diff * report[i]


# Part 2 - initial solution
# def find_sum_of_three_and_mult(report: List[int]) -> int:
#     for num1 in report:
#         diff = 2020 - num1
#         for num2 in report:
#             num3 = diff - num2
#             if all(elem in report for elem in [num1, num2, num3]):
#                 return num1*num2*num3

# Part 2 - attempt to account for edge case test ([1010, 505, 1], None)
def find_sum_of_three_and_mult(report: List[int]) -> int:
    for i in range(0, len(report)-3):
        diff = 2020 - report[i]
        for j in range(i+1, len(report)-2):
            num3 = diff - report[j]
            for k in range(j+1, len(report)-1):
                if report[k] == num3:
                    return report[i]*report[j]*num3


def main():
    report = get_int_list('newinput.txt')
    part_one = find_sum_of_two_and_mult(report)
    print(f'Answer to part 1 is {part_one}!')

    part_two = find_sum_of_three_and_mult(report)
    print(f'Answer to part 2 is {part_two}!')


if __name__ == "__main__":
    main()

from typing import List

from Year_2020_Events.myutils.myutils import get_str_list


def get_power_consumption(report: List[str]) -> int:
    max_rows = len(report)
    max_cols = len(report[0])
    sum_report = [0] * max_cols

    for row in report:
        items = [x for x in row]
        for col in range(0, max_cols):
            sum_report[col] += int(items[col])

    gamma = ["1" if x > max_rows / 2 else "0" for x in sum_report]
    epsilon = ["0" if x > max_rows / 2 else "1" for x in sum_report]

    gamma = "0b" + "".join(gamma)
    epsilon = "0b" + "".join(epsilon)

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    return gamma * epsilon


def main():
    report = get_str_list("day3_input.txt")
    part_one = get_power_consumption(report)
    print(part_one)


if __name__ == "__main__":
    main()

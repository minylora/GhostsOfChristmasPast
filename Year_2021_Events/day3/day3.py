from typing import List

from Year_2020_Events.myutils.myutils import get_str_list


def get_report_count_list(report: List[str]) -> List[int]:
    max_cols = len(report[0])
    sum_report = [0] * max_cols
    for row in report:
        items = [x for x in row]
        for col in range(0, max_cols):
            sum_report[col] += int(items[col])
    return sum_report


def get_power_consumption(report: List[str]) -> int:
    max_rows = len(report)
    sum_report = get_report_count_list(report)

    gamma = ["1" if x > max_rows / 2 else "0" for x in sum_report]
    epsilon = ["0" if x > max_rows / 2 else "1" for x in sum_report]

    gamma = "0b" + "".join(gamma)
    epsilon = "0b" + "".join(epsilon)

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    return gamma * epsilon


def get_life_support_rating(report: List[str]) -> int:
    o2 = get_o2_report(0, report)
    co2 = get_co2_report(0, report)
    o2 = "0b" + "".join(o2)
    co2 = "0b" + "".join(co2)
    o2 = int(o2, 2)
    co2 = int(co2, 2)
    return o2 * co2


def get_o2_report(count: int, report: List[str]) -> (int, List[str]):
    if len(report) > 1 and count < len(report[0]):
        max_rows = len(report)
        sum_list = get_report_count_list(report)
        compare_list = ["1" if x >= max_rows / 2 else "0" for x in sum_list]
        keep_list = []
        for i in range(max_rows):
            if report[i][count] == compare_list[count]:
                keep_list.append(i)
        new_report = []
        for r in range(max_rows):
            if r in keep_list:
                new_report.append(report[r])
        count += 1
        return get_o2_report(count, new_report)
    else:
        return report


def get_co2_report(count: int, report: List[str]) -> (int, List[str]):
    if len(report) > 1 and count < len(report[0]):
        max_rows = len(report)
        sum_list = get_report_count_list(report)
        compare_list = ["1" if x >= max_rows / 2 else "0" for x in sum_list]
        keep_list = []
        for i in range(max_rows):
            if report[i][count] != compare_list[count]:
                keep_list.append(i)
        new_report = []
        for r in range(max_rows):
            if r in keep_list:
                new_report.append(report[r])
        count += 1
        return get_co2_report(count, new_report)
    else:
        return report


def main():
    report = get_str_list("day3_input.txt")
    part_one = get_power_consumption(report)
    print(part_one)
    part_two = get_life_support_rating(report)
    print(part_two)


if __name__ == "__main__":
    main()

from typing import List

from Year_2020_Events.myutils.myutils import get_int_list


def get_sliding_window(measurements: List[int]) -> List[int]:
    sliding_window_values = []
    for i in range(0, len(measurements) - 2):
        win = measurements[i] + measurements[i + 1] + measurements[i + 2]
        sliding_window_values.append(win)
    return sliding_window_values


def how_many_are_larger_than_the_previous(measurements: List[int]) -> int:
    count = 0
    for i in range(0, len(measurements) - 1):
        if measurements[i] < measurements[i + 1]:
            count += 1
    return count


def main():
    measurements = get_int_list("day1_input.txt")
    part_one = how_many_are_larger_than_the_previous(measurements)
    print(part_one)
    window = get_sliding_window(measurements)
    part_two = how_many_are_larger_than_the_previous(window)
    print(part_two)


if __name__ == "__main__":
    main()

from typing import List

from Year_2020_Events.myutils.myutils import get_str_list


def get_multiplied_location(course: List[str]) -> int:
    depth = 0
    horizontal = 0
    for change in course:
        change_value = change.split()
        if change_value[0].lower() == "forward":
            horizontal += int(change_value[1])
        elif change_value[0].lower() == "down":
            depth += int(change_value[1])
        else:
            depth -= int(change_value[1])
    return depth*horizontal


def get_multiplied_location_with_aim(course):
    aim = 0
    depth = 0
    horizontal = 0
    for change in course:
        change_value = change.split()
        if change_value[0].lower() == "forward":
            horizontal += int(change_value[1])
            depth += aim*int(change_value[1])
        elif change_value[0].lower() == "down":
            aim += int(change_value[1])
        else:
            aim -= int(change_value[1])
    return depth*horizontal


def main():
    course = get_str_list("day2_input.txt")
    part_one = get_multiplied_location(course)
    print(part_one)
    part_two = get_multiplied_location_with_aim(course)
    print(part_two)


if __name__ == "__main__":
    main()

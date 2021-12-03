from typing import List

from Year_2020_Events.myutils.myutils import get_str_list


def get_change_in_course(change: str) -> (str, int):
    change_value = change.split()
    return change_value[0].lower(), int(change_value[1])


def get_multiplied_location(course: List[str]) -> int:
    depth = 0
    horizontal = 0
    for change in course:
        direction, amount = get_change_in_course(change)
        if direction == "forward":
            horizontal += amount
        elif direction == "down":
            depth += amount
        else:
            depth -= amount
    return depth*horizontal


def get_multiplied_location_with_aim(course):
    aim = 0
    depth = 0
    horizontal = 0
    for change in course:
        direction, amount = get_change_in_course(change)
        if direction == "forward":
            horizontal += amount
            depth += aim*amount
        elif direction == "down":
            aim += amount
        else:
            aim -= amount
    return depth*horizontal


def main():
    course = get_str_list("day2_input.txt")
    part_one = get_multiplied_location(course)
    print(part_one)
    part_two = get_multiplied_location_with_aim(course)
    print(part_two)


if __name__ == "__main__":
    main()

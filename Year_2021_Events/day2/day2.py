from typing import List, Literal

from Year_2020_Events.myutils.myutils import get_str_list


VALID_DIRECTIONS = ["up", "down", "forward"]


def get_course_change(change: str) -> (Literal["up", "down", "forward"], int):
    change_value = change.split(" ", 1)
    direction = change_value[0].lower()
    amount = int(change_value[1])
    if direction not in VALID_DIRECTIONS:
        raise ValueError
    return direction, amount


def get_multiplied_location(course: List[str]) -> int:
    depth = 0
    horizontal = 0
    for change in course:
        direction, amount = get_course_change(change)
        if direction == "forward":
            horizontal += amount
        elif direction == "down":
            depth += amount
        else:
            depth -= amount
    return depth * horizontal


def get_multiplied_location_with_aim(course):
    aim = 0
    depth = 0
    horizontal = 0
    for change in course:
        direction, amount = get_course_change(change)
        if direction == "forward":
            horizontal += amount
            depth += aim * amount
        elif direction == "down":
            aim += amount
        else:
            aim -= amount
    return depth * horizontal


def main():
    course = get_str_list("day2_input.txt")
    part_one = get_multiplied_location(course)
    print(part_one)
    part_two = get_multiplied_location_with_aim(course)
    print(part_two)


if __name__ == "__main__":
    main()

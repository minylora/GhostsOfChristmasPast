from typing import List

from Year_2020_Events.myutils.myutils import get_str_list


OPENINGS = ["(", "[", "{", "<"]
CLOSINGS = [")", "]", "}", ">"]
CLOSING_CHAR = dict(zip(OPENINGS, CLOSINGS))
CLOSINGS_1 = CLOSINGS + [""]
MATHS = [3, 57, 1197, 25137, 0]
BAD_MATH = dict(zip(CLOSINGS, MATHS))
NEW_MATHS = [1, 2, 3, 4]
COMPLETE_MATHS = dict(zip(OPENINGS, NEW_MATHS))


def get_invalid_char(line: str):
    start_i = 0

    while start_i < len(line):
        open_chars = []

        # stop at first closing char
        i = start_i
        no_close = True
        while i < len(line) and no_close:
            if line[i] in CLOSINGS:
                no_close = False
            else:
                open_chars.append(line[i])
            i += 1

        # find first invalid char
        i -= 1
        while i < len(line) and len(open_chars) > 0:
            last_open_char = open_chars[-1]
            if line[i] == CLOSING_CHAR[last_open_char]:
                open_chars.pop()
            elif line[i] in OPENINGS:
                open_chars.append(line[i])
            else:
                return line[i]
            i = i + 1

        # not invalid, just incomplete
        if i == len(line) and len(open_chars) > 0:
            return None

        # end of valid chunk, but more chunks might exist
        start_i = i
    # Not incomplete, or invalid
    return ""


def calculate_chunk_issues(all_lines: List[str]):
    total = 0
    for line in all_lines:
        invalid_char = get_invalid_char(line)
        if invalid_char:
            total += BAD_MATH[invalid_char]
    return total


def calc_part_one(filename: str) -> int:
    the_chunks = get_str_list(filename)
    return calculate_chunk_issues(the_chunks)


def get_incomplete_line_score(line: str):
    start_i = 0
    open_chars = []

    while start_i < len(line):
        i = start_i

        # stop at first closing char
        no_close = True
        while i < len(line) and no_close:
            if line[i] in CLOSINGS:
                no_close = False
            else:
                open_chars.append(line[i])
            i += 1

        i -= 1
        while len(open_chars) > 0 and i < len(line):
            last_open_char = open_chars[-1]

            # its the correct closing char
            if line[i] == CLOSING_CHAR[last_open_char]:
                open_chars.pop()
            # its a new open char
            elif line[i] in OPENINGS:
                open_chars.append(line[i])
            # its invalid
            elif line[i] in CLOSINGS:
                return None
            else:
                raise ValueError
            i += 1
        start_i = i

    # now create the rest and score
    total = 0
    for k in range(len(open_chars)-1, -1, -1):
        char = open_chars[k]
        total = 5 * total + COMPLETE_MATHS[char]

    return total


def calculate_incomplete_issues(all_lines: List[str]):
    total = []
    for line in all_lines:
        score = get_incomplete_line_score(line)
        if score:
            total.append(score)
    total.sort()
    middle = round(len(total)/2)
    return total[middle]


def calc_part_two(filename: str) -> int:
    the_chunks = get_str_list(filename)
    return calculate_incomplete_issues(the_chunks)


def main():
    print(calc_part_one("day10_input.txt"))
    print(calc_part_two("day10_input.txt"))


if __name__ == "__main__":
    main()

import re
from typing import List

from Year_2020_Events.myutils.myutils import get_str_list

LETTERS_LIST = ["a", "b", "c", "d", "e", "f", "g"]
ORIGINAL_LETTERS_PER_NUMBER = {
    "0": ["a", "b", "c", "e", "f", "g"],
    "1": ["c", "f"],
    "2": ["a", "c", "d", "e", "g"],
    "3": ["a", "c", "d", "f", "g"],
    "4": ["b", "c", "d", "f"],
    "5": ["a", "b", "d", "f", "g"],
    "6": ["a", "b", "d", "e", "f", "g"],
    "7": ["a", "c", "f"],
    "8": ["a", "b", "c", "d", "e", "f", "g"],
    "9": ["a", "b", "c", "d", "f", "g"],
}


def get_digits(filename: str) -> (List[List[int]], List[List[int]]):
    str_list = get_str_list(filename)
    pattern = []
    output = []
    for line in str_list:
        values = line.split(" ")
        pattern.append(values[0:10])
        output.append(values[11:15])
    return pattern, output


def part_one(filename: str) -> int:
    pattern, output = get_digits(filename)
    thedigis = [2, 3, 4, 7]
    count = 0
    for values in output:
        for value in values:
            if len(value) in thedigis:
                count += 1
    return count


def get_known_numbers_from_line(pattern_line):
    known = {}
    unknown = []
    for encoded_num in pattern_line:
        length = len(encoded_num)
        if length == 2:
            known["1"] = encoded_num
        elif length == 3:
            known["7"] = encoded_num
        elif length == 4:
            known["4"] = encoded_num
        elif length == 7:
            known["8"] = encoded_num
        else:
            unknown.append(encoded_num)
    return known, unknown


def get_letter_count(pattern_line):
    letter_values = [0] * len(LETTERS_LIST)
    letter_counter = dict(zip(LETTERS_LIST, letter_values))
    for encoded_num in pattern_line:
        for letter in encoded_num:
            letter_counter[letter] += 1
    return letter_counter


def get_letter_code(letter_counter, known):
    letter_code = {}
    one = set(known["1"])
    seven = set(known["7"])
    letter_code["a"] = list(seven - one)[0]

    d_or_g = []
    for letter, count in letter_counter.items():
        if count == 6:
            letter_code["b"] = letter
        elif count == 4:
            letter_code["e"] = letter
        elif count == 9:
            letter_code["f"] = letter
        elif count == 7:
            d_or_g.append(letter)
        elif count == 8 and letter is not letter_code["a"]:
            letter_code["c"] = letter

    for letter in d_or_g:
        nond = [letter_code["b"], letter_code["c"], letter_code["f"]]
        if letter in known["4"] and letter not in nond:
            letter_code["d"] = letter
        else:
            letter_code["g"] = letter
    return letter_code


def get_number_decoder(letter_code):
    decoder = {}
    for number, letters in ORIGINAL_LETTERS_PER_NUMBER.items():
        new_letters = ""
        for letter in letters:
            new_letters = new_letters + letter_code[letter]
        new_letters = sort_output(new_letters)
        decoder[new_letters] = int(number)
    return decoder


def sort_output(output):
    output_list = [i for i in output]
    output_list.sort()
    return "".join(output_list)


def get_output_number(decoder, output_line):
    num_list = []
    for output in output_line:
        sorted = sort_output(output)
        num_list.append(str(decoder[sorted]))
    print(num_list)
    num_str = "".join(num_list)
    print(num_str)
    return int(num_str)


def part_two(filename):
    total = 0
    patterns, outputs = get_digits(filename)
    for pattern, output in zip(patterns, outputs):
        letter_count = get_letter_count(pattern)
        known, unknown = get_known_numbers_from_line(pattern)
        letter_code = get_letter_code(letter_count, known)
        decoder = get_number_decoder(letter_code)
        total += get_output_number(decoder, output)
    return total


def main():
    print(part_one("day8_input.txt"))
    print(part_two("day8_input.txt"))


if __name__ == "__main__":
    main()

import re
from typing import List

from Year_2020_Events.myutils.myutils import get_str_list


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


def generate_regular_number_code() -> dict:
    numbers = {
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
    return numbers


def generate_init_regular_letter_code() -> dict:
    letter_code = {
        "a": None,
        "b": None,
        "c": None,
        "d": None,
        "e": None,
        "f": None,
        "g": None,
        "h": None,
    }
    return letter_code


def decode(pattern: List[List[int]]):
    decoder = generate_init_regular_letter_code()

    # make list instead of string
    weird_letter_code_list = []
    still_dunno_list = []
    code_as_list = []
    new_number_code_list = []
    for line in pattern:
        weird_letter_code = {}
        still_dunno = []
        for code in line:
            code_len = len(code)
            code_list = [i for i in code]
            if code_len == 2:
                weird_letter_code["1"] = code_list
            elif code_len == 3:
                weird_letter_code["7"] = code_list
            elif code_len == 4:
                weird_letter_code["4"] = code_list
            elif code_len == 7:
                weird_letter_code["8"] = code_list
            else:
                still_dunno.append(code_list)
            weird_letter_code_list.append(weird_letter_code)
            still_dunno_list.append(still_dunno)
            code_as_list.append([i for i in code])

        # count how many of each value exists
        all_letters = decoder.keys()
        letter_count = dict(zip(all_letters, [0]*len(all_letters)))
        for code in line:
            for letter in code:
                letter_count[letter] += 1

        # a: 7 has A but 1 does not
        one = set(weird_letter_code["1"])
        seven = set(weird_letter_code["7"])
        decoder["a"] = list(seven - one)

        # b: there are 6 Bs
        for k, v in letter_count:
            if v == 6:
                decoder["b"] = k

        # c: there are 8 Cs, there are 8 As
            elif v == 8 and k is not "a":
                decoder["c"] = k

        # e: there are 4 Es
            elif v == 9:
                decoder["e"] = k

        # f: there are 9 Fs
            elif v == 9:
                decoder["f"] = k

        # d exists in 8 and 4 and is not b
        for k, v in letter_count:
            if v == 7 and k is not decoder["b"] and k in weird_letter_code["4"] and k in weird_letter_code["8"]:
                decoder["d"] = k

        # g is leftover
        for k, v in decoder:
            if not v:
                decoder["g"] = k

        # decoder is done, now build values
        new_number_code = {}
        regular_number_codes = generate_regular_number_code()
        # given decoder and the regular number code - need to create the new number code
        for number, code in regular_number_codes:
            for letter in code:
                new_letter = decoder[letter]
                new_number_code[number].append(new_letter)
            new_number_code[number].sort()
        # list where each item is the new number code for that line
        new_number_code_list.append(new_number_code)
    return new_number_code


def get_decoded_output(new_number_code, output):
    decoded_output = []
    for value in output:
        value_list = [i for i in value]
        value_list.sort()
        decode = []
        for number_code in new_number_code:
            for k, v in number_code:
                if value_list == v:
                    decode.append(k)
    return decoded_output


def get_answer(decoded_output):
    total = 0
    for output in decoded_output:
        string_from_list = []
        for letter in output:
            string_from_list = string_from_list + letter
        total += int(string_from_list)
    return total


def main():
    print(part_one("day8_input.txt"))

    pattern, output = get_digits("day8_input.txt")
    new_num_code = decode(pattern)
    decoded_output = get_decoded_output(new_num_code)
    ans = get_answer(decoded_output)
    print(ans)




if __name__ == "__main__":
    main()

import pytest

from Year_2020_Events.myutils.myutils import get_str_list
from . import day10

mini_chunks_path = r"C:\Users\Mindy\Documents\CodeyCode\GhostsOfChristmasPast\Year_2021_Events\day10\mini_chunks"
mini_chunks = get_str_list(mini_chunks_path)

not_corrupted = [
    "()",
    "[]",
    "{}",
    '<>',
    "(",
    "[",
    "{",
    '<',
]
corrupted = [
    "(]",
    "[}",
    "{>",
    '<)',
    "{([(<{}[<>[]}>{[]{[(<()>",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
]
# incomplete    [(()[<>])]({[<{<<[]>>(
# invalid       {([(<{}[<>[]}>{[]{[(<()>>
# incomplete    (((({<>}<{<{<>}{[]{[]{}
# invalid       [[<[([]))<([[{}[[()]]]]
# invalid    [{[{({}]{}}([{[{{{}}([]
# incomplete    {<[[]]>}<{[{[{[]{()[[[]
# invalid    [<(<(<(<{}))><([]([]()
# invalid    <{([([[(<>()){}]>(<<{{
# incomplete    <{([{{}}[<[[[<>{}]]]>[]]
lines = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "(((({<>}<{<{<>}{[]{[]{}",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "<{([{{}}[<[[[<>{}]]]>[]]",

]
scores = [288957, 5566, 1480781, 995444, 294]


def test_part_one():
    assert day10.calc_part_one(mini_chunks_path) == 26397


def test_get_invalid_char():
    line = "[{[{({}]{}}([{[{{{}}([]"
    results = day10.get_invalid_char(line)
    assert results == "]"


def test_calc_part_two():
    assert day10.calc_part_two(mini_chunks_path) == 288957


@pytest.mark.parametrize("line, score", zip(lines, scores))
def test_get_incomplete_line_score(line, score):
    assert day10.get_incomplete_line_score(line) == score

import pytest
from . import day4


mini_game_path = r"C:\Users\Mindy\Documents\CodeyCode\GhostsOfChristmasPast\Year_2021_Events\day4\mini_game"


def test_get_bingo_game():
    drawn_list, bingo_boards = day4.get_bingo_game(mini_game_path)
    assert len(drawn_list) == 27
    assert len(bingo_boards) == 25
    assert len(bingo_boards[0]) == 5


def test_update_bingo_board_match():
    drawn_list, bingo_boards = day4.get_bingo_game(mini_game_path)
    bingo_board = bingo_boards[0:5]
    updated_board = day4.update_bingo_board(9, bingo_board)
    assert updated_board[0] == bingo_board[0]
    assert updated_board[1] == bingo_board[1]
    assert updated_board[2][1] is None
    assert updated_board[3] == bingo_board[3]
    assert updated_board[4] == bingo_board[4]


def test_update_bingo_board_no_match():
    drawn_list, bingo_boards = day4.get_bingo_game(mini_game_path)
    bingo_board = bingo_boards[0:5]
    updated_board = day4.update_bingo_board(99, bingo_board)
    assert updated_board[0] == bingo_board[0]
    assert updated_board[1] == bingo_board[1]
    assert updated_board[2] == bingo_board[2]
    assert updated_board[3] == bingo_board[3]
    assert updated_board[4] == bingo_board[4]


def test_update_all_bingo_boards_match():
    drawn_list, bingo_boards = day4.get_bingo_game(mini_game_path)
    all_updated_boards = day4.update_all_bingo_boards(9, bingo_boards)
    assert len(all_updated_boards) == len(bingo_boards)
    assert len(all_updated_boards[0]) == len(bingo_boards[0])
    assert all_updated_boards[2][1] is None
    assert all_updated_boards[6][0] is None
    assert all_updated_boards[11][3] is None


def test_update_all_bingo_boards_no_match():
    drawn_list, bingo_boards = day4.get_bingo_game(mini_game_path)
    updated_boards = day4.update_all_bingo_boards(99, bingo_boards)
    assert updated_boards == bingo_boards


def test_board_is_a_winner_horizontal():
    drawn_list, bingo_boards = day4.get_bingo_game(mini_game_path)
    bingo_board = bingo_boards[15:20]
    for i in range(0, 5):
        bingo_board = day4.update_bingo_board(9, bingo_board)
    assert day4.board_is_a_winner(bingo_board)


def test_board_is_a_winner_vertical():
    drawn_list, bingo_boards = day4.get_bingo_game(mini_game_path)
    bingo_board = bingo_boards[20:25]
    for i in range(0, 5):
        bingo_board = day4.update_bingo_board(8, bingo_board)
    assert day4.board_is_a_winner(bingo_board)


def test_board_is_a_winner_false():
    drawn_list, bingo_boards = day4.get_bingo_game(mini_game_path)
    bingo_board = bingo_boards[0:5]
    for i in range(0, 5):
        bingo_board = day4.update_bingo_board(9, bingo_board)
    assert not day4.board_is_a_winner(bingo_board)


def test_get_winning_board():
    drawn_list, bingo_boards = day4.get_bingo_game(mini_game_path)
    bingo_board = bingo_boards[15:20]
    for i in range(0, 5):
        bingo_board = day4.update_bingo_board(9, bingo_board)
    winner, loc = day4.get_winning_board(bingo_board)
    assert winner == bingo_board
    assert loc == 0


def test_calculate_part_one_answer():
    drawn_list, bingo_boards = day4.get_bingo_game(mini_game_path)
    assert day4.calculate_part_one_answer(drawn_list, bingo_boards) == 4512


def test_calculate_part_two_answer():
    draws, games = day4.get_bingo_game(mini_game_path)
    assert day4.calculate_part_two_answer(draws, games) == 1924

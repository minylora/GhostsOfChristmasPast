from typing import List, Optional
import copy

from Year_2020_Events.myutils.myutils import get_str_list


def get_bingo_game(filename: str) -> (List[int], List[List[int]]):
    f = open(filename, "r")
    drawn_numbers = f.readline().split(",")
    board_numbers = f.read().split()
    f.close()

    # create list of drawn numbers
    drawn_numbers = [int(i) for i in drawn_numbers]

    # create the bingo board
    bingo_boards = []
    board_numbers = [int(i) for i in board_numbers]
    cols = range(0, len(board_numbers), 5)
    for col in cols:
        bingo_boards.append(board_numbers[col : col + 5])
    return drawn_numbers, bingo_boards


def update_bingo_board(
    drawn_number: int, bingo_board: List[List[int]]
) -> List[List[int]]:
    new_bingo_board = copy.deepcopy(bingo_board)
    if len(bingo_board) != 5 or len(bingo_board[0]) != 5:
        raise TypeError
    five = range(0, 5)
    for row in five:
        for col in five:
            if bingo_board[row][col] == drawn_number:
                new_bingo_board[row][col] = None
                return new_bingo_board
    return new_bingo_board


def update_all_bingo_boards(
    drawn_number: int, all_bingo_boards: List[List[int]]
) -> List[List[int]]:
    boards = copy.deepcopy(all_bingo_boards)
    all_updated_bingo_boards = []
    for row in range(0, len(boards), 5):
        bingo_board = boards[row : row + 5]
        updated_board = update_bingo_board(drawn_number, bingo_board)
        all_updated_bingo_boards = all_updated_bingo_boards + updated_board
    return all_updated_bingo_boards


def board_is_a_winner(bingo_board: List[List[int]]) -> bool:
    if len(bingo_board) != 5 or len(bingo_board[0]) != 5:
        raise TypeError
    # horizontal check
    for row in bingo_board:
        if row.count(None) == 5:
            return True
    # vertical check
    five = range(0, 5)
    for col in five:
        none_count = 0
        for row in five:
            if bingo_board[row][col] is None:
                none_count += 1
        if none_count == 5:
            return True
    return False


def get_winning_board(all_bingo_boards: List[List[int]]) -> (List[List[int]], int):
    boards = copy.deepcopy(all_bingo_boards)
    for row in range(0, len(boards), 5):
        bingo_board = boards[row : row + 5]
        if board_is_a_winner(bingo_board):
            return bingo_board, row
    return [], 0


def calculate_part_one_answer(
    drawn_nums: List[int], all_boards: List[List[int]]
) -> int:
    game_boards = copy.deepcopy(all_boards)
    for draw in drawn_nums:
        game_boards = update_all_bingo_boards(draw, game_boards)
        winner, loc = get_winning_board(game_boards)
        if len(winner) > 0:
            total = 0
            for row in winner:
                row_vals = [x for x in row if x is not None]
                total += sum(row_vals)
            break
    return draw * total


def calculate_part_two_answer(
    drawn_nums: List[int], all_boards: List[List[int]]
) -> int:
    game_boards = copy.deepcopy(all_boards)
    multiplier = 0
    sum_multiplier = 0
    for draw in drawn_nums:
        game_boards = update_all_bingo_boards(draw, game_boards)
        winner, loc = get_winning_board(game_boards)
        if len(winner) > 0:
            game_boards = game_boards[:loc] + game_boards[loc + 5 :]
        if len(game_boards) == 5:
            total = 0
            for row in game_boards:
                row_vals = [x for x in row if x is not None]
                total += sum(row_vals)
            multiplier = draw
            sum_multiplier = total
            print(multiplier)
            print(sum_multiplier)
            break
    return multiplier * sum_multiplier


def main():
    drawn_nums, all_boards = get_bingo_game("day4_input.txt")
    part_one = calculate_part_one_answer(drawn_nums, all_boards)
    print(part_one)
    drawn_nums, all_boards = get_bingo_game("day4_input.txt")
    part_two = calculate_part_two_answer(drawn_nums, all_boards)
    print(part_two)


if __name__ == "__main__":
    main()

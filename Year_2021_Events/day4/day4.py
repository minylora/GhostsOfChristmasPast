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

    # create the bingo boards
    bingo_boards = []
    board_numbers = [int(i) for i in board_numbers]
    cols = range(0, len(board_numbers), 5)
    for col in cols:
        bingo_boards.append(board_numbers[col : col + 5])
    return drawn_numbers, bingo_boards


def update_bingo_board(
    drawn_number: int, bingo_board: List[List[int]]
) -> List[List[int]]:
    if len(bingo_board) != 5 or len(bingo_board[0]) != 5:
        raise TypeError

    new_bingo_board = copy.deepcopy(bingo_board)
    five = range(0, 5)
    # Check every value for the drawn number
    for row in five:
        for col in five:
            # if the drawn number exists, change the value to None, and exit
            if bingo_board[row][col] == drawn_number:
                new_bingo_board[row][col] = None
                return new_bingo_board
    return new_bingo_board


def update_all_bingo_boards(
    drawn_number: int, all_bingo_boards: List[List[int]]
) -> List[List[int]]:
    all_updated_bingo_boards = []
    for row in range(0, len(all_bingo_boards), 5):
        bingo_board = all_bingo_boards[row : row + 5]
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
    for row in range(0, len(all_bingo_boards), 5):
        bingo_board = all_bingo_boards[row : row + 5]
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
) -> Optional[int]:

    game_boards = copy.deepcopy(all_boards)

    # Run through the game in order of the draws list
    for draw in drawn_nums:

        # Update all the boards
        game_boards = update_all_bingo_boards(draw, game_boards)

        # Check if there is a winner
        winner, loc = get_winning_board(game_boards)

        # Check if only one board remains
        if len(winner) > 0 and len(game_boards) == 5:
            # calculate sum of values that exist
            total = 0
            for row in game_boards:
                # drop all nulls
                row_vals = [x for x in row if x is not None]
                # add sum to current sum
                total += sum(row_vals)
                print(game_boards)
            # return multiplied values
            return draw * total

        # If there is winner, remove it from board choices
        # Keep removing winners from the current draw until there are none
        # Assume there is a single last board that is the last win
        while len(winner) > 0:
            # Remove the winning board
            game_boards = game_boards[:loc] + game_boards[loc + 5:]
            # Check if winners still remain
            winner, loc = get_winning_board(game_boards)
    return None


def main():
    # drawn_nums, all_boards = get_bingo_game("day4_input.txt")
    # part_one = calculate_part_one_answer(drawn_nums, all_boards)
    # print(part_one)
    drawn_nums, all_boards = get_bingo_game("day4_input_2.txt")
    part_two = calculate_part_two_answer(drawn_nums, all_boards)
    print(part_two)


if __name__ == "__main__":
    main()

from typing import List, Optional

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
        bingo_boards.append(board_numbers[col:col+5])
    return drawn_numbers, bingo_boards


def update_bingo_board(drawn_number: int, bingo_board: List[List[int]]) -> List[List[int]]:
    if len(bingo_board) != 5 or len(bingo_board[0]) != 5:
        raise TypeError
    five = range(0, 5)
    for row in five:
        for col in five:
            if bingo_board[row][col] == drawn_number:
                bingo_board[row][col] = None
                return bingo_board
    return bingo_board


def update_all_bingo_boards(drawn_number: int, all_bingo_boards: List[List[int]]) -> List[List[int]]:
    all_updated_bingo_boards = []
    for row in range(0, len(all_bingo_boards), 5):
        bingo_board = all_bingo_boards[row:row+5]
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
    five = range(0,5)
    for col in five:
        none_count = 0
        for row in five:
            if bingo_board[row][col] is None:
                none_count += 1
        if none_count == 5:
            return True
    return False


def get_winning_board(all_bingo_boards: List[List[int]]) -> Optional[List[List[int]]]:
    for row in range(0, len(all_bingo_boards), 5):
        bingo_board = all_bingo_boards[row:row + 5]
        if board_is_a_winner(bingo_board):
            return bingo_board
    return None


def main():
    drawn_nums, boards = get_bingo_game("day4_input.txt")
    for draw in drawn_nums:
        boards = update_all_bingo_boards(boards)
        if get_winning_board(boards):
            print(get_winning_board(boards))


if __name__ == "__main__":
    main()

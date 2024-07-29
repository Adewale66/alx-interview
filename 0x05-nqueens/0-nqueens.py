#!/usr/bin/python3
"""n queens
"""

import sys


def checkCol(row, col, board):
    """checks column

    Args:
        row (int): row pos
        col (int): col position
        board (List[List[int]]): board

    Returns:
        bool: true if not possible else false
    """
    for i in range(row):
        if board[i][col] == 1:
            return True
    return False


def checkDig(row, col, board):
    """checks diagonal

    Args:
        row (int): row pos
        col (int): col position
        board (List[List[int]]): board
    Returns:
        bool: true if not possible else false
    """
    n = len(board)

    left_check = col - row
    for i in range(row):
        if 0 <= i + left_check < n:
            if board[i][i + left_check] == 1:
                return True

    right_check = row + col
    for i in range(row):
        if 0 <= right_check - i < n:
            if board[i][right_check - i] == 1:
                return True

    return False


def get_board(board):
    """gets the solved board

    Args:
        board (List[List[int]]): board

    Returns:
        ListList[int]: solved board
    """
    board_pos = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                board_pos.append([i, j])
    return board_pos


def solve(queen_count):
    """n queens algorithm

    Args:
        queen_count (int): number of queens

    Returns:
        List[List[int]]: list of boards
    """
    board = [[0 for _ in range(queen_count)] for _ in range(queen_count)]
    ans = []

    def nqueen(row):
        if (row == queen_count):
            result = get_board(board)
            ans.append(result)
            return

        for i in range(queen_count):
            if (not checkCol(row, i, board) and not checkDig(row, i, board)):
                board[row][i] = 1
                nqueen(row+1)
                board[row][i] = 0
    nqueen(0)
    return ans


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        count = int(sys.argv[1])
        if count < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueen = solve(count)
        for i in nqueen:
            print(i)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

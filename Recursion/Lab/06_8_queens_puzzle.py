def print_board(board):
    for r in board:
        print(' '.join(r))
    print()


def can_place_queen(r, c, rows, cols, left_diagonals, right_diagonals):
    if r in rows:
        return False
    if c in cols:
        return False
    if r - c in left_diagonals:
        return False
    if r + c in right_diagonals:
        return False

    return True


def set_queen(r, c, board, rows, cols, left_diagonals, right_diagonals):
    board[r][c] = "*"
    rows.add(r)
    cols.add(c)
    left_diagonals.add(r - c)
    right_diagonals.add(r + c)


def remove_queen(r, c, board, rows, cols, left_diagonals, right_diagonals):
    board[r][c] = "-"
    rows.remove(r)
    cols.remove(c)
    left_diagonals.remove(r - c)
    right_diagonals.remove(r + c)


def put_queens(row, board, rows, cols, left_diagonals, right_diagonals):
    if row == 8:
        print_board(board)
        return

    for col in range(8):
        if can_place_queen(row, col, rows, cols, left_diagonals, right_diagonals):
            set_queen(row, col, board, rows, cols, left_diagonals, right_diagonals)
            put_queens(row + 1, board, rows, cols, left_diagonals, right_diagonals)
            remove_queen(row, col, board, rows, cols, left_diagonals, right_diagonals)


n = 8
board = []
[board.append(['-'] * 8) for _ in range(n)]

put_queens(0, board, set(), set(), set(), set())

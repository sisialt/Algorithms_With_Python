# def move(r, c, board, paths):
#     if not 0 <= r < m or not 0 <= c < n:
#         return
#
#     if r == m - 1 and c == n - 1:
#         paths.append(1)
#         return
#
#     move(r + 1, c, board, paths)
#     move(r, c + 1, board, paths)
#
#
# m = int(input())
# n = int(input())
#
# board = []
# paths = []
#
# for _ in range(m):
#     board.append([""] * n)
#
# move(0, 0, board, paths)
# print(len(paths))
#

def count_all_paths(row, col, rows, cols):
    if row >= rows or col >= cols:
        return 0
    if row == rows - 1 and col == cols - 1:
        return 1

    result = 0
    result += count_all_paths(row, col + 1, rows, cols)
    result += count_all_paths(row + 1, col, rows, cols)

    return result


rows = int(input())
cols = int(input())

print(count_all_paths(0, 0, rows, cols))

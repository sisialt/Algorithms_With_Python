class Area:
    def __init__(self, row, col, size):
        self.row = row
        self.size = size
        self.col = col


def explore_area(row, col, matrix):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return 0

    if matrix[row][col] != "-":
        return 0

    matrix[row][col] = "v"

    result = 1
    result += explore_area(row - 1, col, matrix)
    result += explore_area(row + 1, col, matrix)
    result += explore_area(row, col + 1, matrix)
    result += explore_area(row, col - 1, matrix)

    return result


rows = int(input())
cols = int(input())

matrix = []
for _ in range(rows):
    matrix.append(list(input()))

areas = []

for row in range(rows):
    for col in range(cols):
        size = explore_area(row, col, matrix)

        if size == 0:
            continue

        areas.append(Area(row, col, size))

print(f"Total areas found: {len(areas)}")

for i, area in enumerate(sorted(areas, key=lambda a: a.size, reverse=True)):
    print(f"Area #{i + 1} at ({area.row}, {area.col}), size: {area.size}")

# def find_area(r, c, field, area_found):
#     if not 0 <= r < rows or not 0 <= c < cols:
#         return
#
#     if field[r][c] == "*" or field[r][c] == "f":
#         return
#
#     field[r][c] = "f"
#     area_found.add((r, c))
#
#     find_area(r + 1, c, field, area_found)
#     find_area(r, c + 1, field, area_found)
#
#
# def find_areas(r, c, field, area_found, all_areas):
#     find_area(r, c, field, area_found)
#
#     all_areas.append(area_found)
#
#     for position in area_found:
#         field[position[0]].pop(position[1])
#
#     find_areas(0, 0, field, set(), all_areas)
#
#
# rows = int(input())
# cols = int(input())
#
# board = []
#
# for _ in range(rows):
#     board.append(list(input()))
#
# find_areas(0, 0, board, set(), [])
#
#
#
# # 4
# # 9
# # ---*---*-
# # ---*---*-
# # ---*---*-
# # ----*-*--

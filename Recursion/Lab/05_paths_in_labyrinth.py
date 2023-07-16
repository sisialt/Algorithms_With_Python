def find_paths(r, c, labyrinth, path, dir):
    if not 0 <= r < len(labyrinth) or not 0 <= c < len(labyrinth[0]):
        return

    if labyrinth[r][c] == "*":
        return

    if labyrinth[r][c] == "v":
        return

    path.append(dir)

    if labyrinth[r][c] == "e":
        print(''.join(path))
        path.pop()
        return

    labyrinth[r][c] = "v"

    find_paths(r + 1, c, labyrinth, path, "D")
    find_paths(r - 1, c, labyrinth, path, "U")
    find_paths(r, c + 1, labyrinth, path, "R")
    find_paths(r, c - 1, labyrinth, path, "L")

    labyrinth[r][c] = "-"
    path.pop()


rows = int(input())
cols = int(input())

labyrinth = []

for r in range(rows):
    labyrinth.append(list(input()))

find_paths(0, 0, labyrinth, [], '')

# 3
# 3
# ---
# -*-
# --e

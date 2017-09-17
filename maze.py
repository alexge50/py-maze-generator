import random
from collections import namedtuple


def generate_maze(w, h, seed):
    cell = namedtuple("cell", "x y wallE wallS")

    def get_neighbors(current_cell, w, h, visited):
        xdir = [0, 0, -1, +1]
        ydir = [-1, +1, 0, 0]

        neighbors = []

        for i in range(0, 4):
            x = current_cell.x + xdir[i]
            y = current_cell.y + ydir[i]
            if (0 <= x < w and 0 <= y < h) and visited[y][x] == 0:
                neighbors.append(cell(x, y, 1, 1))

        return neighbors

    maze = [[cell(0, 0, 1, 1) for x in range(0, w)] for y in range(0, h)]
    visited = [[0 for x in range(0, w)] for y in range(0, h)]
    stack = []

    random.seed(seed)
    current_cell = cell(random.randint(0, w), random.randint(0, h), 1, 1)
    visited[current_cell.y][current_cell.x] = 1
    stack.append(current_cell)

    while len(stack) > 0:
        neighbors = get_neighbors(current_cell, w, h, visited)

        if len(neighbors) != 0:
            neighbor = neighbors[random.randint(0, len(neighbors) - 1)]
            stack.append(current_cell)

            # remove the wall
            min_cell = cell(min(current_cell.x, neighbor.x), min(current_cell.y, neighbor.y), 1, 1)
            max_cell = cell(max(current_cell.x, neighbor.x), max(current_cell.y, neighbor.y), 1, 1)

            if max_cell.x - min_cell.x == 0:
                maze[min_cell.y][min_cell.x] = cell(min_cell.x, min_cell.y, maze[min_cell.y][min_cell.x].wallE, 0)
            elif max_cell.y - min_cell.y == 0:
                maze[min_cell.y][min_cell.x] = cell(min_cell.x, min_cell.y, 0, maze[min_cell.y][min_cell.x].wallS)

            current_cell = neighbor
            visited[current_cell.y][current_cell.x] = 1
        elif len(stack) > 0:
            current_cell = stack.pop()

    return maze, w, h
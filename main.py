import random
from collections import namedtuple

cell = namedtuple("cell", "x y wallE wallS")


def get_neighbors(current_cell, w, h, visited):
    xdir = [0, 0, -1, +1]
    ydir = [-1, +1, 0, 0]

    neighbors = []

    for i in range(0, 4):
        x = current_cell.x + xdir[i]
        y = current_cell.y + ydir[i]
        if 0 <= x < w and 0 <= y < h and visited[y][x] == 0:
            neighbors.append(cell(x, y, 1, 1))

    return neighbors


def generate_maze(w, h, seed):
    maze = [[cell(0, 0, 1, 1) for x in range(0, w)] for y in range(0, h)]
    visited = [[0 for x in range(0, w)] for y in range(0, h)]
    stack = []

    number_cells_to_visit = w * h

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


def print_maze(maze, w, h):

    wall = '█'
    empty = ' '

    maze_displayable = [[empty for x in range(2 * w + 1)] for y in range(2 * h + 1)]

    for x in range(0, 2 * w + 1):
        maze_displayable[0][x] = wall
    for y in range(0, 2 * h + 1):
        maze_displayable[y][0] = wall

    for y in range(0, h):
        for x in range(0, w):
            maze_displayable[2 * y + 1][2 * x + 1] = empty

            if maze[y][x].wallS == 1:
                maze_displayable[2 * y + 2][2 * x + 1] = wall
                maze_displayable[2 * y + 2][2 * x + 2] = wall
            if maze[y][x].wallE == 1:
                maze_displayable[2 * y + 1][2 * x + 2] = wall
                maze_displayable[2 * y + 2][2 * x + 2] = wall

    for y in maze_displayable:
        string = ""
        for x in y:
            string = string + x
        print("{}".format(string))


maze, w, h = generate_maze(10, 10, 100)

print_maze(maze, w, h)

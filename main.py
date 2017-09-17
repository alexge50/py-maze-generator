import maze


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


maze, w, h = maze.generate_maze(20, 20, 150)

print_maze(maze, w, h)

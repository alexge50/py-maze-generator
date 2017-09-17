import maze
import curses

import sys, getopt


def print_maze(stdscr, maze, w, h):
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

    line = 0

    for y in maze_displayable:
        string = ""
        for x in y:
            string = string + x
        stdscr.addstr(line, 0, string, curses.color_pair(1))
        line = line + 1


seed = None


def main(stdscr):
    y, x = stdscr.getmaxyx()

    global seed

    if seed is None:
        seed = 10

    _maze, w, h = maze.generate_maze(int((x - 1) / 2), int((y - 1) / 2), 150)

    curses.flash()
    stdscr.scrollok(True)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)

    print_maze(stdscr, _maze, w, h)
    stdscr.refresh()

    stdscr.addstr(y - 1, 0, "seed: {}".format(seed), curses.color_pair(0))

    exit_flag = 0
    while exit_flag == 0:
        if stdscr.getkey() == 'q':
            exit_flag = 1


try:
    opts, args = getopt.getopt(sys.argv, "s:", ["seed="])
except getopt.GetoptError:
    print("main.py -s <number>")
    sys.exit(2)

for opt, arg in opts:
    if opt in ("-s", "--seed"):
        global seed
        seed = int(args)

curses.wrapper(main)

import maze
import curses
import random

import sys, getopt


def print_maze(stdscr, maze_displayable, w, h, startx, endx, steps):
    line = 0

    for y in maze_displayable:
        string = ""
        for x in y:
            string = string + x
        stdscr.addstr(line, 0, string, curses.color_pair(1))
        line = line + 1

    for step in steps:
        stdscr.addstr(step.y, step.x, " ", curses.color_pair(3))

    stdscr.addstr(1, startx, "S", curses.color_pair(3))
    stdscr.addstr(h - 2, endx, "E", curses.color_pair(4))


seed = None


def main(stdscr):
    y, x = stdscr.getmaxyx()

    global seed

    if seed is None:
        seed = random.SystemRandom().randint(0, sys.maxsize)

    _maze, w, h = maze.generate_maze(int((x - 1) / 2), int((y - 1) / 2), seed)
    _maze, w, h = maze.convert_to_displayable(_maze, w, h, ' ', '█')
    startx, endx = maze.generate_points(_maze, ' ', '█')
    steps = maze.get_solution(_maze, ' ', '█', startx, endx)

    curses.flash()
    stdscr.scrollok(True)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_GREEN)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_RED)

    print_maze(stdscr, _maze, w, h, startx, endx, steps)

    for _x in range(0, x - 1):
        stdscr.addstr(y - 1, _x, " ", curses.color_pair(2))
    stdscr.addstr(y - 1, 0, "seed: {}".format(seed), curses.color_pair(2))

    stdscr.refresh()

    exit_flag = 0
    while exit_flag == 0:
        if stdscr.getkey() == 'q':
            exit_flag = 1


try:
    opts, args = getopt.getopt(sys.argv[1:], "s:", ["seed="])
except getopt.GetoptError:
    print("main.py -s <number>")
    sys.exit(2)

for opt, arg in opts:
    if opt in ("-s", "--seed"):
        global seed
        seed = int(arg)

curses.wrapper(main)

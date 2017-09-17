# py-maze-generator
Generates a maze, as well as its solution. The maze is generated using **recursive backtracker**, and the solution is found using **DFS**  
![alt text](https://github.com/alexge50/py-maze-generator/blob/master/screenshots/3.png?raw=true)

## how to use the script
This script is made for python3, so python3 is required to run it. 
`main.py` is the file that should be run.   
The only argument available is `-s`/`--seed` that takes a number. This option sets the seed to the specified number. By default, the seed is randomly generated

## interacting with it
This script should be run in terminal. The width and height of the maze is are calculated from the size of the terminal.   
In order to exit from the script, the user should press `q`. There isn't any other way to interact with the script.

##bugs  
When the solution is generated, some branches are included as being part of the solution.
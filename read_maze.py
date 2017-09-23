import numpy as np
import mpmath as math
import matplotlib as mpl
import matplotlib.pyplot as plt


def mazeinput (maze,filename):
    mazeFile = open(filename, "r")
    columns = mazeFile.readlines()
    for column in columns:
        column = column.strip()
        row = [i for i in column]
        maze.append(row)

def generate_maze():
    maze =[]
    mazeinput(maze,"openMaze.txt")
    [rows,columns] = np.shape(maze)
    visited = [[0 for x in range(columns)] for y in range(rows)]  # visited = 1 means the place has been visited
    unavaiable = [[0 for x in range(columns)] for y in range(rows)] # unavaible = 1 means there is a wall in that position

    for i in range(rows):
        for j in range(columns):
            if maze[i][j] == '%':
                unavaiable[i][j] = 1
            if maze[i][j] == 'P':
                start = [i,j]
            if maze[i][j] == '.':
                goal = [i,j]
    return maze,visited,unavaiable,start,goal,rows,columns
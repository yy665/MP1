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
    mazeinput(maze,"mediumMaze.txt")

    [rows,columns] = np.shape(maze)
    unavaiable = [[0 for x in range(columns)] for y in range(rows)] # unavaible = 1 means there is a wall in that position
    goal = []
    for i in range(rows):
        for j in range(columns):
            if maze[i][j] == '%':
                unavaiable[i][j] = 1
            if maze[i][j] == 'P':
                start = [i,j]
            if maze[i][j] == '.':
                goal.append([i,j])
    #visited = [[[0 for x in range(2**len(goal))] for y in range(columns)]  for z in range(rows)] # visited = 1 means the place has been visited
    visited = []
    #visited = [[0 for x in range(columns)] for y in range(rows)]
    return maze,visited,unavaiable,start,goal,rows,columns

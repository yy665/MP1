import numpy as np
import mpmath as math
import matplotlib as mpl
import matplotlib.pyplot as plt


def mazeinput (maze,filename):
    mazeFile = open(filename, "r")
    columns = mazeFile.readlines()
    for column in columns:
        column = column.strip()
        print(column)
        row = [i for i in column]
        maze.append(row)

maze =[]
mazeinput(maze,"mediumMaze.txt")

[rows,columns] = np.shape(maze)
visited = [[0 for x in range(columns)] for y in range(rows)]  # visited = 1 means the place has been visited
unavaiable = [[0 for x in range(columns)] for y in range(rows)] # unavaible = 1 means there is a wall in that position

for i in range(rows):
    for j in range(columns):
        if maze[i][j] == '%':
            unavaiable[i][j] = 1
        if maze[i][j] == 'P':
            visited[i][j] = 1
            start = [i,j]
        if maze[i][j] == '.':
            goal = [i,j]

print(visited)
print(start)

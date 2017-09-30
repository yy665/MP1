from collections import deque
from scipy.sparse import csr_matrix
import matplotlib.pyplot as plt
import matplotlib as mpl
import mpmath as math
import read_maze
import Astar4

def BFS():
    queue = []
    queue = deque(queue)
    queue.append(read_maze.start)
    points = len(goals)
    prev = [[[-1, -1] for x in range(2**points)] for y in range(points+1)]  # record all the history
    steps = 0
    everyStep = 0
    collected = '0' * points # collected is a vector that contains which dots have been collected
    path = []

    prevPosition = []


    (csgraph,maze,visited,unavaiable,start,goals,rows,columns) = Astar4.setupGraph()
    row = start[0]
    col = start[1]

    while(len(queue) != 0):
        if unavaiable[row+1][col] == 0 and visited[row+1][col] == 0: #up  no wall and unvisit
            visited[row+1][col] = 1
            prevPosition.append(queue.front())
            if [row+1, col] == goal:
                everyStep += 1
                printPath(prevPosition)
                print("Number of nodes expanded by the search algorithm is " + everyStep)
            queue.append([row+1,col])
        if unavaiable[row][col+1] == 0 and visited[row][col+1] == 0: #right
            visited[row][col+1] = 1
            prevPosition.append(queue.front())

            if [row, col+1] == goal:
                everyStep += 1
                printPath(prevPosition)
                print("Number of nodes expanded by the search algorithm is " + everyStep)

            queue.append([row
            ,col+1])
        if unavaiable[row-1][col] == 0 and visited[row-1][col] == 0: #down
            visited[row-1][col] = 1
            prevPosition.append(queue.front())

            if [row-1, col] == goal:
                everyStep += 1
                printPath(prevPosition)
                print("Number of nodes expanded by the search algorithm is " + everyStep)

            queue.append([row-1,col])
        if unavaiable[row][col-1] == 0 and visited[row][col-1] == 0: #left
            visited[row][col-1] = 1
            prevPosition.append(queue.front())

            if [row, col-1] == goal:
                everyStep += 1
                printPath(prevPosition)
                print("Number of nodes expanded by the search algorithm is " + everyStep)

            queue.append([row,col-1])

        queue.pop()
        everyStep += 1

def DFS():
    stack = []
    stack.append(read_maze.start)
    steps = 0
    expand = 0
    row = read_maze.start[0]
    col = read_maze.start[1]
    prevPosition = []
    unavaiable = read_maze.unavaiable
    visited = read_maze.visited

    while(len(stack) != 0):

        queue.pop()

        if unavaiable[row+1][col] == 0 and visited[row+1][col] == 0: #up  no wall and unvisit
            visited[row+1][col] = 1
            prevPosition.append(queue.front())

            if [row+1, col] == goal:
                everyStep += 1
                printPath(prevPosition)
                print("Number of nodes expanded by the search algorithm is " + everyStep)

            queue.append([row+1,col])
        if unavaiable[row][col+1] == 0 and visited[row][col+1] == 0: #right
            visited[row][col+1] = 1
            prevPosition.append(queue.front())

            if [row, col+1] == goal:
                everyStep += 1
                printPath(prevPosition)
                print("Number of nodes expanded by the search algorithm is " + everyStep)

            queue.append([row,col+1])
        if unavaiable[row-1][col] == 0 and visited[row-1][col] == 0: #down
            visited[row-1][col] = 1
            prevPosition.append(queue.front())

            if [row-1, col] == goal:
                everyStep += 1
                printPath(prevPosition)
                print("Number of nodes expanded by the search algorithm is " + everyStep)

            queue.append([row-1,col])
        if unavaiable[row][col-1] == 0 and visited[row][col-1] == 0: #left
            visited[row][col-1] = 1
            prevPosition.append(queue.front())

            if [row, col-1] == goal:
                everyStep += 1
                printPath(prevPosition)
                print("Number of nodes expanded by the search algorithm is " + everyStep)

            queue.append([row,col-1])

        everyStep += 1

def printPath(prevPosition):
    correctSteps = 0
    print("The solution is ")
    for i in range(len(read_maze.maze)):
        for j in range(len(read_maze.maze[0])):
            if [i,j] in prevPosition:
                print(".", end="")
                correctSteps += 1
            else:
                print(maze[i][j], end="")
        print("\n")
    print("The path cost of the solution is " + correctSteps)


if __name__== "__main__":
  main()

def main():
    while(True):
        In = input("DFS or BFS?")
        if In == "DFS":
            DFS()
            break
        elif In == "BFS":
            BFS()
            break

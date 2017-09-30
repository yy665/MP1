from collections import deque
from scipy.sparse import csr_matrix
import matplotlib.pyplot as plt
import matplotlib as mpl
import mpmath as math
import read_maze
import Astar3

def BFS():
    queue = []
    queue = deque(queue)
    maze,visited,unavaiable,start,goals,rows,columns = read_maze.generate_maze()
    points = len(goals)
    prev = [[[[-1, -1, -1] for x in range(2**points)] for y in range(columns)]  for z in range(rows)] # record all the history
    collected = '0' * points # collected is a vector that contains which dots have been collected
    collected_int = int(collected,2) # collected_int is the index of what the 3rd dimension value is
    goal = goals[0]
    path = []
    steps = 1
    expanded = 0
    mincost = [[[9999999 for x in range(2**points)] for y in range(columns)] for z in range(rows)]
    row = start[0]
    col = start[1]
    node_now = [start[0], start[1], None, steps, collected]
    queue.append(node_now)
    while(len(queue) != 0):
        node_now = queue.popleft()
        x = node_now[0]
        y = node_now[1]
        steps = node_now[3]
        collected = node_now[4]
        collected_int = int(collected,2)
        goal_here = copy.deepcopy(goals)
        for i in range(points):
            if collected[i] == '1':
                goal_here[i] = [-2,-2]
        if ([x,y] in goal_here):
            i = goal_here.index([x,y])
            collected[i] = '1'
        if collected == '1'*points:
            print("solution found")
            print(expanded)
            pos_now = [x,y]

            while ([pos_now,collected_int] != [start,0] ):
                path.append(pos_now)
                (pos_now,collected_int) = ([prev[pos_now[0]][pos_now[1]][collected_int][0],prev[pos_now[0]][pos_now[1]][collected_int][1]], prev[pos_now[0]][pos_now[1]][collected_int][2])
                #print(pos_now)
                maze[pos_now[0]][pos_now[1]] = '.'
            maze[start[0]][start[1]] = "P"
            path.reverse()
            print(path)
            length = len(path)
            print("Total length of the path is " + str(length))
            print("Number of expanded nodes is " + str(expanded))
            # write it
            with open('test_file.csv', 'w') as csvfile:
                writer = csv.writer(csvfile)
                for r in maze:
                    r = ''.join(str(word) for word in r)
                    print(r)
                    writer.writerow(r)
            return

        if unavaiable[row+1][col] == 0: #up  no wall and unvisit
            visited[row+1][col] = 1
            prevPosition.append(queue.front())
            if [row+1, col] == goal:
                everyStep += 1
                printPath(prevPosition)
                print("Number of nodes expanded by the search algorithm is " + everyStep)
            queue.append([row+1,col])

        if unavaiable[row][col+1] == 0: #right
            visited[row][col+1] = 1
            prevPosition.append(queue.front())
            if [row, col+1] == goal:
                everyStep += 1
                printPath(prevPosition)
                print("Number of nodes expanded by the search algorithm is " + everyStep)
            queue.append([row,col+1])

        if unavaiable[row-1][col] == 0: #down
            visited[row-1][col] = 1
            prevPosition.append(queue.front())
            if [row-1, col] == goal:
                everyStep += 1
                printPath(prevPosition)
                print("Number of nodes expanded by the search algorithm is " + everyStep)
            queue.append([row-1,col])

        if unavaiable[row][col-1] == 0: #left
            visited[row][col-1] = 1
            prevPosition.append(queue.front())
            if [row, col-1] == goal:
                everyStep += 1
                printPath(prevPosition)
                print("Number of nodes expanded by the search algorithm is " + everyStep)
            queue.append([row,col-1])

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

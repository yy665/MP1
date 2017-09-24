import numpy as np
import mpmath as math
import matplotlib as mpl
import matplotlib.pyplot as plt
from collections import deque
import csv



# direction definition:
# 0: left 1: right 2: up 3: down

def heuristic(x,y):
    return(abs(y[0] - x[0]) + abs(y[1]-x[1]))
    #return ((y[0] - x[0])**2 + (y[1] - x[1])**2)


def Greedy():
    import read_maze
    maze,visited,unavaiable,start,goal,rows,columns = read_maze.generate_maze()
    print(start,goal)
    prev = [[[-1,-1] for x in range(columns)] for y in range(rows)]  # record all the history
    path = []
    queue = [start]
    queue = deque(queue)
    frontier = []
    steps = 0
    while(len(queue)!=0):
        node_now = queue.popleft()
        x = node_now[0]
        y = node_now[1]
        unavaiable[x][y] = 1
        if (x == goal[0] and y == goal[1]):
            print("solution found")
            pos_now = goal
            while (pos_now!=start):
                path.append(pos_now)

                pos_now = prev[pos_now[0]][pos_now[1]]
                maze[pos_now[0]][pos_now[1]] = '.'
            maze[start[0]][start[1]] = "P"
            path.reverse()
            print(path)
            length = len(path)
            print("Total length of the path is " + str(length))
            print("Number of expanded nodes is " + str(steps))
            # write it
            with open('test_file.csv', 'w') as csvfile:
                writer = csv.writer(csvfile)
                for r in maze:
                    r = ''.join(str(word) for word in r)
                    print(r)
                    writer.writerow(r)
            return
        # loop over all possible nodes
        if (unavaiable[x+1][y] == 0 and visited[x+1][y] == 0): # right
            heu = heuristic([x+1,y],goal)
            frontier.append([x+1,y,heu])
            prev[x+1][y] = [x, y]
        if (unavaiable[x-1][y] == 0 and visited[x-1][y] == 0): # left
            heu = heuristic([x-1,y],goal)
            frontier.append([x-1,y,heu])
            prev[x-1][y] = [x, y]
        if (unavaiable[x][y-1] == 0 and visited[x][y-1] == 0): # down
            heu = heuristic([x,y-1],goal)
            frontier.append([x,y-1,heu])
            prev[x][y-1] = [x, y]
        if (unavaiable[x][y+1] == 0 and visited[x][y+1] == 0): # up
            heu = heuristic([x,y+1],goal)
            frontier.append([x,y+1,heu])
            prev[x][y+1] = [x, y]

        expand = min(frontier, key = lambda t: t[2])
        queue.append(expand)
        frontier.remove(expand)
        steps += 1

def main():
    Greedy()

if __name__ == "__main__":
    main()

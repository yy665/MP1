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
 #   goal = goal[0]
    print(start,goal)
    prev = [start]  # record all the history
    expanded = 0
    heu_start = heuristic(start,goal)
    mincost = [[9999999 for x in range(columns)] for y in range(rows)]
    frontier = [[start[0],start[1],heu_start,prev]]
    while(len(frontier)!=0):
        steps = len(prev)
        node_now = min(frontier, key=lambda t: t[2])
        frontier.remove(node_now)
        x = node_now[0]
        y = node_now[1]
        prev = node_now[3]
        visited[x][y] = 1
        if (x == goal[0] and y == goal[1]):
            print("solution found")

            print(prev)
            length = len(prev)
            print("Total length of the path is " + str(length))
            print("Number of expanded nodes is " + str(expanded))
            # write it
            for i in range(rows):
                for j in range(columns):
                    if [i,j] in prev:
                        print(".", end="")
                    else:
                        print(maze[i][j], end="")
                print("\n",end="")
            return
        # loop over all possible nodes
        if (unavaiable[x+1][y] == 0 and visited[x+1][y] == 0 and (steps+1 < mincost[x+1][y])): # right
            mincost[x+1][y] = steps+1
            heu = heuristic([x+1,y],goal)
            prev_right = list(prev)
            prev_right.append([x+1,y])
            frontier.append([x+1,y,heu,prev_right])
        if (unavaiable[x-1][y] == 0 and visited[x-1][y] == 0 and (steps+1 < mincost[x-1][y])): # left
            mincost[x-11][y] = steps+1
            heu = heuristic([x-1,y],goal)
            prev_left = list(prev)
            prev_left.append([x-1,y])
            frontier.append([x-1,y,heu,prev_left])
        if (unavaiable[x][y-1] == 0 and visited[x][y-1] == 0) and (steps+1 < mincost[x][y-1]): # down
            mincost[x][y-1] = steps+1
            heu = heuristic([x,y-1],goal)
            prev_down = list(prev)
            prev_down.append([x,y-1])
            frontier.append([x,y-1,heu,prev_down])
        if (unavaiable[x][y+1] == 0 and visited[x][y+1] == 0 and (steps+1 < mincost[x][y+1])): # up
            mincost[x][y+1] = steps+1
            heu = heuristic([x,y+1],goal)
            prev_up = list(prev)
            prev_up.append([x,y+1])
            frontier.append([x,y+1,heu,prev_up])

        expanded += 1

def main():
    Greedy()

if __name__ == "__main__":
    main()
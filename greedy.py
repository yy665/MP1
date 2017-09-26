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
    goal = goal[0]
    print(start,goal)
    prev = [[[-1, -1] for x in range(columns)] for y in range(rows)]  # record all the history
    path = []
    steps = 1
    expanded = 0
    heu_start = heuristic(start,goal)
    mincost = [[9999999 for x in range(columns)] for y in range(rows)]
    frontier = [[start[0],start[1],heu_start,steps]]
    while(len(frontier)!=0):
        node_now = min(frontier, key=lambda t: t[2])
        steps = node_now[3]
        print(steps)
        frontier.remove(node_now)
        x = node_now[0]
        y = node_now[1]
        visited[x][y] = 1
        if (x == goal[0] and y == goal[1]):
            print("solution found")
            pos_now = goal
            while (pos_now != start):
                path.append(pos_now)

                pos_now = prev[pos_now[0]][pos_now[1]]
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
        # loop over all possible nodes
        if (unavaiable[x+1][y] == 0 and visited[x+1][y] == 0 and (steps+1 < mincost[x+1][y])): # right
            mincost[x+1][y] = steps+1
            heu = heuristic([x+1,y],goal)
            prev[x+1][y] = [x,y]
            frontier.append([x+1,y,heu,steps+1])
        if (unavaiable[x-1][y] == 0 and visited[x-1][y] == 0 and (steps+1 < mincost[x-1][y])): # left
            mincost[x-1][y] = steps+1
            heu = heuristic([x-1,y],goal)
            prev[x-1][y] = [x,y]
            frontier.append([x-1,y,heu,steps+1])
        if (unavaiable[x][y-1] == 0 and visited[x][y-1] == 0) and (steps+1 < mincost[x][y-1]): # down
            mincost[x][y-1] = steps+1
            heu = heuristic([x,y-1],goal)
            prev[x][y-1] = [x,y]
            frontier.append([x,y-1,heu,steps+1])
        if (unavaiable[x][y+1] == 0 and visited[x][y+1] == 0 and (steps+1 < mincost[x][y+1])): # up
            mincost[x][y+1] = steps+1
            heu = heuristic([x,y+1],goal)
            prev[x][y+1] = [x,y]
            frontier.append([x,y+1,heu,steps+1])

        expanded += 1

def main():
    Greedy()

if __name__ == "__main__":
    main()
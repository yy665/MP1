import numpy as np
import mpmath as math
import matplotlib as mpl
import matplotlib.pyplot as plt
from heapq import heappush, heappop
import read_maze

def heuristic(x,y):
    return (abs(x[0]-y[0]) + abs(x[1]-y[1]))

def Astar():
    maze,visited,unavaiable,start,goal,rows,columns = read_maze.generate_maze()
    pqueue = []
    steps = 0
    idx = 0
    maxexpands = 1
    expandsum = 1
    pathstruct = (0,1,[start])
    heappush(pqueue,pathstruct)
    mincost = [[9999999 for x in range(columns)] for y in range(rows)]
    while(len(pqueue)!=0):
        (cost,curridx,path) = heappop(pqueue)
        x = path[-1][0]
        y = path[-1][1]
        visited[x][y] = 1
        f_cost = len(path)
        if(len(pqueue)>maxexpands):
            maxexpands = len(pqueue)

        if(x == goal[0] and y == goal[1]):
            print("current steps: {}, expand states: {}".format(steps, expandsum))
            return (maze,cost,curridx,path)

        if (unavaiable[x+1][y] == 0 and visited[x+1][y] == 0): # right
            heu = heuristic([x+1,y],goal)
            rightpath = list(path)
            rightpath.append([x+1,y])
            rightstruct = (f_cost+1+heu,idx+1,rightpath)
            idx+=1
            if(f_cost+1 < mincost[x+1][y]):
                heappush(pqueue,rightstruct)
                mincost[x+1][y]=f_cost+1
                expandsum +=1

        if (unavaiable[x-1][y] == 0 and visited[x-1][y] == 0): # left
            heu = heuristic([x-1,y],goal)
            leftpath = list(path)
            leftpath.append([x-1,y])
            leftstruct = (f_cost+1+heu,idx+1,leftpath)
            idx+=1
            if(f_cost+1 < mincost[x-1][y]):
                heappush(pqueue,leftstruct)
                mincost[x-1][y]=f_cost+1
                expandsum +=1

        if (unavaiable[x][y-1] == 0 and visited[x][y-1] == 0): # down
            heu = heuristic([x,y-1],goal)
            downpath = list(path)
            downpath.append([x,y-1])
            downstruct = (f_cost+1+heu,idx+1,downpath)
            idx+=1
            if(f_cost+1 < mincost[x][y-1]):
                heappush(pqueue,downstruct)
                mincost[x][y-1]=f_cost+1
                expandsum +=1

        if (unavaiable[x][y+1] == 0 and visited[x][y+1] == 0): # up
            heu = heuristic([x,y+1],goal)
            uppath = list(path)
            uppath.append([x,y+1])
            upstruct = (f_cost+1,idx+1,uppath)
            idx+=1
            if(f_cost+1+heu < mincost[x][y+1]):
                heappush(pqueue,upstruct)
                mincost[x][y+1]=f_cost+1
                expandsum +=1
        steps += 1

def main():
    (maze,cost,curridx,path) = Astar()
    printPath(path,maze)
    #printPath(path)

def printPath(prevPosition,maze):
    correctSteps = 0
    print("The solution is ")
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if [i,j] in prevPosition:
                print(".", end="")
                correctSteps += 1
            else:
                print(maze[i][j], end="")
        print("\n",end="")
    #print("The path cost of the solution is " + correctSteps)

if __name__== "__main__":
  main()

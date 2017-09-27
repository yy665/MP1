import numpy as np
import mpmath as math
import matplotlib as mpl
import matplotlib.pyplot as plt
from heapq import heappush, heappop
import read_maze

def heuristic(x,y):
    return (abs(x[0]-y[0]) + abs(x[1]-y[1]))


def Astar(maze,visited,unavaiable,start,goal,rows,columns):

    print(start,goal)
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

def setupGraph ():
    import itertools
    import copy

    maze, visited, unavaiable, start, pure_goal, rows, columns = read_maze.generate_maze()
    goal = copy.deepcopy(pure_goal)
    goal.insert(0,start)

    print(len(goal))
    paths = []
    costs = []
    pairs = []
    graph = []
    for first, second in itertools.combinations(goal,2):
        visited1= copy.deepcopy(visited)
        maze1 = copy.deepcopy(maze)
        unavaiable1 = copy.deepcopy(unavaiable)
        (maze1,cost,curridx,path) = Astar(maze1,visited1,unavaiable1,first,second,rows,columns)
        graph.append([cost,path,[first,second]])
        pairs.append([first,second])
        costs.append(cost)
        paths.append(path)
    return (graph, pairs, costs, paths,pure_goal,start,goal,maze1)

# def solveGraph1(graph,pairs, costs, paths,pure_goal,start,goal):
#     n = len(goal)
#     index = 1
#     hasAssigned = [False for i in range(n)]
#     global permutation
#     permutation= [-1 for i in range(n)]
#     permutation[0] = 0
#     global sum
#     sum = 0
#     global min
#     min = 9999999
#     dfs(index,n,min,sum,permutation,pairs,costs,hasAssigned,goal)
#
# def dfs(index, n, min, sum,permutation,pairs,costs,hasAssigned,goal):
#     if index == n+1:
#         min = sum
#         print('min' + str(min))
#         print(sum)
#         return (permutation, min,sum)
#
#     for i in range(1,n):
#         if (not hasAssigned[i]):
#             permutation[index] = i
#             hasAssigned[i] = True
#             s = goal[permutation[index - 1]]
#             e = goal[permutation[index]]
#             cost_now = find_cost(pairs, costs, s,e)
#             if (sum + cost_now >= min):
#                 return (permutation, min, sum)
#             sum = sum + cost_now
#             print(sum)
#             (permutation,min,sum) = dfs(index+1, n, min, sum,permutation,pairs,costs,hasAssigned,goal)
#             hasAssigned[i] = False
#             permutation[index] = -1

def solveGraph1(graph,pairs, costs, paths,pure_goal,start,goal,maze):
    global n, min, sum,permutation,hasAssigned
    n = len(goal)
    index = 1
    hasAssigned = [False for i in range(n)]
    permutation= [-1 for i in range(n)]
    permutation[0] = 0
    sum = 0
    min = 9999999
    dfs(index,sum,goal,pairs,costs)
    print(min)
    print(result)
    path_result = []
    for i in range(n-1):
        s = goal[result[i]]
        e = goal[result[i+1]]
        if [s, e] in pairs:
            idx = pairs.index([s, e])
            path_result = path_result + paths[idx]
        else:
            idx = pairs.index([e, s])
            path_result = path_result +paths[idx].reverse()

    print(path_result)
    printPath(path_result,maze)

#initialize permutation, hasAssigned and goal here

def dfs(index,sum,goal,pairs,costs):
    global min,result
    if index == n:
        min = sum
        print('min' + str(min))

        result = list(permutation)
        return

    for i in range(1,n):
        if (not hasAssigned[i]):
            permutation[index] = i
            hasAssigned[i] = True
            s = goal[permutation[index - 1]]
            e = goal[permutation[index]]
            cost_now = find_cost(pairs, costs, s,e)
            if (sum + cost_now >= min):
                return
            sum = sum + cost_now
            #print(sum)
            dfs(index+1,sum,goal,pairs, costs)
            sum = sum - cost_now
            hasAssigned[i] = False
            permutation[index] = -1

def solveGraph2(graph,pairs, costs, paths,pure_goal,start,goal,maze):
    # smallest
    import copy
    cycle = [[0,0] for i in range(len(goal))]
    count = []
    for i in range(len(goal)):
        cycle[i].append(goal[i])
        count.append([goal[i],0])
    path_result = []
    order = []
    sum = 0
    print(len(graph))
    print(len(goal))
    while (len(order)!= len(goal)-1):
        select = min(graph, key=lambda t: t[0])
        print(select)
        cost = select[0]
        print(cost)
        [first,second] = select[2]

        if (first!= start and second != start and count[goal.index(first)][1] != 2 and count[goal.index(second)][1] !=2) or (first == start  and count[goal.index(first)][1] != 1 and count[goal.index(second)][1] !=2)or (second == start  and count[goal.index(first)][1] != 2 and count[goal.index(second)][1] !=1):
            print(cycle)
            print(len(cycle))
            for i in range(len(cycle)):
                if first in cycle[i]:
                    one = i
                    for j in range(len(cycle)):
                        if second in cycle[j]:
                            two = j
            if one!=two:
                print('yes')
                print(two)
                count[goal.index(first)][1] +=1
                count[goal.index(second)][1] +=1

                cycle[one] = cycle[one]+cycle[two]
                cycle.pop(two)
                print(cycle)
                sum += cost
                order.append([first,second])
            print(sum)
            print(order)
        graph.remove(select)

        #print(cycle)
        #print(graph)
def find_cost(pairs, costs, s,e):
    if [s,e] in pairs:
        idx = pairs.index([s,e])
    else:
        idx = pairs.index([e,s])
    return (costs[idx])

def main():
    (graph,pairs, costs, paths,pure_goal,start,goal,maze) = setupGraph()
    print("start solving")
    solveGraph1(graph, pairs, costs, paths, pure_goal, start, goal,maze)
    #print(costs)

   # (maze,cost,curridx,path) = Astar()
    #printPath(path,maze)
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

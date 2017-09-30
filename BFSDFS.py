from collections import deque
import matplotlib.pyplot as plt
import matplotlib as mpl
import mpmath as math
import read_maze
import Astar3
import csv

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

        if unavaiable[x+1][y] == 0: #up  no wall and unvisit
            if [x + 1, y] in goal_here:
                idx = goal_here.index([x+1,y])
                collected_temp = copy.deepcopy(collected)
                temp = list(collected_temp)
                temp[idx] = '1'
                collected_temp = "".join(temp)
                collected_int_temp = int(collected_temp,2)
                goal_temp = copy.deepcopy(goal_here)
                goal_temp[idx] = [-2,-2]
                if (steps + 1 < mincost[x+1][y][collected_int_temp]): # right
                    mincost[x+1][y][collected_int_temp] = steps+1
                    prev[x+1][y][collected_int_temp] = [x,y,collected_int]
                    queue.append([x+1,y,node_now,steps+1,collected_temp])
            else:
                if (steps + 1 < mincost[x+1][y ][collected_int]) : # right
                    mincost[x + 1][y][collected_int] = steps + 1
                    prev[x+1][y][collected_int] = [x,y,collected_int]
                    queue.append([x+1,y,node_now,steps+1,collected])

        if unavaiable[x][y+1] == 0: #right
            if [x, y+1] in goal_here:
                idx = goal_here.index([x,y+1])
                collected_temp = copy.deepcopy(collected)
                temp = list(collected_temp)
                temp[idx] = '1'
                collected_temp = "".join(temp)
                collected_int_temp = int(collected_temp,2)
                goal_temp = copy.deepcopy(goal_here)
                goal_temp[idx] = [-2,-2]
                if (steps + 1 < mincost[x+1][y][collected_int_temp]): # right
                    mincost[x][y+1][collected_int_temp] = steps+1
                    prev[x][y+1][collected_int_temp] = [x,y,collected_int]
                    queue.append([x,y+1,node_now,steps+1,collected_temp])
            else:
                if (steps + 1 < mincost[x+1][y ][collected_int]) : # right
                    mincost[x][y+1][collected_int] = steps + 1
                    prev[x][y+1][collected_int] = [x,y,collected_int]
                    queue.append([x,y+1,node_now,steps+1,collected])

        if unavaiable[x-1][y] == 0: #down
            if [x-1, y] in goal_here:
                idx = goal_here.index([x-1,y])
                collected_temp = copy.deepcopy(collected)
                temp = list(collected_temp)
                temp[idx] = '1'
                collected_temp = "".join(temp)
                collected_int_temp = int(collected_temp,2)
                goal_temp = copy.deepcopy(goal_here)
                goal_temp[idx] = [-2,-2]
                if (steps + 1 < mincost[x+1][y][collected_int_temp]): # down
                    mincost[x-1][y][collected_int_temp] = steps+1
                    prev[x-1][y][collected_int_temp] = [x,y,collected_int]
                    queue.append([x-1,y,node_now,steps+1,collected_temp])
            else:
                if (steps + 1 < mincost[x+1][y ][collected_int]) : # down
                    mincost[x-1][y][collected_int] = steps + 1
                    prev[x-1][y][collected_int] = [x,y,collected_int]
                    queue.append([x-1,y,node_now,steps+1,collected])

        if unavaiable[x][y-1] == 0: #left
            if [x, y-1] in goal_here:
                idx = goal_here.index([x,y-1])
                collected_temp = copy.deepcopy(collected)
                temp = list(collected_temp)
                temp[idx] = '1'
                collected_temp = "".join(temp)
                collected_int_temp = int(collected_temp,2)
                goal_temp = copy.deepcopy(goal_here)
                goal_temp[idx] = [-2,-2]
                if (steps + 1 < mincost[x+1][y][collected_int_temp]): # down
                    mincost[x][y-1][collected_int_temp] = steps+1
                    prev[x][y-1][collected_int_temp] = [x,y,collected_int]
                    queue.append([x,y-1,node_now,steps+1,collected_temp])
            else:
                if (steps + 1 < mincost[x+1][y ][collected_int]) : # down
                    mincost[x][y-1][collected_int] = steps + 1
                    prev[x][y-1][collected_int] = [x,y,collected_int]
                    queue.append([x,y-1,node_now,steps+1,collected])

        expanded += 1

def DFS():
    stack = []
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
    node_now = [start[0], start[1], None, steps, collected]
    stack.append(node_now)
    while(len(stack) != 0):
        node_now = stack.pop()
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

        if unavaiable[x+1][y] == 0: #up  no wall and unvisit
            if [x + 1, y] in goal_here:
                idx = goal_here.index([x+1,y])
                collected_temp = copy.deepcopy(collected)
                temp = list(collected_temp)
                temp[idx] = '1'
                collected_temp = "".join(temp)
                collected_int_temp = int(collected_temp,2)
                goal_temp = copy.deepcopy(goal_here)
                goal_temp[idx] = [-2,-2]
                if (steps + 1 < mincost[x+1][y][collected_int_temp]): # right
                    mincost[x+1][y][collected_int_temp] = steps+1
                    prev[x+1][y][collected_int_temp] = [x,y,collected_int]
                    stack.append([x+1,y,node_now,steps+1,collected_temp])
            else:
                if (steps + 1 < mincost[x+1][y ][collected_int]) : # right
                    mincost[x + 1][y][collected_int] = steps + 1
                    prev[x+1][y][collected_int] = [x,y,collected_int]
                    stack.append([x+1,y,node_now,steps+1,collected])

        if unavaiable[x][y+1] == 0: #right
            if [x, y+1] in goal_here:
                idx = goal_here.index([x,y+1])
                collected_temp = copy.deepcopy(collected)
                temp = list(collected_temp)
                temp[idx] = '1'
                collected_temp = "".join(temp)
                collected_int_temp = int(collected_temp,2)
                goal_temp = copy.deepcopy(goal_here)
                goal_temp[idx] = [-2,-2]
                if (steps + 1 < mincost[x+1][y][collected_int_temp]): # right
                    mincost[x][y+1][collected_int_temp] = steps+1
                    prev[x][y+1][collected_int_temp] = [x,y,collected_int]
                    stack.append([x,y+1,node_now,steps+1,collected_temp])
            else:
                if (steps + 1 < mincost[x+1][y ][collected_int]) : # right
                    mincost[x][y+1][collected_int] = steps + 1
                    prev[x][y+1][collected_int] = [x,y,collected_int]
                    stack.append([x,y+1,node_now,steps+1,collected])

        if unavaiable[x-1][y] == 0: #down
            if [x-1, y] in goal_here:
                idx = goal_here.index([x-1,y])
                collected_temp = copy.deepcopy(collected)
                temp = list(collected_temp)
                temp[idx] = '1'
                collected_temp = "".join(temp)
                collected_int_temp = int(collected_temp,2)
                goal_temp = copy.deepcopy(goal_here)
                goal_temp[idx] = [-2,-2]
                if (steps + 1 < mincost[x+1][y][collected_int_temp]): # down
                    mincost[x-1][y][collected_int_temp] = steps+1
                    prev[x-1][y][collected_int_temp] = [x,y,collected_int]
                    stack.append([x-1,y,node_now,steps+1,collected_temp])
            else:
                if (steps + 1 < mincost[x+1][y ][collected_int]) : # down
                    mincost[x-1][y][collected_int] = steps + 1
                    prev[x-1][y][collected_int] = [x,y,collected_int]
                    stack.append([x-1,y,node_now,steps+1,collected])

        if unavaiable[x][y-1] == 0: #left
            if [x, y-1] in goal_here:
                idx = goal_here.index([x,y-1])
                collected_temp = copy.deepcopy(collected)
                temp = list(collected_temp)
                temp[idx] = '1'
                collected_temp = "".join(temp)
                collected_int_temp = int(collected_temp,2)
                goal_temp = copy.deepcopy(goal_here)
                goal_temp[idx] = [-2,-2]
                if (steps + 1 < mincost[x+1][y][collected_int_temp]): # down
                    mincost[x][y-1][collected_int_temp] = steps+1
                    prev[x][y-1][collected_int_temp] = [x,y,collected_int]
                    stack.append([x,y-1,node_now,steps+1,collected_temp])
            else:
                if (steps + 1 < mincost[x+1][y ][collected_int]) : # down
                    mincost[x][y-1][collected_int] = steps + 1
                    prev[x][y-1][collected_int] = [x,y,collected_int]
                    stack.append([x,y-1,node_now,steps+1,collected])

        expanded += 1

'''
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
'''

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

from collections import deque
import matplotlib.pyplot as plt
import matplotlib as mpl
import mpmath as math
import read_maze
import csv
import copy




def DFS():
    import read_maze
    import copy
    maze,visited,unavaiable,start,goals,rows,columns = read_maze.generate_maze()
    #costs = setupGraph()
    points = len(goals)
    #print(points)
    #print(start,goals)
    prev = [[[[-1, -1, -1] for x in range(2**points)] for y in range(columns)]  for z in range(rows)] # record all the history
    collected = '0' * points # collected is a vector that contains which dots have been collected
    #print(collected)
    collected_int = int(collected,2) # collected_int is the index of what the 3rd dimension value is
    path = []
    steps = 1
    expanded = 0
    goal = goals[0]
    #print(goals)
    mincost = [[[9999999 for x in range(2**points)] for y in range(columns)] for z in range(rows)]
    frontier = [[start[0],start[1],steps,collected]]
    while(len(frontier)!=0):

        node_now = frontier.pop()

        x = node_now[0]
        y = node_now[1]
        collected = node_now[3]
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
            goalnames = ['0','1','2','3','4','5','6','7','8','9']
            goalnames.extend(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t'])
            goalnames.extend(['u','v','w','x','y','z'])
            goalnames.extend(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W'])
            goalnames.extend(['X','Y','Z'])
            goalcounter = 2

            while ([pos_now,collected_int] != [start,0] ):
                path.append(pos_now)
                print(pos_now)
                (pos_now,collected_int) = ([prev[pos_now[0]][pos_now[1]][collected_int][0],prev[pos_now[0]][pos_now[1]][collected_int][1]], prev[pos_now[0]][pos_now[1]][collected_int][2])
                #print(pos_now)
                if pos_now in goals:
                    if not maze[pos_now[0]][pos_now[1]] in goalnames:

                        maze[pos_now[0]][pos_now[1]] = goalnames[points-goalcounter-1]
                        goalcounter += 1
                else:
                    if points == 1:
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
        if (unavaiable[x+1][y] == 0):
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
                    frontier.append([x+1,y,steps+1,collected_temp])

            else:
                if (steps + 1 < mincost[x+1][y ][collected_int]) : # right
                    mincost[x + 1][y][collected_int] = steps + 1
                    prev[x+1][y][collected_int] = [x,y,collected_int]
                    frontier.append([x+1,y,steps+1,collected])

        if (unavaiable[x-1][y] == 0):
            if [x - 1, y] in goal_here:
                idx = goal_here.index([x-1,y])
                collected_temp = copy.deepcopy(collected)
                temp = list(collected_temp)
                temp[idx] = '1'
                collected_temp = "".join(temp)
                collected_int_temp = int(collected_temp,2)
                goal_temp = copy.deepcopy(goal_here)
                goal_temp[idx] = [-2, -2]
                if (steps + 1 < mincost[x-1][y][collected_int_temp]): # left
                    mincost[x-1][y][collected_int_temp] = steps+1
                    prev[x-1][y][collected_int_temp] = [x,y,collected_int]
                    frontier.append([x-1,y,steps+1,collected_temp])

            else:
                if (steps + 1 < mincost[x-1][y ][collected_int]) : # left
                    mincost[x - 1][y][collected_int] = steps + 1
                    prev[x-1][y][collected_int] = [x,y,collected_int]
                    frontier.append([x-1,y,steps+1,collected])

        if (unavaiable[x][y-1] == 0):
            if [x, y-1] in goal_here:
                idx = goal_here.index([x, y-1])
                collected_temp = copy.deepcopy(collected)
                temp = list(collected_temp)
                temp[idx] = '1'
                collected_temp = "".join(temp)
                collected_int_temp = int(collected_temp,2)
                goal_temp = copy.deepcopy(goal_here)
                goal_temp[idx] = [-2, -2]
                if (steps + 1 < mincost[x ][y-1][collected_int_temp]):  # down
                    mincost[x][y-1][collected_int_temp] = steps + 1
                    prev[x][y-1][collected_int_temp] = [x, y, collected_int]
                    frontier.append([x, y-1, steps + 1, collected_temp])

            else:
                if (steps + 1 < mincost[x][y-1][collected_int]):  # down
                    mincost[x][y-1][collected_int] = steps + 1
                    prev[x][y-1][collected_int] = [x, y, collected_int]
                    frontier.append([x, y-1, steps + 1, collected])

        if (unavaiable[x][y +1] == 0):
            if [x, y + 1] in goal_here:
                idx = goal_here.index([x, y + 1])
                collected_temp = copy.deepcopy(collected)
                temp = list(collected_temp)
                #print(temp)
                temp[idx] = '1'
                collected_temp = "".join(temp)
                collected_int_temp = int(collected_temp,2)
                goal_temp = copy.deepcopy(goal_here)
                goal_temp[idx] = [-2, -2]
                if (steps + 1 < mincost[x][y + 1][collected_int_temp]):  # up
                    mincost[x][y + 1][collected_int_temp] = steps + 1
                    prev[x][y + 1][collected_int_temp] = [x, y, collected_int]
                    frontier.append([x, y + 1,steps + 1, collected_temp])

            else:
                if (steps + 1 < mincost[x][y +1][collected_int]):  # up
                    mincost[x][y + 1][collected_int] = steps + 1
                    prev[x][y + 1][collected_int] = [x, y, collected_int]
                    frontier.append([x, y + 1, steps + 1, collected])

        expanded += 1


def BFS():
    import read_maze
    import copy
    maze,visited,unavaiable,start,goals,rows,columns = read_maze.generate_maze()
    #costs = setupGraph()
    points = len(goals)
    prev = [[[[-1, -1, -1] for x in range(2**points)] for y in range(columns)]  for z in range(rows)] # record all the history
    collected = '0' * points # collected is a vector that contains which dots have been collected
    collected_int = int(collected,2) # collected_int is the index of what the 3rd dimension value is
    path = []
    steps = 1
    expanded = 0
    goal = goals[0]
    mincost = [[[9999999 for x in range(2**points)] for y in range(columns)] for z in range(rows)]
    frontier = [[start[0],start[1],steps,collected]]
    frontier = deque(frontier)
    while(len(frontier)!=0):
        node_now = frontier.popleft()

        x = node_now[0]
        y = node_now[1]
        collected = node_now[3]
        collected_int = int(collected,2)
        #print(collected)
        goal_here = copy.deepcopy(goals)
        #print(goal_here)
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
            goalnames = ['0','1','2','3','4','5','6','7','8','9']
            goalnames.extend(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t'])
            goalnames.extend(['u','v','w','x','y','z'])
            goalnames.extend(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W'])
            goalnames.extend(['X','Y','Z'])
            goalcounter = 2
            while ([pos_now,collected_int] != [start,0] ):
                path.append(pos_now)
                print(pos_now)
                (pos_now,collected_int) = ([prev[pos_now[0]][pos_now[1]][collected_int][0],prev[pos_now[0]][pos_now[1]][collected_int][1]], prev[pos_now[0]][pos_now[1]][collected_int][2])
                #print(pos_now)
                if pos_now in goals:
                    if not maze[pos_now[0]][pos_now[1]] in goalnames:
                        maze[pos_now[0]][pos_now[1]] = goalnames[points-goalcounter-1]
                        goalcounter += 1
                else:
                    if points == 1:
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
        if (unavaiable[x+1][y] == 0):
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
                    frontier.append([x+1,y,steps+1,collected_temp])

            else:
                if (steps + 1 < mincost[x+1][y ][collected_int]) : # right
                    mincost[x + 1][y][collected_int] = steps + 1
                    prev[x+1][y][collected_int] = [x,y,collected_int]
                    frontier.append([x+1,y,steps+1,collected])

        if (unavaiable[x-1][y] == 0):
            if [x - 1, y] in goal_here:
                idx = goal_here.index([x-1,y])
                collected_temp = copy.deepcopy(collected)
                temp = list(collected_temp)
                temp[idx] = '1'
                collected_temp = "".join(temp)
                collected_int_temp = int(collected_temp,2)
                goal_temp = copy.deepcopy(goal_here)
                goal_temp[idx] = [-2, -2]
                if (steps + 1 < mincost[x-1][y][collected_int_temp]): # left
                    mincost[x-1][y][collected_int_temp] = steps+1
                    prev[x-1][y][collected_int_temp] = [x,y,collected_int]
                    frontier.append([x-1,y,steps+1,collected_temp])

            else:
                if (steps + 1 < mincost[x-1][y ][collected_int]) : # left
                    mincost[x - 1][y][collected_int] = steps + 1
                    prev[x-1][y][collected_int] = [x,y,collected_int]
                    frontier.append([x-1,y,steps+1,collected])

        if (unavaiable[x][y-1] == 0):
            if [x, y-1] in goal_here:
                idx = goal_here.index([x, y-1])
                collected_temp = copy.deepcopy(collected)
                temp = list(collected_temp)
                temp[idx] = '1'
                collected_temp = "".join(temp)
                collected_int_temp = int(collected_temp,2)
                goal_temp = copy.deepcopy(goal_here)
                goal_temp[idx] = [-2, -2]
                if (steps + 1 < mincost[x ][y-1][collected_int_temp]):  # down
                    mincost[x][y-1][collected_int_temp] = steps + 1
                    prev[x][y-1][collected_int_temp] = [x, y, collected_int]
                    frontier.append([x, y-1, steps + 1, collected_temp])

            else:
                if (steps + 1 < mincost[x][y-1][collected_int]):  # down
                    mincost[x][y-1][collected_int] = steps + 1
                    prev[x][y-1][collected_int] = [x, y, collected_int]
                    frontier.append([x, y-1,  steps + 1, collected])

        if (unavaiable[x][y +1] == 0):
            if [x, y + 1] in goal_here:
                idx = goal_here.index([x, y + 1])
                collected_temp = copy.deepcopy(collected)
                temp = list(collected_temp)
                #print(temp)
                temp[idx] = '1'
                collected_temp = "".join(temp)
                collected_int_temp = int(collected_temp,2)
                goal_temp = copy.deepcopy(goal_here)
                goal_temp[idx] = [-2, -2]
                if (steps + 1 < mincost[x][y + 1][collected_int_temp]):  # up
                    mincost[x][y + 1][collected_int_temp] = steps + 1
                    prev[x][y + 1][collected_int_temp] = [x, y, collected_int]
                    frontier.append([x, y + 1, steps + 1, collected_temp])

            else:
                if (steps + 1 < mincost[x][y +1][collected_int]):  # up
                    mincost[x][y + 1][collected_int] = steps + 1
                    prev[x][y + 1][collected_int] = [x, y, collected_int]
                    frontier.append([x, y + 1,  steps + 1, collected])

        expanded += 1


def main():
        In = input("DFS or BFS?")
        if In == "DFS":
            DFS()
        else:
            BFS()


if __name__ == "__main__":
    main()
from collections import deque


def BFS():
    queue = []
    queue = deque(queue)
    queue.append(read_maze.start)
    steps = 0
    everyStep = 0
    row = start[0]
    col = start[1]
    prevPosition = []

    while(len(queue) != 0):
        if unavaiable[row+1][col] == 0 and visited[row+1][col] == 0: #up  no wall and unvisit
            visited[row+1][col] = 1
            prevPosition.append(queue.front())

            if [row+1, col] == goal:

            queue.append([row+1,col])
        if unavaiable[row][col+1] == 0 and visited[row][col+1] == 0: #right
            visited[row][col+1] = 1
            prevPosition.append(queue.front())

            if [row, col+1] == goal:

            queue.append([row,col+1])
        if unavaiable[row-1][col] == 0 and visited[row-1][col] == 0: #down
            visited[row-1][col] = 1
            prevPosition.append(queue.front())

            if [row-1, col] == goal:

            queue.append([row-1,col])
        if unavaiable[row][col-1] == 0 and visited[row][col-1] == 0: #left
            visited[row][col-1] = 1
            prevPosition.append(queue.front())

            if [row, col-1] == goal:

            queue.append([row,col-1])

        queue.pop()
        everyStep += 1

def DFS():
    stack = []
    stack.append(read_maze.start)
    steps = 0
    expand = 0
    row = start[0]
    col = start[1]
    prevPosition = []

    while(len(stack) != 0):

        queue.pop()

        if unavaiable[row+1][col] == 0 and visited[row+1][col] == 0: #up  no wall and unvisit
            visited[row+1][col] = 1
            prevPosition.append(queue.front())

            if [row+1, col] == goal:

            queue.append([row+1,col])
        if unavaiable[row][col+1] == 0 and visited[row][col+1] == 0: #right
            visited[row][col+1] = 1
            prevPosition.append(queue.front())

            if [row, col+1] == goal:

            queue.append([row,col+1])
        if unavaiable[row-1][col] == 0 and visited[row-1][col] == 0: #down
            visited[row-1][col] = 1
            prevPosition.append(queue.front())

            if [row-1, col] == goal:

            queue.append([row-1,col])
        if unavaiable[row][col-1] == 0 and visited[row][col-1] == 0: #left
            visited[row][col-1] = 1
            prevPosition.append(queue.front())

            if [row, col-1] == goal:

            queue.append([row,col-1])

        everyStep += 1

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

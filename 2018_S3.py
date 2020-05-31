# CCC 2018 Senior Problem 3: RoboThieves
# https://cemc.uwaterloo.ca/contests/computing/2018/stage%201/seniorEF.pdf

from sys import stdin, stdout

n, m = (int(x) for x in stdin.readline().split())
grid = [[x for x in input()] for y in range (n)]

empty = [[0 for i in range (m)] for j in range(n)]
visited = [[False for x in range (m)] for y in range(n)]
robot = None

visitable = [[True for x in range (m)] for y in range (n)]


def camera(i, j):
    #up
    x = i - 1
    while grid[x][j] != 'W':
        if grid[x][j] == '.' or grid[x][j] == 'S':
            visitable[x][j] = False
        x -= 1

    #down
    x = i + 1
    while grid[x][j] != 'W':
        if grid[x][j] == '.' or grid[x][j] == 'S':
            visitable[x][j] = False
        x += 1
    
    #left
    y = j - 1
    while grid[i][y] != 'W':
        if grid[i][y] == '.' or grid[i][y] == 'S':
            visitable[i][y] = False
        y -= 1
    
    #right
    y = j + 1
    while grid[i][y] != 'W':
        if grid[i][y] == '.' or grid[i][y] == 'S':
            visitable[i][y] = False
        y += 1



for i in range (n):
    for j in range (m):
        if grid[i][j] == 'W':
            visitable[i][j] = False
        if grid[i][j] == '.':
            empty[i][j] = -1
        elif (grid[i][j] == 'S'):
            robot = [i,j]
        elif (grid[i][j] == 'C'):
            camera(i, j)
            visitable[i][j] = False

def isConveyor(i, j):
    if grid[i][j] == 'U' or grid[i][j] == 'D' or grid[i][j] == 'L' or grid[i][j] == 'R':
        return(True)
    return(False)

def up(i, j, leftInLayer):
    if visitable[i-1][j]:
        if not visited[i-1][j]:
            if isConveyor(i-1, j):
                rq.insert(0, i-1)
                cq.insert(0, j)
                visited[i-1][j] = True
                leftInLayer += 1
                return(0,leftInLayer)
            else:
                rq.append(i-1)
                cq.append(j)
                visited[i-1][j] = True
                return(1, leftInLayer)
    return(0,leftInLayer)

def down(i, j, leftInLayer):
    if visitable[i+1][j]:
        if not visited[i+1][j]:
            if isConveyor(i+1, j):
                rq.insert(0, i+1)
                cq.insert(0, j)
                visited[i+1][j] = True
                leftInLayer += 1
                return(0,leftInLayer)
            else:
                rq.append(i+1)
                cq.append(j)
                visited[i+1][j] = True
                return(1,leftInLayer)
    return(0,leftInLayer)

def left(i,j, leftInLayer):
    if visitable[i][j-1]:
        if not visited[i][j-1]:
            if isConveyor(i, j-1):
                rq.insert(0,i)
                cq.insert(0, j-1)
                visited[i][j-1] = True
                leftInLayer += 1
                return(0, leftInLayer)
            else:
                rq.append(i)
                cq.append(j-1)
                visited[i][j-1] = True
                return(1,leftInLayer)
    return(0,leftInLayer)

def right(i,j, leftInLayer):
    if visitable[i][j+1]:
        if not visited[i][j+1]:
            if isConveyor(i, j+1):
                rq.insert(0,i)
                cq.insert(0,j+1)
                visited[i][j+1] = True
                leftInLayer += 1
                return(0,leftInLayer)
            else:
                rq.append(i)
                cq.append(j+1)
                visited[i][j+1] = True
                return(1,leftInLayer)
    return(0,leftInLayer)

if visitable[robot[0]][robot[1]]:
    rq = [robot[0]]
    cq = [robot[1]]
else:
    rq =[]
visited[robot[0]][robot[1]] = True

moves = 0
leftInLayer = 1
nextLayer = 0

while len(rq) > 0:
    i = rq.pop(0)
    j = cq.pop(0)

    if grid[i][j] == '.':
        empty[i][j] = moves
    
    #checking 4 spots
    if grid[i][j] == '.' or grid[i][j] == 'S':
        q, leftInLayer = up(i,j, leftInLayer)
        nextLayer += q

        q, leftInLayer = down(i,j, leftInLayer)
        nextLayer += q

        q, leftInLayer = left(i,j, leftInLayer)
        nextLayer += q

        q, leftInLayer = right(i,j, leftInLayer)
        nextLayer += q
    elif grid[i][j] == 'U':
        q, leftInLayer = up(i,j, leftInLayer)
        nextLayer += q
    elif grid[i][j] == 'D':
        q, leftInLayer = down(i, j, leftInLayer)
        nextLayer += q
    elif grid[i][j] == 'L':
        q, leftInLayer = left(i, j, leftInLayer)
        nextLayer += q
    elif grid[i][j] == 'R':
        q, leftInLayer = right(i, j, leftInLayer)
        nextLayer += q

    leftInLayer -= 1
    if leftInLayer == 0:
        moves += 1
        leftInLayer = nextLayer
        nextLayer = 0

for i in range(n):
    for j in range(m):
        if empty[i][j] != 0:
            stdout.write(str(empty[i][j]) + '\n')
# CCC 2008 Senior Problem 3: Maze
# https://www.cemc.uwaterloo.ca/contests/computing/2008/stage1/seniorEn.pdf


def up(i, j):
    if i - 1 >= 0:
        if city[i-1][j] != "*":
            if visited[i-1][j] == False:
                rq.append(i-1)
                cq.append(j)
                visited[i-1][j] = True
                return(1)
    return (0)

def down(i, j):
    if i + 1 < r:
        if city[i+1][j] != "*":
            if visited[i+1][j] == False:
                rq.append(i+1)
                cq.append(j)
                visited[i+1][j] = True
                return(1)
    return (0)

def left(i, j):
    if j - 1 >= 0:
        if city[i][j-1] != "*":
            if visited[i][j-1] == False:
                rq.append(i)
                cq.append(j-1)
                visited[i][j-1] = True
                return(1)
    return (0)

def right(i, j):
    if j + 1 < c:
        if city[i][j+1] != "*":
            if visited[i][j+1] == False:
                rq.append(i)
                cq.append(j+1)
                visited[i][j+1] = True
                return(1)
    return(0)


def shortestPath(r, c):

    moves = 0
    leftInLayer = 1
    nextLayer = 0
    
    rq.append(0)
    cq.append(0)
    visited[0][0] = True    


    while len(rq)>0:
        i = rq.pop(0)
        j = cq.pop(0)

        if i == r - 1 and j == c - 1:
            return(moves + 1)
            break

        # checking four spots
        if city[i][j] == '+':
            nextLayer += up(i,j)
            nextLayer += down(i,j)
            nextLayer += left(i,j)
            nextLayer += right(i,j)
        elif city[i][j] == '-':
            nextLayer += left(i,j)
            nextLayer += right(i,j)
        elif city[i][j] == '|':
            nextLayer += up(i,j)
            nextLayer += down(i,j)

        leftInLayer -= 1
        if leftInLayer == 0:
            leftInLayer = nextLayer
            nextLayer = 0
            moves += 1

    return (-1)



t = int(input())
final = []

for i in range(t):
    r = int(input())
    c = int(input())
    city = []
    for j in range (r):
        city.append(list(input()))
    
    rq = []
    cq = []
    
    visited = [[False for col in range (c)] for row in range (r)]

    final.append(shortestPath(r, c))

for i in range(t):
    print(final[i])    

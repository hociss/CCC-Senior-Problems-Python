# CCC 2012 Senior Problem 5: Mouse Journey
# https://www.cemc.uwaterloo.ca/contests/computing/2012/stage1/seniorEn.pdf

from sys import stdin, stdout

r, c = (int(x) for x in stdin.readline().split())

steps = [[0 for col in range (c + 1)] for row in range (r + 1)]
visitable = [[True for col in range(c + 1)] for row in range (r + 1)]

k = int(stdin.readline())

for i in range (r + 1):
    visitable[i][0] = False
for i in range (c + 1):
    visitable[0][i] = False

for i in range (k):
    x, y = (int(x) for x in stdin.readline().split())

    visitable[x][y] = False


rq = [1]
cq = [1]
visited = [[False for col in range(c + 1)] for row in range (r + 1)]

while len(rq) > 0:
    i = rq.pop(0)
    j = cq.pop(0)

    if (i == 2 and j == 1) or (i == 1 and j == 2):
        steps[i][j] = 1
    else:
        steps[i][j] = steps[i - 1][j] + steps[i][j - 1]
    
    #down 
    if i + 1 <= r:
        if visitable[i + 1][j]:
            if not visited[i + 1][j]:
                rq.append(i + 1)
                cq.append(j)
                visited[i + 1][j] = True
    
    #right
    if j + 1 <= c:
        if visitable[i][j + 1]:
            if not visited[i][j + 1]:
                rq.append(i)
                cq.append(j + 1)
                visited[i][j + 1] = True


stdout.write(str(steps[r][c]))
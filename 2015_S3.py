# CCC 2015 Senior Problem 3: Gates
# https://cemc.uwaterloo.ca/contests/computing/2015/stage%201/seniorEn.pdf

from sys import stdin, stdout

G = int(stdin.readline())
visited = [0 for i in range (int(stdin.readline()) + 1)]

p = int(stdin.readline())
success = 0

closed = False
for i in range (p):
    g = int(stdin.readline())
    if not closed:
        while visited[g] > 0:
            temp = visited[g]
            visited[g] += 1
            g -= temp - 1
        if g <= 0:
            closed = True
        elif visited[g] == 0:
            success += 1
            visited[g] += 1

stdout.write(str(success))

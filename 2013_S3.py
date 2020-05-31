# CCC 2013 Senior Problem 3: Chances of Winning
# https://www.cemc.uwaterloo.ca/contests/computing/2013/stage1/seniorEn.pdf

from sys import stdin, stdout

t = int(stdin.readline())
g = int(stdin.readline())

games = [[0 for col in range (5)] for row in range (5)]
for i in range (5):
    games[i][i] = 1

points = [0 for i in range(5)]


for i in range (g):
    a, b, sa, sb = stdin.readline().split()
    a = int(a)
    b = int(b)
    sa = int(sa)
    sb = int(sb)

    games[a][b] = 1
    games[b][a] = 1

    if sa > sb:
        points[a] += 3
    elif sb > sa:
        points[b] += 3
    else:
        points[a] += 1
        points[b] += 1
    
q1 = []
q2 = []
for i in range (1, 5):
    for j in range (1, 5):
        if games[i][j] == 0:
            q1.append(i)
            q2.append(j)
            games[i][j] = 1
            games[j][i] = 1


print(q1, q2)
print(points)

def solve(counter, l, q1, q2, points):
    if l == 0:
        print(points)

        m = max(points)
        if points.index(m) == t and points.count(m) == 1:
            print("TRUE")
            return(1)
        else:
            return(0)
    else:
        # q1 win
        points[q1[counter]] += 3
        a = solve(counter + 1, l - 1, q1, q2, points)
        points[q1[counter]] -= 3

        # q1 and q2 tie
        points[q1[counter]] += 1
        points[q2[counter]] += 1
        a += solve(counter + 1, l - 1, q1, q2, points)
        points[q1[counter]] -= 1
        points[q2[counter]] -= 1

        # q2 win
        points[q2[counter]] += 3
        a += solve(counter + 1, l - 1, q1, q2, points)
        points[q2[counter]] -= 3

        return(a)
    

print(solve(0, len(q1), q1, q2, points))
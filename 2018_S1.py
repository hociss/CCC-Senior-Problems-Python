# CCC 2018 Senior Problem 1: Voronoi Villages
# https://cemc.uwaterloo.ca/contests/computing/2018/stage%201/seniorEF.pdf

n = int(input())
v = []
for i in range (n):
    v.append(int(input()))
v.sort()

smallest = 2000000001
for i in range (1, n - 1):
    if ((v[i + 1] + v[i]) / 2) - ((v[i] + v[i - 1]) / 2) < smallest:
        smallest = ((v[i + 1] + v[i]) / 2) - ((v[i] + v[i - 1]) / 2)

print(smallest)
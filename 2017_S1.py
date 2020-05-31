# CCC 2017 Senior Problem 1: Sum Game
# https://cemc.uwaterloo.ca/contests/computing/2017/stage%201/seniorEF.pdf

n = int(input())
swifts = [int(x) for x in input().split()]
semaphores = [int(x) for x in input().split()]

k = 0
s1 = 0 
s2 = 0

for i in range (n):
    s1 += swifts[i]
    s2 += semaphores[i]

    if s1 == s2:
        k = i + 1


print (k)
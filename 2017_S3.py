# CCC 2017 Senior Problem 3: Nailed It!
# https://cemc.uwaterloo.ca/contests/computing/2017/stage%201/seniorEF.pdf

from sys import stdin, stdout

n = int(stdin.readline())
fenceLengths = [0 for i in range (2001)]
sumFence = [0 for i in range (4001)]
l = [int(x) for x in stdin.readline().rstrip().split()]

for i in range (n):
    fenceLengths[l[i]] += 1

for i in range (2001):
    if fenceLengths[i] > 0:
        sumFence[2 * i] += fenceLengths[i] // 2
        for j in range (i + 1,2001):
            sumFence[i + j] += min(fenceLengths[i], fenceLengths[j])

maxFence = 0
maxFenceNum = 1
for i in range (4001):
    if sumFence[i] > maxFence:
        maxFence = sumFence[i]
        maxFenceNum = 1
    elif sumFence[i] == maxFence:
        maxFenceNum += 1


stdout.write(str(maxFence) + " " + str(maxFenceNum))
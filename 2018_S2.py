# CCC 2018 Senior Problem 2: Sunflowers
# https://cemc.uwaterloo.ca/contests/computing/2018/stage%201/seniorEF.pdf

from sys import stdout

n = int(input())
rotatedtable = []

for i in range (n):
    a = [int (x) for x in input().split()]
    rotatedtable.append(a)

while min(min(x) for x in rotatedtable) != rotatedtable[0][0]:
    tempTable = []

    for i in range(n-1, -1, -1):
        tempList = []
        for j in range (n):
            tempList.append(rotatedtable[j][i])
        tempTable.append(tempList)
    
    rotatedtable = tempTable
            
for i in range (n):
    for j in range (n):
        stdout.write(str(rotatedtable[i][j]) + " ")
    stdout.write("\n")


# while min(min(x) for x in rotatedtable) != rotatedtable[0][0]:
#     rotatedtable = list(zip(*reversed(rotatedtable)))

# for row in rotatedtable:
#     print(' '.join([str(col) for col in row]))
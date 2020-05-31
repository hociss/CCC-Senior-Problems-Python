# CCC 2009 Senior Problem 2: The Lights Going On and Off
# https://www.cemc.uwaterloo.ca/contests/computing/2009/stage1/seniorEn.pdf

r = int(input())
l = int(input())
lights = []
patterns = []


for i in range (r):
    temp = input().replace(" ", "")
    lights.append(temp)

    if i == 0:
        patterns.append([temp])
    if i > 0:
        temp2 = [temp]
        for j in range (i):
            c = int(patterns[i-1][j],2)^int(temp,2)
            temp2.append("{0:00b}".format(c).zfill(l))

        patterns.append(temp2)

total = []
for i in range (len(patterns[r-1])):
    if patterns[r-1][i] not in total:
        total.append(patterns[r-1][i])

print(len(total))
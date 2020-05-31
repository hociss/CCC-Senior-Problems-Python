# CCC 2013 Senior Problem 2: Bridge Transport
# https://www.cemc.uwaterloo.ca/contests/computing/2013/stage1/seniorEn.pdf

w = int(input())
n = int(input())
m = []
maxcars = 0

found = False

for i in range(n):
    m.append(int(input()))

    if not found:
        if i == 0 and m[i] <= w:
            maxcars += 1
        elif i == 0:
            found = True

        if i == 1 and m[i] + m[i-1] <= w:
            maxcars += 1
        elif i == 1:
            found = True

        if i == 2 and m[i] + m[i-1] + m[i-2] <= w:
            maxcars += 1
        elif i == 2:
            found = True

        if i >= 3 and m[i] + m[i-1] + m[i-2] + m[i-3] <= w:
            maxcars += 1
        elif i >= 3:
            found = True

print(maxcars)
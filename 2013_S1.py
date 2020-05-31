# CCC 2013 Senior Problem 1: From 1987 to 2013
# https://www.cemc.uwaterloo.ca/contests/computing/2013/stage1/seniorEn.pdf

y = int(input())
y += 1


if len(str(y)) == 1:
    print (y)

while len(str(y)) == 2:
    x = str(y)

    if x[0] != x[1]:
        print(y)
        break
    else:
        y += 1

while len(str(y)) == 3:
    x = str(y)

    if x[0] != x[1] and x[0] != x[2] and x[1] != x[2]:
        print(y)
        break
    else:
        y += 1

while len(str(y)) == 4:
    x = str(y)

    if x[0] != x[1] and x[0] != x[2] and x[0] != x[3] and x[1] != x[2] and x[1] != x[3] and x[2] != x[3]:
        print(y)
        break
    else:
        y += 1

while len(str(y)) == 5:
    x = str(y)

    if x[0] != x[1] and x[0] != x[2] and x[0] != x[3] and x[0] != x[4] and x[1] != x[2] and x[1] != x[3] and x[1] != x[4] and x[2] != x[3] and x[2] != x[4] and x[3] != x[4]:
        print(y)
        break
    else:
        y += 1
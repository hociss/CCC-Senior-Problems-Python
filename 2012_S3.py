# CCC 2012 Senior Problem 3: Absolutely Acidic
# https://www.cemc.uwaterloo.ca/contests/computing/2012/stage1/seniorEn.pdf

from sys import stdin, stdout


n = int(input())

f = [0 for i in range (1001)]


firstmax = 0
firstcount = 0
firstindexvalue = []

secondmax = 0
secondcount = 0
secondindexvalue = []

for i in range (n):
    r = int(stdin.readline())
    f[r] += 1

for i in range (1001):
    if f[i] > firstmax:
        secondmax = firstmax
        secondcount = firstcount
        secondindexvalue = firstindexvalue

        firstmax = f[i]
        firstcount = 1
        firstindexvalue = [i]
    elif f[i] == firstmax:
        firstcount += 1
        firstindexvalue.append(i)
    elif f[i] > secondmax:
        secondmax = f[i]
        secondcount = 1
        secondindexvalue = [i]
    elif f[i] == secondmax:
        secondcount += 1
        secondindexvalue.append(i)



if firstcount == 1:
    a = firstindexvalue[0]
    b = secondindexvalue[0]
    c = secondindexvalue[len(secondindexvalue)-1]

    p = max(a,b) - min(a,b)
    q = max(a,c) - min(a,c)
    print(max(p,q))
else:
    print(firstindexvalue[len(firstindexvalue) - 1] - firstindexvalue[0])
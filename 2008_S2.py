# CCC 2008 Senior Problem 2: Pennies in the Ring
# https://www.cemc.uwaterloo.ca/contests/computing/2008/stage1/seniorEn.pdf

import math

r = int(input())
total = []

while r!= 0:
    x = r

    t = 0

    j = r - 1
    for i in range (1, r + 1):
        while (i**2) + (j**2) > (r**2):
            j -= 1
        t += (j*4) + 2
    
    t += (r * 2) + 1
    total.append(t)

    r = int(input())

for i in range (len(total)):
    print(total[i])
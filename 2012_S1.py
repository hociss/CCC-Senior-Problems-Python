# CCC 2012 Senior Problem 1: Don't Pass Me the Ball!
# https://www.cemc.uwaterloo.ca/contests/computing/2012/stage1/seniorEn.pdf

import math

j = int(input())
if j < 4:
    print(0)
else:
    print(int(math.factorial(j-1) / (math.factorial(3) * math.factorial(j - 4))))
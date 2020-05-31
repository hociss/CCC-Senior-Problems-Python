# CCC 2009 Senior Problem 1: Cool Numbers
# https://www.cemc.uwaterloo.ca/contests/computing/2009/stage1/seniorEn.pdf

import math

a = int(input())
b = int(input())
if a == b and round(a ** (1/6)) ** 6 == a:
    print (1)
else:
    print (math.floor(b ** (1/6)) - math.ceil(a ** (1/6)) + 1)
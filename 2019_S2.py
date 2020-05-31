# CCC 2019 Senior Problem 2: Pretty Average Primes
# https://cemc.uwaterloo.ca/contests/computing/2019/stage%201/seniorEF.pdf

import math
from sys import stdin, stdout

t = int(stdin.readline())
n = []
a = 0
b = 0

for i in range (t):
    n.append(int(stdin.readline()))

prime = []
prime.append(2)
prime.append(3)

for i in range (5, max(n) * 2, 2):
    x = math.floor(i**0.5) 

    for j in range (2, x + 1):
        if (i % j == 0):
            break
        elif(j >= x):
            prime.append(i)

for i in range (len(n)):    
    j = 0
    while (prime[j] <= n[i]):
        x = (n[i] * 2) - prime[j]
        if (prime.count(x) == 1):
            print (prime[j], x) 
            break
        else:
            j += 1
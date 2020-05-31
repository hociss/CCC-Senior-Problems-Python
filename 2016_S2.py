# CCC 2016 Senior Problem 2: Tandem Bicycle
# https://cemc.uwaterloo.ca/contests/computing/2016/stage%201/seniorEn.pdf

answer = int(input())
n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]


if answer == 1:
    a.sort()
    b.sort()
    minSpeed = 0
    
    for i in range(n):
        minSpeed += max(a[i], b[i])
    
    print(minSpeed)

elif answer == 2:
    bikers = a + b
    bikers.sort(reverse = True)
    
    print(sum(bikers[:n]))
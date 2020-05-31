# CCC 2010 Senior Problem 3: Firehose
# https://www.cemc.uwaterloo.ca/contests/computing/2010/stage1/seniorEn.pdf

from sys import stdin, stdout

h = int(stdin.readline())
houses = []

for i in range (h):
    houses.append(int(stdin.readline()))

houses.sort()

k = int(stdin.readline())


def hydrants(hoselength, houses):
    diameter = hoselength * 2

    currentHouse = houses[0]
    lastHouse = houses[len(houses) - 1]

    hoseCount1 = 1

    i = 0
    while i < len(houses):
        if houses[i] > diameter + currentHouse and houses[i] <= lastHouse:
            if currentHouse == houses[0]:
                j = len(houses) - 1
                while (1000000 - houses[j]) + houses[i - 1] <= diameter:
                    j -= 1
                lastHouse = houses[j]

            hoseCount1 += 1
            currentHouse = houses[i]
        
        i += 1





    currentHouse = 1000000 + houses[0]
    if len(houses) > 1:
        lastHouse = houses[1]
    else: lastHouse = 0

    hoseCount2 = 1

    i = len(houses) - 1
    while i > 0:
        if currentHouse - houses[i] > diameter and houses[i] >= lastHouse:
            if currentHouse == houses[0]:
                j = 0
                while (1000000 - houses[i]) + houses[j] <= diameter:
                    j += 1
                lastHouse = houses[j]

            hoseCount2 += 1
            currentHouse = houses[i]
        
        i -= 1
        
    return (min(hoseCount1, hoseCount2))




low = -1
high = 1000000

while high > (low + 1):
    mid = (high + low) // 2
    if hydrants(mid, houses) > k:
        low = mid
    else:
        high = mid
    
stdout.write(str(high))
# CCC 2017 Senior Problem 2: High Tide, Low Tide
# https://cemc.uwaterloo.ca/contests/computing/2017/stage%201/seniorEF.pdf

n = int(input())

measurements = [int(x) for x in input().split()]
low = []
high = []
measurements.sort()

for i in range (n):
    if n % 2 == 0: 
        if i < n / 2:
            low.append(measurements[i])
        else:
            high.append(measurements[i])
    else:
        if i <= n / 2:
            low.append(measurements[i])
        else:
            high.append(measurements[i])

low.sort(reverse = True)
high.sort()

for i in range (len(low)):
    print (low[i], end = " ")

    if (n % 2 != 0 or len(high) == 0) and i == len(high):
       break
    else:
        print (high[i], end = " ")
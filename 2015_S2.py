# CCC 2015 Senior Problem 2: Jerseys
# https://cemc.uwaterloo.ca/contests/computing/2015/stage%201/seniorEn.pdf


j = int(input())
a = int(input())
jerseys = []

satisfied = 0
used = [0 for i in range(j)]

for i in range(j):
    jerseys.append(input())

for i in range(a):
    size, number = input().split()
    number = int(number)
    if used[number - 1] == 0:
        if size == "S":
            satisfied += 1
            used[number - 1] = 1
        elif size == "M" and jerseys[number - 1] != "S":
            satisfied += 1
            used[number - 1] = 1
        elif size == "L" and jerseys[number - 1] == "L":
            satisfied += 1
            used[number - 1] = 1

print(satisfied)
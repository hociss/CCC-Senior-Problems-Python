# CCC 2015 Senior Problem 1: Zero That Out
# https://cemc.uwaterloo.ca/contests/computing/2015/stage%201/seniorEn.pdf

k = int(input())
n = []
total = 0

for i in range (k):
    number = int(input())
    if number == 0 and len(n) > 0:
        n.pop(len(n) - 1)
    elif number != 0:
        n.append(number)

print(sum(n))
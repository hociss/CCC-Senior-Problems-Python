# CCC 2014 Senior Problem 3: The Geneva Confection
# https://www.cemc.uwaterloo.ca/contests/computing/2014/stage%201/seniorEn.pdf

from sys import stdin, stdout

t = int(stdin.readline())
answers = []

for i in range (t):
    n = int(stdin.readline())
    mountain = []
    for j in range (n):
        mountain.append(int(stdin.readline()))

    branch = []

    k = 1
    done = False
    while not done:
        if len(mountain) == 0 and len(branch) == 0:
            done = True
        elif len(branch) > 0 and branch[len(branch) - 1] == k:
            branch.pop(len(branch) - 1)
            k += 1
        else:
            a = mountain.pop(len(mountain) - 1)
            if len(branch) > 0 and a > branch[len(branch) - 1]:
                done = True
            else:
                branch.append(a)
    
    if len(branch) > 0:
        answers.append("N")
    else:
        answers.append("Y")


for i in range (t):
    stdout.write(answers[i] + "\n")      
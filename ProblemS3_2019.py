# CCC Senior 3 Problem: Arithmetic Square
# https://cemc.uwaterloo.ca/contests/computing/2019/stage%201/seniorEF.pdf

square = [[0 for row in range(3)] for column in range(3)]

square[0][0], square[0][1], square[0][2] = input().split()
square[1][0], square[1][1], square[1][2] = input().split()
square[2][0], square[2][1], square[2][2] = input().split()


for i in range(3):
    for j in range(3):
        if (square[i][j] != 'X'):
            square[i][j] = int(square[i][j])

def output(a, b, c, d, e, f, g, h, i):
    print(a, b, c)
    print(d, e, f)
    print(g, h, i)

count = sum([i.count('X') for i in square])
def solve():
    done = False
    while not done:
        global count
        count1 = count
        for i in range(3):
            for j in range(3):
                if square[i][j] == 'X':
                    if j == 0 and square[i][1] != 'X' and square[i][2] != 'X':
                        square[i][j] = int((2 * square[i][1]) - square[i][2])
                        count -= 1
                    elif j == 1 and square[i][0] != 'X' and square[i][2] != 'X':
                        square[i][j] = int((square[i][2] + square[i][0]) / 2)
                        count -= 1
                    elif j == 2 and square[i][0] != 'X' and square[i][1] != 'X':
                        square[i][j] = int((2 * square[i][1]) - square[i][0])
                        count -= 1
                    elif i == 0 and square[1][j] != 'X' and square[2][j] != 'X':
                        square[i][j] = int((2 * square[1][j]) - square[2][j])
                        count -= 1
                    elif i == 1 and square[0][j] != 'X' and square[2][j] != 'X':
                        square[i][j] = int((square[0][j] + square[2][j]) / 2)
                        count -= 1
                    elif i == 2 and square[0][j] != 'X' and square[1][j] != 'X':
                        square[i][j] = int((2 * square[1][j]) - square[0][j])
                        count -= 1
        
        if count == 0:
            output(square[0][0], square[0][1], square[0][2], square[1][0], square[1][1], square[1][2], square[2][0], square[2][1], square[2][2])
            done = True
        elif count1 == count:
            done = True

solve()

if count == 9:
    output(1, 1, 1, 1, 1, 1, 1, 1, 1)
    count = 0

if count == 8:
    for i in range (3):
        for j in range (3):
            if square[i][j] != 'X':
                a = square[i][j]
                output(a, a, a, a, a, a, a, a, a)
                count = 0

x = []
y = []
for i in range(3):
    for j in range(3):
        if square[i][j] != 'X':
            x.append(i)
            y.append(j)

if count == 7:
    if x[0] == 1:
        for j in range(3):
            square[1][j] = square[x[0]][y[0]]
        count = 5
        solve()
    elif x[1] == 1:
        for j in range(3):
            square[1][j] = square[x[1]][y[1]]
        count = 5
        solve()
    elif y[0] == 1:
        for i in range(3):
            square[i][y[0]] = square[x[0]][y[0]]
        count = 5
        solve()
    elif y[1] == 1:
        for i in range(3):
            square[i][y[1]] = square[x[1]][y[1]]
        count = 5
        solve()
    else:
        for i in range(3):
            square[i][y[0]] = square[x[0]][y[0]]
            square[i][y[1]] = square[x[1]][y[1]]
        count = 3
        solve()

if count == 6:
    if square[1][1] == 'X':
        square[1][1] = square[x[2]][y[2]]
        count -= 1
        solve()
    else:
        for i in range(3):
            for j in range(3):
                if square[i][j] == 'X' and (i == 1 or j == 1):
                    square[i][j] = square[x[1]][y[1]]
                    count -= 1
                    solve()
    
if count == 4:
    for i in range (3):
        for j in range (3):
            if square[0][0] == 'X' and square[0][2] == 'X' and square[2][0] == 'X' and square[2][2] == 'X':
                square[0][0] = square[0][1] + square[1][0] - square[1][1]
                count -= 1
                solve()
            elif square[i][j] == 'X' and square[i][j+1] == 'X' and square[i+1][j] == 'X' and square [i+1][j+1] == 'X':
                if i == 0 and j == 0:
                    square[1][1] = square[2][1] - square[2][2] + square[1][2]
                    count -= 1
                    solve()
                elif i == 0 and j == 1:
                    square[1][1] = square[2][1] - square[2][0] + square[1][0]
                    count -= 1
                    solve()
                elif i == 1 and j == 0:
                    square[1][1] = square[0][1] + square[1][2] - square[0][2]
                    count -= 1
                    solve()
                elif i == 1 and j == 1:
                    square[1][1] = square[0][1] + square[1][0] - square[0][0]
                    count -= 1
                    solve()
                
            elif square[i][j] == 'X' and square[i+1][j] == 'X' and square[i][j+2] == 'X' and square[i+1][j+2] == 'X':
                if i == 1 and j == 0:
                    square[1][0] = square[1][1] - square[0][1] + square[0][0]
                    count -= 1
                    solve()
                elif i == 0 and j == 0:
                    square[1][0] = square[1][1] - square[2][1] + square[2][0]
                    count -= 1
                    solve()
            elif square[i][j] == 'X' and square[i][j+1] == 'X' and square[i+2][j] == 'X' and square[i+2][j+1] == 'X':
                if i == 0 and j == 0:
                    square[0][1] = square[1][1] - square[1][2] + square[0][2]
                    count -= 1
                    solve()
                elif i == 0 and j == 1:
                    square[0][1] = square[1][1] - square[1][0] + square[0][0]
                    count -= 1
                    solve()
            
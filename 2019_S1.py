# CCC 2019 Senior Problem 1: Flipper
# https://cemc.uwaterloo.ca/contests/computing/2019/stage%201/seniorEF.pdf

flip = input()
board = [1, 2, 3, 4]

if flip.count('H')%2 != 0:
    p1 = board[0]
    p2 = board[1]
    p3 = board[2]
    p4 = board[3]
    board[0] = p3
    board[2] = p1
    board[1] = p4
    board[3] = p2
if flip.count('V')%2 != 0:
    p1 = board[0]
    p2 = board[1]
    p3 = board[2]
    p4 = board[3]
    board[0] = p2
    board[1] = p1
    board[2] = p4
    board[3] = p3

print (board[0], board[1])
print (board[2], board[3])
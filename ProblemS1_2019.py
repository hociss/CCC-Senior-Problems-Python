# CCC 2019 Senior 1 Program: Flipper
# https://cemc.uwaterloo.ca/contests/computing/2019/stage%201/seniorEF.pdf

flip = input()
board = [1, 2, 3, 4]

print(len(flip))

for i in range (len(flip)):
    p1 = board[0]
    p2 = board[1]
    p3 = board[2]
    p4 = board[3]

    if (flip[i] == "H"):
        board[0] = p3
        board[2] = p1
        board[1] = p4
        board[3] = p2
    elif (flip[i] == "V"):
        board[0] = p2
        board[1] = p1
        board[2] = p4
        board[3] = p3

print (board[0], board[1])
print (board[2], board[3])
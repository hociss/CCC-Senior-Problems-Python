# CCC 2016 Senior Problem 3: Phonomenal Reviews
# https://cemc.uwaterloo.ca/contests/computing/2016/stage%201/seniorEn.pdf

from sys import stdin, stdout

class myTree:
    def __init__(self, number):
        self.node = number
        self.subNode = []

    def theTraversal(self, total, firstIsFound, isPho):
        print("CURRent NODE", self.node, total)
        if isPho[self.node] == 1:
            firstIsFound = True
        if len(self.subNode) > 0:
            a = 0
            for i in range (len(self.subNode)):
                
                some, firstIsFound = self.subNode[i].theTraversal(total, firstIsFound, isPho)
                total += some
                a += 1

            if firstIsFound:
                return(a, firstIsFound)
        elif firstIsFound:
            return(1, firstIsFound)
        return(0, firstIsFound)

        




n, m = stdin.readline().split()
n = int(n)
m = int(m)

nodes = [myTree(x) for x in range (n)]

path = [[0 for col in range (n)] for row in range(n)]
isPho = [0 for x in range (n)]

temp = [int(x) for x in stdin.readline().split()]

for i in range (m):
    isPho[temp[i]] = 1

for i in range (n - 1):
    a, b = stdin.readline().split()
    a = int(a)
    b = int(b)

    path[a][b] = 1
    path[b][a] = 1

for i in range (n):
    for j in range(n):
        if path[i][j] == 1:
            nodes[i].subNode.append(nodes[j])
            path[i][j] = 0
            path[j][i] = 0

for i in range (n):
    print("TREE", i)
    for j in range (len(nodes[i].subNode)):
        print(nodes[i].subNode[j].node)


total, firstIsFound = nodes[0].theTraversal(0, False, isPho)
stdout.write(str(total))
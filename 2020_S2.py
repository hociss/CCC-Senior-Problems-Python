from sys import stdin, stdout

m = int(stdin.readline())
n = int(stdin.readline())

values = []

for i in range (m + 1):
    if i == 0:
        values.append([0 for x in range(n + 1)])
    else:
        temp = [int(x) for x in stdin.readline().split()]
        temp.insert(0, 0)
        values.append(temp)
    

visited = [[False for row in range(n + 1)] for col in range (m + 1)]

rq = [1]
cq = [1]
visited[1][1] = True

found = False
numbersUsed = [False for i in range(1000001)]

numbersUsed[values[1][1]] = True

while (len(rq) > 0):
    r = rq.pop(0)
    c = cq.pop(0)

    currentValue = values[r][c]

    counter1 = 0
    counter2 = 0
    if currentValue < m and currentValue < n:
       counter1 = currentValue//2
       counter2 = currentValue//2
    else:
       counter1 = m
       counter2 = n
    
    for i in range (counter1 + 1):
        for j in range (counter2 + 1):
            if i * j == currentValue:
                if not visited[i][j]:
                    if i == m and j == n:
                        found = True
                        break
                    else:
                        if not numbersUsed[values[i][j]]:
                            rq.append(i)
                            cq.append(j)
                            visited[i][j] = True
                            numbersUsed[values[i][j]] = True

    if currentValue <= m:
        if not visited[currentValue][1]:
            if not numbersUsed[values[currentValue][1]]:
                rq.append(currentValue)
                cq.append(1)
                visited[currentValue][1] = True
                numbersUsed[values[currentValue][1]] = True
    if currentValue <= n:
        if not visited[1][currentValue]:
            if not numbersUsed[values[1][currentValue]]:
                rq.append(1)
                cq.append(currentValue)
                visited[1][currentValue] = True
                numbersUsed[values[1][currentValue]] = True
        
    # if currentValue % 2 == 0 and currentValue//2 <= m:
    #     if not visited[currentValue//2][2]:
    #         rq.append(currentValue//2)
    #         cq.append(2)
    #         visited[currentValue//2][2] = True
    # if currentValue % 2 == 0 and currentValue//2 <= n:
    #     if not visited[2][currentValue//2]:
    #         rq.append(2)
    #         cq.append(currentValue//2)
    #         visited[2][currentValue//2] = True

    if found:
        break

if found:
    stdout.write("yes")
else:
    stdout.write("no")
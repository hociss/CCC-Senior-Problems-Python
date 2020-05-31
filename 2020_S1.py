from sys import stdin, stdout

n = int(stdin.readline())
positions = []


for i in range (n):
    a, b = (int(x) for x in stdin.readline().split())
    positions.append([a, b])

positions.sort()
maxSpeed = 0


for i in range (n - 1):
    speed = (positions[i + 1][1] - positions[i][1])/(positions[i+1][0] - positions[i][0])
    if speed < 0:
        speed = -speed

    if speed > maxSpeed:
        maxSpeed = speed

stdout.write(str(maxSpeed))
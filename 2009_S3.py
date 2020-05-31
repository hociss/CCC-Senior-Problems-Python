# CCC 2009 Senior Problem 3: Degrees of Separataion
# https://www.cemc.uwaterloo.ca/contests/computing/2009/stage1/seniorEn.pdf

f = [[] for x in range (50)]
f[1].append(6)
f[2].append(6)
f[3].extend((4,5,6,15))
f[4].extend((3,5,6))
f[5].extend((3,4,6))
f[6].extend((1,2,3,4,5,7))
f[7].extend((6,8))
f[8].extend((7,9))
f[9].extend((8,10,12))
f[10].extend((9,11))
f[11].extend((10,12))
f[12].extend((9,11,13))
f[13].extend((12,14,15))
f[14].append(13)
f[15].extend((3,13))
f[16].extend((17,18))
f[17].extend((16,18))
f[18].extend((16,17))


running = True
while running:
    command = input()
    if command == 'i':
        x = int(input())
        y = int(input())
        if y not in f[x]:
            f[x].append(y)
            f[y].append(x)
    elif command == 'd':
        x = int(input())
        y = int(input())
        f[x].remove(y)
        f[y].remove(x)
    elif command == 'n':
        x = int(input())
        print (len(f[x]))
    elif command == 'f':
        x = int(input())

        visited = [0 for x in range (50)]
        visited[x] = 2
        for i in range (len(f[x])):
            visited[f[x][i]] = 2
        for i in range (len(f[x])):
            person = f[x][i]
            for j in range (len(f[person])):
                if visited[f[person][j]] == 0:
                    visited[f[person][j]] = 1
        print (visited.count(1))
    elif command == 's':
        x = int(input())
        y = int(input())

        visited = [0 for x in range (50)]
        visited[x] = 1

        q = [x]

        layer = 0
        clayer = 1
        nlayer = 0

        found = False
        while len(q) > 0:
            person = q.pop(0)

            if person == y:
                found = True
                break
                
            for i in range (len(f[person])):
                if visited[f[person][i]] == 0:
                    q.append(f[person][i])
                    visited[f[person][i]] = 1
                    nlayer += 1
            
            clayer -= 1
            if clayer == 0:
                clayer = nlayer
                nlayer = 0
                layer += 1
        if found == True:
            print(layer)
        else:
            print("Not connected")       
    else:
        running = False
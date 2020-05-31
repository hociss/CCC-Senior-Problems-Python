# CCC 2014 Senior Problem 2: Assigning Partners
# https://www.cemc.uwaterloo.ca/contests/computing/2014/stage%201/seniorEn.pdf

n = int(input())
line1 = [x for x in input().split()]
line2 = [x for x in input().split()]
partners = []

break1 = False

for i in range (n):    
    for j in range (len(partners)):
        if line1[i] == line2[i]:
            print("bad")
            break1 = True
            break
        if (line1[i] in partners[j] and line2[i] not in partners[j]) or (line2[i] in partners[j] and line1[i] not in partners[j]):
            print("bad")
            break1 = True
            break
        elif j == len(partners) - 1:
            partners.append([line1[i], line2[i]])
    
    if line1[i] != line2[i] and i == 0:
        partners.append([line1[i], line2[i]])
    elif i == 0 and line1[i] == line2[i]:
        print("bad")
        break
    
    if break1 == True:
        break

    if i == n - 1:
        print ("good")
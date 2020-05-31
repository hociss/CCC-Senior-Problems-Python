# CCC 2010 Senior Problem 1: Computer Purchase
# https://www.cemc.uwaterloo.ca/contests/computing/2010/stage1/seniorEn.pdf

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
n = int(input())
first = ["",0]
second = ["",0]

if n == 1:
    name, r, s, d = input().split()
    print(name)
else:
    for i in range (n):
        name, r, s, d = input().split()
        r = int(r)
        s = int(s)
        d = int(d)

        performance = (2 * r) + (3 * s) + d
        if (performance > first[1]) or (performance == first[1] and alphabet.index(name[0].lower()) < alphabet.index(first[0][1].lower())):
            second = first
            first = [name, performance]
        elif performance > second[1] or (performance == second[1] and alphabet.index(name[0].lower()) < alphabet.index(first[0][1].lower())):
            second = [name, performance]

    print(first[0])
    print(second[0])
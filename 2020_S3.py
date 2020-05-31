from sys import stdin, stdout
# import math

n = stdin.readline()
h = stdin.readline()

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

charH = list(h)
charN = list(n)

total = 0

used = []


def count(subH, subN):
    stillSame = True
    for i in range (26):
        if subH.count(alphabet[i]) != subN.count(alphabet[i]):
            stillSame = False
            break
        if i == 25 and stillSame:
            if subH not in used:
                used.append(subH)
                return(1)
    return(0)

# countAlphabetN = [0 for i in range (26)]
# for i in range (len(n) - 1):
#     currentChar = charN[i]
#     indexNum = alphabet.index(currentChar)
#     countAlphabetN[indexNum] += 1

# temp = 1
# for i in range (26):
#     if countAlphabetN[i] > 0:
#         temp *= math.factorial(countAlphabetN[i])

# totalPermutations = math.factorial(len(n))/temp

for i in range (len(h) - len(n) + 1):
    a = charH[i: i + len(n) - 1]

    total += count(a, charN)
    # if total == totalPermutations:
    #     break

stdout.write(str(total))
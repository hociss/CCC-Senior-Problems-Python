# CCC 2010 Senior Problem 2: Huffman Encoding
# https://www.cemc.uwaterloo.ca/contests/computing/2010/stage1/seniorEn.pdf

k = int(input())
codes = []

for i in range (k):
    character, code = input().split()
    codes.append([character, code])

sequence = input()

binarysequence = []
i = 0
while i < len(sequence):
    for j in range (k):
        if codes[j][1] == sequence[i: i + len(codes[j][1])]:
            binarysequence.append(codes[j][0])
            i += len(codes[j][1])
            break

for i in range (len(binarysequence)):
    print(binarysequence[i], end = "")
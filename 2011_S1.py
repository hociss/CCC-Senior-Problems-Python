# CCC 2011 Senior Problem 1: English or French?
# https://www.cemc.uwaterloo.ca/contests/computing/2011/stage1/seniorEn.pdf

n = int(input())
english = 0
french = 0
for i in range (n):
    sentence = input()
    english += sentence.count("t")
    english += sentence.count("T")
    french += sentence.count("s")
    french += sentence.count("S")

if english > french:
    print ("English")
else:
    print ("French")
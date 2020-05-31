# CCC 2016 Senior Problem 1: Ragaman
# https://cemc.uwaterloo.ca/contests/computing/2016/stage%201/seniorEn.pdf

alphabet = ["a", "b", "c", "d","e", "f", "g", "h","i", "j", "k", "l","m", "n", "o", "p","q", "r", "s", "t","u", "v", "w", "x","y","z"]

s1 = input()
s2 = input()

for i in range (26):
    if s1.count(alphabet[i]) < s2.count(alphabet[i]):
        print("N")
        break
    if i == 25:
        print("A")
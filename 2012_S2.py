# CCC 2012 Senior Problem 2: Aromatic Numbers
# https://www.cemc.uwaterloo.ca/contests/computing/2012/stage1/seniorEn.pdf

aromatic = input()
symbols = []
total = 0

for i in range (len(aromatic)):
    symbols.append(aromatic[i])

for i in range (0, len(symbols), 2):
    arabic = int(symbols[i])
    roman = None
    romanNext = None
    if symbols[i + 1] == "I":
        roman = 1
    elif symbols[i + 1] == "V":
        roman = 5
    elif symbols[i + 1] == "X":
        roman = 10
    elif symbols[i + 1] == "L":
        roman = 50
    elif symbols[i + 1] == "C":
        roman = 100
    elif symbols[i + 1] == "D":
        roman = 500
    elif symbols[i + 1] == "M":
        roman = 1000
    

    if i < len(symbols) - 2:
        if symbols[i + 3] == "I":
            romanNext = 1
        elif symbols[i + 3] == "V":
            romanNext = 5
        elif symbols[i + 3] == "X":
            romanNext = 10
        elif symbols[i + 3] == "L":
            romanNext = 50
        elif symbols[i + 3] == "C":
            romanNext = 100
        elif symbols[i + 3] == "D":
            romanNext = 500
        elif symbols[i + 3] == "M":
            romanNext = 1000

        if romanNext > roman:
            total -= roman * arabic
        else:
            total += roman * arabic
    else:
        total += roman * arabic

print (total)
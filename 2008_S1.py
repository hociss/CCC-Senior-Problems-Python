# CCC 2008 Senior Problem 1: It's Cold Here!
# https://www.cemc.uwaterloo.ca/contests/computing/2008/stage1/seniorEn.pdf

city, temperature = input().split()
lowest = [city, int(temperature)]
while city != "Waterloo":
    city, temperature = input().split()
    if int(temperature) < lowest[1]:
        lowest = [city, int(temperature)]
    
print(lowest[0])
# CCC 2011 Senior Problem 2: Multiple Choice
# https://www.cemc.uwaterloo.ca/contests/computing/2011/stage1/seniorEn.pdf

n = int(input())
studentAnswers = []
correct = 0

for i in range (n):
    studentAnswers.append(input())
for i in range (n):
    correctAnswer = input()
    if studentAnswers[i] == correctAnswer:
        correct += 1

print (correct)
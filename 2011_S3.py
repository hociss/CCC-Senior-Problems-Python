# CCC 2011 Senior Problem 3: Alice Through the Looking Glass
# https://www.cemc.uwaterloo.ca/contests/computing/2011/stage1/seniorEn.pdf

t = int(input())

def check (m, x, y):
    if (x > (5**(m-1) - 1)  and x < (4*(5**(m-1))) and y < (5**(m-1))) or (x > (2*(5**(m-1))) - 1 and x < (3*(5**(m-1))) and y < (2*(5**(m-1)))):
        return("crystal")
    elif x > (5**(m-1) - 1) and x < (2*(5**(m-1))) and y > (5**(m-1) - 1) and y < (2*(5**(m-1))) and m > 1:
        return(check(m-1, x - (5**(m-1)), y - (5**(m-1))))
    elif x > (3*(5**(m-1))) - 1 and x < (4*(5**(m-1))) and y > (5**(m-1) - 1) and y < (2*(5**(m-1))) and m > 1:
        return(check(m-1, x - (3*(5**(m-1))), y - (5**(m-1))))
    elif x > (2*(5**(m-1))) - 1 and x < (3*(5**(m-1))) and y > (2*(5**(m-1))) - 1 and y < (3*(5**(m-1))) and m > 1:
        return(check(m-1, x - (2*(5**(m-1))), y - (2*(5**(m-1)))))
    else:
        return("empty")

answers = []

for i in range (t):
    m, x, y = input().split()
    m = int(m)
    x = int(x)
    y = int(y)

    answers.append(check(m,x,y))

for i in range (t):
    print(answers[i])
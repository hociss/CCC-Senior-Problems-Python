# CCC 2011 Senior Problem 4: Blood Distribution
# https://www.cemc.uwaterloo.ca/contests/computing/2011/stage1/seniorEn.pdf

blood = [int(x) for x in input().split()]
patients = [int(x) for x in input().split()]

success = 0

def update(a, b, c):
    blood[b] -= a
    patients[c] -= a


# o neg people
a = min(blood[0], patients[0])
update(a,0,0)
success += a

# a neg people
a = min(blood[2], patients[2])
update(a,2,2)
success += a

a = min(blood[0], patients[2])
update(a,0,2)
success += a

# b neg people
a = min(blood[4], patients[4])
update(a,4,4)
success += a

a = min(blood[0], patients[4])
update(a,0,4)
success += a

# ab neg people
for i in range(6,-1,-2):
    a = min(blood[i], patients[6])
    update(a,i,6)
    success += a

# o pos people
a = min(blood[0], patients[1])
update(a,0,1)
success += a

a = min(blood[1], patients[1])
update(a,1,1)
success += a

# a pos people
a = min(blood[2], patients[3])
update(a,2,3)
success += a

a = min(blood[3], patients[3])
update(a,3,3)
success += a

a = min(blood[0], patients[3])
update(a,0,3)
success += a

a = min(blood[1], patients[3])
update(a,1,3)
success += a

# b pos people
a = min(blood[4], patients[5])
update(a,4,5)
success += a

a = min(blood[5], patients[5])
update(a,5,5)
success += a

a = min(blood[0], patients[5])
update(a,0,5)
success += a

a = min(blood[1], patients[5])
update(a,1,5)
success += a

# ab pos people
for i in range(8):
    a = min(blood[i], patients[7])
    update(a,i,7)
    success += a

print(success)
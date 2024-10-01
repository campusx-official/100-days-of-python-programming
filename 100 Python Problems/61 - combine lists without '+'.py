# Write a program to merge two lists without using the + operator.

L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]

L = []

for i in L1:
    L.append(i)
for j in L2:
    L.append(j)

print(L)
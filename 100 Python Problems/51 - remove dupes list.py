# Write a program to remove all duplicates from a list.

L1 = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7]
L2 = []

for i in L1:
    if i not in L2:
        L2.append(i)

print(L2)
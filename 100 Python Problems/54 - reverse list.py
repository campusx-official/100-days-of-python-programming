# Write a program to reverse a list.

L = [1, 2, 3, 4, 5]
rev = []

for i in range(len(L) - 1, -1, -1):
    rev.append(L[i])
print(rev)
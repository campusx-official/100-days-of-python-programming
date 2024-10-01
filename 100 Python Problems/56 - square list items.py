# Write a program that can create a new list from a given list, where each item in the new list is the square of the corresponding item in the old list.

L1 = [2, 3, 4, 5, 6]
L2 = []

for i in L1:
    L2.append(i**2)
print(L2)
# Assume a list with numbers from 1 to 10 and then convert it into a dictionary where the keys would be the numbers of the list, and the values would be the squares of those numbers.

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

D = {}

for i in L:
    D[i] = i**2

print(D)
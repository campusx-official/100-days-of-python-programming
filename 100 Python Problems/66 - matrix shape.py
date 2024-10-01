# Write a program to print the shape of a matrix.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row = 0

for i in matrix:
    row = row + 1
print('The shape of this matrix is:', row, '*', len(i))
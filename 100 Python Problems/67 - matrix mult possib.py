# Write a program that can check whether you can perform matrix multiplication on two matrices.

matrix_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row_1 = 0

for i in matrix_1:
    row_1 = row_1 + 1
    column_1 = len(i)
    print('Matrix_1', i)

print('Row_1', row_1)
print('Column_1', column_1)

matrix_2 = [
    [2, 3],
    [4, 5],
    [7, 8]
]

row_2 = 0

for j in matrix_2:
    row_2 = row_2 + 1
    column_2 = len(j)
    print('Matrix_2', j)

print('Row_2', row_2)
print('Column_2', column_2)

if column_1 == row_2:
    print('Multiplication is possible')
else:
    print('Not possible')
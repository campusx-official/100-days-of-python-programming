# The maximum item in each row of a matrix.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in matrix:
    max_value = i[0]
    for j in i:
        if j > max_value:
            max_value = j
    print(max_value)
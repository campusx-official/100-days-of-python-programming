# To print different patterns using nested loops.

# *
# **
# ***
# ****

row = int(input('Enter number of rows: '))

for i in range(1, row + 1):
    for j in range(0, i):
        print('*', end=' ')
    print('')

# *
# **
# ***
# **
# *

row = int(input('Enter number of rows: '))

for i in range(1, row + 1):
    for j in range(0, i):
        print('*', end=' ')
    print('')

for k in range(row, 0, -1):
    for l in range(0, k - 1):
        print('*', end=' ')
    print('')

# 1
# 121
# 12321
# 1234321

row = int(input('Enter number of rows: '))

for i in range(1, row + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    for k in range(i - 1, 0, -1):
        print(k, end=' ')
    print(' ')

# 1
# 23
# 456

row = int(input('Enter row value: '))

num = 1

for i in range(1, row + 1):
    for j in range(1, i + 1):
        print(num, end=' ')
        num = num + 1
    print(' ')
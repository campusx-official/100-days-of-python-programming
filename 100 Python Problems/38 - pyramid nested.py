# Write a program to print the following pattern.

#   *
#  * *
# * * *

row = int(input('Enter number of rows: '))

for i in range(0, row):
    for j in range(0, row - i - 1):
        print(end=' ')
    for k in range(0, i + 1):
        print('*', end=' ')
    print()
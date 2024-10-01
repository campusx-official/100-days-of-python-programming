# Write a program to search for a given number in a list.

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num = int(input('Enter your number: '))

for i in L:
    if i == num:
        print('True')
        break
else:
    print('False')
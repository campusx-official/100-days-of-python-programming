# Find the length of a given string without using the len() function.

a = input('Enter your string: ')

count = 0

for i in a:
    count = count + 1

print('Length of the string is:', count)
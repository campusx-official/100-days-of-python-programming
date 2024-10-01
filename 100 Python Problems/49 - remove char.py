# Write a program that can remove a particular character from a string.

a = input('Enter your string: ')
b = int(input('Enter the value of the character: '))

c = a[0:b - 1]
d = a[b:]

result = c + d

print(result)
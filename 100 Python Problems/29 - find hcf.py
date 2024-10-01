# The user will provide two numbers, and you have to find the HCF of those two numbers.

a = int(input('Enter your first number: '))
b = int(input('Enter your second number: '))

while a % b != 0:
    rem = a % b
    a = b
    b = rem

print('Your HCF is:', b)
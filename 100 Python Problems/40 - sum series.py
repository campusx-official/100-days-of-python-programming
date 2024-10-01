# Write a program to calculate the sum of the following series up to the nth term:

# 1/1! + 2/2! + 3/3! + 4/4! + ... + n/n!

# The value of n will be provided by the user.

num = int(input('Enter your number: '))

result = 0
fact = 1

for i in range(1, num + 1):
    fact = fact * i
    result = result + (i / fact)

print(result)
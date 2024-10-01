# Write a program to find the sum of the series up to the nth term:

# 1 + x^2/2 + x^3/3 + ... + x^n/n

# The value of n will be provided by the user.

x = int(input('Enter your number: '))
n = int(input('Enter nth value: '))

sum = 1

for i in range(2, n + 1):
    sum = sum + ((x**i)/i)

print(sum)

# The natural logarithm can be approximated by the following series:

# (x-1)/x + 1/2 * ((x-1)/x)^2 + 1/2 * ((x-1)/x)^3 + ... + 1/2 * ((x-1)/x)^7

# If x is input through the keyboard, write a program to calculate the sum of the first seven terms of this series.

x = int(input('Enter your number: '))

n = 7

sum = ((x - 1) / x)

for i in range(2, n + 1):
    sum = sum + (1 / 2 * ((x - 1) / x)**i)

print(sum)
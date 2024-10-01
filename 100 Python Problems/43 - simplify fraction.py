# Write a program that accepts two numbers from the user, a numerator and a denominator, and then simplifies them.
# For example, if the numerator is 5 and the denominator is 15, the answer should be 1/3.
# For example, if the numerator is 6 and the denominator is 9, the answer should be 2/3.

a = int(input('Enter your first number: '))
num_1 = a
b = int(input('Enter your second number: '))
num_2 = b

while num_1 % num_2 != 0:
    rem = num_1 % num_2
    num_1 = num_2
    num_2 = rem

hcf = num_2

a = a/hcf
b = b/hcf

print(a/b)
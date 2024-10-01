# Write a program that checks whether a given number is an Armstrong number or not.

user_input = int(input("Enter your number: "))

num = user_input

a = num % 10
num = num // 10
b = num % 10
c = num // 10

if (a**3) + (b**3) + (c**3) == user_input:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
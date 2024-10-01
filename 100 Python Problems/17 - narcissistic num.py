# Write a program that will take user input of a (4-digit number) and check whether the number is a narcissist number or not.

user_input = int(input("Enter a four digit number: "))

num = user_input

a = num % 10
num = num // 10
b = num % 10
num = num // 10
c = num % 10
d = num // 10

if (a**4) + (b**4) + (c**4) + (d**4) == user_input:
    print("Narcissist number")
else:
    print("Not a Narcissist number")
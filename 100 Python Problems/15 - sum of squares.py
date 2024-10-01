# Write a program that takes three digits from the user and adds the square of each digit.

num = int(input("Enter your number: "))

a = num % 10
num = num // 10
b = num % 10
c = num // 10

add = (a**2) + (b**2) + (c**2)

print("Required number is: ", add)
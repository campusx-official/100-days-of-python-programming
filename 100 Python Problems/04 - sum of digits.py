# Write a program that will give you the sum of three digits.

num = int(input("Enter the three-digit number: "))

a = num % 10  # (123 % 10 = 3)
num = num // 10  # (123 // 10 = 12)
b = num % 10  # (12 % 10 = 2)
c = num // 10  # (12 // 10 = 1)
rev = (a + b + c)

print(rev)
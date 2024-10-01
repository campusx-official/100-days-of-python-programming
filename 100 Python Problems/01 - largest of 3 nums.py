# User will input (3 ages).
# Find the oldest one.

a = int(input("Enter the first age: "))
b = int(input("Enter the second age: "))
c = int(input("Enter the third age: "))

max_age = a

if max_age < b:
    max_age = b
if max_age < c:
    max_age = c

print(max_age)
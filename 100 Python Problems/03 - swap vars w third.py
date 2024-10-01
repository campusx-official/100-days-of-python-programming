# The user will input two numbers.
# Write a program to swap the numbers.

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b: "))

temp = a
a = b
b = temp

print("value of a: ", a)
print("value of b: ", b)
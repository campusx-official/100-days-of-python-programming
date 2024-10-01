# Write a program that swaps numbers.

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

a = a + b
b = a - b
a = a - b

print("After swapping:")
print("Your 'a' is: ", a)
print("Your 'b' is: ", b)
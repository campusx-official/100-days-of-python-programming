# Write a program to find the sum of the first n numbers, where n will be provided by the user.
# For example, if the user provides n = 10, the output should be 55.

n = int(input("Enter your number: "))

s = n * (n + 1) / 2

print("Your sum is: ", s)
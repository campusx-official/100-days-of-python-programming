# Write a program that will determine whether the given number is divisible by 3 and 6.

num = int(input("Enter your number: "))

if num % 3 == 0 and num % 6 == 0:
    print(num, "is divisible by 3 and 6")
else:
    print(num, "is not divisible by 3 and 6")
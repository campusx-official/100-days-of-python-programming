# Write a program that can calculate the factorial of a given number provided by the user.

num = int(input("Enter your number: "))

i = 1

if num > 0:
    while num >= 1:
        i = i * num
        num = num - 1
    print("Factorial of the given number is: ", i)
else:
    print("Factorial not possible")
# Write a program that can multiply two numbers provided by the user without using the * operator.

first_num = int(input("Enter your first number: "))
second_num = int(input("Enter your second number: "))

sum = 0

for i in range(0, second_num):
    sum = sum + first_num

print("Your result is: ", sum)
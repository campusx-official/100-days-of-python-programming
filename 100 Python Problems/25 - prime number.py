# Write a program to print whether a given number is a prime number or not.

num = int(input("Enter your number: "))

if num == 2:
    print("Prime number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
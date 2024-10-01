# Write a program that will determine whether the given year is a leap year or not.

year = int(input("Enter your year: "))

if year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")
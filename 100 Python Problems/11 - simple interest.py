# Write a program to find the simple interest when the values of principal, rate of interest, and time period are given.

p = int(input("Enter principal: "))
r = int(input("Enter rate of interest: "))
t = int(input("Enter time period in years: "))

si = (p * r * t) / 100

print("Your Simple Interest is: ", si)

a = p + si
print("Your Amount is: ", a)
# Write a program to find the volume of the cylinder.
# Also, determine the cost when the price of 1 liter of milk is 40 Rs.

r = float(input("Enter your radius: "))
h = float(input("Enter your height: "))

v = 3.14 * (r ** 2) * h

print("Your Volume is:", v)

cost = v / 1000 * 40

print("Your cost is: Rs", cost)
# Write a program to calculate the Euclidean distance between two coordinates.

x_1 = float(input("Enter x1 of x coordinate: "))
y_1 = float(input("Enter y1 of y coordinate: "))

x_2 = float(input("Enter x2 of x coordinate: "))
y_2 = float(input("Enter y2 of y coordinate: "))

d = ((x_2 - x_1)**2 + (y_2 - y_1)**2)**0.5

print(d)
# Write a program that takes user input for three angles and determines whether they can form a triangle or not.

a = int(input("Enter your first angle: "))   
b = int(input("Enter your second angle: "))  
c = int(input("Enter your third angle: "))   

if a + b + c == 180 and a != 0 and b != 0 and c != 0:
    print("Possible")
else:
    print("Not Possible")
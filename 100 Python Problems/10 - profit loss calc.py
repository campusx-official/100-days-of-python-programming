# Write a program that takes user input for cost price and selling price, and determines whether it's a loss or a profit.

cp = float(input("Enter your cost price: "))
sp = float(input("Enter your selling price: "))

if cp > sp:
    amount = cp - sp
    print("Loss:", amount)
else:
    amount = sp - cp
    print("Profit:", amount)
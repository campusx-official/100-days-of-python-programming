# Write a menu-driven program with the following options:

# 1. cm to inch,
# 2. km to miles,
# 3. USD to INR,
# 4. exit.

user_input = input('''
Hi! Welcome to my page
What would you like to do?

1. Convert cm to inches
2. Convert km to miles
3. Convert usd to inr
4. Exit''')

if user_input == '1':
    cm = float(input('Enter value in cm: '))
    inch = cm * 0.394
    print('Your value in inches is:', inch)
elif user_input == '2':
    km = float(input('Enter value in km: '))
    miles = km * 0.621
    print('Your value in miles is:', miles)
elif user_input == '3':
    usd = float(input('Enter value in usd: '))
    inr = usd * 76.63
    print('Your value in inr is:', inr)
else:
    print('Exit')
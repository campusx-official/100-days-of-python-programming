# Write a program to calculate compound interest.

p = int(input('Enter your principal: '))
r = int(input('Enter rate of interest: '))
t = int(input('Enter the time period elapsed: '))

a = p * (1 + r / 100)**t
print('Your amount is:', a)

ci = a - p
print('Your compound interest is:', ci)
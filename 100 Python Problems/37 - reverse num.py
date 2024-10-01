# Find the reverse of a number provided by the user (any number of digits).

a = int(input('Enter your number: '))

rev = 0

while a > 0:
    rem = a % 10
    a = a // 10
    rev = (rev * 10) + rem

print('Reversed value:', rev)

# 657

# rem = 657 % 10 = 7
# a = 657 // 10 = 65
# (0 * 10) + 7 = 7

# 65 % 10 = 5
# a = 65 // 10 = 6
# rev = 7 * 10 + 5 = 75

# rev = 75 * 10 + 6
# rev = 756
# Write a function that accepts a string and returns the number of uppercase characters and lowercase characters as a dictionary.

a = input('Enter your string: ')

D = {}

upper_count = 0
lower_count = 0

for i in a:
    if i.isupper():
        upper_count = upper_count + 1
    elif i.islower():
        lower_count = lower_count + 1

D = {'Upper case:': upper_count, 'Lower_case': lower_count}

print(D)
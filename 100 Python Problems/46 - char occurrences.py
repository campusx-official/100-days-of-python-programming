# Count the frequency of a particular character in a provided string.
# For example, in the string 'hello, how are you,' the frequency of 'h' is 2.

a = input('Enter your string: ')
b = input('Enter the character: ')

count = 0

for i in a:
    if i in b:
        count = count + 1

print('Character occurred:', count, 'times')